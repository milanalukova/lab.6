n = int(input())
synonyms = {}
for _ in range(n):
    x = input().split()
    n1 = x[0]
    n2 = x[1]
    synonyms[n1] = n2
    synonyms[n2] = n1
target_n = input()
print(synonyms[target_n]) 