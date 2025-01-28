# Test dictionary
test_dict = {
    "name1": "Akshay",
    "name2": "Rahul",
    "name3": "Akshay",
    "name4": "Priya",
    "name5": "Akshay"
}

# Count the frequency of "Akshay"
frequency = list(test_dict.values()).count("Akshay")

print(f"The value 'Akshay' appears {frequency} times in the dictionary.")
