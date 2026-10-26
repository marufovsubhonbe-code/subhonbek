import sqlite3

con = sqlite3.connect("baza-2.db")
c = con.cursor()

# # jadvl yaratish
# c.execute("""
# CREATE TABLE student(
# id INTEGER PRIMARY KEY,
# name TEXT,
# class TEXT,
# years)
# """)

# con.commit()

# # malumot qo'shish
# c.execute("""
#     INSERT INTO student(id,name,class,years )
#         VALUES(3,"Umarov ismoil","9-B","2011")
# """)
# con.commit()

# # malumot olish

# c.execute("""
#     SELECT * FROM student
# """)

# a = c.fetchall()
# for i in a:
#     print(i)

# c.execute("SELECT * FROM student where id=2")
# a = c.fetchall()
# for i in a:
#     print(i)

# # update qilish
# c.execute("""
#     UPDATE student SET name="MA'RUFOV SUBHONBEK" WHERE id=3
# """)

# con.commit()

c.execute("""
DELETE FROM student where id = 1
""")
con.commit()