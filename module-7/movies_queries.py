
import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "root",
    "password": "dragonslayed1A2!",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


import mysql.connector

# Establish a connection to the MySQL database
def connect_to_database():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="dragonslayed1A2!",
        database="movies"
    )
    return connection

# Function to execute a query and fetch all results
def execute_query(query):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# Query 1: Select all fields from the studio table
query1 = "SELECT * FROM studio"
studio_results = execute_query(query1)
print("Studio Table:")
for row in studio_results:
    print(row)

# Query 2: Select all fields from the genre table
query2 = "SELECT * FROM genre"
genre_results = execute_query(query2)
print("\nGenre Table:")
for row in genre_results:
    print(row)

# Query 3: Select movie names for movies with a runtime of less than two hours
query3 = "SELECT film.film_name FROM film WHERE film.film_runtime < 120"
short_movies_results = execute_query(query3)
print("\nMovies with Runtime Less Than Two Hours:")
for row in short_movies_results:
    print(row)

# Query 4: Get a list of film names and directors grouped by director
query4 = "SELECT film_director, GROUP_CONCAT(film_name) FROM film GROUP BY film_director"

movies_by_director_results = execute_query(query4)
print("\nMovies Grouped by Director:")
for row in movies_by_director_results:
    print(row)





try:
    db = mysql.connector.connect(**config)
    print("Database user {user} connected to MYSQL on host {host} with database {database}".format(
        user=config["user"], host=config["host"], database=config["database"]))

    input("Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    connector.close()