
import pyodbc


global conn
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=MY_COMPUTER_AVI\\SQLEXPRESS;"
    "Database=TanksGame;"
    "Trusted_Connection=yes;"
)

def adds_a_user(name, pas):
    if not checks_if_user_exists(name):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PLAYERS (PlayerName, PlayerPassword) VALUES (?, ?);", (name, pas))
        conn.commit()
        print(f"User {name} added successfully.")
    else:
        print(f"User {name} already exists.")

def checks_if_user_exists(name):
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM PLAYERS WHERE PlayerName COLLATE Latin1_General_CI_AS = ?", (name,))
    if cursor.fetchone():
        return True
    return False






# import pyodbc
# global conn
# conn = pyodbc.connect(
    
#     "Driver={SQL Server};"
#     "Server=MY_COMPUTER_AVI\SQLEXPRESS;"
#     "Database=TanksGame;"
#     "Trusted_Connection=yes;"

# )

# def adds_a_user(name,pas):
#     cursor = conn.cursor()
#     cursor.execute(F"INSERT  INTO PLAYERS (PlayerName,PlayerPassword) VALUES(?,?);" ,(name, pas))
#     conn.commit()

# def checks_if_user_exists(name,pas):
#     name="('"+name+"',)"
#     pas="("+pas+",)"
#     nameExists=False
#     pasExists=False
#     cursor = conn.cursor()
#     cursor.execute("SELECT P.PlayerName FROM PLAYERS AS P")
#     for row in cursor:
#         if str(row) == name:
#             nameExists=True


#     cursor.close()
#     cursor = conn.cursor()
#     cursor.execute("SELECT P.PlayerPassword FROM PLAYERS AS P")
#     print(pas,"-------------------")
#     for row in cursor:
#         print(row)
#         if str(row) == pas:
#             pasExists=True
#     if nameExists and pasExists:
#         return True
    
#     return False
# print(checks_if_user_exists("AVI","65"))
# # def read(conn):
# #     print("read")
# #     cursor = conn.cursor()
# #     cursor.execute("SELECT P.PlayerName FROM PLAYERS AS P")
# #     for row in cursor:
# #         print(row)
# # read(conn)

# # cursor.close()
# #conn.close()