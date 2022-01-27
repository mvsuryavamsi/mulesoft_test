#import required modules
import mysql.connector
import pandas as pd


#creating mysql database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="vamsi",
    password="V@msi495",
    database="python"
)

#create Database cursor
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM information_schema.tables WHERE table_name = 'Movies'")
myresult = mycursor.fetchall()

'''
This dispy() is used to retrive all movies data from the movies table.
'''

def dispy():
    mycursor.execute('SELECT * FROM movies');
    dis = mycursor.fetchall()
    field = [i[0] for i in mycursor.description]
    df1 = pd.DataFrame(dis, columns=field)
    print(df1)

#This Actor_Name() accepts 'actor name' as the parameter and retrives and print all the movies acted by the actor.
def Actor_Name(name):
    mycursor.execute("select * from  Movies where Actor_Name =" + "\'" + name + "\'")
    ply = mycursor.fetchall()
    field = [i[0] for i in mycursor.description]
    df2 = pd.DataFrame(ply, columns=field)
    print(df2)


n = int(input('''
    1.Display All Movies
    2.Enter Actor Name to get movies
    '''))

if n == 1:
    dispy()
elif n == 2:
    name = input("Enter Actor name\n")
    Actor_Name(name)
