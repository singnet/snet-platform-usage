from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PWD, DB_HOST, DB_NAME, DB_DRIVER

engine = create_engine(f"{DB_DRIVER}://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}")

Session = sessionmaker(bind=engine)
default_session = Session()


class BaseRepository:

    def __init__(self):
        self.session = default_session

    def add_item(self, item):
        try:
            self.session.add(item)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def add_all_items(self, items):
        try:
            self.session.add_all(items)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
