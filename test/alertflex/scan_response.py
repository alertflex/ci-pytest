import json


class ScanResponse:
    critical_alerts = 0
    major_alerts = 0
    minor_alerts = 0
    info_alerts = 0
    posture_type = ""
    target = ""
    node = ""
    host = ""

    def __init__(self, json_response):
        json_obj = json.loads(json_response)

        self.critical_alerts = json_obj["criticalAlerts"]
        self.major_alerts = json_obj["majorAlerts"]
        self.minor_alerts = json_obj["minorAlerts"]
        self.info_alerts = json_obj["infoAlerts"]
        self.posture_type = json_obj["postureType"]
        self.target = json_obj["target"]
        self.node = json_obj["node"]
        self.host = json_obj["host"]

    def get_critical_alerts(self):
        return self.critical_alerts

    def set_critical_alerts(self, critical_alerts):
        self.critical_alerts = critical_alerts

    def get_major_alerts(self):
        return self.major_alerts

    def set_major_alerts(self, major_alerts):
        self.major_alerts = major_alerts

    def get_minor_alerts(self):
        return self.minor_alerts

    def set_minor_alerts(self, minor_alerts):
        self.minor_alerts = minor_alerts

    def get_info_alerts(self):
        return self.info_alerts

    def set_info_alerts(self, info_alerts):
        self.info_alerts = info_alerts

    def get_posture_type(self):
        return self.posture_type

    def set_posture_type(self, posture_type):
        self.posture_type = posture_type

    def get_target(self):
        return self.target

    def set_target(self, target):
        self.target = target

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host
