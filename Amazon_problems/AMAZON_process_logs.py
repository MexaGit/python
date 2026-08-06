def processLogs(logs, threshold):
    # Dictionary to store the count of transactions for each user
    transaction_count = {}

    # Process each log entry
    for log in logs:
        # Split the log into sender, recipient, and amount
        sender, recipient, _ = log.split()

        # Increment transaction count for sender
        if sender not in transaction_count:
            transaction_count[sender] = 0
        transaction_count[sender] += 1

        # Increment transaction count for recipient, only if different from sender
        if recipient != sender:
            if recipient not in transaction_count:
                transaction_count[recipient] = 0
            transaction_count[recipient] += 1

    # Filter users who have transactions greater than or equal to the threshold
    result = [user for user, count in transaction_count.items() if count >= threshold]

    # Sort the result in ascending numeric order (convert to int for sorting)
    result.sort(key=int)

    return result


# Sample Input
logs = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
threshold = 2

logs1 = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold1 = 2


# Function call
print(processLogs(logs, threshold))  # Expected output: ['1', '2']
print(processLogs(logs1, threshold1))  # Expected output: ['88', '99']

"""
Your Amazonian team is responsible for maintaining a monetary transaction service. The transactions are tracked in 
a log file. A log file is provided as a string array where each entry represents a transaction to the service. 
Each transaction consists of:

sender_user_id: A unique identifier for the user that initiated the transaction. It consists of only digits, with 
a maximum of 9 digits.
recipient_user_id: A unique identifier for the user that is receiving the transaction. It consists of only digits, 
with a maximum of 9 digits.
amount_of_transaction: The amount of the transaction. It consists of only digits, with a maximum of 9 digits.
The values are separated by a space. For example: "sender_user_id recipient_user_id amount_of_transaction".

Users that perform an excessive amount of transactions might be abusing the service, so you have been tasked to 
identify the users that have a number of transactions over a threshold. The list of user IDs should be ordered in 
ascending numeric value.

Example:
logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = 2
The transaction count for each user, regardless of the role, is as follows:

ID	Transactions
99	3
88	2
12	1
32	1
There are two users with at least threshold = 2 transactions: 99 and 88. In ascending order, the returned array 
is ['88', '99'].

Note: In the last log entry, user 12 was on both sides of the transaction. This counts as only 1 transaction for 
user 12.

Function Description:
Complete the function processLogs with the following parameters:

String logs[n]: Each logs[i] denotes the ith entry in the logs.
int threshold: The minimum number of transactions that a user must have to be included in the result.
Returns:

string[]: An array of user IDs as strings, sorted in ascending numeric value.

Constraints:
1<n<10'5
1<threshold<n
The sender_user_id, recipient_user_id, and amount_of_transaction contain only characters in the range ASCII [‘0’-‘9’].
The sender_user_id, recipient_user_id, and amount_of_transaction start with a non-zero digit.
0 < \text{length of sender_user_id, recipient_user_id, amount_of_transaction} < 9
The result will contain at least one element.

Sample Input:
STDIN                    Function
--------                 ---------------
4                        logs[] size = 4
1  2  50                 logs = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
1  7  70
1  3  20
2  2  17
2                        threshold = 2
"""
