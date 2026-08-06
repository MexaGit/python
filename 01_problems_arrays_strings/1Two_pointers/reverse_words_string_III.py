def reverseWords(s: str) -> str:
    # Step 1: Split the sentence into words
    words = s.split()

    # Step 2: Reverse each word using two pointers
    for i in range(len(words)):
        # e.g: ["Let's", 'take', 'LeetCode', 'contest']
        word = list(words[i])  # Convert the word to a list of characters (strings are immutable)
        # print(words[i])
        left, right = 0, len(word) - 1  # Set two pointers: left at the start, right at the end

        # Step 3: Reverse the characters in the word
        while left < right:
            # Swap the characters at the left and right pointers
            word[left], word[right] = word[right], word[left]
            left += 1  # Move the left pointer to the right
            right -= 1  # Move the right pointer to the left

        # After reversing the word, join the characters back together
        words[i] = ''.join(word)

    # Step 4: Join the reversed words into a single string and return it
    return ' '.join(words)


# Example usage
print(reverseWords("Let's take LeetCode contest"))  # Output: "s'teL ekat edoCteeL tsetnoc"

"""
Time Complexity of reverseWords:

Splitting the sentence into words:
The function uses Python’s split() method to split the input string s into individual words. This operation scans 
through the entire string once and takes O(n) time, where n is the length of the input string s.

Reversing each word:
The function iterates over each word in the list of words. If there are k words in the sentence and the total number 
of characters is n, the sum of all the characters across the words is n. For each word, the function reverses its 
characters using a two-pointer technique, which takes O(m) time for a word of length m.
Since each character is reversed exactly once, across all words, this process takes O(n) time in total.

Joining the reversed words:
After reversing the words, the join() method is used to concatenate them back into a single string. This operation 
takes O(n) time since it involves joining all characters in the list.
Thus, the overall time complexity is O(n), where n is the total number of characters in the input string.

Space Complexity of reverseWords:

Space for the list of words:
The split() method creates a list of words, and each word is a string. This requires O(n) space, where n is 
the total number of characters in the input string.

Space for each word's characters:
During the reversal process, each word is converted into a list of characters, which requires temporary O(m) space 
for each word of length m. However, since we are processing one word at a time, the extra space used is O(m) at any 
given point. Summing over all words, the space required is O(n).

Constant space for pointers:
The two pointers (left and right) used to reverse each word take O(1) constant space.
Thus, the overall space complexity is O(n) due to the list of words and character lists used during the process.
"""