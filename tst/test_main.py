''' Main test script which executes all the test cases 
	Test Structure:
		- Main test determine which type of test to run
		-- Regression: When all test are run
		-- Non-regression: When certain specific tests are excuted
		--- These specific test can be functionality based
		--- These specific test can be a group-functionality based
		--- These specific test can be a unit tests

	Note: One can add specific test if test case doesn't fall in any of the above category.

'''

''' System specific import'''
import sys

''' Test specific import '''
import test_Customer
import test_GUIAddItem
import test_GUICreateUser
import test_GUICustomer


def test_main():
	
	print 'Main test fucntion called';
	try:
		test_type = sys.argv[1];
	
		if test_type == 'Regression':
			test_regression();
		elif test_type == 'Functionality':
			test_functionality('None');
		elif test_type == 'Unit':
			test_unit('None');
		else:
			print 'Input Argument did not matched:: sys.argv[1]:', test_type, ':Warning';
		
	except(IndexError):
		print 'ERROR: No test type matched. Error Message', IndexError;
		print '--------------------'
		print 'Test type can be of following type'
		print '- Regression'
		print '- Functionality [functionality type]'
		print '- Unit {unit test type}'

	return True;

def test_regression():

	print 'Regression test called';

	print 'Calling test_Customer';
	test_Customer.test_execute();

	return True;

def test_functionality(functionality_name):

	print 'Functionality test called';

	return True;

def test_unit(unit_name):

	print 'Unit test called'

	return True;

if __name__ == '__main__':
	test_main()

