'''Tính tổng n số'''
tong=[]
s=0
m=int(input('số các số hạng: '))
for j in range(m):
    a=int(input('Nhập vào số: '))
    tong.append(a)
for so in tong:
    s=s+so
print('Tổng của',m,'số là: ',s)