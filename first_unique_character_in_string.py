def firstUniqChar(s) -> int:
    # create an empty dictionary
    counter = {}
    # First pass: Count the frequency of each character in the string
    for char in s:
        counter[char] = counter.get(char, 0) + 1

        # Second pass: Find the first unique character
    for index, char in enumerate(s):
        if counter[char] == 1:
            return index

        # If no unique character is found, return -1
    return -1

    # loop through the char in s. For each char:
    # if the char is a key in dictionary:
    # add one to the value
    # else:
    # add char as a ket, value = 1

    # loop through the INDEXES in s. For each index:
    # find the char in s at that index
    # if the value for that char == 1, return index

    # If we get to the end, this means there are no unique chars
    # So return -1

    # PRO Tip: Run your code as you go
    # PRO Tip: Use print statements

    '''
        Understand:

        Pro TIP: Create a test case for your own example 
        string with some inique characters "baby". => -1 
        string with some unique characters: "baba" => -1 

        PRO TIP: Ask the interviever am I done?

        Plan:
        Approach: Count the characters in s.
        Loop through s again and return the index of 
        the first chr that has a frequency of 1 
        (Or return -1)

    '''


# Test the function
s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"
# Output: 0, since 'l' is the first unique character
print(firstUniqChar(s1))
print(firstUniqChar(s2))
print(firstUniqChar(s3))
