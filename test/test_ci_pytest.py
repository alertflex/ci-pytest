from alertflex.controller_rest import ControllerRest
import pytest


class TestCiPytest:

    def test_docker_config(self):
        scan_docker_config = ControllerRest(
            "http://192.168.1.20:8080/alertflex-ctrl/rest/posture",  # url
            1000,  # delay
            "DockerConfig",  # scan type
            "OnlyNew", # alert correlation
            "/root/downloads/altprobe-docker",  # target
            "devhost",  # host
            "node01",  # node
            "5a50c6fe-ef05-49b8-9d21-14567b58d4e7"  # project id
        )

        assert scan_docker_config.get_alerts(
            2,  # Threshold for critical alerts
            0,  # Threshold for major alerts
            0,  # Threshold for minor alerts
            0   # Threshold for info alerts
        )
