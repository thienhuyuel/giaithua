def welcome():
    entry = int(input("""
                        1. Hiển thị
                        2. Thêm liên lạc
                        3, Kiểm tra danh bạ
                        4. Xóa liên lạc
                        5. Thoát
                        Enter your number: """))
    return entry

def phonebook():
    contacts = []
    while True:
        entry = welcome()
        if entry == 4:
            checked = False
            delete_var = 0
            f = open("Contact.txt", "r")
            contacts = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in contacts:
                if i.find(name) != -1:
                    print(i)
                    delete_var = contacts.index(i)
                    checked = True
                    confirm = input("Bạn có chắc chắn xóa? Y/N:")
                    if confirm.capitalize() == "Y":
                        contacts.pop(delete_var)
                        f = open("Contact.txt", "w")
                        for i in contacts:
                            f.write(i)
                        f.close()
                    else:
                        print("Quay trở lại menu!")
                    break
            if checked == False:
                print("Liên lạc không tồn tại")
phonebook()