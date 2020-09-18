import psycopg2

def create_table(table_name):
    connection = psycopg2.connect(user='postgres',\
                                  password='1995',
                                  host='localhost',
                                  port='5432',
                                  database='django_project')
    print('Connection created ...')
    cursor = connection.cursor()
    print('Cursor created...')

    # Drop the table if exists
    drop_query = "DROP TABLE IF EXISTS {};".format(table_name)
    cursor.execute(drop_query)

    # Create the table
    print('Creating Table')
    create_query = "CREATE TABLE {}(\
                    ID CHARACTER VARYING NOT NULL PRIMARY KEY,\
                    Email CHARACTER VARYING,\
                    Password CHARACTER VARYING);".format(table_name)
    cursor.execute(create_query)

    connection.commit()
    cursor.close()
    connection.close()
    print('Successful ... ')

# create_table('user_info')

def update_table(table_name,user_id,user_email,user_password):
    connection = psycopg2.connect(user='postgres',\
                                  password='1995',
                                  host='localhost',
                                  port='5432',
                                  database='django_project')
    print('Connection created ...')
    cursor = connection.cursor()
    print('Cursor created...')


    # Insert a row
    create_query = "INSERT INTO {}\
                    VALUES('{}','{}','{}');".format(table_name,user_id,user_email,user_password)
    cursor.execute(create_query)

    connection.commit()
    cursor.close()
    connection.close()
    print('Successful ... ')

# update_table('user_info','12345678','test@gmail.com','1234567890abcdef')