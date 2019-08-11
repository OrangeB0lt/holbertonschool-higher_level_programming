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
    state = sess.query(State).filter(
            State.name == argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()