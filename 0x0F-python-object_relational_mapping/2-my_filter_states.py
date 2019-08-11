#!/usr/bin/python3
''' lists states from DB hbtn_0e_0_usa that match a query from CL arg '''


if __name__ == "__main__":
    from sys import argv
    userN = argv[1]
    password = argv[2]
    dataBase = argv[3]
    state_name = argv[4]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=userN, \
        passwd=password, db=dataBase)
    curs = db.cursor()
    sql = "SELECT * FROM states WHERE name = '{}' \
        ORDER BY id ASC".format(state_name,)

    curs.execute(sql)

    for row in curs.fetchall():
        if row[1][0] == 'N':
            print(row)

    curs.close()
    db.close()
    