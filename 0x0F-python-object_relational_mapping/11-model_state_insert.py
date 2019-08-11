#!/usr/bin/python3
''' adds a new state in a CL query '''


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=engine)
    sess = Sess()
    louisiana = State(name='Louisiana')
    sess.add(louisiana)
    sess.commit()
    print(louisiana.id)
