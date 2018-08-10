import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_email(self):
        e1 = Employee('Corey', 'Schafer', 50000)
        e2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(e1.email, 'Corey.Schafer@email.com')
        self.assertEqual(e2.email, 'Sue.Smith@email.com')

        e1.first = 'John'
        e2.first = 'Jane'

        self.assertEqual(e1.email, 'John.Schafer@email.com')
        self.assertEqual(e2.email, 'Jane.Smith@email.com')

    def test_fullName(self):
        e1 = Employee('Corey', 'Schafer', 50000)
        e2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(e1.fullName, 'Corey Schafer')
        self.assertEqual(e2.fullName, 'Sue Smith')

        e1.first = 'John'
        e2.first = 'Jane'

        self.assertEqual(e1.fullName, 'John Schafer')
        self.assertEqual(e2.fullName, 'Jane Smith')

    def test_applyRaise(self):
        e1 = Employee('Corey', 'Schafer', 50000)
        e2 = Employee('Sue', 'Smith', 60000)

        e1.applyRaise()
        e2.applyRaise()

        self.assertEqual(e1.pay, 52500)
        self.assertEqual(e2.pay, 63000)


if __name__ == '__main__':
    unittest.main()

        