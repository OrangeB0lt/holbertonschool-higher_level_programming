#!/usr/bin/python3
''' lists states from DB hbtn_0e_0_usa that starts with letter N '''


if __name__ == "__main__":
    from sys import argv
    userN = argv[1]
    password = argv[2]
    dataBase = argv[3]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=userN,
        passwd=password, db=dataBase)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in curs.fetchall():
        if row[1][0] == 'N':
            print(row)

    curs.close()
    db.close()
    