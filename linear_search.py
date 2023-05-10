
def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("Found at index", x)
            return x
    print("Target is not in the list")
    return -1

my_list = [6, 3, 4, 2, 5, 7]
linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 8)

### Another Example of Linear Search

def linearSearch(array, n, x):
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)

## Linear search for Dictionary


# for state in state_capitals:
#     print(state) ---> This prints out the keys

def linear_search_dictionary(the_dictionary, target):
    for key, value in the_dictionary.items():
        if target == value:
            print("Success! You found the key", key)
            return key
    print("Failed! Key does not exist")
    return None

# Driver Code
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)

    # for i in range(0, n):
    #     if ()



