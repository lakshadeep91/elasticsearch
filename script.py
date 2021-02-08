from medical.models import Product, Seller, Role, Inventory
from random import random

for product in x:
    Product(name=product, description=product).save()

for i in range(1,5):
    Seller(name=f"Manufacturer {i}", role=Role.MANUFACTURER).save()

parent_ids = [1,3,2,1]
for i in range(1,5):
    Seller(name=f"Distributer {i}", role=Role.DISTRIBUTER, parent_id=parent_ids.pop()).save()

parent_ids = [6,8,6,8,7,6,5]
for i in range(1,8):
    Seller(name=f"Reseller {i}", role=Role.RESELLER, parent_id=parent_ids.pop()).save()

i, j, k = [1, 5, 9]
for product in Product.objects.all():
    flag = int(random() * 10 % 2)
    price = int(random() * 100)
    Inventory(product=product, seller_id=i, price=price).save()
    i += 1
    i = 1 if i > 4 else i
    if flag:
        Inventory(product=product, seller_id=j, price=price*10).save()
        j += 1
        j = 5 if j > 8 else j
    flag or int(random() * 10 % 2)
    if flag:
        Inventory(product=product, seller_id=k, price=price*100).save()
        k += 1
        k = 9 if k > 15 else k

