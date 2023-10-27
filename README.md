## HW3
This is a Flask application that connects to a PostgreSQL database and provides two functional requirements

**Group Members**:
  Darian O'Dirling, 
Jethro Libutan

**Update Basket A**

When a user accesses the Flask server with /api/update_basket_a, it inserts a new row (5, 'Cherry') into the basket_a table in the database.
        It will display "Success!" if the insertion is successful, or an error message from PostgreSQL if there is a problem.

**Unique Fruits**

When a user accesses the Flask server with /api/unique, it displays unique fruits from the basket_a and basket_b tables in an HTML table.
In case of any errors from PostgreSQL, it shows the error message on the browser.

**Access the Application**    

Open your web browser and go to http://127.0.0.1:5000/api/update_basket_a to insert a new row into basket_a.
Access http://127.0.0.1:5000/api/unique to see unique fruits in an HTML table from both basket_a and basket_b.

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```
