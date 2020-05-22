import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

# cursor.execute('''
# CREATE TABLE users (
#   id INTEGER PRIMARY KEY,
#   name TEXT NOT NULL,
#   email TEXT NOT NULL UNIQUE
# )
# ''')

# cursor.execute("INSERT INTO users (name, email) VALUES ('Some text', 'some@text.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('github', 'github@github.com')")

# cursor.executescript('''
# INSERT INTO users (name, email) VALUES ('github', 'github@github.com')
# INSERT INTO users (name, email) VALUES ('git', 'git@git.com')
# ''')


users = [
  ('User 1', 'user1@user.com'),
  ('User 2', 'user2@user.com'),
  ('User 3', 'user3@user.com')
]

cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

db.commit()


db.close()