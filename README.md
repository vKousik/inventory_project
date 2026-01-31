# 📦 Inventory Management System (SQLAlchemy + PostgreSQL)

A backend-focused inventory management system demonstrating **relational database design**, **raw SQL**, **SQLAlchemy ORM**, **Alembic migrations**, and **transaction-safe operations** using PostgreSQL.

This project showcases professional-grade database handling and backend fundamentals.

---

## 🚀 Features

- Normalized relational schema (`products`, `categories`)
- PostgreSQL with UUID primary keys and foreign keys
- Raw SQL queries (select, join, aggregation, transactions)
- SQLAlchemy 2.0 ORM for Pythonic DB interaction
- Alembic migrations for safe schema evolution
- Environment-based configuration using `.env`
- Transaction-safe bulk price updates
- Git-versioned and reproducible setup

---

## 🛠️ Tech Stack

- Python 3
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- psycopg2-binary
- python-dotenv
- Git

---

## 🗂️ Project Structure

inventory_project/
│
├── app/
│ ├── db.py # Database engine & session setup
│ ├── models.py # ORM models (Product, Category)
│ └── final.py # Final integration script
│
├── alembic/
│ ├── versions/ # Migration scripts
│ └── env.py # Alembic configuration
│
├── alembic.ini
├── requirements.txt
├── .gitignore
├── README.md
└── .env # Environment variables (not committed)


---

## 🧱 Database Schema

### Tables

**categories**
- id (UUID, Primary Key)
- name (VARCHAR, UNIQUE)

**products**
- id (UUID, Primary Key)
- product_name (VARCHAR)
- price (DECIMAL)
- quantity (INTEGER)
- description (VARCHAR, nullable)
- category_id (UUID, Foreign Key → categories.id)
- created_at (TIMESTAMP)


---

## ⚙️ Environment Setup

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=inventory_db
DB_USER=inventory_user
DB_PASSWORD=your_password

📦 Install Dependencies
pip install -r requirements.txt


🔄 Database Migrations (Alembic)
Generate migration:

alembic revision --autogenerate -m "migration message"

Apply migration:

alembic upgrade head

Alembic ensures schema changes are applied safely without data loss.

🧠 Final Integration Script

Run the project using:

python -m app.final