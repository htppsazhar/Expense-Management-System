import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend import db_helper


def test_fetch_expenses_for_data():
    expenses = db_helper.fetch_expense_for_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes'] == "Bought potatoes"


def test_fetch_expenses_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2099-01-01", "2099-12-30")
        
