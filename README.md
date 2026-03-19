💱 Currency CLI Manager
📌 Overview

Currency CLI Manager is a backend-oriented command-line application designed to manage currencies, retrieve real-time exchange rates, and persist historical data using a MySQL database.

The project was built with a focus on clean architecture, separation of concerns, and scalable backend practices, simulating a real-world service layer.

🎯 Purpose

This project aims to demonstrate practical experience in:

Backend development with Python

API integration and data handling

Relational database modeling

CLI application design

Containerized environments with Docker

🧠 Architecture & Design

The application follows a modular and layered architecture:

Config Layer → Handles CLI commands and input parsing

Core Layer → Manages database connection

CRUD Layer → Responsible for data persistence

Service Layer → Handles external API communication

Entry Point → Orchestrates application flow

This structure improves:

Maintainability

Scalability

Code readability

🚀 Features

Currency management (create, list, delete)

Real-time exchange rate retrieval via external API

Automatic persistence of exchange history

Historical query support

CLI-based interaction using argparse

🛠️ Tech Stack
Category	Technology
Language	Python 3
Database	MySQL
Containerization	Docker & Docker Compose
HTTP Client	requests
CLI	argparse
Environment	python-dotenv
📁 Project Structure
currency-cli-manager/
│
├── app/
│   ├── config/          # CLI logic and command handling
│   ├── core/            # Database connection setup
│   ├── crud/            # Data persistence layer
│   ├── services/        # External API integrations
│   └── main.py          # Application entry point
│
├── docker/
│   └── mysql/           # Database container configuration
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env
⚙️ Environment Configuration

The application uses environment variables for secure configuration.

Example .env:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=currency_db
DB_PORT=3307

API_KEY=your_api_key

💡 The database runs on a custom port (3307) to avoid conflicts with local MySQL instances.

🐳 Running with Docker
docker-compose up --build

This will:

Start a MySQL container

Configure the database automatically

Run the application environment

💻 Running Locally
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python app/main.py
🗄️ Database Design
currencies
Field	Type	Description
id	INT	Primary key
code	VARCHAR	Currency code (USD, BRL, etc.)
exchange_history
Field	Type	Description
id	INT	Primary key
from_currency	VARCHAR	Source currency
to_currency	VARCHAR	Target currency
rate	DECIMAL	Exchange rate
created_at	TIMESTAMP	Auto-generated timestamp
🔌 Example Commands
# Add currency
python app/main.py add USD

# List currencies
python app/main.py list

# Delete currency
python app/main.py delete 1

# Convert currency
python app/main.py convert USD BRL

# Show history
python app/main.py history
📊 Engineering Highlights

✔️ Layered architecture (inspired by real backend systems)

✔️ Environment-based configuration (.env)

✔️ Database normalization and persistence strategy

✔️ External API integration with structured response handling

✔️ CLI abstraction for user interaction

✔️ Dockerized infrastructure

📈 Future Improvements

Transform CLI into a REST API (FastAPI)

Add caching layer (Redis)

Implement logging and monitoring

Add unit and integration tests

Introduce authentication layer

👨‍💻 Author

Luis Filippe Reis Nogueira
Backend Developer

🔗 LinkedIn:
https://www.linkedin.com/in/luis-filippe-reis-nogueira-244111355/

⭐ Final Note

This project reflects a strong foundation in backend development, focusing on real-world practices, clean code, and scalable architecture.
