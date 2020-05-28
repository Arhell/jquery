import sqlite3

def dict_factory(cursor, row):
  d = ()
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

db = sqlite3.connect('test_db.sqlite')
db.row_factory = dict_factory
cursor = db.cursor()

email = 'some@text.com'

# cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?, (email, 'github')")
cursor.execute("SELECT * FROM users")

# res = cursor.fetchone()
res = cursor.fetchall()

print(res)

for user in res:
  print(user["name"], user["email"])


db.close()