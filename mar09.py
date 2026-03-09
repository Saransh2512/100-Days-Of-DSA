#Implement a Priority Queue using an array. An element with smaller value has higher priority.
#Supported Operations:
#- insert x
#- delete
#- peek
#Input Format:
#- First line contains integer N
#- Next N lines contain operations
#Output Format:
#- Print the deleted or peeked element
#- Print -1 if the queue is empty

n = int(input())
pq = []

for _ in range(n):
    parts = input().split()

    if parts[0] == "insert":
        x = int(parts[1])
        pq.append(x)

    elif parts[0] == "peek":
        if len(pq) == 0:
            print(-1)
        else:
            print(min(pq))

    elif parts[0] == "delete":
        if len(pq) == 0:
            print(-1)
        else:
            m = min(pq)
            pq.remove(m)
            print(m)