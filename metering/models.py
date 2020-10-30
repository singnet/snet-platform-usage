from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, TIMESTAMP, func, FLOAT

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OrgServiceConfigModel(Base):
    __tablename__ = 'service_config'
    id = Column('id', Integer, primary_key=True)
    org_id = Column('org_id', VARCHAR(225), nullable=False)
    service_id = Column('service_id', VARCHAR(225), nullable=False)
    free_calls = Column('free_calls', Integer, nullable=False)
    effective_start_date = Column(
        'effective_start_date', TIMESTAMP(timezone=True))
    effective_end_date = Column('effective_end_date', TIMESTAMP(timezone=True))
    created_at = Column('created_at', TIMESTAMP(
        timezone=True), server_default=func.current_timestamp())


class UserOrgGroupModel(Base):
    __tablename__ = 'user_org_group'
    id = Column('id', Integer, primary_key=True)
    payment_group_id = Column('group', VARCHAR(225))
    org_id = Column('org_id', VARCHAR(225), nullable=False)
    user_name = Column('user_name', VARCHAR(225))
    user_address = Column('user_address', VARCHAR(225))
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
    payment_mode = Column('payment_mode', VARCHAR(225))
    group_id = Column('group_id', VARCHAR(225))
    registry_address_key = Column('registry_address_key', VARCHAR(225))
    ethereum_json_rpc_endpoint = Column('ethereum_json_rpc_endpoint', VARCHAR(225))
    response_time = Column('response_time', FLOAT)
    response_code = Column('response_code', VARCHAR(225))
    error_message = Column('error_message', VARCHAR(225))
    version = Column('version', VARCHAR(225))
    client_type = Column('client_type', VARCHAR(225))
    user_details = Column('user_details', VARCHAR(225))
    channel_id = Column('channel_id', VARCHAR(225))
    operation = Column('operation', VARCHAR(225))
    user_address = Column('user_address', VARCHAR(225))
    user_name = Column('username', VARCHAR(225))
    org_id = Column('org_id', VARCHAR(225))
    service_id = Column('service_id', VARCHAR(225))
    resource = Column('resource', VARCHAR(225))
    request_id = Column('request_id', VARCHAR(225))
