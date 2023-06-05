import hashlib
import sys
import datetime
import time
i = datetime.datetime.now()
print('运行时间为是{}月{}日{}点{}分{}秒'.format(i.month, i.day, i.hour, i.minute, i.second))
print("开始第一次自检")
time.sleep(1)
print("自建完毕")
jiami = "inti"
enter_main = "yes"
sha_file_main = "no"
md5_file_main = "no"
main = "no"
python_quit = "no"
quit_enter = "no"
while quit_enter == "no":
    print("目前已支持的加密方式有[md5,sha]")
    while main == "no":
        jiami = (input("请选择加密方式:"))
        if jiami in ["md5", "sha"]:
            main = "yes"
        else:
            main = "no"
            print("错误的加密方式")

    if main == "yes":
        message = (input("请输入原文:"))
    else:
        sys.exit(0)
    if jiami == "md5":
        if main == "yes":
            md5 = hashlib.md5(message.encode())
            print("正在加密，请稍后")
            time.sleep(1)
            print("加密结果为", md5.hexdigest())

            while md5_file_main == "no":
                file_xuanze = (input("是否输出到文件内:"))
                if file_xuanze in ["yes", "no"]:
                    if file_xuanze == "yes":
                        md5_file_main = "yes"
                        filename = (input("保存的文件名:"))
                        filenames = filename + ".txt"
                        with open(filenames, 'w') as file_object:
                            file_object.write(md5.hexdigest())
                            time.sleep(1)
                            print("已保存至", filenames)
                            print("感谢使用")
                            time.sleep(1)
                    else:
                        md5_file_main = "yes"
                        print("感谢使用")
                else:
                    md5_file_main = "no"
                    print("错误的输入")

        else:
            pass
    else:
        pass

    if jiami == "sha":
        if main == "yes":
            sha1 = hashlib.sha1(message.encode())
            print("正在加密，请稍后")
            time.sleep(1)
            print("加密结果为", sha1.hexdigest())

            while sha_file_main == "no":
                file_xuanze = (input("是否输出到文件内:"))
                if file_xuanze in ["yes", "no"]:
                    if file_xuanze == "yes":
                        sha_file_main = "yes"
                        filename = (input("保存的文件名:"))
                        filenames = filename + ".txt"
                        with open(filenames, 'w') as file_object:
                            file_object.write(sha1.hexdigest())
                            time.sleep(1)
                            print("已保存至", filenames)
                            print("感谢使用")
                            time.sleep(1)
                    else:
                        sha_file_main = "yes"
                        print("感谢使用")
                else:
                    sha_file_main = "no"
                    print("错误的输入")

    else:
        pass
    while quit_enter == "no":
        python_quit = input("是否退出yes of no:")
        if python_quit in ["yes", "no"]:
            if python_quit == "yes":
                quit_enter = "yes"
                break

            if python_quit == "no":
                quit_enter = "no"
                break

        else:
            print("错误的输入")
