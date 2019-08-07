from models import UserOrgGroupModel, UsageModel
from repository.base_repository import BaseRepository


class UserOrgGroupRepository(BaseRepository):
    def get_user_org_group_data(self, payment_group_id, org_id, user_name, service_id, resource):
        session = self.get_default_session()
        user_org_query = session.query(UserOrgGroupModel) \
            .filter(UserOrgGroupModel.resource == resource) \
            .filter(UserOrgGroupModel.service_id == service_id) \
            .filter(UserOrgGroupModel.user_name == user_name) \
            .filter(UserOrgGroupModel.org_id == org_id)

        if payment_group_id is not None:
            user_org_query = user_org_query.filter(UserOrgGroupModel.payment_group_id == payment_group_id)

        user_org_group_data = user_org_query.first()
        return user_org_group_data

    def get_free_calls(self, org_id, service_id, optin_time):
        pass
