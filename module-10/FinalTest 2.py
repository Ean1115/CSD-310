# Kyle Marlia-Conner

import mysql.connector
from mysql.connector import errorcode

# MySQL connection configuration
config = {
    'user': 'root',
    'password': '#Conner1311995', # Replace with your password, as this is not it.
    'host': 'localhost',  # Replace with your host if not localhost
}

database_name = "LASTTEST"

# Function to create the database
def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Database '{database_name}' created successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{database_name}' already exists.")
        else:
            print(f"Failed to create database: {err}")
            exit(1)

# SQL schema for table creation
sql_schema = [
    "DROP TABLE IF EXISTS Sales;",
    "DROP TABLE IF EXISTS Distributor;",
    "DROP TABLE IF EXISTS Inventory;",
    "DROP TABLE IF EXISTS Supplier;",
    "DROP TABLE IF EXISTS Wine;",
    "DROP TABLE IF EXISTS GrapeVariety;",
    "DROP TABLE IF EXISTS Department;",
    "DROP TABLE IF EXISTS Employee;",
    """
    CREATE TABLE Employee (
        EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(100) NOT NULL,
        LastName VARCHAR(100) NOT NULL,
        Role ENUM('Finance', 'Marketing', 'Production', 'Distribution', 'Owner') NOT NULL,
        DepartmentID INT,
        WorkHours INT
    );
    """,
    """
    CREATE TABLE Department (
        DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
        DepartmentName VARCHAR(100) NOT NULL,
        HeadEmployeeID INT
    );
    """,
    """
    CREATE TABLE GrapeVariety (
        GrapeVarietyID INT PRIMARY KEY AUTO_INCREMENT,
        VarietyName VARCHAR(100) NOT NULL
    );
    """,
    """
    CREATE TABLE Wine (
        WineID INT PRIMARY KEY AUTO_INCREMENT,
        WineType ENUM('Merlot', 'Cabernet', 'Chablis', 'Chardonnay') NOT NULL,
        GrapeVarietyID INT
    );
    """,
    """
    CREATE TABLE Supplier (
        SupplierID INT PRIMARY KEY AUTO_INCREMENT,
        SupplierName VARCHAR(100) NOT NULL,
        DeliveryPerformance DECIMAL(5, 2)
    );
    """,
    """
    CREATE TABLE Inventory (
        InventoryID INT PRIMARY KEY AUTO_INCREMENT,
        ItemType ENUM('Raw Material', 'Finished Product') NOT NULL,
        ItemName VARCHAR(100) NOT NULL,
        Quantity INT NOT NULL,
        ResponsibleEmployeeID INT
    );
    """,
    """
    CREATE TABLE Distributor (
        DistributorID INT PRIMARY KEY AUTO_INCREMENT,
        DistributorName VARCHAR(100) NOT NULL,
        ContactInformation TEXT
    );
    """,
    """
    CREATE TABLE Sales (
        SalesID INT PRIMARY KEY AUTO_INCREMENT,
        WineID INT,
        DistributorID INT,
        SaleDate DATE NOT NULL,
        QuantitySold INT NOT NULL,
        SaleAmount DECIMAL(10, 2) NOT NULL
    );
    """
]

# Adding the Foreign Keys
foreign_key_constraints = [
    """
    ALTER TABLE Inventory
    ADD FOREIGN KEY (ResponsibleEmployeeID) REFERENCES Employee(EmployeeID);
    """,
    """
    ALTER TABLE Sales
    ADD FOREIGN KEY (WineID) REFERENCES Wine(WineID),
    ADD FOREIGN KEY (DistributorID) REFERENCES Distributor(DistributorID);
    """,
    """
    ALTER TABLE Wine
    ADD FOREIGN KEY (GrapeVarietyID) REFERENCES GrapeVariety(GrapeVarietyID);
    """,
    """
    ALTER TABLE Department
    ADD FOREIGN KEY (HeadEmployeeID) REFERENCES Employee(EmployeeID);
    """,
    """
    ALTER TABLE Employee
    ADD FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID);
    """
]

# Employee data to insert
employees = [
    (1, "Scott", "Bacchus", "Owner", 1, 28),
    (2, "John", "Clark", "Finance", 1, 27),
    (3, "James", "Kirk", "Marketing", 4, 35),
    (4, "Joe", "McCarthy", "Marketing", 4, 35),
    (5, "Jane", "Foster", "Production", 5, 44),
    (6, "Johanson", "McDonald", "Distribution", 6, 39)
]

