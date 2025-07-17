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
## 🗂️ Project Structure
expense-management-system/
├── frontend/                   # Streamlit frontend app
│   ├── app.py                 # Main entry point
│   ├── add_update_ui.py       # UI for adding/updating expenses
│   └── analytics_ui.py        # UI for analytics view
│
├── backend/                    # FastAPI backend app
│   ├── server.py              # Main FastAPI app
│   ├── db_helper.py           # Database logic
│   └── logging_setup.py       # Logging configuration
│
├── tests/                      # Pytest test cases
│   ├── test_backend.py
│   └── test_frontend.py
│
├── requirements.txt            # Required Python dependencies
└── README.md                   # Project overview and usage

---

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/htppszahar/Expense-Management-System.git
cd Expense-Management-System
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Backend (FastAPI)
bash
Copy
Edit
uvicorn backend.server:app --reload
By default, the FastAPI server runs at: <br>
🔗 http://127.0.0.1:8000 <br>
📘 Swagger UI: http://127.0.0.1:8000/docs <br>
4. Run the Frontend (Streamlit)
bash
Copy
Edit
streamlit run frontend/app.py
The Streamlit app will launch in your browser at: <br>
🌐 http://localhost:8501
---
### ⚙️ Technologies Used

🔸 **Frontend**: Streamlit  
🔸 **Backend**: FastAPI  
🔸 **Database**: MySQL  
🔸 **Data Handling**: Pandas, Pydantic  
🔸 **HTTP**: Requests  
🔸 **Testing**: Pytest  
🔸 **Server**: Uvicorn

---
## ✅ Requirements

The project depends on the following Python packages:

🔹 `streamlit==1.35.0`  
🔹 `fastapi==0.112.2`  
🔹 `pydantic==1.10.9`  
🔹 `uvicorn==0.30.6`  
🔹 `mysql-connector-python==8.0.33`  
🔹 `pandas==2.0.2`  
🔹 `requests==2.31.0`  
🔹 `pytest==8.3.2`  

> These are automatically installed via `requirements.txt`.

---

### 📸 Screenshots

Add / Update Expenses:
<img width="881" height="766" alt="image" src="https://github.com/user-attachments/assets/9ee663db-7bc1-4c77-93e3-543c59728717" />

---

Expense Analytics:
<img width="832" height="965" alt="image" src="https://github.com/user-attachments/assets/3071d8b2-06e3-41aa-8842-1928b02a1d73" />

---

### 🤝 Acknowledgements <br>
This project was guided by online learning and hands-on practice. Thanks to all contributors, open-source libraries, and the tech community that made it possible.

### 📬 Contact
Have questions or suggestions?<br>
📧 [azharuk23@gmail.com]<br>
🌐 https://www.linkedin.com/in/azhar-ullah-khan-b8293a252/
