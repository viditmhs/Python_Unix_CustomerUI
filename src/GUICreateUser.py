''' GUI to control Create a User profile '''

''' import files '''

import Tkinter
import tkMessageBox
import Customer



class GUICreateUser(object):
    ''' Description:
    		GUI application to create new user '''
    
    ''' Input Parameters '''
    
    ''' Initialize do '''
    
    def __init__(self):
        self.createUserFrame = Tkinter.Tk();
	self.initializing();
	self.createUserFrame.mainloop();

	
    def initializing(self):
    	''' Frame Titel '''
	self.createUserFrame.title("Custome Data Portal: Create User")
	
	''' Layout '''
	#Row 0
	self.createUserLabelNewCustomerName = Tkinter.Label(self.createUserFrame, text="New Username").grid(row=0, column=0);
	self.createUserEntryCustomerName = Tkinter.Entry(self.createUserFrame)	
	self.createUserEntryCustomerName.grid(row=0, column=1);
	
	#Row 1
	self.createUserButtonCreate = Tkinter.Button(self.createUserFrame, text ="Create", command = self.createUser_def, width=10 );
	self.createUserButtonCreate.grid(row=1, column=0, pady=4);
	
    	self.createUserCancel = Tkinter.Button(self.createUserFrame, text ="cancel", command = self.createUserCancel_def, width=10 );
	self.createUserCancel.grid(row=1, column=1, pady=4);
    
    def createUser_def(self):
	newCustomer = Customer.Customer(self.createUserEntryCustomerName.get())
	if (newCustomer.customerExist()):
	    self.popUpCustomerAlreadyExist();
	else:
	    print "Customer is created"
	    newCustomer.saveItemList();
	    self.createUserCancel_def();
	return
	
    def createUserCancel_def(self):
	
	self.createUserFrame.destroy();
	return
	
    def popUpCustomerAlreadyExist(self):
    	pop = Tkinter.Toplevel();
	pop.title("Error: Customer name already exist");
	msg = Tkinter.Label(pop, text='    Customer with name already exist...    ', width=100, height=5)
	msg.pack();	
	button = Tkinter.Button(pop, text="Dismiss", comman=pop.destroy)
	button.pack();
	return
    

