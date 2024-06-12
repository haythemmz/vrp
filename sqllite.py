import sqlite3

# Function to create tables if they don't exist
def create_tables(conn):
    cursor = conn.cursor()

    # Create Vehicles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vehicles (
            VehicleID INTEGER PRIMARY KEY,
            Capacity FLOAT
        )
    ''')

    # Create Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INTEGER PRIMARY KEY,
            Name TEXT
        )
    ''')

    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            ProductID INTEGER PRIMARY KEY,
            Weight FLOAT
        )
    ''')

    # Create CustomerDemands table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CustomerDemands (
            CustomerID INTEGER,
            ProductID INTEGER,
            Demand INTEGER,
            PRIMARY KEY (CustomerID, ProductID),
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
            FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
        )
    ''')

    # Create TimeWindows table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TimeWindows (
            CustomerID INTEGER,
            Day TEXT,
            StartHour INTEGER,
            EndHour INTEGER,
            PRIMARY KEY (CustomerID, Day, StartHour, EndHour),
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        )
    ''')

    # Create Distances table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Distances (
            FromID INTEGER,
            ToID INTEGER,
            Distance FLOAT,
            TravelTime FLOAT,
            PRIMARY KEY (FromID, ToID),
            FOREIGN KEY (FromID) REFERENCES Locations(LocationID),
            FOREIGN KEY (ToID) REFERENCES Locations(LocationID)
        )
    ''')

    # Create Deadlines table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Deadlines (
            CustomerID INTEGER PRIMARY KEY,
            Deadline TEXT,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        )
    ''')

    conn.commit()

# Function to insert data into tables
def insert_data(conn):
    cursor = conn.cursor()

    # Example data
    vehicles_data = [
        (1, 100),
        (2, 100)
    ]

    customers_data = [
        (1, 'Customer A'),
        (2, 'Customer B')
    ]

    products_data = [
        (1, 10.0),
        (2, 20.0)
    ]

    customer_demands_data = [
        (1, 1, 2),
        (1, 2, 1),
        (2, 1, 1),
        (2, 2, 1)
    ]

    time_windows_data = [
        (1, '2024-06-08', 8, 15),
        (1, '2024-06-10', 9, 18),
        (2, '2024-06-09', 10, 13),
        (2, '2024-06-11', 11, 14)
    ]

    distances_data = [
        (1, 2, 15.0, 1.5),
        (1, 3, 25.0, 2.5),
        (2, 3, 35.0, 3.5)
    ]

    deadlines_data = [
        (1, '2024-06-15'),
        (2, '2024-06-18')
    ]

    # Insert data into Vehicles table
    cursor.executemany('INSERT INTO Vehicles (VehicleID, Capacity) VALUES (?, ?)', vehicles_data)

    # Insert data into Customers table
    cursor.executemany('INSERT INTO Customers (CustomerID, Name) VALUES (?, ?)', customers_data)

    # Insert data into Products table
    cursor.executemany('INSERT INTO Products (ProductID, Weight) VALUES (?, ?)', products_data)

    # Insert data into CustomerDemands table
    cursor.executemany('INSERT INTO CustomerDemands (CustomerID, ProductID, Demand) VALUES (?, ?, ?)', customer_demands_data)

    # Insert data into TimeWindows table
    cursor.executemany('INSERT INTO TimeWindows (CustomerID, Day, StartHour, EndHour) VALUES (?, ?, ?, ?)', time_windows_data)

    # Insert data into Distances table
    cursor.executemany('INSERT INTO Distances (FromID, ToID, Distance, TravelTime) VALUES (?, ?, ?, ?)', distances_data)

    # Insert data into Deadlines table
    cursor.executemany('INSERT INTO Deadlines (CustomerID, Deadline) VALUES (?, ?)', deadlines_data)

    conn.commit()

# Main function to connect to SQLite and run the script
def main():
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('vrp.db')

        # Create tables if they don't exist
        #create_tables(conn)

        # Insert data into tables
        insert_data(conn)

        print("Data inserted successfully.")
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
