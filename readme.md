# Flask Application - ERP System

## Project Overview

This project is a Flask-based ERP System designed for managing user data and other functionalities. The application interacts with a database to store, retrieve, and manage user information.

## Setup Instructions

### Prerequisites

Before running the application, ensure you have the following installed on your system:

- Python 3.x
- Pip (Python package manager)
- Virtualenv (recommended for isolated environments)

### Steps to Set Up

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nikhilgupta738/ERPSystem.git
    cd collegeerp
    ```

2. **Create and activate a virtual environment**:
    - For Linux/macOS:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - For Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install MySQL and Set up the Database**:
    - **Install MySQL** if you haven't already. You can follow instructions from the [official MySQL website](https://dev.mysql.com/doc/refman/8.0/en/installing.html).
    - **Create a database** in MySQL for the application:
    ```sql
    CREATE DATABASE users;
    ```

    - **Set up the users table**. Use the following SQL script to create the `users` table:
    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        role VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

5. **Configure MySQL connection**:
    Open `app.py` and ensure the following database connection settings are correct:
    ```python
    app.config['MYSQL_HOST'] = 'localhost'  # Change if MySQL is hosted elsewhere
    app.config['MYSQL_USER'] = 'root'      # MySQL username
    app.config['MYSQL_PASSWORD'] = 'password'  # Your MySQL password
    app.config['MYSQL_DB'] = 'users'      # Name of the database
    ```

6. **Run the application**:
    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

## Database Schema

The database schema includes the following tables:

### Users Table

| Field        | Type        | Description                                      |
|--------------|-------------|--------------------------------------------------|
| id           | Integer     | Primary key                                      |
| name         | String      | Name of the user                                |
| email        | String      | Email address of the user (unique)              |
| role         | String      | describe the role of user           |

### Other Tables

- Additional tables (like permissions, etc.) can be added based on your requirements.

### Populating Sample Data

You can populate the database with sample data using MySQL commands or through the Flask app. To add a user using the Flask app, follow these steps:

1. Open the app and go to the `/new_users` page.
2. Fill in the form with sample data for name, email, and role.
3. Upon submission, the data will be added to the `users` table.

### Example to Manually Insert Data via MySQL:

1. Open the MySQL client:
    ```bash
    mysql -u root -p
    ```

2. Insert a sample user into the `users` table:
    ```sql
    INSERT INTO users (name, email, role) VALUES ('John Doe', 'johndoe@example.com', 'Admin');
    ```

## Additional Dependencies

- **Flask**: Web framework used for building the application.
- **Flask-MySQLdb**: MySQL database connector for Flask.
- **Flask-WTF**: Form handling and validation.
- **Flask-Login**: User session management for authentication (if needed).
- **Jinja2**: Templating engine used by Flask.

You can install all the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt