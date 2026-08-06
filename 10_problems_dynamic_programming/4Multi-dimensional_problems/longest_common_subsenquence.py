from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            # Base case: If we reach the end of either string, no more characters to compare
            if i == len(text1) or j == len(text2):
                return 0

            # If the characters match, move to the next characters in both strings
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)

            # If the characters don't match, explore both possibilities:
            # 1. Move to the next character in text1
            # 2. Move to the next character in text2
            return max(dp(i + 1, j), dp(i, j + 1))

        # Start the dynamic programming recursion from the start of both strings
        return dp(0, 0)


# Test cases
solution = Solution()

# Test case 1: text1 = "abcde", text2 = "ace"
text1_1 = "abcde"
text2_1 = "ace"
# The longest common subsequence is "ace", so output should be 3
print(solution.longestCommonSubsequence(text1_1, text2_1))  # Output: 3

# Test case 2: text1 = "abc", text2 = "def"
text1_2 = "abc"
text2_2 = "def"
# There are no common subsequences, so output should be 0
print(solution.longestCommonSubsequence(text1_2, text2_2))  # Output: 0

"""
https://leetcode.com/problems/longest-common-subsequence/description/
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

#--------------------------------------------------------------------------------------#

Overview
This is a nice problem, as unlike some interview questions, this one is a real-world problem! Finding the longest
common subsequence between two strings is useful for checking the difference between two files (diffing). Git needs to
do this when merging branches. It's also used in genetic analysis (combined with other algorithms) as a measure of
similarity between two genetic codes.

For that reason, the examples used in this article will be strings consisting of the letters a, c, g, and t. You might
remember these letters from high school biology—they are the symbols we use to represent genetic codes. By using just
four letters in examples, it is easier for us to construct interesting examples to discuss here. You don't need to know
anything about genetics or biology for this though, so don't worry.

Before we look at approaches that do work, we'll have a quick look at some that do not. This is because we're going to
pretend that you've just encountered this problem in an interview, and have never seen it before, and have not been
told that it is a "dynamic programming problem". After all, in this interview scenario, most people won't realize
immediately that this is a dynamic programming problem. Being able to approach and explore problems with an open mind
without jumping to early conclusions is essential in tackling problems you haven't seen before.

What is a Common Subsequence?

Here's an example of two strings that we need to find the longest common subsequence of.

Two strings "actgattag" and "gtgtgatcg"

A common subsequence is a sequence of letters that appears in both strings. Not every letter in the strings has to be
used, but letters cannot be rearranged. In essence, a subsequence of a string s is a string we get by deleting some
letters in s.

Here are some of the common subsequences for the above example. To help show that the subsequence really is a common
subsequence, we've drawn lines between the corresponding characters.

Common subsequence "tga"
Common subsequence "ttt"
Common subsequence "g"
Common subsequence "tgtg"

Drawing lines between corresponding letters is a great way of visualizing the problem and is potentially a valuable
technique to use on a whiteboard during an interview. Observe that if lines cross over each other, then they do not
represent a common subsequence.

This is because lines that cross over are representing letters that have been rearranged.
We will use and refer to "lines" between the words extensively throughout this article.

Brute-force

The most obvious approach would be to iterate through each subsequence of the first string and check whether or not it
is also a subsequence of the second string.

This, however, will require exponential time to run. The number of subsequences in a string is up to 2L, where L is the
length of the string. This is because, for each character, we have two choices; it can either be in the subsequence or
not in it. Duplicates characters reduce the number of unique subsequences a bit, although in the general case, it's
still exponential.

This would be a brute-force approach.

Greedy

By this point, it's hopefully clear that we're dealing with an optimization problem. We need to generate a common
subsequence that has the maximum possible number of letters. Using our analogy of drawing lines between the words, we
could also phrase it as maximizing the number of non-crossing lines.

There are a couple of strategies we use to design a tractable (non-exponential) algorithm for an optimization problem.
    1. Identifying a greedy algorithm
    2. Dynamic programming

There is no guarantee that either is possible. Additionally, greedy algorithms are strictly less common than dynamic
programming algorithms and are often more difficult to identify. However, if a greedy algorithm exists, then it will
almost always be better than a dynamic programming one. You should, therefore, at least give some thought to the
potential existence of a greedy algorithm before jumping straight into dynamic programming.

The best way of doing this is by drawing an example and playing around with it. One idea could be to iterate through
the letters in the first word, checking whether or not it is possible to draw a line from it to the second word
(without crossing lines). If it is, then draw the left-most line possible.

For example, here's what we would do with the first letter of our example from earlier.
Connecting 'a' in top to 'a' in bottom

And then, the second letter.
Connecting 'c' in top to 'c' in bottom

And finally, the third letter.
Connecting 'g' in top to 'g' in bottom

This solution, however, isn't optimal. Here is a better solution.
A better solution "tgag"

What if we were to do the same, but instead going from the second word to the first word? Perhaps one way or the other
will always be optimal?

A greedy solution with second string

Unfortunately, this hasn't worked either. This solution is still worse than a better one we know about.

Perhaps, instead, we could draw all possible lines. Could there be a way of eliminating some of the lines that cross over?

Uhoh, we now have what looks like an even more complicated problem than the one we began with. With some lines crossing
over many other lines, where would you even begin?

Applying Dynamic Programming to a Problem

While it's very difficult to be certain that there is no greedy algorithm for your interview problem, over time you'll
build up an intuition about when to give up. You also don't want to risk spending so long trying to find a greedy
algorithm that you run out of time to write a dynamic programming one (and it's also best to make sure you write a
working solution!).

Besides, sometimes the process used to develop a dynamic programming solution can lead to a greedy one. So, you might
end up being able to further optimize your dynamic programming solution anyway.

Recall that there are two different techniques we can use to implement a dynamic programming solution; memoization and
tabulation.
    Memoization is where we add caching to a function (that has no side effects). In dynamic programming, it is
    typically used on recursive functions for a top-down solution that starts with the initial problem and then
    recursively calls itself to solve smaller problems.
    Tabulation uses a table to keep track of subproblem results and works in a bottom-up manner: solving the smallest
    subproblems before the large ones, in an iterative manner. Often, people use the words "tabulation" and "dynamic
    programming" interchangeably.
For most people, it's easiest to start by coming up with a recursive brute-force solution and then adding memoization
to it. After that, they then figure out how to convert it into an (often more desired) bottom-up tabulated algorithm.

"""