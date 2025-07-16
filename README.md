# 💸 Expense Management System

A full-stack Expense Management System built with **FastAPI** (backend), **Streamlit** (frontend), and **MySQL** for data storage. This project allows users to **track, categorize, and analyze expenses** over custom date ranges through an intuitive web interface.

The system also includes visual analytics for better financial insights and a robust backend to handle RESTful requests efficiently.

---

## 🧭 Features

- 📅 Add and categorize daily expenses
- 📊 Visualize expense breakdown by category
- 🔎 Analyze spending patterns over a custom date range
- ⚙️ Clean and responsive UI with dark mode
- 🚀 FastAPI-powered backend with Pydantic validation
- 🧪 Pytest test suite for backend validation

---

## 📁 Project Structure
expense-management-system/
│
├── frontend/ # Streamlit frontend app
│ ├── app.py # Main entry point
│ ├── add_update_ui.py # UI for adding/updating expenses
│ └── analytics_ui.py # UI for analytics view
│
├── backend/ # FastAPI backend app
│ ├── server.py # Main FastAPI app
│ ├── db_helper.py # Database logic
│ └── logging_setup.py # Logging configuration
│
├── tests/ # Pytest test cases
│ ├── test_backend.py
│ └── test_frontend.py
│
├── requirements.txt # Required Python dependencies
└── README.md # Project overview and usage

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/htppsazhar/Expense-Management-System.git
cd Expense-Management-System
---
`###` 2. Install Dependencies
pip install -r requirements.txt
---
`###` 3. Run the Backend(FastAPI)
uvicorn backend.server:app --reload
By default, the FastAPI server runs at:
🔗 http://127.0.0.1:8000
📚 Swagger UI: http://127.0.0.1:8000/docs
---
`###` 4. Run the Frontend (Streamlit)
streamlit run frontend/app.py

The Streamlit app will launch in your browser at:
🔗 http://localhost:8501
---

`###` ⚙️ Technologies Used

- **Frontend**: Streamlit  
- **Backend**: FastAPI  
- **Database**: MySQL  
- **Data Handling**: Pandas, Pydantic  
- **HTTP**: Requests  
- **Testing**: Pytest  
- **Server**: Uvicorn  

