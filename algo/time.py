print('１つ目の時間を入力してください')
print('時')
h1 = int(input())
print('分')
m1 = int(input())
print('秒')
s1 = int(input())
print('２つ目の時間を入力してください')
print('時')
h2 = int(input())
print('分')
m2 = int(input())
print('秒')
s2 = int(input())

time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2

if time1 > time2:
    diff = time1 - time2
else:
    diff = time2 - time1

h = diff / 3600
n = diff % 3600
m = n / 60
s = n % 60
print(f"２つの時間差は、",{h},'時間',{m},'分',{s},'秒です。')