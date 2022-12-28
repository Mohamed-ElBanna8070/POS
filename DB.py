import sqlite3

class DBActions():
    __connection = sqlite3.connect("POS.db", check_same_thread=False)

    @classmethod
    def GetRecords(cls, query:str) -> sqlite3.Cursor:
        resultSet = cls.__connection.execute(query)
        cls.__connection.commit()
        return resultSet

# DBActions.GetRecords("create table Students " 
# "(stdID integer primary key autoincrement, stdFirstName varchar(20), " 
# "stdLastName varchar(50), stdBirthYear integer)")

# DBActions.GetRecords("create table Categories  (ctgID integer primary key autoincrement, ctgName varchar(60),Ctgstate integer ) ")
# DBActions.GetRecords("create table Items  (itmID integer primary key autoincrement, itmName varchar(60),itmprice integer,Itmstate integer) ")