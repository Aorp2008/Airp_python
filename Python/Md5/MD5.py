import hashlib


def hash_login_sha512(passwd):
    login_sha512 = hashlib.sha512(passwd.encode())
    return login_sha512.hexdigest()


def hash_md5(message):
    md5 = hashlib.md5(message.encode())
    return md5.hexdigest()


def hash_sha1(message):
    sha1 = hashlib.sha1(message.encode())
    return sha1.hexdigest()


def hash_sha256(message):
    sha256 = hashlib.sha256(message.encode())
    return sha256.hexdigest()


def hash_sha512(message):
    sha512 = hashlib.sha512(message.encode())
    return sha512.hexdigest()


def hash_new(message):
    new = hashlib.new(message.encode)
    return new.hexdigest()


while True:
    User_input_User_name = input("User:")
    User_input_User_Passwd = input("Passwd:")
    login_hash_Passwd = hash_login_sha512(User_input_User_Passwd)
    with open("User.txt", mode="rt", encoding='utf-8') as file:
        for User in file:
            User_Name, User_Passwd = User.strip().split("----")
            if User_input_User_name == User_Name and login_hash_Passwd == User_Passwd:
                login_main = "Yes"
                print("登陆成功")
                break
        else:
            login_main = "No"
            print("登陆失败")
    if login_main == "Yes":
        break
while True:
    print(r"exit(退出),hash(加密)")
    User_input_chenge = input("<<<")
    if User_input_chenge in ["exit", "hash"]:
        if User_input_chenge == "exit":
            exit()
        elif User_input_chenge == "hash":
            print("目前支持{md5,sha1,sha256,sha512}")
            while True:
                User_input_hash = input("<<<")
                if User_input_hash == "~exit":
                    break
                if User_input_hash in ["md5", "sha1", "sha256", "sha512"]:
                    if User_input_hash == "md5":
                        while True:
                            User_input_message = input("原文:")
                            if User_input_message == "~exit":
                                print("目前支持{md5,sha1,sha256,sha512}")
                                break
                            else:
                                pass
                            print(hash_md5(User_input_message))
                    elif User_input_hash == "sha1":
                        while True:
                            User_input_message = input("原文:")
                            if User_input_message == "~exit":
                                print("目前支持{md5,sha1,sha256,sha512}")
                                break
                            else:
                                pass
                            print(hash_sha1(User_input_message))
                    elif User_input_hash == "sha256":
                        while True:
                            User_input_message = input("原文:")
                            if User_input_message == "~exit":
                                print("目前支持{md5,sha1,sha256,sha512}")
                                break
                            else:
                                pass
                            print(hash_sha256(User_input_message))
                    elif User_input_hash == "sha512":
                        while True:
                            User_input_message = input("原文:")
                            if User_input_message == "~exit":
                                print("目前支持{md5,sha1,sha256,sha512}")
                                break
                            else:
                                pass
                            print(hash_sha512(User_input_message))
    else:
        print("错误的输入")
