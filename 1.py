input_list = [
    "https://t.me/chbujb","hdvWoSeFR0VjNTBi","https://t.me/example1","hdvWoSeFR0VjNTBi","https://t.me/test1","hdvWoSeFR0VjNTBi",
]

output_list = []

for item in input_list:
    parts = item.split(',')
    if len(parts) == 1:
        output_list.append(parts[0])


print(output_list)