# import json
# import base64
# people ={
#     "names": {
#         "first_name": "John",
#         "last_name": "Doe"
#         },
#     "ages":{
#         "age": 30,
#         "dob": "01-01-1990"
#     }
# }

# fin = json.dumps(people)

# print(fin)

# encoded_data = base64.b64encode(fin.encode('utf-8'))

# print(encoded_data.decode('utf-8'))
# print(base64.b64decode(encoded_data).decode('utf-8'))
        



# # with open("names.json", "w") as file:
# #     data = json.dump(people,file)
from collections import defaultdict


text = 'Thank you for visiting our carwash. You have been enrolled into our loyalty program. You are eligible for a FREE WASH on your 7th visit. Valid till 20/10/2024'
# print(len(text))

staff_sales_dict = defaultdict(lambda: {"paid": [], "unpaid": []})

staff_sales_dict['paulo']['paid'].append(1000)
staff_sales_dict['paulo']['paid'].append(1000)
staff_sales_dict['akello']['unpaid'].append(2000)
staff_sales_dict['mike']['unpaid'].append(3000)
staff_sales_dict['mike']['paid'].append(3000)
staff_sales_dict['mike']['unpaid'].append(3000)

for name, sales in staff_sales_dict.items():
    paid_total = sum(sales['paid'])
    unpaid_total = sum(sales['unpaid'])
    total = paid_total + unpaid_total
    print(f"{name}:")
    print(f"  Paid total: {paid_total}")
    print(f"  Unpaid total: {unpaid_total}")
    print(f"  Overall total: {total}")
    print()

# <QuerySet [{'uid': UUID('5ce91b8c-72b8-4841-99ce-537ef60da6ec'), 'created': datetime.datetime(2024, 10, 30, 19, 34, 28, 270956, tzinfo=datetime.timezone.utc), 'updated': datetime.datetime(2024, 10, 30, 19, 34, 28, 270988, tzinfo=datetime.timezone.utc), 'category': 'Carwash', 'item': 'Electricity', 'expense_description': None, 'amount': Decimal('2000.00')}, {'uid': UUID('eab77cbd-c06d-4f1a-8923-2c7234377e61'), 'created': datetime.datetime(2024, 10, 30, 19, 33, 6, 987221, tzinfo=datetime.timezone.utc), 'updated': datetime.datetime(2024, 10, 30, 19, 33, 6, 987240, tzinfo=datetime.timezone.utc), 'category': 'Toilet', 'item': 'Tissue', 'expense_description': None, 'amount': Decimal('1000.00')}]>
    



