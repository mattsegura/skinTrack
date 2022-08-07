import sqlite3

# if there is no DB create it
# else connect
con = sqlite3.connect("example.db")
cur = con.cursor()

# execute sql queries
cur.execute(
    """CREATE TABLE IF NOT EXISTS tshirts
                (sku text, name text, size text, price real)"""
)

# add some data
cur.execute(
    """INSERT INTO tshirts VALUES 
                ('SKU1234', 'Black Logo Tshirt', 'Medium', '24.99')"""
)

con.commit()

# fetch everything in DB
for row in cur.execute("""SELECT * FROM tshirts"""):
    print(row)
