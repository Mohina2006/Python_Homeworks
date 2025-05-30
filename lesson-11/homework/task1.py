import sqlite3

with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, Age INTEGER)")
    cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ("Benjamin Sisko", "Human", 40))
    cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ("Jadzia Dax", "Trill", 300))
    cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ("Kira Nerys", "Bajoran", 29))
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
    for row in cursor.fetchall():
        print(row)
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    cursor.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", ("Ezri Dax", "Trill", 300))
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ("Captain", "Benjamin Sisko"))
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ("Lieutenant", "Ezri Dax"))
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ("Major", "Kira Nerys"))
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    for row in cursor.fetchall():
        print(row)
