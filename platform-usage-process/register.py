import calendar
import secrets
import time
from datetime import datetime as dt

from constant import METRICS_NETWORK_ID
from repository import Repository


class Token:
    def __init__(self):
        self.repo = Repository(METRICS_NETWORK_ID)

    def process_token(self, daemon_id):
        print("process_token::daemon_id: ", daemon_id);
        result = {}
        token = secrets.token_urlsafe(64)
        exist_info = self.daemon_id_exist(daemon_id=daemon_id)
        if exist_info.get('status', False):
            qry = "UPDATE daemon_token set token = %s WHERE daemon_id = %s "
            updt_info = self.repo.execute(qry, [token, daemon_id])
            print(updt_info)
            if updt_info[0] > 0:
                return {"token": token}
            else:
                return {"error": "unable to generate token"}
        ctime_epoch = calendar.timegm(time.gmtime())
        expiration = ctime_epoch + (6 * 60 * 60)
        qry = "INSERT INTO daemon_token (daemon_id, token, expiration, row_updated, row_created) " \
              "VALUES(%s, %s, %s, %s, %s)"
        res = self.repo.execute(qry, [daemon_id, token, expiration, dt.utcnow(), dt.utcnow()])
        if len(res) > 0 and res[0] > 0:
            result["token"] = token
        return result

    def daemon_id_exist(self, daemon_id):
        print("daemon_id_exist::daemon_id: ", daemon_id);
        qry = "SELECT * FROM daemon_token WHERE daemon_id = %s"
        res = self.repo.execute(qry, [daemon_id])
        if len(res) > 0:
            return {'status': True, "token": res[0]['token']}
        return {'status': False}
