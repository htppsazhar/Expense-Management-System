from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper
from logging_setup import setup_logger

logger = setup_logger('server')

app = FastAPI()


# ---------- Models ----------
class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date


class ExpenseWrapper(BaseModel):
    expenses: List[Expense]


class CategorySummary(BaseModel):
    category: str
    total: float
    percentage: float

# ---------- Endpoints ----------


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expense_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail='Failed to retrieve expense summary.')
    return expenses


@app.post("/expenses/{expense_date}")
def add_expenses(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(
            expense_date,
            expense.amount,
            expense.category,
            expense.notes
        )
    return {"message": "Expenses updated successfully"}


# ---------- Endpoint ----------
@app.post("/analytics/", response_model=List[CategorySummary])
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    total = sum(row['total'] for row in data)

    result = []
    for row in data:
        percentage = (row['total'] / total) * 100 if total != 0 else 0
        result.append({
            "category": row['category'],
            "total": row['total'],
            "percentage": round(percentage, 2)
        })
    return result


