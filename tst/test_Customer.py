'''
	Note: Any new fucnitonality added to this class should be duely tested/

	Testing scenario
	- Class : 
		Customer
	- function : 
		saveItemList
		readItemList
		addItemList
		getItemList
		customerExist
		getUserName
		
'''

''' Import files '''

import Customer as Customer

def test_execute():
	''' Testing NEGATIVE of customerExist '''
	test_function_NEGATIVE_customerExist();

	''' Testing addItemList '''
	test_function_addItemList();

	''' Testing saveItemList '''
	test_function_saveItemList();

	''' Testing customerExist '''
	test_function_customerExist();

	''' Testing readItemList '''
	test_function_readItemList();

	''' Testing getItemList '''
	test_functon_getItemList();

	''' Test getUserName'''
	test_funciton_getUserName();

	''' Clean Up '''
	clean_up();

def test_function_NEGATIVE_customerExist():
	
	result = True;
	
	print 'FUNCTION Called:: test_function_NEGATIVE_customerExist()';

	return result;

def test_function_addItemList():

	result = True;
	
	print 'FUNCTION Called:: test_fucntion_addItemList()';

	return result;

def test_function_saveItemList():

	result = True;

	print 'FUNCTION Called:: test_function_saveItemList()';

	return result;

def test_function_customerExist():

	result = True;

	print 'FUNCTION Called:: test_function_customerExist()';

	return result;

def test_function_readItemList():

	result = True;

	print 'FUNCTION Called:: test_function_readItemList()';

	return result;

def test_functon_getItemList():

	result = True;

	print 'FUNCTION Called:: test_function_getItemList()';

	return result;

def test_funciton_getUserName():

	result = True;

	print 'FUNCTION Called:: test_function_getUserName()';

	return result;

def clean_up():

	result = True;

	print 'FUNCTION Called:: clean_up()';

	return result;

