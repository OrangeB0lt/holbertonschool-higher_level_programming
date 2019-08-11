#!/usr/bin/python3
''' lists states from DB hbtn_0e_0_usa that starts with letter N '''


if __name__== "__main__":
    from sys import argv
    import MySQLdb
    dataBase = MySQLdb.connect(user=argv[1],
                                passwd=argv[2],
                                dataBase=argv[3])
    
    current = dataBase.cursor()
    current.execute("SELECT * from states WHERE name LIKE
                    'N%' COLLATE latin1_general_cd ORDER BY states.id")
    state_list = current.fetchall()
    for state in state_list:
        print(state)
    current.close()
    dataBase.close()
    