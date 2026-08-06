def countGroups(N, n):
    visited = [False] * n

    def dfs(person):
        for friend in range(n):
            if N[person][friend] == '1' and not visited[friend]:
                visited[friend] = True
                dfs(friend)

    groups = 0
    for person in range(n):
        if not visited[person]:
            dfs(person)
            groups += 1

    return groups

# Test case
N = ["1100", "1110", "0110", "0001"]
n = 4
print(countGroups(N, n))  # Output: 2

# Test case
N = ["10000", "01000", "00100", "00010", "00001"]
n = 5
print(countGroups(N, n))  # Output: 2


