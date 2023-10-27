from flask import Flask, render_template
import util

# Create an application instance
app = Flask(__name__)

# evil global variables
username='jethrolibutan'
password='Virtual123!'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/

# index page route
@app.route('/')
def index():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT * from basket_a;")
    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        log = record[:5]
        
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    
    # index.html returned with sql data
    return render_template('index.html', sql_table = log, table_title=col_names)

def insert_into_basket_a():
    #connect to db
    cursor, connection = util.connect_to_db(username,password,host,port,database)

    #trying to execute the sql command
    try:
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        connection.commit()
        return "Success"
        
    except Exception as e:
        return "There was an error. You were not able to add the row to your database."
       
    # disconnect from database
    util.disconnect_from_db(connection,cursor)   

# route to update basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    result = insert_into_basket_a()
    return result


#route to unique
@app.route('/api/unique')
def unique_fruits():
    # initializing the cursor and connection
    cursor, connection = None, None

    try:
        # connect to the db
        cursor, connection = util.connect_to_db(username, password, host, port, database)
    
        # execute sql commands
        record = util.run_and_fetch_sql(cursor, "SELECT fruit_a AS fruit FROM basket_a UNION SELECT fruit_b AS fruit FROM basket_b")
    
        if record == -1:
            # Return an error response
            return "Something is wrong with the SQL command", 500  # Use an appropriate HTTP status code

        col_names = [desc[0] for desc in cursor.description]
        log = record[:7]

        # disconnect from database
        util.disconnect_from_db(connection, cursor)
        
    except Exception as e:
        # returns an error response
        return "There was an error. You could not display the unique fruits!"

    # index.html returned with sql data
    return render_template('index.html', sql_table=log, table_title=col_names)

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)










