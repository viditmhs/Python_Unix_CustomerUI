'''
    Info::
'''

import os.path
POST_FILE_NAME = '_itemDetails.txt'


class Customer(object):
    ''' A Customer class which keeps a detail of the expenses of the
        customer.
    '''

    ''' :: Attributes ::
        name:: Name of the customer
        itemList:: a list that contains the itemName and itemCost
    '''

    def __init__(self, name):
        self.username = name;
        self.name = '/home/vidit/Project/CustomerUI/dat/' + name;
        self.itemList = [];


    def saveItemList(self):
        fileName = self.name + POST_FILE_NAME;

        fileObject = open(fileName, 'w');
        dataString = '';

        for i in range(len(self.itemList)):
            dataString = dataString + self.itemList[i][0] + '!'+ str(self.itemList[i][1])+'\n';

        fileObject.write(dataString);
        fileObject.close();

    def readItemList(self):
        fileName = self.name + '_itemDetails.txt';
        fileObject = open(fileName, 'r');
        self.itemList = [];
        for line in fileObject:
            pos = line.index('!');
            itemName = line[:pos];
            itemCost = float(line[pos+1:-1]);
            self.itemList.append([itemName, itemCost]);

        fileObject.close();

    def addItem(self, itemName, itemCost):
        self.itemList.append([itemName, itemCost]);
	
    def getItemList(self):
        if len(self.itemList)>0:
	    return self.itemList;
	else:
	    raise ValueError('No item in the list');
	    
    def customerExist(self):
        fileName = self.name + POST_FILE_NAME;
	return os.path.isfile(fileName);
	
    def getUserName(self):
    	return self.username;
	
	    
	  
