#!/usr/bin/python3
''' lists all states in selected DB using SQLAlchemy '''


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=engine)
    sess = Sess()
    for state,city in sess.query(State, City).join(City)\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    sess.close()
