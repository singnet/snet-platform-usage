from storage import DatabaseStorage


class UsageService(object):
    storage_service = DatabaseStorage()

    def get_free_call_details(self, username, org_id, service_id, group_id=None):
        total_calls, free_calls = self.storage_service.get_usage_details(
            username, org_id, service_id, group_id)

        if not free_calls:
            free_calls = 0
        else:
            free_calls = free_calls[0]
        if not total_calls:
            total_calls = 0

        return {"username": username, "org_id": org_id, "service_id": service_id, "total_calls_made": total_calls,
                "free_calls_allowed": free_calls}

    def save_usage_details(self, usage_details_dict):
        # nedd to introduce entities when we enhance  feature to this service right now directly using dicts
        self.storage_service.add_usage_data(usage_details_dict)
        return
