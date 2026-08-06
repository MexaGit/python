from collections import defaultdict, deque
from typing import List

class Solution:
    # Breadth First Search
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if endWord is in the word list, otherwise return 0 since no transformation is possible
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # All words are the same length
        L = len(beginWord)

        # Dictionary to store all combinations of words where one letter is replaced by '*'
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Add each word to the dictionary by creating keys with one missing letter
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Initialize BFS queue with the starting word and level (starting from 1)
        queue = deque([(beginWord, 1)])
        # Set to keep track of visited words
        visited = {beginWord: True}

        # BFS loop
        while queue:
            current_word, level = queue.popleft()

            # Try changing each character in current_word
            for i in range(L):
                # Intermediate word with one character replaced by '*'
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Go through all words that can be formed by this intermediate word
                for word in all_combo_dict[intermediate_word]:
                    # If we find the endWord, return the current level plus 1
                    if word == endWord:
                        return level + 1

                    # If this word has not been visited, mark it as visited and add to queue
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))

                # Empty the intermediate list after processing to avoid revisiting
                all_combo_dict[intermediate_word] = []

        # If no transformation sequence was found, return 0
        return 0

# Test Cases
# Test Case 1:
# beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# The transformation sequence is: "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# Expected output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog",
# which is 5 words long.
print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Output: 5

# Test Case 2:
# beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# There is no valid transformation sequence to reach "cog"
# Expected output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # Output: 0

"""
https://leetcode.com/problems/word-ladder/description/
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Solution Article
We are given a beginWord and an endWord. Let these two represent start node and end node of a graph. We have to reach 
from the start node to the end node using some intermediate nodes/words. The intermediate nodes are determined by the 
wordList given to us. The only condition for every step we take on this ladder of words is the current word should 
change by just one letter.

We will essentially be working with an undirected and unweighted graph with words as nodes and edges between words 
which differ by just one letter. The problem boils down to finding the shortest path from a start node to a destination
node, if there exists one. Hence it can be solved using Breadth First Search approach.

One of the most important step here is to figure out how to find adjacent nodes i.e. words which differ by one letter. 
To efficiently find the neighboring nodes for any given word we do some pre-processing on the words of the given 
wordList. The pre-processing involves replacing the letter of a word by a non-alphabet say, *.

This pre-processing helps to form generic states to represent a single letter change.
For e.g. Dog ----> D*g <---- Dig
Both Dog and Dig map to the same intermediate or generic state D*g.

The preprocessing step helps us find out the generic one letter away nodes for any word of the word list and hence 
making it easier and quicker to get the adjacent nodes. Otherwise, for every word we will have to iterate over the 
entire word list and find words that differ by one letter. That would take a lot of time. This preprocessing step 
essentially builds the adjacency list first before beginning the breadth first search algorithm.

For eg. While doing BFS if we have to find the adjacent nodes for Dug we can first find all the generic states for Dug.
Dug => *ug
Dug => D*g
Dug => Du*
The second transformation D*g could then be mapped to Dog or Dig, since all of them share the same generic state. 
Having a common generic transformation means two words are connected and differ by one letter.

#------------------------------------------------------------------------------------------------#

Approach 1: Breadth First Search
Intuition
Start from beginWord and search the endWord using BFS.

Algorithm
1. Do the pre-processing on the given wordList and find all the possible generic/intermediate states.
Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which
have the same intermediate word.
2. Push a tuple containing the beginWord and 1 in a queue. The 1 represents the level number of a node.
We have to return the level of the endNode as that would represent the shortest sequence/distance from the beginWord.
3. To prevent cycles, use a visited dictionary.
4. While the queue has elements, get the front element of the queue. Let's call this word as current_word.
5. Find all the generic transformations of the current_word and find out if any of these transformations is also a
transformation of other words in the word list. This is achieved by checking the all_combo_dict.
6. The list of words we get from all_combo_dict are all the words which have a common intermediate state with the
current_word. These new set of words will be the adjacent nodes/words to current_word and hence added to the queue.
7. Hence, for each word in this list of intermediate words, append (word, level + 1) into the queue where level is the
level for the current_word.
8. Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.
    Termination condition for standard BFS is finding the end word.
"""