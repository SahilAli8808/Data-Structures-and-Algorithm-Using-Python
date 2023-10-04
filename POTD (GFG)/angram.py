def isAnagram(a, b):
    # Check if the lengths of both strings are the same
    if len(a) != len(b):
        return False
    
    # Initialize frequency dictionaries for both strings
    freq_a = {}
    freq_b = {}
    
    # Count the frequency of characters in string 'a'
    for char in a:
        print(char)
        print(f"{freq_a.get(char, 0)}")
        freq_a[char] = freq_a.get(char, 0) + 1
    
    # Count the frequency of characters in string 'b'
    for char in b:
        freq_b[char] = freq_b.get(char, 0) + 1
    
    # Compare the frequency dictionaries
    return freq_a == freq_b

# Example 1
a1 = "geeksforgeeks"
b1 = "forgeeksgeeks"
print(isAnagram(a1, b1))  # Output: True

# # Example 2
# a2 = "allergy"
# b2 = "allergic"
# print(isAnagram(a2, b2))  # Output: False
