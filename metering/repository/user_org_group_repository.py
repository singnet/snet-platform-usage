from models import UserOrgGroupModel, UsageModel
from repository.base_repository import BaseRepository


class UserOrgGroupRepository(BaseRepository):

    def get_user_org_group_id_by_username(self, username, org_id, service_id, resource):
        session = self.get_default_session()
        user_org_query = session.query(UserOrgGroupModel).filter(UserOrgGroupModel.user_name == username) \
            .filter(UserOrgGroupModel.service_id == service_id) \
            .filter(UserOrgGroupModel.resource == resource) \
            .filter(UserOrgGroupModel.org_id == org_id)

        user_org_group_data = user_org_query.first()
        session.commit()
        session.flush()
        return user_org_group_data

    def get_user_org_group_id_by_user_address(self, user_address, org_id, service_id, resource, payment_group_id):
        session = self.get_default_session()
        user_org_query = session.query(UserOrgGroupModel).filter(UserOrgGroupModel.user_address == user_address) \
            .filter(UserOrgGroupModel.service_id == service_id) \
            .filter(UserOrgGroupModel.resource == resource) \
            .filter(UserOrgGroupModel.org_id == org_id) \
            .filter(UserOrgGroupModel.payment_group_id == payment_group_id)
        user_org_group_data = user_org_query.first()
        session.commit()
        session.flush()
        return user_org_group_data

    def get_free_calls(self, org_id, service_id, optin_time):
        pass
