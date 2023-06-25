import time
import requests
import json


class ControllerRest:
    scan_id = ""
    result = True
    url = ""
    delay = 1000
    posture_type = ""
    alert_corr = ""
    target = ""
    node = ""
    host = ""
    project = ""

    def __init__(self, url, delay, posture_type, alert_corr, target, host, node, project):
        self.url = url
        self.delay = delay
        self.posture_type = posture_type
        self.alert_corr = alert_corr
        self.target = target
        self.host = host
        self.node = node
        self.project = project
        self.run_scan()

    def run_scan(self):
        if not self.result:
            return False
        r = requests.post(self.url, data=self.convert_params_to_json(), headers={"Content-Type": "application/json"})
        if r.status_code != 200:
            return False
        json_obj = json.loads(r.content)
        self.scan_id = json_obj["taskId"]
        time.sleep(5)
        return True

    def get_alerts(self, critical, major, minor, info):
        alerts_url = self.url + "/alerts/" + self.scan_id
        r = requests.get(alerts_url)
        if r.status_code != 200:
            return False
        json_obj = json.loads(r.content)

        critical_alert = int(json_obj["alert_critical"])
        if critical_alert >= critical != 0:
            return False

        major_alerts = int(json_obj["alert_major"])
        if major_alerts >= major != 0:
            return False

        minor_alerts = int(json_obj["alert_minor"])
        if minor_alerts >= minor != 0:
            return False

        info_alerts = int(json_obj["alert_info"])
        if info_alerts >= info != 0:
            return False

        return True

    def convert_params_to_json(self):
        return "{\"delay\": " + str(self.delay) + "," + \
               "\"postureType\": \"" + self.posture_type + "\"," + \
               "\"alertCorr\": \"" + self.alert_corr + "\"," + \
               "\"target\": \"" + self.target + "\"," + \
               "\"host\": \"" + self.host + "\"," + \
               "\"node\": \"" + self.node + "\"," + \
               "\"project\": \"" + self.project + "\"}"
