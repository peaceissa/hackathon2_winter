import json
import time

unix_timestamp = int(time.time())


data = []

def process_input(u):
    return [int(x.strip()) for x in u]



def analyze_list_elements(input_list):

    # Loop through each element in the list
    for element in input_list:
        # Check if the element is even or odd
        if element % 2 == 0:
            print(f"{element} is an even number.")
        else:
            print(f"{element} is an odd number.")

        data.append(element)

    # Calculate the sum of all elements in the list using a loop
    sum_of_elements = sum(input_list)
    #data.remove(element)
    print(f"The sum of all elements in the list is: {sum_of_elements}")




def main():
    user_input_list = input("Enter a list of numbers separated by commas: ").split(',')
    my_list = process_input(user_input_list)

    # Call the function with the provided list
    total = analyze_list_elements(my_list)

    if total == sum(data):

        group_name = input("Enter the name of your group: ")

        timestamp_group_name = group_name + str(unix_timestamp)
        # Specify the file path
        file_path = f"{timestamp_group_name}_GROUP.json"

        # Write the data to the JSON file
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
    else:
        print('Failed')


main()







