import logging
import unittest


class ChristmasTestCase(unittest.TestCase):
    def setUp(self):
        print "in setup"

    def test_call_view_index(self):
        # same again, but with valid data, then
        print "------------Test for view index--------------"
        pass
        ##response = self.client.get(r'^(?P<location>[^0-9]+)/$', follow=True)
        ##self.assertRedirects(response, 'christmas/index.html')
        
    def tearDown(self):
        print "in teardown"
        
if __name__ == '__main__':
    unittest.main()
