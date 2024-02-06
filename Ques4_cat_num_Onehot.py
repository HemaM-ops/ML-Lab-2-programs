def one_hot_encode(data):
    unique_values = list(set(data))
    encoding_dict = {val: i for i, val in enumerate(unique_values)}# enumerate index value pairs
    encoded_data = []
    for val in data:
        encoding = [0] * len(unique_values)
        encoding[encoding_dict[val]] = 1
        encoded_data.append(encoding)
    return encoded_data, encoding_dict, unique_values

user_input = input("Enter categorical values separated by spaces: ")

data = user_input.split()

encoded_data, encoding_dict, unique_values = one_hot_encode(data)

print("Values corresponding to each position:")
for i, val in enumerate(unique_values):
    print(f"Position {i}: {val}")#values corresponding to each column position in the matrix

print("\nOriginal Data:", data)
print("One-Hot Encoded Data:")


for entry in encoded_data:
    print(entry,"\t", [unique_values[i] for i, v in enumerate(entry) if v == 1])

print("\nEncoding Dictionary:")
for key, value in encoding_dict.items():
    print(f"{key}: {value}")
