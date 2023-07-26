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
                "site": account.site,
            },
        )


def getAccountbySite(site):
    c.execute("SELECT * FROM accounts WHERE site=:site", {"site": site})


def updateAccountPass(site, email, password):
    with connection:
        c.execute(
            """UPDATE accounts SET password = :password
              WHERE email = :email AND site=:site""",
            {
                "password": password,
                "email": email,
                "site": site,
            }
        )


def print_query_results():
    rows = c.fetchall()
    if not rows:
        print("No results found.")
    else:
        headers = [i[0] for i in c.description]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))

def generateSiteList():
    c.execute("SELECT * FROM accounts")
    site_list = []
    site_string = "| "
    for row in c.fetchall():
        site_list.append(row[3])
        site_string += row[3] + " | "
    return (site_list, site_string + "\n")
        
def createAccount():
    username = input(">>Input username: ")
    password = input(">>Input password: ")
    email = input(">>Input email: ")
    site = input(">>Input site name: ")
    return Account(username, password, email, site)

acc_1 = Account("me", "securepassword", "me@gmail.com", "google")

# insertAccount(acc_1)
# getAccountbySite("google")
# print_query_results()

if __name__ == "__main__":
    command = 0
    command_display = "| exit | quit | insert | update | get |\n"

    while command != "exit" and command != "quit":
        command = str(input(">>Input master password: "))
        if command != "master":
            pass
        else:
            while command != "exit" and command != "quit":
                print(command_display)  # display commands
                command = str(input(">>Input command: "))
                if command == "insert":
                    insertAccount(createAccount())
                elif command == "get":
                    site_list = generateSiteList()[0]
                    site_string = generateSiteList()[1]
                    print(site_string)  # display sites
                    command = str(input(">>Input the site you would like to receive credentials of: "))
                    if command in site_list:
                        getAccountbySite(command)
                        print_query_results()
                elif command == "update":
                    site = input(">>Input the site of the password to change: ")
                    email = input(">>Input the email of the password to change: ")
                    password = input(">>Input new password: ")
                    updateAccountPass(site, email, password)
                else:
                    print("!! Invalid command.")
                    
        print("! Exiting Password Manager. Goodbye.")


    connection.close()
