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

---

# Installation

Clone the repository:

```bash
git clone https://github.com/SEU_USUARIO/currency-cli-manager.git
```

Enter the project folder:

```bash
cd currency-cli-manager
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

Linux / Mac:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the CLI:

```bash
python app/main.py
```

---

# Commands

## Add currency

```bash
python app/main.py moeda add --nome USD
```

---

## List currencies

```bash
python app/main.py moeda list
```

---

## Delete currency

```bash
python app/main.py moeda delete --id 1
```

---

## Get exchange rate

```bash
python app/main.py cotacao --nome USD
```

---

## Show history

```bash
python app/main.py historico list
```

---

## Delete history

```bash
python app/main.py historico delete
```
---
# Database

Example tables used in the project:

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
```

---

# Learning Goals

This project was created to practice:

* CLI application development with Python
* API consumption using Requests
* Database integration with MySQL
* Project structure organization
* Backend development fundamentals

---

# Author

Luis Filippe Reis Nogueira
