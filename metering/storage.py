from models import UserOrgGroupModel, UsageModel
from repository.org_service_config_repository import OrgServiceRepo
from repository.usage_repository import UsageRepository
from repository.user_org_group_repository import UserOrgGroupRepository


def add_usage_data(usage_details):
    user_org_group_repo = UserOrgGroupRepository()
    user_org_group_repo_data = user_org_group_repo.get_user_org_group_data(
        payment_group_id=usage_details.payment_group_id,
        org_id=usage_details.org_id,
        user_name=usage_details.user_name,
        user_id=usage_details.user_id,
        service_id=usage_details.service_id,
        resource=add_usage_data.resource
    )

    if user_org_group_repo_data is None:
        new_user_org_record = UserOrgGroupModel(
            payment_group_id=usage_details.payment_group_id,
            org_id=usage_details.org_id,
            user_name=usage_details.user_name,
            user_id=usage_details.user_id,
            service_id=usage_details.service_id,
            resource=add_usage_data.resource
        )
        user_org_group_repo.add_item(new_user_org_record)
        user_org_group_repo_data = user_org_group_repo.get_user_org_group_data(
            payment_group_id=usage_details.payment_group_id,
            org_id=usage_details.org_id,
            user_name=usage_details.user_name,
            user_id=usage_details.user_id,
            service_id=usage_details.service_id,
            resource=add_usage_data.resource
        )

    user_org_group_id = user_org_group_repo_data.id
    usage_record = UsageModel(
        user_org_group_id=user_org_group_id,
        usage_type=usage_details.usage_type,
        usage_value=usage_details.usage_type,
        start_time=usage_details.start_time,
        end_time=usage_details.start_time
    )
    usage_repo = UsageRepository()
    usage_repo.add_item(usage_record)


def get_usage_details(user_name, org_id, service_id):
    usage_repo = UsageRepository()
    org_service_config_repo = OrgServiceRepo()
    optin_time = usage_repo.get_optin_time(user_name, org_id, service_id)
    free_calls = org_service_config_repo.get_service_config(org_id, service_id, optin_time)
    total_calls = usage_repo.get_total_calls(user_name, org_id, service_id)
    return total_calls, free_calls


if __name__ == '__main__':
    get_usage_details('1', '1', '2')