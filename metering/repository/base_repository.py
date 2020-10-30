from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PWD, DB_HOST, DB_NAME, DB_DRIVER
from utils import db_exception_handler

engine = create_engine(f"{DB_DRIVER}://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}")

Session = sessionmaker(bind=engine)
default_session = Session()


class BaseRepository:

    def __init__(self):
        self.session = default_session

    @db_exception_handler()
    def add_item(self, item):
        self.session.add(item)

    @db_exception_handler()
    def add_all_items(self, items):
        self.session.add_all(items)
