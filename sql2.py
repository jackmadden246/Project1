import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
            VALUES (1, 'Anna', 35, 'London', 10000.00)");
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
            VALUES (2, 'John',25, 'Lichfield', 85000.00)");
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
            VALUES (3, 'Maria',29, 'Cambridge', 60000.00)");
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
            VALUES (4, 'Sam',25, 'Sunderland', 20000.00)");
conn.commit()
print('Records created successfully');
conn.close()