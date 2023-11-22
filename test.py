import unittest
import main as app

class TestMyRowsApp(unittest.TestCase):
    def setUp(self):
        self.app = app

    def test_plus(self):
        self.assertEqual(app.plus(1,2), 3)
        self.assertEqual(app.plus(0,-1), -1)
        self.assertRaises(ValueError, self.app.plus, "a", 1)

    def test_minus(self):
        self.assertEqual(app.minus(1, 2), -1)
        self.assertEqual(app.minus(0, -1), 1)
        self.assertRaises(ValueError, self.app.minus, "a", 1)

    def test_multiply(self):
        self.assertEqual(app.mult(1, 2), 2)
        self.assertEqual(app.mult(0, -1), 0)
        self.assertRaises(ValueError, self.app.mult, "asd", 1)

    def test_divide(self):
        self.assertEqual(app.div(1,2), .5)
        self.assertEqual(app.div(0,-1), 0)
        self.assertRaises(ValueError, self.app.div, "a", 1)

    def tearDown(self):
        pass
if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output="test-reports")
    unittest.main(testRunner=runner)
    unittest.main()