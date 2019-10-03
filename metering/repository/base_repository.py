import os

from settings import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_URL, echo=False)

Session = sessionmaker(bind=engine)
default_session = Session()


class BaseRepository(object):
    def get_default_session(self, session=None):
        if not session:
            return default_session

        return session

    def create_item(self, item, session=None):
        session = self.get_default_session(session)
        session.add(item)
        session.commit()
        session.flush()
        return item

    def create_all_items(self, items, session=None):
        session = self.get_default_session(session)
        session.add_all(items)
        session.commit()
        session.flush()
        return items

    def remove_item(self, item, session=None):
        pass

    def update_item(self, item, session=None):
        pass
