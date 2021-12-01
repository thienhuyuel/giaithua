'''Tính tổng n phân số'''
phanso=[0,1]
n=int(input('số phân số cần tính: '))

for i in range(n):
    ps=[]
    print('Nhập phân số thứ', i+1)
    ps.append(int(input('nhập tử số: ')))
    ps.append(int(input('nhập mẫu số: ')))
    print('')
    phanso[0]=phanso[0]*ps[1]+phanso[1]*ps[0]
    phanso[1]=phanso[1]*ps[1]

a=phanso[0]
b=phanso[1]
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
UCLN=a

print('Tổng ',n,'phân số là: ',phanso[0]//UCLN,'/',phanso[1]//UCLN)   
