# Problems
# 1.	Reverse a string
# a.	Write code that takes a string as input and returns the string reversed
# b.	i.e. “Hello” will be returned as “olleH”
def reverse(word):
    backwards_word = ""
    for letter in range(len(word)-1, -1, -1):
        backwards_word += word[letter]
    return backwards_word
print(f"Your reversed word is: {reverse('Hello')}")

print("")
# 2.	Capitalize letter
# a.	Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
string = "this string will capitalize the first letter in each word!"
capitalized_string = string.title()
print(capitalized_string)

print("")
# 3.	Compress a string of characters
# a.	For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"
def compress(string):
    index = 0
    compressed = ""
    string_length = len(string)
    while index != string_length:
        count = 1
        while (index < string_length-1) and (string[index] == string[index+1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed += str(string[index])
        else:
            compressed += str(string[index]) + str(count)
        index = index + 1
    return compressed
string = "bookkeeping"
print(compress(string))

# 4.	BONUS CHALLENGE: Palindrome
# a.	A word, phrase, or sequence that reads the same backward as forward i.e. madam
# b.	Write code that takes a user input and checks to see if it is a Palindrome and reports the result
# def palindrome(string):