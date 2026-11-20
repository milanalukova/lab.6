n = int(input())
files = {}
for _ in range(n):
  parts = input().split()
  filename = parts[0]
  rights = parts[1:]
  files[filename] = rights
ops = {"read": "R", "write": "W", "execute": "X"}
m = int(input())
for _ in range(m):
  action, filename = input().split()
  code = ops[action]

  if code in files[filename]:
    print("OK")
  else:
    print("Access denied")