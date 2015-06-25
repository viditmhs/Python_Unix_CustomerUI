''' File to perform testing on Customer.py'''

import Customer

def main():
    cus = Customer.Customer('Tango');
    cus.addItem('Apple', 2.34);
    cus.addItem('Orange', 4.56);
    cus.saveItemList();

    cus2 = Customer.Customer('Tango');
    cus2.readItemList();
    cus2.addItem('Banana', 3.65);
    cus2.saveItemList();
    
    print cus2.getItemList();

    return 1;

if __name__ == '__main__':
    main();
