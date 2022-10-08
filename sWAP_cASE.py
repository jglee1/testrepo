def swap_case(s):
    new_str = ""
    for e in s:
        if e.isupper():
            new_e = e.lower()
            new_str += new_e
            print(new_str)
        elif e.islower():
            new_e = e.upper()
            new_str += new_e
            print(new_str)
        else:
            new_str += e
            print(new_str)
    return new_str

input_str = "Swap Case 1"

swap_case(input_str)

output_list = [ e.lower() if e.isupper() else e.upper() if e.islower() else e for e in input_str ]
print(output_list)
output_str = "".join(output_list)
print(output_str)
