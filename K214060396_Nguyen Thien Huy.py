'''tam giac'''

import math
while True:
    canh1 = float(input('Do dai canh 1:'))
    canh2 = float(input('Do dai canh 2:'))
    canh3 = float(input('Do dai canh 3:'))
    if abs(canh1 - canh2) < canh3 < canh1 + canh2:
        print('Tam giac hop le')
        break
    else:
        print('Tam giac khong hop le, moi ban nhap lai')
chuvi=canh1+canh2+canh3
p=chuvi//2
dientich=math.sqrt(p*(p-canh1)*(p-canh2)*(p-canh3)) #hê-rông
print(f'Chu vi tam giac: {chuvi:.0f}')
print(f'Dien tich tam giac: {dientich:.3f}')

print('----------------------------------------')

'''nhập vào con số'''

so=int(input('Nhap vao 1 con so:'))
if so==1:
    print('Tôi là người Việt Nam')
elif so==2:
    print('Tôi là người Hàn Quốc')
elif so==3 :
    print('Tôi là người Campuchia')
else:
    print('Tôi không phải là con người')

print('--------------------------------------------')

'''Giải phương trình bậc 1'''

print('Phuong trinh co dang ax+b=0')
a=float(input('Nhap vao a:'))
b=float(input('Nhap vao b:'))
if a==0:
    if b==0:
        print('PT vo so nghiem')
    else:
        print('PT vô nghiệm')
else:
    x=-b/a
    print(f'Nghiem cua pt la:{x:.3f}')

print('--------------------------------------------')

'''Ngày tháng năm'''

flag=0
while True:
    day=int(input('Nhập ngày:'))
    month=int(input('Nhập tháng:'))
    year=int(input('Nhập năm:'))
    if year%4==0:
        print(year,'là năm nhuận')
        if month==2 and day<=29:
            print('Tháng',month,'năm',year,'có 29 ngày')
            break
        elif (month==1 or month==3 or month==5 or month==6 or month==8 or month==10 or month==12) and (day>0 and day<=31):
            print('Tháng',month,'năm',year,'có 31 ngày')
            break
        elif (month==4 or month==7 or month==9 or month==11) and (day>0 and day<=30):
            print('Tháng',month,'năm',year,'có 30 ngày')
            break
        else:
            print('Bạn đã nhập sai!\nVui lòng nhập lại')
    else:
        if month==2 and day <= 28:
            print('Tháng', month,'năm',year, 'có 28 ngày')
            break
        elif (month==1 or month==3 or month==5 or month==6 or month==8 or month==10 or month==12) and (day>0 and day<=31):
            print('Tháng', month,'năm',year, 'có 31 ngày')
            break
        elif (month==4 or month==7 or month==9 or month== 11) and (day>0 and day<=30):
            print('Tháng', month,'năm',year, 'có 30 ngày')
            break
        else:
            print('Bạn đã nhập sai!\nVui lòng nhập lại')

print('--------------------------------------------')

'''n giai thua'''

print('Nhập số cần tính giai thừa')
z=int(input())
giai_thua=1
for i in range(1,z+1):
    giai_thua*=i
gt="{}!={}".format(z,giai_thua)
print(gt)

print('--------------------------------------------')

'''tính tổng N sô'''
n=int(input('nhập vào số N: '))
s=0
s1=0
s2=0
for j in range(n+1):
    s=s+j
print('tổng N: ',s)
print('')
#chẵn
for m in range(0,n+1):
    if m%2==0:
        s1=s1+m
    else:
        s2=s2+m
print('Tổng N số chẵn là:{}'.format(s1))
print('Tổng N số lẻ là:{}'.format(s2))

print('--------------------------------------------')

'''Chuyển Dec sang Bin'''
print('Chuyển số thập phân sang nhị phân')
o=int(input('Nhập vào số cần chuyển'))
while o>0:
    thuong=0
    du=0
    du+=o%2
    thuong+=o/2
    e=str(thuong)+str(du)
print(e)



