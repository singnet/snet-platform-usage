from sqlalchemy import func

from models import UsageModel, UserOrgGroupModel
from repository.base_repository import BaseRepository


class UsageRepository(BaseRepository):

    def get_total_calls(self, user_name, org_id, service_id):
        query_data = self.session.query(func.count(UsageModel.id).label('total_calls')).join(UserOrgGroupModel) \
            .filter(UserOrgGroupModel.user_name == user_name)\
            .filter(UserOrgGroupModel.org_id == org_id) \
            .filter(UserOrgGroupModel.service_id == service_id)\
            .filter(UsageModel.status == 'success').all()
        self.session.commit()
        return query_data[0].total_calls

    def get_optin_time(self, user_name, org_id, service_id):
        query_data = self.session.query(func.min(UsageModel.created_at).label('opt_time')).join(UserOrgGroupModel).filter(
            UserOrgGroupModel.user_name == user_name).filter(UserOrgGroupModel.org_id == org_id).filter(
            UserOrgGroupModel.service_id == service_id).all()
        self.session.commit()
        return query_data[0].opt_time
