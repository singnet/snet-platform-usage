from storage import DatabaseStorage


class UsageService(object):
    storage_service = DatabaseStorage()

    def get_free_call_details(self, user_name, org_id, service_id, group_id=None):
        free_calls, total_calls = self.storage_service.get_usage_details(user_name, org_id, service_id, group_id)

        if not free_calls:
            free_calls = 0
        if not total_calls:
            total_calls = 0

        return {"username": user_name, "org_id": org_id, "service_id": service_id, "total_calls": total_calls,
                "free_calls": free_calls}

    def save_usage_details(self, usage_details_dict):
        # nedd to introduce entities when we enhance  feature to this service right now directly using dicts
        self.storage_service.add_usage_data(usage_details_dict)
        return
