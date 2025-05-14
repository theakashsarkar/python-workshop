import sqlite3

con = sqlite3.connect('mytest.db')
cur = con.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS book(name text, author text, price real)")
# cur.execute("INSERT INTO book VALUES('PYTHON 3 BOOK', 'Tamim Shariar', 260)")
# book_list = [
#   ('PYTHON book 2', 'Tamim Shariar', 250),
#   ('PYTHON book 4', 'Tamim Shariar', 260),
# ]
# cur.executemany("INSERT INTO book VALUES(?, ?, ?)", book_list)
# cur.close()
# con.commit()
# con.close()

def search_by_author(cur, author):
  # cur.execute("SELECT * FROM book WHERE author = '" + author + "'")
  query = "SELECT * FROM book WHERE author = ?"(author)
  cur.execute(query)
  return cur.fetchall()
  
cur.execute("SELECT * FROM book")
row = cur.fetchone()
while row:
  print(row)
  row = cur.fetchone()
cur.close()
con.commit()
con.close()