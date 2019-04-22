#! /usr/bin/env python


import MySQLdb




class DB(object):
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db

        self._connect()


    def _connect(self):
        self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset='utf8')
        cursor = self.conn.cursor()
        
        
        self.conn.commit()


    def _reconnect(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute('SET NAMES utf8mb4')
        except:
            self._connect()


    def query(self, sql):
        cursor = self.conn.cursor()

        rows = None
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
        except:
            self._reconnect()
            
            print "query failed"
            return None
        else:
            return rows



    def getNM(self):
       
        sql = """SELECT DrugID, NameMain
            FROM Drug"""
            

        rows = db.query(sql)

        res=[]

        for row in rows:
            res.append(list(row))

        return res

    def getNG(self):
       
        sql = """SELECT DrugID, NamesGeneric
            FROM Drug"""
            

        rows = db.query(sql)

        res=[]

        for row in rows:
            res.append(list(row))

        return res

    def getNB(self):
       
        sql = """SELECT DrugID, NamesBrand
            FROM Brand"""
            

        rows = db.query(sql)

        res=[]

        for row in rows:
            res.append(list(row))

        return res

    def getNC(self):
       
        sql = """SELECT DrugID, NamesCode
            FROM Drug"""
            

        rows = db.query(sql)

        res=[]

        for row in rows:
            res.append(list(row))

        return res


    def getMC(self):
       
        sql = """SELECT MechID, MechName
            FROM Mechanism"""
            

        rows = db.query(sql)
        res=[]

        for row in rows:
            res.append(list(row))



        return res


        


        

    def close(self):
        self.conn.close()



    


db = DB('localhost', 3306, 'root', '940216', 'Genospace')
