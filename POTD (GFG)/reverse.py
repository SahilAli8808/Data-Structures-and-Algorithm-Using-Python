def reverseWords(S):
    words = S.split('.')
    print(words)
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words using '.' as the separator
    reversed_string = '.'.join(reversed_words)
    
    return reversed_string
input_string = "i.like.this.program.very.much"
output_string = reverseWords(input_string)
print(output_string)  # Output: "much.very.program.this.like.i"
