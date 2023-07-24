import sqlite3
from account import Account

connection = sqlite3.connect("passmanager.db")
c = connection.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS accounts (
          password text,
          user text,
          email text,
          site text
        )""")

connection.commit()

def insertAccount(account):
  with connection:
    c.execute("INSERT INTO accounts VALUES (:password, :user, :email, :site)",
              {'password':account.password, 'user':account.username, 'email':account.email, 'site':account.appname})

def getAccountbySite(site):
  c.execute("SELECT * FROM accounts WHERE site=site")

def updateAccountPass(account, password):
  with connection:
    c.execute("""UPDATE accounts SET password = :password
              WHERE user = :user AND email = :email AND site=:site""",
              {'user':account.username, 'email':account.email, 'site':account.appname, 'password':password})

def printResult():
  results = c.fetchall() #list of results
  for r in results:
    print(f">> [{r[2]}]- user:{r[1]}, password:{r[0]}")

acc_1 = Account("me", "securepassword", "me@gmail.com", "google")

# insertAccount(acc_1)
getAccountbySite("google")
printResult()

connection.close()
