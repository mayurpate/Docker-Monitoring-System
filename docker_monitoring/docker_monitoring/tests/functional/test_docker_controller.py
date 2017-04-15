from docker_monitoring.tests import *

class TestDockerControllerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='docker_controller', action='index'))
        # Test response...
