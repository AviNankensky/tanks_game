
import pyodbc


global conn
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=MY_COMPUTER_AVI\\SQLEXPRESS;"
    "Database=TanksGame;"
    "Trusted_Connection=yes;"
)


def adds_a_user(name, pas):

    if not checks_if_user_exists(name, pas):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO PLAYERS (PlayerName, PlayerPassword) VALUES (?, ?);", (name, pas))
        cursor.execute(
            "INSERT INTO GameStats (PlayerName, Score, Coins ,Heart ,Level) VALUES (?, ?, ? , ? ,?);", (name, 0, 0, 3, 1))

        conn.commit()
    #     print(f"User {name} added successfully.")
    # else:
    #     print(f"User {name} already exists.")


def return_how_is_not_exists(name, password):

    cursor = conn.cursor()
    cursor.execute("""
        SELECT 1 
        FROM PLAYERS 
        WHERE PlayerName COLLATE Latin1_General_CI_AS = ? 
        
    """, (name))
    result = cursor.fetchone()
    if result is not None:
        return (f"the password --{password}-- is not exists \n")

    cursor.execute("""
        SELECT 1 
        FROM PLAYERS 
        WHERE PlayerPassword COLLATE Latin1_General_CI_AS = ? 
        
    """, (password))
    result = cursor.fetchone()
    if result is not None:
        return (f"the name --{name}-- is not exists \n")
    return "One or more of the details is incorrect ;\n"


def checks_if_user_exists(name, password):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 1 
        FROM PLAYERS 
        WHERE PlayerName COLLATE Latin1_General_CI_AS = ? 
        AND PlayerPassword = ?
    """, (name, password))

    result = cursor.fetchone()
    return result is not None


def checks_input(input_name, input_password, type_):
    error_m = ""
    if input_name == "name" or input_password == "password" or input_name == "" or input_password == "":
        error_m += "One or more of the details is missing ;\n"

    if len(input_name) > 0 and (len(input_password) == 0 or input_password == "password"):
        error_m += "Please enter a password ;\n"

    if len(input_password) > 0 and (len(input_name) == 0 or input_name == "name"):
        error_m += "Please enter a username ; \n"
    # print(ord(input_name[0]),"____________________test",ord(input_name[1]))
    if type_ == "log in":
        if checks_if_user_exists(input_name, input_password):
            error_m += (f"The user --{input_name}-- is already exists ; \n")
            error_m += return_how_is_not_exists(input_name, input_password)
    if type_ == "sing up":
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 1 
            FROM PLAYERS 
            WHERE PlayerName COLLATE Latin1_General_CI_AS = ? 
            
        """, (input_name))
        result = cursor.fetchone()
        if result is not None:
            error_m += (f"The user --{input_name}-- is already exists ; \n")

    # for i in range(len(input_password)):
    #     print(input_password[i])
    #     if ord(input_password[i])>ord("9") or ord(input_password[i])<ord("0"):
    #         error_m+=(f"The password--{input_name}-- is not valid ;     ")
    return error_m


class Information():
    def __init__(self, conn=None, name="", score=0, coins=0, password="0", heart=0, level=0):
        self.coins = coins
        self.name = name
        self.password = password
        self.score = score
        self.conn = conn
        self.heart = heart
        self.level = level
        self.data_connect = False
        if len(self.name) > 0:
            self.pull()

    def pull(self):
        # if checks_if_user_exists(self.name," "):
        cursor = self.conn.cursor()
        # cursor.execute("SELECT 1 FROM PLAYERS WHERE PlayerName COLLATE Latin1_General_CI_AS = ? ", (self.name))

        # if cursor.fetchone():
        if checks_if_user_exists(self.name, self.password):
            self.data_connect = True
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM GameStats WHERE PlayerName = ?;", (self.name))
            for row in cursor:
                self.name = row[1]
                self.score = row[2]
                self.coins = row[3]
                self.level = row[4]
                self.heart = row[5]
            self.conn.commit()

    def push(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT 1 FROM GameStats WHERE PlayerName COLLATE Latin1_General_CI_AS = ? ", (self.name))
        if cursor.fetchone():
            cursor = self.conn.cursor()
            cursor.execute("UPDATE GameStats SET Score = ?, Coins = ? ,Heart = ? ,Level = ? WHERE PlayerName = ?;",
                           (self.score, self.coins, self.heart, self.level , self.name ))
        # else:
        #     cursor.execute("INSERT INTO GameStats (PlayerName, Score, Coins) VALUES (?, ?, ?);", (self.name, self.score,self.coins))
        self.conn.commit()
    def toString_(self):
        return "name",self.name,"password",self.password,"level",self.level,"coins",self.coins

global data

data = Information(conn)
data.pull()
# print(data.coins)
# data.pull()
# print(checks_if_user_exists(" meir","5b9"))

# data = Information(conn)
# data.pull()
# data = Information(conn," meir" ,100,100)

# print(a.name,a.coins)
# a.update_data()


# def read(conn):
#     print("read")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM PLAYERS AS P")
#     for row in cursor:
#         print(row)
# read(conn)
