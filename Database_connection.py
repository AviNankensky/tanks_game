import os
import sqlite3
import traceback

try:
    
    conn = sqlite3.connect('Databases/data.sqlite')
except Exception as e:
    log_error(f"Error occurred: {str(e)}")  

def adds_a_user(name, pas):

    if not checks_if_user_exists(name, pas):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO PLAYERS (PlayerName, PlayerPassword) VALUES (?, ?);", (name, pas))

        cursor.execute(
            "INSERT INTO GameStats (PlayerName, Score, Coins ,Heart ,Level) VALUES (?, ?, ? , ? ,?);", (name, 0, 0, 3, 1))

        cursor.execute(
            "INSERT INTO PlayerProducts (PlayerName) VALUES (?);", (name))

        conn.commit()



def check_user_credentials(name, password):
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT PlayerPassword
        FROM 'dbo.PLAYERS'
        WHERE LOWER(PlayerName) = LOWER(?)
    """, (name,))
    result = cursor.fetchone()
    
    if result is None:
        return f"The username '{name}' does not exist.\n"
    
    stored_password = result[0]
    if password != stored_password:
        return f"The password for user '{name}' is incorrect.\n"
    
    return "One or more of the details is incorrect ;\n"

def checks_if_user_exists(name, password):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 1
        FROM 'dbo.PLAYERS'
        WHERE LOWER(PlayerName) = LOWER(?)
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

    if type_ == "log in":
        if checks_if_user_exists(input_name, input_password):
            error_m += (f"The user --{input_name}-- is already exists ; \n")
            error_m += check_user_credentials(input_name, input_password)
    if type_ == "sign up":
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 1
            FROM PLAYERS
            WHERE LOWER(PlayerName) = LOWER(?)
        """, (input_name,))
        result = cursor.fetchone()
        if result is not None:
            error_m += f"The user '{input_name}' already exists;\n"

    return error_m


class ShopDate():
    def __init__(self, name, conn):
        self.conn = conn
        self.ice = 0
        self.tnt = 0
        self.hart = 1
        self.playerName = name


    def pull(self, newName=""):
        if newName != "":
            self.playerName = newName
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM 'dbo.PlayerProducts' WHERE PlayerName = ?", (self.playerName,))
        row = cursor.fetchone()
        if row:
            self.ice = int(row[1])
            self.tnt = int(row[2])
            self.hart = int(row[3])
        self.conn.commit()
        self.push()

    def push(self):

        cursor = self.conn.cursor()
        cursor.execute('UPDATE "dbo.PlayerProducts" SET Ice = ?, Tnt = ?, Heart = ? WHERE PlayerName = ?; ',
                       (self.ice, self.tnt, self.hart, self.playerName))

        self.conn.commit()


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
        self.shopDate = ShopDate("", self.conn)

    def pull(self):
        cursor = self.conn.cursor()
        if checks_if_user_exists(self.name, self.password):
            if self.shopDate.playerName == "":
                self.shopDate.pull(self.name)
            else:
                self.shopDate.pull()
            self.data_connect = True
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM 'dbo.GameStats' WHERE PlayerName = ?;", (self.name,))
            row = cursor.fetchone()
            if row:
            # for row in cursor:
                self.name = row[1]
                self.score = row[2]
                self.coins = int(row[3])
                self.level = int(row[4])
                self.heart = int(row[5])
            self.conn.commit()

    def push(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT 1 FROM 'dbo.GameStats' WHERE LOWER(PlayerName) = LOWER(?)", (self.name,))
        if cursor.fetchone():
            cursor.execute("""
                UPDATE 'dbo.GameStats' 
                SET Score = ?, Coins = ?, Heart = ?, Level = ? 
                WHERE LOWER(PlayerName) = LOWER(?)
            """, (self.score, self.coins, self.heart, self.level, self.name))
        else:
            cursor.execute("""
                INSERT INTO 'dbo.GameStats' (PlayerName, Score, Coins, Heart, Level) 
                VALUES (?, ?, ?, ?, ?)
            """, (self.name, self.score, self.coins, self.heart, self.level))
        self.conn.commit()

    def toString_(self):
        return "name", self.name, "password", self.password, "level", self.level, "coins", self.coins


global data

data = Information(conn)
