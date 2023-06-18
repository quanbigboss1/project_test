import random

def Welcome():
    print("----Chào mừng bạn đã đến với chương trình chẵn lẻ----")
    print("____________________Menu_______________________")
    print("Chọn 1 để chơi trò chơi\nGhi exit để thoát chương trình")
    print("---- nhấn số để thực hiện chức năng menu ------")
    switch_case(input("Nhập giá trị : "))
def switch_case(argument):
    if argument == '1':
        case1()
        Welcome()
    elif argument == "exit":
        print("kết thúc chương trình - goodbye")
    else:
        print("Vui lòng nhập 1 hoặc ghi exit để thoát khỏi chương trình")
        Welcome()

def case1():
    tk = 1 # Số dư tài khoản ban đầu
    while True:
        random_number = random.randint(1, 2)
        chanle = str(random_number)
        a = input("Chọn số bạn muốn chọn chẳn hay lẻ (nhấn exit để thoát): ")
        if a == 'exit':  # Nhấp 'exit' để thoát 
            print("Bạn đã kết thúc trò chơi với số dư là : ",tk,"VNĐ")
            break
        if a == chanle:
            print("Bạn đã thắng")
            tk *= 2
        else:
            print("Bạn đã thua")
            
        print("Số dư tài khoản của bạn là: ", tk, "VNĐ")
    return tk
Welcome()