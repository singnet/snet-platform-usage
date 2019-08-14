from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, TIMESTAMP, func

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class OrgServiceConfigModel(Base):
    __tablename__ = 'service_config'
    id = Column('id', Integer, primary_key=True)
    org_id = Column('org_id', VARCHAR(225), nullable=False)
    service_id = Column('service_id', VARCHAR(225), nullable=False)
    free_calls = Column('free_calls', Integer, nullable=False)
    effective_start_date = Column(
        'effective_start_date', TIMESTAMP(timezone=True))
    effective_end_date = Column('effective_end_date', TIMESTAMP(
        timezone=True))
    created_at = Column('created_at', TIMESTAMP(timezone=True))


class UserOrgGroupModel(Base):
    __tablename__ = 'user_org_group'
    id = Column('id', Integer, primary_key=True)
    payment_group_id = Column('group', VARCHAR(225))
    org_id = Column('org_id', VARCHAR(225), nullable=False)
    user_name = Column('user_name', VARCHAR(225), nullable=False)
    created_at = Column('created_at', TIMESTAMP(
        timezone=True), nullable=False, server_default=func.current_timestamp())
    service_id = Column('service_id', VARCHAR(225), nullable=False)
    resource = Column('resource', VARCHAR(225))


class UsageModel(Base):
    __tablename__ = 'usage_table'
    id = Column('id', Integer, primary_key=True)
    user_org_group_id = Column('user_org_group_id', Integer, ForeignKey(
        'user_org_group.id'), nullable=False)
    usage_type = Column('usage_type', VARCHAR(225), nullable=False)
    status = Column('status', VARCHAR(225), nullable=False)
    usage_value = Column('usage_value', Integer, nullable=False)
    start_time = Column('start_time', TIMESTAMP(timezone=True))
    end_time = Column('end_time', TIMESTAMP(timezone=True))
    created_at = Column('created_at', TIMESTAMP(
        timezone=True), nullable=False, server_default=func.current_timestamp())
