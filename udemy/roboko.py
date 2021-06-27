import csv

print('こんにちは！私はRobokoです。あなたの名前は何ですか？')
name  = input('')
print(name,'さん。どこの会社のデバイスが好きですか？')
device = input('')
print(name,'さん。ありがとうございました。良い一日を！さようなら')

file = open('device.csv', 'r')
data = csv.reader(file)
for row in data:
    for col in row:
        print(col, end=',')
    print()
file.close 
