import unittest   # The test framework
from sklearn_helper.base import make_pipeline

class Test_MakePipeline(unittest.TestCase):
    def test_returnpipe(self):
        self.assertEqual(make_pipeline(), 1)

if __name__ == '__main__':
    unittest.main()