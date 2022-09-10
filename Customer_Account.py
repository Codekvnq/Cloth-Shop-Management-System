class Product:
    def __init__(self, name, id, rate, stock):
        self.id = input('Enter ID: ')
        self.name = input('Enter Name: ')
        self.rate = int(input('Enter rate: '))
        self.stock = int(input('Enter Stock: '))

    def PutProduct(self):
        print(self.id, self.name, self.rate, self.stock)

    def Search_by_ID(self, id):
        if self.id == id:
            return True
        else:
            return False

    def Search_by_name(self, name):
        if self.name == name:
            return True
        else:
            return False

    def Sale(self):
        print('Sale.....')
        print('Quantity of Product Present In Stock Is: ', self.stock)
        quantity = int(input('Enter Quantity: '))
        if (self.stock > quantity):
            amt = quantity * self.rate
            print('Amount:', amt)

            self.stock -= quantity
        else:
            print('Less Stock')

    def Purchase(self):
        print('Purchase.....')
        q = int(input('Enter Quantity Of Product Purchase: '))
        self.stock += q

