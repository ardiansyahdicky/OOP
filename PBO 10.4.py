input_strings=['1', '5', '28', '131', '3']
output_ints=[int(n) for n in input_strings if len(n) <3]
for i in output_ints:
    print(i)