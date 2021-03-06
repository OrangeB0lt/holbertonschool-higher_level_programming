#!/usr/bin/python3
''' lists all states in DB hbtn_0e_0_usa using SQLAlchemy '''


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=engine)
    sess = Sess()
    for instance in sess.query(State).order_by(State.id):
        if 'a' in instance.name:
            print('{}: {}'.format(instance.id, instance.name))
    sess.close()
