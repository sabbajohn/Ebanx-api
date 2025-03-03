# Flask Account Management API

This project is a simple Flask application that manages account balances, allowing users to create accounts, deposit, withdraw, and transfer funds. It uses an in-memory data structure to store account information.

## Project Structure

```
Ebanx
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── services.py
├── tests
│   ├── __init__.py
│   └── test_app.py
├── venv
├── requirements.txt
└── README.md
```

## Installation

1. **Clone the repository:**
  ```
  git clone <repository-url>
  cd flask-app
  ```

2. **Set up a virtual environment:**
  ```
  python3 -m venv venv
  ```

3. **Activate the virtual environment:**
  - On macOS/Linux:
    ```
    source venv/bin/activate
    ```
  - On Windows:
    ```
    venv\Scripts\activate
    ```

4. **Install the required packages:**
  ```
  pip install -r requirements.txt
  ```

## Python Version

This project uses Python version 3.12.6. Ensure you have this version installed before setting up the virtual environment.

## Running the Application

To run the Flask application, execute the following command:

```
flask run
```

Make sure to set the `FLASK_APP` environment variable to `app` before running the command. You can do this by executing:

- On macOS/Linux:
  ```
  export FLASK_APP=app
  ```
- On Windows:
  ```
  set FLASK_APP=app
  ```

The application will be accessible at `http://localhost:5000`.

## Running Tests

To run the tests, ensure your virtual environment is activated and execute:

```
pytest
```

This will run all the tests defined in the `tests/test_app.py` file.

## API Endpoints

- **POST /reset**: Resets the account balances.
- **GET /balance**: Retrieves the balance for a specific account.
- **POST /event**: Handles deposits, withdrawals, and transfers.

## License

This project is licensed under the MIT License.