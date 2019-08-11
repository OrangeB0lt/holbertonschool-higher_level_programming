#!/usr/bin/python3
''' lists states from DB hbtn_0e_0_usa that match a query from CL arg 
protects against sql injection
'''



if __name__ == "__main__":
    from sys import argv
    userN = argv[1]
    password = argv[2]
    dataBase = argv[3]
    state_name = argv[4]

    if ';' in state_name:
        print('nice try.')
        exit()

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=userN, \
        passwd=password, db=dataBase)
    curs = db.cursor()
    sql = "SELECT * FROM states WHERE name = '{}' \
        ORDER BY id ASC".format(state_name,)

    curs.execute(sql)

    for row in curs.fetchall():
        print(row)

    curs.close()
    db.close()
    