# Department data to insert
departments = [
    (1, "Owner", 1),
    (2, "Sales", 4),
    (3, "Finance", 2),
    (4, "Marketing", 3),
    (5, "Production", 5),
    (6, "Distribution", 6)
]

# GrapeVariety data to insert
grape_varieties = [
    (1, "CabernetFranc"),
    (2, "SauvignonBlanc"),
    (3, "Chardonnay"),
    (4, "Pinot Noir"),
    (5, "GouaisBlanc"),
    (6, "MagdeleineNoireDesCharentes")
]

# Wine data to insert
wines = [
    (1, "Merlot", 1),
    (2, "Cabernet", 2),
    (3, "Chablis", 3),
    (4, "Chardonnay", 4)
]

# Supplier data to insert
suppliers = [
    (1, "BottlesNCorks", 90.5),
    (2, "Pack4You", 80.0),
    (3, "NotHiesenburg", 95.0)
]

# Inventory data to insert
inventory = [
    (1, "Raw Material", "Grapes", 10000, 5),
    (2, "Raw Material", "Bottles", 1000, 1),
    (3, "Raw Material", "Corks", 1000, 1),
    (4, "Raw Material", "Labels", 1000, 1),
    (5, "Raw Material", "Boxes", 1000, 1),
    (6, "Raw Material", "Vats", 1000, 1),
    (7, "Raw Material", "Tubing", 1000, 1),
    (8, "Finished Product", "Wines", 500, 6)
]

# Distributor data to insert
distributors = [
    (1, "Mom'N'Pop_Shop", "(555)980-8855"),
    (2, "Wine'Os", "(555)123-6897"),
    (3, "NineteenthAmendment", "(555)143-6622"),
    (4, "TwoGlassesDown", "(555)420-6969"),
    (5, "TwelveFingers", "(555)326-3825"),
    (6, "TheMixer", "(555)830-3037")
]

# Sales data to insert
sales = [
    (1, 1, 5, '2024-12-08', 10, 150),
    (2, 3, 3, '2024-12-08', 10, 150),
    (3, 5, 3, '2024-12-08', 15, 225),
    (4, 4, 4, '2024-12-08', 17, 255),
    (5, 2, 1, '2024-12-08', 2, 30),
    (6, 2, 2, '2024-12-08', 25, 375)
]

# Connect to MySQL server
try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Create database if it doesn't exist
    create_database(cursor)

    # Switch to the new database
    connection.database = database_name

    # Execute the schema (tables and foreign keys)
    for statement in sql_schema:
        cursor.execute(statement)
    
    for fk in foreign_key_constraints:
        cursor.execute(fk, multi=True)

    # Insert data into the tables
    cursor.executemany("INSERT INTO Employee (EmployeeID, FirstName, LastName, Role, DepartmentID, WorkHours) VALUES (%s, %s, %s, %s, %s, %s);", employees)
    cursor.executemany("INSERT INTO Department (DepartmentID, DepartmentName, HeadEmployeeID) VALUES (%s, %s, %s);", departments)
    cursor.executemany("INSERT INTO GrapeVariety (GrapeVarietyID, VarietyName) VALUES (%s, %s);", grape_varieties)
    cursor.executemany("INSERT INTO Wine (WineID, WineType, GrapeVarietyID) VALUES (%s, %s, %s);", wines)
    cursor.executemany("INSERT INTO Supplier (SupplierID, SupplierName, DeliveryPerformance) VALUES (%s, %s, %s);", suppliers)
    cursor.executemany("INSERT INTO Inventory (InventoryID, ItemType, ItemName, Quantity, ResponsibleEmployeeID) VALUES (%s, %s, %s, %s, %s);", inventory)
    cursor.executemany("INSERT INTO Distributor (DistributorID, DistributorName, ContactInformation) VALUES (%s, %s, %s);", distributors)
    cursor.executemany("INSERT INTO Sales (SalesID, WineID, DistributorID, SaleDate, QuantitySold, SaleAmount) VALUES (%s, %s, %s, %s, %s, %s);", sales)

    connection.commit()
    print("Database, tables, foreign keys, and data inserted successfully.")

    # Fetch and print all tables in the database
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    print("\nTables in the database:")
    for table in tables:
        print(f"- {table[0]}")

    print("\nContents of each table:")

    # For each table, select and display its contents
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        
        # Fetch all rows from the current table
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        # Get column names
        cursor.execute(f"DESCRIBE {table_name};")
        columns = cursor.fetchall()
        column_names = [column[0] for column in columns]

        # Print column names
        print(f"Columns: {', '.join(column_names)}")

        # Print rows
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data in this table.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
