# Currency CLI Manager 💱

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?logo=mysql">
  <img src="https://img.shields.io/badge/Docker-Container-blue?logo=docker">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>


A simple command-line application built with **Python** that manages currencies, fetches **real-time exchange rates**, and stores exchange history in a **MySQL database**.

The application allows users to interact through CLI commands to perform operations like adding currencies, listing them, converting values, and tracking historical data.

This project was created for **learning purposes** to practice backend development, API consumption, and database integration.

---

# Technologies Used

* Python
* MySQL
* Docker
* Docker Compose
* Requests
* argparse
* mysql-connector-python
* python-dotenv

---

# Installation

Clone the repository:

```bash
git clone https://github.com/SEU_USUARIO/currency-cli-manager.git

Enter the project folder:

cd currency-cli-manager

Create a virtual environment:

python -m venv .venv

Activate the environment.

Linux / Mac:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

Install the dependencies:

pip install -r requirements.txt
Environment Configuration

Create a .env file in the root directory:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=currency_db
DB_PORT=3307

API_KEY=your_api_key
Running the Application

Run the CLI:

python app/main.py
Commands
Add a currency
python app/main.py add USD
List currencies
python app/main.py list
Delete a currency
python app/main.py delete 1
Convert currency
python app/main.py convert USD BRL
Show history
python app/main.py history
Database

Example tables used in the project:

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
Learning Goals

This project was created to practice:

CLI application development with Python

API consumption using Requests

Database integration with MySQL

Environment variables management

Project structure organization

Backend development fundamentals

Author

Luis Filippe Reis Nogueira

🔥 adaptar isso pra **ficar mais chamativo ainda (tipo o de projetos grandes)**  
🔥 ou criar um **segundo projeto igual, mas em FastAPI (nível estágio forte)**
