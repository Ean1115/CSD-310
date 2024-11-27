import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "dragonslayed1A2!",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


# Establish a connection to the MySQL database
def connect_to_database():
    connection = mysql.connector.connect(**config)
    return connection


def display_film_contents(cursor, title):
    query = """
    SELECT 
        film.film_name AS Name, 
        film.film_director AS Director, 
        genre.genre_name AS Genre, 
        studio.studio_name AS Studio
    FROM 
        film
    INNER JOIN 
        genre ON film.genre_id = genre.genre_id
    INNER JOIN 
        studio ON film.studio_id = studio.studio_id
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print(f"{title}\n{'-' * len(title)}")
    for row in results:
        print(f"Name: {row['Name']}, Director: {row['Director']}, Genre: {row['Genre']}, Studio: {row['Studio']}")


def execute_query(cursor, query):
    cursor.execute(query)


try:
    db = connect_to_database()
    cursor = db.cursor(dictionary=True)
    print(
        f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

    # Display initial films
    display_film_contents(cursor, "DISPLAYING FILMS")

    # Insert a new record into the film table
    insert_query = """
    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime,film_releaseDate)
    VALUES ('Inception', 'Christopher Nolan', 1, 1, 148,2010)
    """
    execute_query(cursor, insert_query)
    db.commit()
    display_film_contents(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update the film Alien to being a Horror film
    update_query = """
    UPDATE film
    SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
    WHERE film_name = 'Alien'
    """
    execute_query(cursor, update_query)
    db.commit()
    display_film_contents(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete the movie Gladiator
    delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
    execute_query(cursor, delete_query)
    db.commit()
    display_film_contents(cursor, "DISPLAYING FILMS AFTER DELETE")

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    if db.is_connected():
        db.close()