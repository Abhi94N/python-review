import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    
    # runs starts at the beginning of a test
    # example includes populating a databse
    # in your case fetching aws secrets
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    # runs at the end of a test
    # teardown database
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
    
    # create this for instances to test
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Abhi', 'Nair', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    # runs code after every single test
    def tearDown(self):
        print('tearDown\n')
        pass
    
    def test_email(self):

        print('test_email')
        self.assertEqual(self.emp_1.email, 'Abhi.Nair@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Healther'

        self.assertEqual(self.emp_1.email, 'John.Nair@email.com')
        self.assertEqual(self.emp_2.email, 'Healther.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Abhi Nair')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Healther'

        self.assertEqual(self.emp_1.fullname, 'John Nair')
        self.assertEqual(self.emp_2.fullname, 'Healther Smith')

    def test_apply_raise(self):
        print('test_apply_raise')    
        self.assertEqual(self.emp_1.pay, 50000)
        self.assertEqual(self.emp_2.pay, 60000)
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52000)
        self.assertEqual(self.emp_2.pay, 62400)
    
    def test_monthly_schedule(self):
        # get the request.get from employee modules using context manager
        with patch('employee.requests.get') as mocked_get:
            # passing test
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            # call with url
            mocked_get.assert_called_with('http://company.com/Nair/May')
            self.assertEqual(schedule, 'Success')         
            
            mocked_get.return_value.ok = False
            # failing test
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')
              
        
if __name__ == '__main__':
    unittest.main()