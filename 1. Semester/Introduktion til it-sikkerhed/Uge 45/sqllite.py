import sqlite3
from pathlib import Path # read https://realpython.com/python-pathlib/#creating-paths
files_path = Path(str(Path.cwd()) + '/databases/')
print(files_path)

# Create and connect to database
conn = sqlite3.connect(files_path / 'music.db')

cur = conn.cursor()

# Create table in database
with conn:
    cur.execute('DROP TABLE IF EXISTS Tracks')
    cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# Insert rows in tracks table
with conn:
    cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
    cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))

with conn:
    cur.execute('UPDATE Tracks SET title = "Vil du noget?" WHERE title = "Thunderstruck"')

with conn:
    cur.execute('DROP TABLE IF EXISTS artists')
    cur.execute('CREATE TABLE artists (name TEXT)')

for i in range(10):
    with conn:
        cur.execute("INSERT INTO artists (name) VALUES (?)", (f"Band{i}",))
cur.execute("INSERT INTO artists (name) VALUES (?)", (f"Alphabeat",))

cur.execute("DELETE FROM artists WHERE name='Band5';")
# info to user
print('All rows in the Tracks table:')

# select values from table
cur.execute('SELECT title, plays FROM Tracks')

# print out the values
for row in cur:
    print(row)
cur.execute('DELETE FROM Tracks WHERE plays < 100')

cur.execute('SELECT * FROM artists ORDER BY name; ')
for row in cur:
    print(row)


# Close database connection
conn.close()