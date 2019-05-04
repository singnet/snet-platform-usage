from repository import Repository
from constant import METRICS_NETWORK_ID

class Token:
    def __init__(self):
        self.repo = Repository(METRICS_NETWORK_ID)

    def validate_token(self, daemon_id, token):
        print("validate_token::daemon_id: ", daemon_id);
        qry = "SELECT * FROM daemon_token WHERE daemon_id = %s and token = %s "
        res = self.repo.execute(qry, [daemon_id, token])
        if len(res) > 0:
            return {'validated': True}
        return {'validated': False}