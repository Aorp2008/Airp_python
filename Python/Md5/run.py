import hashlib


def logup_inspect(inspect_user_name):
    if inspect_user_name == "~exit":
        return "exit"
    else:
        with open("User_login", mode="rt", encoding='utf-8') as file:
            for User in file:
                user_name, user_passwd = User.strip().split("----")
                if inspect_user_name == user_name:
                    return "No"
            else:
                return "Yes"


def user_login(user_input_name, user_input_passwd):
    login_hash_passwd = hash_login_md5(user_input_passwd)
    with open("User_login", mode="rt", encoding='utf-8') as file:
        for User in file:
            user_name, user_passwd = User.strip().split("----")
            if user_input_name == user_name and login_hash_passwd == user_passwd:
                return "Yes"
        else:
            return "No"


def chenge_list(username):
    with open("User_chenge_list", mode='rt', encoding='utf-8') as list_chenge:
        for User_chenge in list_chenge:
            user_name, username_chenge = User_chenge.strip().split("--")
            if username == user_name:
                if username_chenge == "0":
                    return "0"
                elif username_chenge not in ["0"]:
                    return username_chenge
                else:
                    return "X"


def hash_login_md5(passwd):
    login_md5 = hashlib.md5(passwd.encode())
    return login_md5.hexdigest()


def logup(logup_username, logup_passwd):
    logup_passwd_md5 = hash_login_md5(logup_passwd)
    if logup_inspect(logup_username) == "Yes":
        with open("User_chenge_list", mode="a", encoding='utf-8') as logup_User:
            logup_User.write(f"{logup_username}--{5}\n")
        with open("User_login", mode="a", encoding='utf-8') as logup_User:
            logup_User.write(f"{logup_username}----{logup_passwd_md5}\n")
        return "0"
    elif logup_inspect(logup_username) == "No":
        return "X"
    elif logup_inspect(logup_username) == "exit":
        return "exit"


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
    print("login(登录)\nlogup(注册)")
    chenge = input("<<").strip()
    if chenge in ["login", "logup", "~admin"]:
        if chenge == "login":
            admin_login_main = "No"
            while True:
                User_input_User_name = input("User:").strip()
                User_input_User_Passwd = input("Passwd:").strip()
                user_log = user_login(User_input_User_name, User_input_User_Passwd)
                if user_log == "Yes":
                    login_main = "Yes"
                    print("登陆成功")
                    break
                else:
                    login_main = "No"
                    print("登陆失败")

        elif chenge == "logup":
            while True:
                logup_input_Username = input("Username:").strip()
                logup_input_Passwd = input("Passwd:").strip()
                inspect_logup = logup(logup_input_Username, logup_input_Passwd)
                if inspect_logup == "0":
                    print("注册成功")
                    login_main = "No"
                    break
                elif inspect_logup == "X":
                    print("注册失败[用户已存在]")
                elif inspect_logup == "exit":
                    admin_login_main = "No"
                    login_main = "No"
                    break
        elif chenge == "~admin":
            admin_input_passwd = input("管理员密码:")
            if user_login("~admin", admin_input_passwd) == "Yes":
                admin_login_main = "Yes"
            else:
                continue
    if admin_login_main == "Yes":
        break
    else:
        if login_main == "Yes":
            break
        else:
            continue
while True:
    print(r"exit(退出),hash(加密)")
    if chenge_list(User_input_User_name) == "0":
        print("您的机会已用尽,请尽快联系管理员")
        exit(0)
    elif chenge_list(User_input_User_name) == "X":
        print("您的账户未激活,联系管理员")
        exit(0)
    else:
        print("您的次数剩余:", chenge_list(User_input_User_name))
    User_input_chenge = input("<<<").strip()
    if User_input_chenge in ["exit", "hash"]:
        if User_input_chenge == "exit":
            exit()
        elif User_input_chenge == "hash":
            print("目前支持{md5,sha1,sha256,sha512}")
            while True:
                User_input_hash = input("<<<").strip()
                if User_input_hash == "~exit":
                    break
                if User_input_hash == "~List":
                    print("目前支持{md5,sha1,sha256,sha512}")
                    continue
                if User_input_hash in ["md5", "sha1", "sha256", "sha512"]:
                    if User_input_hash == "md5":
                        while True:
                            User_input_message = input("原文:")
                            if User_input_message == "~exit":
                                print("目前支持{md5,sha1,sha256,sha512}")
                                break
                            else:
                                pass
                            print("结果为:", hash_md5(User_input_message))
                    elif User_input_hash == "sha1":
                        while True:
                            User_input_message = input("原文:")
                            if User_input_message == "~exit":
                                print("目前支持{md5,sha1,sha256,sha512}")
                                break
                            else:
                                pass
                            print("结果为:", hash_sha1(User_input_message))
                    elif User_input_hash == "sha256":
                        while True:
                            User_input_message = input("原文:")
                            if User_input_message == "~exit":
                                print("目前支持{md5,sha1,sha256,sha512}")
                                break
                            else:
                                pass
                            print("结果为:", hash_sha256(User_input_message))
                    elif User_input_hash == "sha512":
                        while True:
                            User_input_message = input("原文:")
                            if User_input_message == "~exit":
                                print("目前支持{md5,sha1,sha256,sha512}")
                                break
                            print("结果为:", hash_sha512(User_input_message))
                else:
                    print("不支持的加密方式,请输入'~List'查询目前支持的加密方式")
    else:
        print("错误的输入")
