#!/usr/bin/python3
''' displays states in a CL query '''


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=engine)
    sess = Sess()
    for instance in session.query(State).order_by(State.id):
        if instance.name == state_name:
            print(instance.id)
            exit()
    print('Not found')
