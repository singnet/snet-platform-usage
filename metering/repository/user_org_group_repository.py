from models import UserOrgGroupModel
from repository.base_repository import BaseRepository
from utils import read_from_db


class UserOrgGroupRepository(BaseRepository):

    @read_from_db()
    def get_user_org_group_id_by_username(self, username, org_id, service_id, resource):
        user_org_query = self.session.query(UserOrgGroupModel).filter(UserOrgGroupModel.user_name == username) \
            .filter(UserOrgGroupModel.service_id == service_id) \
            .filter(UserOrgGroupModel.resource == resource) \
            .filter(UserOrgGroupModel.org_id == org_id)
        user_org_group_data = user_org_query.first()
        if user_org_group_data is None:
            user_org_group_id = None
        else:
            user_org_group_id = user_org_group_data.id
        return user_org_group_id

    @read_from_db()
    def get_user_org_group_id_by_user_address(self, user_address, org_id, service_id, resource, payment_group_id):
        user_org_query = self.session.query(UserOrgGroupModel).filter(UserOrgGroupModel.user_address == user_address) \
            .filter(UserOrgGroupModel.service_id == service_id) \
            .filter(UserOrgGroupModel.resource == resource) \
            .filter(UserOrgGroupModel.org_id == org_id) \
            .filter(UserOrgGroupModel.payment_group_id == payment_group_id)
        user_org_group_data = user_org_query.first()
        if user_org_group_data is None:
            user_org_group_id = None
        else:
            user_org_group_id = user_org_group_data.id
        return user_org_group_id

    def get_free_calls(self, org_id, service_id, optin_time):
        pass
