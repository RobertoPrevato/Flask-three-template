import server
import unittest


class HelpersTestCase(unittest.TestCase):
    """
      Custom template helpers tests.
    """
    def setUp(self):
        """
          The code in the setUp() method is called before each individual test function is run.
        """
        self.app = server.app.test_client()


    def tearDown(self):
        """
          The code in the setUp() method is called before each individual test function is run.
        """
        pass


    def test_resources_helper(self):
        # TODO
        assert True == True
