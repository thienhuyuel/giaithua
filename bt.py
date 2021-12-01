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
        if entry == 1:
            f = open("Contact.txt", "r")
            contacts = f.readlines()
            f.close()
            if not contacts:
                print("Danh sách liên lạc trống")
            else:
                for i in contacts:
                    print(i)
        elif entry == 2:
            checked = False
            phone_number = input("Số điện thoại:")
            contact_name = input("Tên liên lạc?")
            f = open("Contact.txt", "r")
            contacts = f.readlines()
            f.close()
            for i in contacts:
                if i.find(name) != -1:
                    print("Liên lạc đã tồn tại!")
                    checked = True
                    break
            if checked == False:
                f = open("Contact.txt", "a")
                contacts.append(contact_name + ": " + phone_number + "\n")
                contacts = f.write(contacts[-1])
                f.close()
                print("Liên lạc đã được lưu")
        elif entry == 3:
            checked = False
            f = open("Contact.txt", "r")
            contacts = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in contacts:
                if i.find(name) != -1:
                    print(i)
                    checked = True
                    break
            if checked == False:
                print("Liên lạc không tồn tại")
        elif entry == 4:
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
        elif entry == 5:
            print("Xin cảm ơn!")
            break
        else:
            print("Mời bạn nhập lại!")

phonebook()