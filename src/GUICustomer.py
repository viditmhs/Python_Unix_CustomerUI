''' GUI to control the Cutormer App '''

''' import files '''

import Tkinter
import tkMessageBox
import main
import GUICreateUser
import GUIAddItem



class GUICustomer(object):
    ''' Description '''
    ''' Input Parameters '''
    
    ''' Initialize do '''
    
    def __init__(self):
        self.mainFrame = Tkinter.Tk();
	self.initializing();
	self.mainFrame.mainloop();

	
    def initializing(self):
    	''' Frame Titel '''
	self.mainFrame.title("Custome Data Portal")
	
	''' Layout '''
	
    	self.mainFrameButtonCreateNew = Tkinter.Button(self.mainFrame, text ="Create New", command = self.createNewCustomer, width=10 );
	self.mainFrameButtonCreateNew.grid(row=0, column=0, pady=4);
    	self.mainFrameButtonAddToExisting = Tkinter.Button(self.mainFrame, text ="Add Item", command = self.addToExisiting, width=10 );
	self.mainFrameButtonAddToExisting.grid(row=0, column=1, pady=4);
    	self.mainExit = Tkinter.Button(self.mainFrame, text ="Exit Portal", command = self.exitPortal, width=10 );
	self.mainExit.grid(row=0, column=2, pady=4);
    
    def createNewCustomer(self):
	newUser = GUICreateUser.GUICreateUser();
	
    def addToExisiting(self):
        self.mainFrame.destroy()
    	user = GUIAddItem.GUIAddItem();
	
    def exitPortal(self):
    	try:
	    if tkMessageBox.askokcancel("Quit", "Do you want to quit the portal?"):
	        self.mainFrame.destroy();
	    else:
	       print "Log: User cancel quit."
	except ValueError:
	    print "Opps, cannot close the Window."
	
	
    
