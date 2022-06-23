num = list((input('Digite 3 números: ')).strip().split())
num = [float(i) for i in num]
num.sort()
print(num)