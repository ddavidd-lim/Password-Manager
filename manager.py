import sqlite3
import hashlib
from tabulate import tabulate
from account import Account

connection = sqlite3.connect("passmanager.db")
c = connection.cursor()


c.execute(
    """CREATE TABLE IF NOT EXISTS accounts (
          password text,
          user text,
          email text,
          site text
        )"""
)

connection.commit()


def insertAccount(account):
    with connection:
        c.execute(
            "INSERT INTO accounts VALUES (:password, :user, :email, :site)",
            {
                "password": account.password,
                "user": account.username,
                "email": account.email,
                "site": account.appname,
            },
        )


def getAccountbySite(site):
    c.execute("SELECT * FROM accounts WHERE site=:site", {"site": site})


def updateAccountPass(account, password):
    with connection:
        c.execute(
            """UPDATE accounts SET password = :password
              WHERE user = :user AND email = :email AND site=:site""",
            {
                "user": account.username,
                "email": account.email,
                "site": account.appname,
                "password": password,
            },
        )
    account.password = password


def print_query_results():
    rows = c.fetchall()
    if not rows:
        print("No results found.")
    else:
        headers = [i[0] for i in c.description]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))


acc_1 = Account("me", "securepassword", "me@gmail.com", "google")

# insertAccount(acc_1)
# getAccountbySite("google")
# print_query_results()

command = "none"
while command != "exit" or command != "quit":
    command = str(input(">>Input master password\n"))
    if command != "master":
        pass
    else:
        print("ok you did it correctly")
        while command != "exit" or command != "quit":
            command = str(input(">>Input the site you would like to receive credentials of.\n"))


connection.close()
