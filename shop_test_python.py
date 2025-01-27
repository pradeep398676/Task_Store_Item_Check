store1 = [
    { "item_name": "Laptop", "quantity": 5, "price": 1300, "store_name": "StoreA" },
    { "item_name": "Smartphone", "quantity": 10, "price": 700, "store_name": "StoreA" },
    { "item_name": "Headphones", "quantity": 7, "price": 100, "store_name": "StoreA" }
]

store2 = [
    { "item_name": "Laptop", "quantity": 11, "price":1200, "store_name": "StoreB" },
    { "item_name": "Smartphone", "quantity": 8, "price": 900, "store_name": "StoreB" },
    { "item_name": "Smartwatch", "quantity": 5, "price": 200, "store_name": "StoreB" }
]

# more sale from store store1 and store2 in terms of quantity
# More price from store store1 and store2 in terms of quantity

def home(**kwargs):
    store = kwargs
    newdict = {}

    for i,j  in store.items():
        max_quantity = 0
        max_orice = 0
        for k in j:
            # print(k.get('item_name'),k.get('quantity'),k.get('price'))
            l=[]
            if newdict.get(k.get('item_name')):
                if newdict.get(k.get('item_name'))[0] < k.get('quantity'):
                    newdict.get(k.get('item_name'))[0] = ('Quantity High',k.get('quantity'),k.get('store_name'))
                else:
                    newdict.get(k.get('item_name'))[0] = ('Quantity High', newdict.get(
                        k.get('item_name'))[0], newdict.get(k.get('item_name'))[2])
              
                if newdict.get(k.get('item_name'))[1] < k.get('price'):
                    newdict.get(k.get('item_name'))[1] = ('Price High', k.get('price'), k.get('store_name'))
                else:
                    newdict.get(k.get('item_name'))[1] = ('Price High', newdict.get(
                        k.get('item_name'))[1], newdict.get(k.get('item_name'))[2])

                
            else:
                # print(k['item_name'])
                l.append(k['quantity'])
                l.append(k['price'])
                l.append(k['store_name'])
                newdict[k.get('item_name')] = l
                
    return newdict

k = home(store1=store1,store2=store2)

# print('final_result',k)
for final_item, item_detail in k.items():
    if type(item_detail[0]) != int:
        item_detail.pop()
        k[final_item]=item_detail
    else:
        k[final_item] = item_detail
print('final_result',k)
     
home(store1=store1,store2=store2)
        
        
        