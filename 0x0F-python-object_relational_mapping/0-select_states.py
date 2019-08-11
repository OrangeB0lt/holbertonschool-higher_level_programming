#!/usr/bin/python3
''' Lists states from database hbtn_0e_0_usa'''


if __name__ == "__manin__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                        passwd=argv[2],
                        db=arvg[3])
    current = db.cursor()
    current.execute("SELECT * from states ORDER BY states.id")
    state_list = current.fetchall()
    for state in state_list:
        print(state)
    current.close()
    db.close()
    