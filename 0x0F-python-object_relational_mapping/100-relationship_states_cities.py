#!/usr/bin/python3
''' makes State "California" with city San Fran '''


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Sess = sessionmaker(bind=engine)
    sess = Sess()
    state = State(name="California", cities=[City(name="San Francisco")])
    sess.add(state)
    sess.commit()
    sess.close()
    