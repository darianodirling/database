from flask import Flask, render_template
import util

# create an application instance
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='darian'
password='1563'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/')
# this is how you define a function in Python

def index():
    # this is your index page
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT * from basket_a;")
    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        log = record[:5]
        # log=[[1,2],[3,4]]
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
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
    
# Route to update basket_a


@app.route('/api/update_basket_a', methods=['GET'])
def update_basket_a():
    result = insert_into_basket_a()
    return result


@app.route('/api/unique')
def unique_fruits():
    cursor, connection = util.connect_to_db(username, password, host, port, database)

    # Execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT fruit_a AS fruit FROM basket_a UNION SELECT fruit_b AS fruit FROM basket_b;")

    if record == -1:
        # You can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # This will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = [desc[0] for desc in cursor.description]
        # Only use the first five rows
        log = record[:7]
        # log=[[1,2],[3,4]]

    # Disconnect from the database
    util.disconnect_from_db(connection, cursor)

    # Using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', sql_table=log, table_title=col_names)




@app.route('/test')
def test():
    return 'test'

if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)