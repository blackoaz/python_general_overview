
def convert_int_to_alph(int_val):
    dec_alpha = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    for i in dec_alpha:
        if i == int_val:
            return dec_alpha[i]

def decimal_to_hex(value):
    base = 16
    remainder_list = [] 
    cont = 1
    while cont:
        quotient = value // base
        remainder = value % base
        if remainder >9<=15:
            remainder = convert_int_to_alph(remainder)
            print(remainder)
        remainder_list.append(remainder)
        value = quotient
        if quotient == 0:
            cont = 0
    return remainder_list[::-1]


def main():
    user_input = eval(input("Enter the value to find its hexadecimal representation: "))
    if user_input > 0:
        hex_val = decimal_to_hex(user_input)
        print(hex_val)
        val = "".join(str(hex) for hex in hex_val)
        print(val)
    else:
        print("You have entered an invalid value")
    
main()

