N,D = map(int,input().split())

count = 0
for i in range(N):
  X,Y = map(int,input().split())
  d2 = X**2 + Y**2
  if d2 <= D**2:
    count += 1
    
print(count)
