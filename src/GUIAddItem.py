''' GUI to control to add item in user profile '''

''' import files '''

import Tkinter
import tkMessageBox
import Customer
import GUICustomer



class GUILogin(object):
	''' Description:
			GUI to login and verify if user exist'''
	
	''' Input Parameters '''
	
	''' Initialize do '''
	
	def __init__(self):
        
		self.addItemFrame = Tkinter.Tk();
		self.initializing();
		self.addItemFrame.mainloop();

	
	def initializing(self):
		''' Frame Titel '''
		self.addItemFrame.title("Custome Data Portal: User Login")
	
		''' Layout '''
		#Row 0
		self.addItemLabelUserName = Tkinter.Label(self.addItemFrame, text="Username").grid(row=0, column=0);
		self.addItemEntryUserName = Tkinter.Entry(self.addItemFrame)	
		self.addItemEntryUserName.grid(row=0, column=1);
		
		#Row 1
		self.addItemButtonLogin = Tkinter.Button(self.addItemFrame, text ="Login", command = self.userLogin, width=10);
		self.addItemButtonLogin.grid(row=1, column=0, pady=4);
		self.addItemButtonCancel = Tkinter.Button(self.addItemFrame, text ="Cancel", command = self.userCancel, width=10);
		self.addItemButtonCancel.grid(row=1, column=1, pady=4);
	
	def userLogin(self):
		''' Check if user exsit'''
		user = Customer.Customer(self.addItemEntryUserName.get())
		if (user.customerExist()):
			user.readItemList();
			self.addItemFrame.destroy()
			showUserProfile = GUIShowUser(user);
   	        #addItemListView = GUIAddItemListView(user);
		else:	
			self.popUpUserDoNotExist();
		return
    
	def userCancel(self):
		self.addItemFrame.destroy()
		returnGUICustomer_instance = GUICustomer.GUICustomer();
		return 
    
	def popUpUserDoNotExist(self):
		pop = Tkinter.Toplevel();
		pop.title("Error: Login Failed");
		msg = Tkinter.Label(pop, text='    No such user exsit...    ', width=100, height=5)
		msg.pack();	
		button = Tkinter.Button(pop, text="Dismiss", comman=pop.destroy)
		button.pack();
		return

class GUIShowUser(object):
	'''
        It show user profile
	'''
	def __init__(self, userCustomerClass):
		self.userCustomerClass = userCustomerClass;
		self.userProfilePageFrame = Tkinter.Tk();
        	self.initializing()
        	self.userProfilePageFrame.mainloop();

	def initializing(self):
		''' Frame Titel '''
		welcome_msg = "Customer Profile Page"
		self.userProfilePageFrame.title(welcome_msg)

		#Row 0
		#self.userProfilePageLabelUserName = Tkinter.Label(self.userProfilePageFrame, text=welcome_msg).grid(row=0, column=0()
		
		#Row 1
		return -1;


class GUIAddItemListView(object):
	''' Description:
			GUI application to add item for given user'''

	''' Input Parameters '''

	''' Initialize do '''

	def __init__(self, userCustomerClass):
		self.userCustomerClass = userCustomerClass
		self.username = self.userCustomerClass.getUserName()
		self.addItemListViewFrame = Tkinter.Tk();
		self.initializing();
		self.addItemListViewFrame.mainloop();


	def initializing(self):
    		''' Frame Titel '''
		welcome_msg = "Custome Data Portal: User:" + self.username;
		self.addItemListViewFrame.title(welcome_msg);
		
		''' Layout '''
		#Row 0
		welcome_msg = 'Username : '+ self.username;
		self.addItemListViewLabelUserName = Tkinter.Label(self.addItemListViewFrame, text=welcome_msg).grid(row=0, column=0);
	
		#Row 1
		self.addItemListViewLabelItemName = Tkinter.Label(self.addItemListViewFrame, text="Item Name").grid(row=1, column=0);
		self.addItemListViewEntryItemName = Tkinter.Entry(self.addItemListViewFrame)	
		self.addItemListViewEntryItemName.grid(row=1, column=1);
	
		#Row 2
		self.addItemListViewLabelItemCost = Tkinter.Label(self.addItemListViewFrame, text="Item Cost").grid(row=2, column=0);
		self.addItemListViewEntryItemCost = Tkinter.Entry(self.addItemListViewFrame)	
		self.addItemListViewEntryItemCost.grid(row=2, column=1);
	
		#Row 3
		self.addItemListViewButtonSubmit = Tkinter.Button(self.addItemListViewFrame, text ="Submit", command = self.addItemListViewSubmit, width=10);
		self.addItemListViewButtonSubmit.grid(row=3, column=0, pady=4);
		self.addItemListViewButtonCancel = Tkinter.Button(self.addItemListViewFrame, text ="Cancel", command = self.addItemListViewCancel, width=10);
		self.addItemListViewButtonCancel.grid(row=3, column=1, pady=4);
		
	
	def addItemListViewSubmit(self):
		itemName = self.addItemListViewEntryItemName.get();
		self.addItemListViewEntryItemName.delete(0, 'end');
		itemCost = self.addItemListViewEntryItemCost.get();
		self.addItemListViewEntryItemCost.delete(0, 'end');
	
		''' Adding item to the data'''
		self.userCustomerClass.addItem(itemName, itemCost);
	
		return
	
	def addItemListViewCancel(self):
		self.addItemListViewFrame.destroy()
		returnGUIAddItem_instance = GUIAddItem();
		self.userCustomerClass.saveItemList();
		return
