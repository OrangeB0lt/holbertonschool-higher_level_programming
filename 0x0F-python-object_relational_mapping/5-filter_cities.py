#!/usr/bin/python3
''' lists cities ''' of names state


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
    sql = "SELECT cities.name FROM \
        cities JOIN states ON cities.state_id = states.id WHERE \
        states.name = '{}'".format(state_name)

    curs.execute(sql)

    results = []
    for city in curs.fetchall():
        results.append(city[0])
    results = ", ".join(results)

    print(results)

    curs.close()
    db.close()
    