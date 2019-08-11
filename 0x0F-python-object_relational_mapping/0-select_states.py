#!/usr/bin/python3
''' Lists states from database hbtn_0e_0_usa'''


if __name__ == "__main__":
    from sys import argv
    userN = argv[1]
    password = argv[2]
    dataBase = argv[3]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=userN,
                        passwd=password, db=dataBase)
    curs = db.cursor()
    curs.execute('SELECT * FROM states ORDER BY id ASC')
    for row in curs.fetchall():
        print(row)

