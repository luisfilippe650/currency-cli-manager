# 💱 Currency CLI Manager

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?logo=mysql">
  <img src="https://img.shields.io/badge/Docker-Container-blue?logo=docker">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

---

## 📌 Overview

**Currency CLI Manager** is a command-line application built with **Python** that allows users to manage currencies, fetch real-time exchange rates, and store exchange history in a **MySQL database**.

This project was designed to simulate a real backend system, focusing on clean architecture, modularization, and integration with external APIs.

---

## 🎯 Purpose

This project demonstrates practical experience in:

- Backend development with Python  
- API consumption and data processing  
- Relational database modeling (MySQL)  
- CLI application development  
- Environment variable management  
- Containerization using Docker  

---

## 🚀 Features

- ➕ Add currencies to the database  
- 📄 List all saved currencies  
- ❌ Delete currencies by ID  
- 💱 Fetch real-time exchange rates  
- 🕓 Automatically store exchange history  
- 📊 View exchange history  
- 🗑️ Delete exchange history  

---

## 🛠️ Technologies Used

- Python 3  
- MySQL  
- Docker & Docker Compose  
- argparse  
- requests  
- mysql-connector-python  
- python-dotenv  

---

## 🧠 Architecture

The project follows a layered architecture:

- **Config Layer** → Handles CLI input and commands  
- **Core Layer** → Database connection  
- **CRUD Layer** → Data persistence  
- **Service Layer** → External API integration  
- **Main** → Application entry point  

This structure ensures better scalability and maintainability.

---

## 📁 Project Structure


currency-cli-manager/
│
├── app/
│ ├── config/
│ ├── core/
│ ├── crud/
│ │ ├── cotacao_crud.py
│ │ └── historic_crud.py
│ ├── services/
│ └── main.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env


---

## ⚙️ Environment Variables

Create a `.env` file:


DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=currency_db
DB_PORT=3307

API_KEY=your_api_key


> ⚠️ Using port `3307` avoids conflicts with local MySQL.

---

## 🐳 Running with Docker


docker-compose up --build


---

## 💻 Running Locally


python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python app/main.py


---

## 🗄️ Database Schema

```sql
CREATE TABLE currencies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE exchange_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    from_currency VARCHAR(10),
    to_currency VARCHAR(10),
    rate DECIMAL(10,4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
💻 Usage
Add currency
python app/main.py add USD
List currencies
python app/main.py list
Delete currency
python app/main.py delete 1
Convert currency
python app/main.py convert USD BRL
Show history
python app/main.py history
📊 Example Output
Currency: USD → BRL
Rate: 5.12
Saved successfully in history
📈 Future Improvements

Transform CLI into a REST API (FastAPI)

Add Redis caching

Implement logging system

Add unit and integration tests

Improve error handling

👨‍💻 Author

Luis Filippe Reis Nogueira

🔗 LinkedIn:
https://www.linkedin.com/in/luis-filippe-reis-nogueira-244111355/

⭐ Final Note

This project represents a solid backend foundation, applying real-world concepts such as API integration, database persistence, and modular architecture.
