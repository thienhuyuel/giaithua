from tkinter import *
from selenium import webdriver

def dangnhap():
    user = username.get()
    pas = password.get()
    driver = webdriver.Chrome()
    driver.get('https://facebook.com')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(user)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys(pas)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    thongbao.insert(INSERT, 'Đã đăng nhập')
    thongbao.configure(fg='green')


ROOF = Tk()
ROOF.geometry('550x100')
ROOF.title('PHẦN MỀM MỆT MỎI VÌ HỌC GIỎI == MAKE BY HỒ HẬN TÌNH ĐỜI')
ROOF.configure(bg='lavender')
Label(ROOF, text='Tên đăng nhập: ', bg='lavender').grid(row=0, column=0)
Label(ROOF, text='Mật khẩu: ', bg='lavender').grid(row=1, column=0)
username = Entry(ROOF, width=15)
username.grid(row=0, column=1)
password = Entry(ROOF, width=15)
password.grid(row=1, column=1)
Button(ROOF, text='Đăng nhập', bg='skyblue', command=dangnhap).grid(row=2, column=0)
thongbao = Text(ROOF, height = 1, width=15)
thongbao.grid(row=2, column=1)
ROOF.mainloop()