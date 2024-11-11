import base64


names = ['mike','merino','navin','akello','mike']
# Given data
my_dict = {}
val = lambda: {"paid": [], "unpaid": []}
my_dict["mike"] = val()
my_dict["John"] = val()
my_dict["mike"]["unpaid"].append({"invoice_1": 100})
my_dict["mike"]["unpaid"].append({"invoice_1": 100})
my_dict["John"]["unpaid"].append({"invoice_1": 100})
my_dict["John"]["unpaid"].append({"invoice_1": 100})
my_dict["John"]["paid"].append({"invoice_2": 150})

# Function to calculate the sums
def calculate_sums(data):
    sums_dict = {}
    for person, invoices in data.items():
        paid_sum = sum(item[next(iter(item))] for item in invoices["paid"])
        unpaid_sum = sum(item[next(iter(item))] for item in invoices["unpaid"])
        # paid_sum = sum(value for item in invoices["paid"] for key, value in item.items())
        # unpaid_sum = sum(value for item in invoices["unpaid"] for key, value in item.items())

        sums_dict[person] = {"paid_sum": paid_sum, "unpaid_sum": unpaid_sum}
    return sums_dict

# Calculate and display the results
# sums = calculate_sums(my_dict)
# print(sums)

my_chr = ord('a')
print(bin(my_chr))
print(format(my_chr, 'b'))
binary_representation = f"{my_chr:b}".encode()
baseenco = base64.b64encode(binary_representation)
print(binary_representation,baseenco.decode())

# def get_name(name:str,age:int):
#     return name,age

my_list = []
new_dict = {
    "mercy":{"student":True,"Age":30},
    "Linet":{"student":True,"Age":27}
}

print(my_list)

# x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         # HTTP_X_FORWARDED_FOR can contain multiple IPs if the client is behind a proxy chain
#         # The first IP in this list is typically the client's original IP
#         ip = x_forwarded_for.split(',')[0].strip()
#         print("IP Address: ", ip)
#     else:
#         # If HTTP_X_FORWARDED_FOR is not present, fall back to REMOTE_ADDR
#         ip = request.META.get('REMOTE_ADDR')
#         print("IP Address: ", ip)

