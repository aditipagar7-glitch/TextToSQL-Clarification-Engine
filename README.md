# Text-to-SQL with Clarification Engine

## Overview

The Text-to-SQL with Clarification Engine is a natural language interface for databases. It allows users to ask questions in plain English and converts their requests into SQL queries.

When a question is ambiguous, the application can ask follow-up questions to understand the user's intent before generating the SQL query.

The goal is to make database querying easier for users who may not know SQL.

## Key Features

* Convert natural language questions into SQL queries.
* Identify ambiguous user requests and ask clarification questions.
* Generate SQL queries based on the user's intent and database schema.
* Connect to a PostgreSQL database.
* Validate generated SQL queries before execution.
* Display query results when query execution is implemented and enabled.

Update this list to reflect the features currently working in your application.

## Technology Stack

* Python
* PostgreSQL
* SQLAlchemy
* Ollama / local language model
* SQLGlot for SQL parsing and validation
* Streamlit or the project's existing frontend framework

Keep only the technologies actually used in the project.

## Project Workflow

1. The user enters a question in natural language.
2. The application identifies the relevant database schema.
3. If the question is ambiguous, the application asks for clarification.
4. The application generates an SQL query.
5. The query is validated before execution.
6. If execution is enabled, the query runs against the configured database.
7. The application displays the results.

## Prerequisites

* Python
* PostgreSQL
* Git
* Ollama, if a local language model is used

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/TextToSQL-Clarification-Engine.git
cd TextToSQL-Clarification-Engine
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the project's dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file based on `.env.example` and configure your local database connection.

Create the PostgreSQL database and configure the required schema and sample data according to your project setup.

If the application uses Ollama, install it and download the model required by your application.

## Running the Application

Follow the project's actual startup command.

For example, if the application uses Streamlit:

```bash
streamlit run app.py
```

Replace `app.py` with the actual entry-point filename if different.

## Security

* Never commit database passwords, API keys, or other secrets.
* Do not commit your virtual environment.
* Validate generated SQL before execution.
* Restrict database permissions and avoid executing destructive SQL statements from untrusted input.

## Future Improvements

* Support for multiple database types.
* Improved clarification handling.
* Better query execution and error reporting.
* Query history and result visualization.
* Support for larger and more complex database schemas.

## Author

Aditi Pagar
