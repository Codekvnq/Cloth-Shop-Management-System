from Customer_Account import Product
from  Customer_Account import *
Total = int(input('Enter Total Products: '))
L = []
for i in range(Total):
    P = Product
    L.append(P)
while True:
    print("**** Welcome To Milly's Closet ****")
    user_input = int(input('1. Main Menu\n'
                           '2, Show All Products\n'
                           '3. Search By ID\n'
                           '4. Search By Name\n'
                           '5. Sale\n'
                           '6. Purchase\n'
                           '7. Exit\n\n'
                           'Enter your choice: '))

    if user_input == 1:
        for c in L:
            c.PutProduct()

    elif user_input == 2:
        name = input('Enter Product Name: ')
        count = 0
        for c in L:
            found = c.Search_by_name(name)
            if found:
                c.PutProduct(Product)
                count += 1

        if count == 0:
            print('Product Not Found....')
        else:
            print('Product Found:', count)

    elif user_input == 3:
        id = input('Enter Product ID You Want To Search: ')
        found = False
        for c in L:
            found = c.Search_by_ID(id)
            if found:
                c.PutProduct()
                break
        if not found:
            print('Records Not Found....')

    elif user_input == 4:
        product_name = input('Enter Product Name: ')
        count = 0
        for c in L:
            found = c.Search_by_name(product_name)
            if found:
                c.Sale()
                c.PutProduct()
        if count == 0:
            print('No products')

    elif user_input == 5:
        name == input('Enter product name you want to purchase: ')
        count = 0
        for c in L:
            found = c.Search_by_name(name)
            if found:
                c.Purchase()
                c.PutProduct()
                count += 1

    elif user_input == 6:
        break
    else:
        print('Invalid Choice')






