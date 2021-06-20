flag = True
n = int(input("値を入力してください"))

for i in range(2,n):
  if n % i == 0:
    flag = False
    break

if flag == True:
  print("{}は素数です".format(n))


if flag == False:
  print("{}は素数ではありません".format(n))
