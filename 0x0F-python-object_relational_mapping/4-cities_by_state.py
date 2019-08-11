#!/usr/bin/python3
''' lists states from DB hbtn_0e_0_usa that match a query from CL arg '''


if __name__ == "__main__":
    from sys import argv
    userN = argv[1]
    password = argv[2]
    dataBase = argv[3]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=userN, \
        passwd=password, db=dataBase)
    curs = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM \
            cities JOIN states on cities.state_id = states.id"

    curs.execute(sql)

    for row in curs.fetchall():
        print(row)

    curs.close()
    db.close()
    