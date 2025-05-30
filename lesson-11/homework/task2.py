import sqlite3

with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Books")
    cursor.execute("CREATE TABLE Books(Title Text, Author TEXT, Year_Published INTEGER, Genre TEXT)")
    cursor.execute("INSERT INTO Books Values(?, ?, ?, ?)", ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"))
    cursor.execute("INSERT INTO Books Values(?, ?, ?, ?)", ("1984", "George Orwell", 1949, "Dystopian"))
    cursor.execute("INSERT INTO Books Values(?, ?, ?, ?)", ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"))
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    cursor.execute("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", 
                   ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"))
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.8, "To Kill a Mockingbird"))
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.7, "1984"))
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.5, "The Great Gatsby"))
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    for row in cursor.fetchall():
        print(row)

