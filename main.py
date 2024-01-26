##  Student management system
##  Author by :ChenYong
##  Created on 2023-12-12
##  Version 1.0
##  Python 3.9.7
import os
from colorama import init, Fore, deinit, Style
import colorama
import pickle
import base64


class color:
    def __init__(self):
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.yellow = Fore.YELLOW
        self.blue = Fore.BLUE
        self.magenta = Fore.MAGENTA
        self.cyan = Fore.CYAN
        self.white = Fore.WHITE
        self.reset = Fore.RESET

    def print_BLUE(message):
        print(Fore.BLUE + message)
        print(Style.RESET_ALL)

    def print_RED(message):
        print(Fore.RED + message)
        print(Style.RESET_ALL)

    def print_GRREN(message):
        print(Fore.GREEN + message)
        print(Style.RESET_ALL)


class scores:
    def __init__(self, english, chinese, math):
        self.english = english
        self.chinese = chinese
        self.math = math

    def get_aver(self):
        return (self.english + self.chinese + self.math) / 3

    def get_sum(self):
        return self.english + self.chinese + self.math

    def get_english(self):
        return self.english

    def get_chinese(self):
        return self.chinese

    def get_math(self):
        return self.math


class students:
    def __init__(self, id, name, age, phone, scores, password):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.scores = scores
        self.password = password

    def get_id(self):
        return self.id

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_scores(self):
        return self.scores

    def get_password(self):
        return self.password


class systemForAdmin:
    def __init__(self):
        self.students = []
        self.color = color()
        self.students_tmp = []

    # 显示菜单
    def show_menu(self):
        while True:
            print("请输入你的选择：")
            print("1.添加学生")
            print("2.删除学生")
            print("3.查询学生")
            print("4.查询所有学生")
            print("5.对学生进行排序")
            print("6.修改学生数据")
            print("7.退出系统并保存数据")
            choice = input()
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.show_student()
            elif choice == "4":
                self.showAllStudents()
            elif choice == "5":
                self.sort_student()
            elif choice == "6":
                self.modify()
            elif choice == "7":
                self.save_data()
                color.print_GRREN("数据保存成功，系统退出！！！")
                os._exit(0)
            else:
                os.system("cls")
                color.print_RED("输入错误，请重新输入")

    # 保存数据
    def save_data(self):
        file = open("systemAdmin.txt", "wb")
        pickle.dump(self, file)
        file.close()

    # 判断学生是否存在
    def judgeIsExist(self, student):
        for stu in self.students:
            # 当名字或者id相同时，判断为同一个学生
            if stu.get_id() == student.get_id():
                return False
        return True

    # 添加学生
    def add_student(self):
        try:
            id = input("请输入学生的学号：")
            if not id.isdigit():
                color.print_RED("学号输入有误，添加失败，请输入数字！！！")
                return
            name = input("请输入学生的姓名：")
            if not name.isalpha():
                color.print_RED("姓名输入有误，添加失败，请输入字符！！！")
                return
            age = input("请输入学生的年龄：")
            if not age.isdigit():
                color.print_RED("年龄输入有误，添加失败，请输入数字！！！")
                return
            phone = input("请输入学生的电话：")
            if not phone.isdigit():
                color.print_RED("电话输入有误，添加失败，请输入数字！！！")
                return
            password = input("请输入学生的密码：")
            if not password.isdigit():
                color.print_RED("密码输入有误，添加失败，请输入数字！！！")
                return
            # 对密码进行编码
            password = base64.b64encode(password.encode("utf-8"))
            flag = input("请问是否继续添加学生成绩(y/n)：")
            if "y" in flag or "Y" in flag:
                english = eval(input("请输入学生的英语成绩："))
                chinese = eval(input("请输入学生的语文成绩："))
                math = eval(input("请输入学生的数学成绩："))
                score = scores(english, chinese, math)
                student = students(id, name, age, phone, score, password)
            else:
                student = students(id, name, age, phone, None, password)
            if self.judgeIsExist(student):
                self.students.append(student)
                os.system("cls")
                color.print_GRREN(f"{name}的信息添加成功！！！")
            else:
                os.system("cls")
                color.print_RED(f"该学生已存在，添加失败！！！")
        except Exception as e:
            color.print_RED(f"输入有误，添加失败！！！")
            print(e)
            pass

    # 删除学生
    def remove_student(self):
        print("是否需要列出所有学生的学号加姓名(y/n)：")
        choice = input()
        if "y" in choice or "Y" in choice:
            color.print_GRREN("学号\t姓名")
            for student in self.students:
                color.print_BLUE(f"{student.get_id()}\t{student.get_name()}")
        print("请输入你要通过学生的姓名删除还是学号删除：(1.学号 2.姓名)")
        choice = input()
        if choice == "1":
            id = input("请输入学生的学号：")
            if not id.isdigit():
                os.system("cls")
                color.print_RED("学号输入有误，删除失败，请输入数字！！！")
                return
            student = self.get_student_id(id)
            if student:
                name = student.get_name()
                self.students.remove(student)
                os.system("cls")
                color.print_GRREN(f"{name}的信息删除成功！！！")
            else:
                os.system("cls")
                color.print_RED(f"该学生不存在，删除失败！！！")
        elif choice == "2":
            name = input("请输入学生的姓名：")
            if not name.isalpha():
                os.system("cls")
                color.print_RED("姓名输入有误，删除失败，请输入字符！！！")
                return
            student = self.get_student_name(name)
            if student:
                self.students.remove(student)
                os.system("cls")
                color.print_GRREN(f"{name}的信息删除成功！！！")
            else:
                os.system("cls")
                color.print_RED(f"该学生不存在，删除失败！！！")
        else:
            os.system("cls")
            color.print_RED("输入错误，请重新输入")

    # 通过id获取学生
    def get_student_id(self, id):
        for student in self.students:
            if student.get_id() == id:
                return student
        return None

    # 通过姓名获取学生
    def get_student_name(self, name):
        for student in self.students:
            if student.get_name() == name:
                return student
        return None

    # 查询学生
    def show_student(self):
        print("请输入你要通过学生的姓名查询还是学号查询：(1.学号 2.姓名)")
        choice = input()
        if choice == "1":
            id = input("请输入学生的学号：")
            if not id.isdigit():
                os.system("cls")
                color.print_RED("学号输入有误，查询失败，请输入数字！！！")
                return
            student = self.get_student_id(id)
            self.show_student2(student)
        elif choice == "2":
            name = input("请输入学生的姓名：")
            if not name.isalpha():
                os.system("cls")
                color.print_RED("姓名输入有误，查询失败，请输入字符！！！")
                return
            student = self.get_student_name(name)
            self.show_student2(self, student)
        else:
            os.system("cls")
            color.print_RED("输入错误，请重新输入")

    # 查询学生2
    def show_student2(self, student):
        if student:
            os.system("cls")
            color.print_GRREN("====================================")
            print(
                f"学号：{student.get_id()} 姓名：{student.get_name()} 年龄：{student.get_age()} 电话：{student.get_phone()}"
            )
            if student.get_scores() != None:
                print(
                    f"英语成绩：{student.get_scores().get_english()}分 语文成绩：{student.get_scores().get_chinese()}分 数学成绩：{student.get_scores().get_math()}分 平均分：{student.get_scores().get_aver()}分 总分：{student.get_scores().get_sum()}分"
                )

            else:
                print("该学生暂无成绩信息")
            color.print_GRREN("====================================")
        else:
            os.system("cls")
            color.print_RED(f"该学生不存在，查询失败！！！")

    # 展示所有学生
    def showAllStudents(self):
        os.system("cls")
        count = 1
        for student in self.students:
            color.print_GRREN("====================================")
            print(count)
            count += 1
            print(
                f"学号：{student.get_id()} 姓名：{student.get_name()} 年龄：{student.get_age()} 电话：{student.get_phone()}"
            )
            if student.get_scores() != None:
                print(
                    f"英语成绩：{student.get_scores().get_english()}分 语文成绩：{student.get_scores().get_chinese()}分 数学成绩：{student.get_scores().get_math()}分 平均分：{student.get_scores().get_aver()}分 总分：{student.get_scores().get_sum()}分"
                )

            else:
                print("该学生暂无成绩信息")
        color.print_GRREN("====================================")

    # 对学生进行排序
    def sort_student(self):
        print("请输入要根据什么进行排序：")
        print("1、学号")
        print("2、平均成绩")
        print("3、总成绩")
        print("4、单科成绩")
        choice = input()
        if choice == "1":
            self.students_tmp = sorted(self.students, key=lambda x: x.get_id())
            os.system("cls")
            for student in self.students_tmp:
                color.print_GRREN("====================================")
                print(
                    f"学号：{student.get_id()} 姓名：{student.get_name()} 年龄：{student.get_age()} 电话：{student.get_phone()}"
                )
                if student.get_scores() != None:
                    print(
                        f"英语成绩：{student.get_scores().get_english()}分 语文成绩：{student.get_scores().get_chinese()}分 数学成绩：{student.get_scores().get_math()}分 平均分：{student.get_scores().get_aver()}分 总分：{student.get_scores().get_sum()}分"
                    )

                else:
                    print("该学生暂无成绩信息")
            color.print_GRREN("====================================")
        elif choice == "2":
            # 如果存在学生没有成绩，则不进行排序
            self.students_tmp = sorted(
                self.students,
                key=lambda x: x.get_scores().get_aver()
                if x.get_scores()
                else float("-inf"),
                reverse=True,
            )
            os.system("cls")
            for student in self.students_tmp:
                color.print_GRREN("====================================")
                print(
                    f"学号：{student.get_id()} 姓名：{student.get_name()} 年龄：{student.get_age()} 电话：{student.get_phone()}"
                )
                if student.get_scores() != None:
                    print(
                        f"英语成绩：{student.get_scores().get_english()}分 语文成绩：{student.get_scores().get_chinese()}分 数学成绩：{student.get_scores().get_math()}分 平均分：{student.get_scores().get_aver()}分 总分：{student.get_scores().get_sum()}分"
                    )

                else:
                    print("该学生暂无成绩信息")
            color.print_GRREN("====================================")
        elif choice == "3":
            self.students_tmp = sorted(
                self.students,
                key=lambda x: x.get_scores().get_sum()
                if x.get_scores()
                else float("-inf"),
                reverse=True,
            )
            os.system("cls")
            for student in self.students_tmp:
                color.print_GRREN("====================================")
                print(
                    f"学号：{student.get_id()} 姓名：{student.get_name()} 年龄：{student.get_age()} 电话：{student.get_phone()}"
                )
                if student.get_scores() != None:
                    print(
                        f"英语成绩：{student.get_scores().get_english()}分 语文成绩：{student.get_scores().get_chinese()}分 数学成绩：{student.get_scores().get_math()}分 平均分：{student.get_scores().get_aver()}分 总分：{student.get_scores().get_sum()}分"
                    )

                else:
                    print("该学生暂无成绩信息")
            color.print_GRREN("====================================")
        elif choice == "4":
            print("请输入要根据什么进行排序：")
            print("1、英语成绩")
            print("2、语文成绩")
            print("3、数学成绩")
            choice = input()
            if choice == "1":
                self.students_tmp = sorted(
                    self.students,
                    key=lambda x: x.get_scores().get_english()
                    if x.get_scores()
                    else float("-inf"),
                    reverse=True,
                )
                os.system("cls")
                for student in self.students_tmp:
                    color.print_GRREN("====================================")
                    print(
                        f"学号：{student.get_id()} 姓名：{student.get_name()} 年龄：{student.get_age()} 电话：{student.get_phone()}"
                    )
                    if student.get_scores() != None:
                        print(
                            f"英语成绩：{student.get_scores().get_english()}分 语文成绩：{student.get_scores().get_chinese()}分 数学成绩：{student.get_scores().get_math()}分 平均分：{student.get_scores().get_aver()}分 总分：{student.get_scores().get_sum()}分"
                        )

                    else:
                        print("该学生暂无成绩信息")
                color.print_GRREN("====================================")
            elif choice == "2":
                self.students_tmp = sorted(
                    self.students,
                    key=lambda x: x.get_scores().get_chinese()
                    if x.get_scores()
                    else float("-inf"),
                    reverse=True,
                )
                os.system("cls")
                for student in self.students_tmp:
                    color.print_GRREN("====================================")
                    print(
                        f"学号：{student.get_id()} 姓名：{student.get_name()} 年龄：{student.get_age()} 电话：{student.get_phone()}"
                    )
                    if student.get_scores() != None:
                        print(
                            f"英语成绩：{student.get_scores().get_english()}分 语文成绩：{student.get_scores().get_chinese()}分 数学成绩：{student.get_scores().get_math()}分 平均分：{student.get_scores().get_aver()}分 总分：{student.get_scores().get_sum()}分"
                        )

                    else:
                        print("该学生暂无成绩信息")
                color.print_GRREN("====================================")
            elif choice == "3":
                self.students_tmp = sorted(
                    self.students,
                    key=lambda x: x.get_scores().get_math()
                    if x.get_scores()
                    else float("-inf"),
                    reverse=True,
                )
                os.system("cls")
                for student in self.students_tmp:
                    color.print_GRREN("====================================")
                    print(
                        f"学号：{student.get_id()} 姓名：{student.get_name()} 年龄：{student.get_age()} 电话：{student.get_phone()}"
                    )
                    if student.get_scores() != None:
                        print(
                            f"英语成绩：{student.get_scores().get_english()}分 语文成绩：{student.get_scores().get_chinese()}分 数学成绩：{student.get_scores().get_math()}分 平均分：{student.get_scores().get_aver()}分 总分：{student.get_scores().get_sum()}分"
                        )
                    else:
                        print("该学生暂无成绩信息")
            else:
                os.system("cls")
                color.print_RED("输入错误，请重新输入")

    # 修改函数
    def modify2(self, student):
        if student:
            print("请输入要修改的内容：")
            print("1、电话")
            print("2、密码")
            print("3、成绩")
            choice = input()
            if choice == "1":
                print("请输入新的电话：")
                phone = input()
                if not phone.isdigit():
                    os.system("cls")
                    color.print_RED("电话输入有误，修改失败，请输入数字！！！")
                    return
                student.phone = phone
                os.system("cls")
            elif choice == "2":
                password = input("请输入新的密码：")
                if not password.isdigit():
                    os.system("cls")
                    color.print_RED("密码输入有误，修改失败，请输入数字！！！")
                    return
                # 对密码进行编码
                password = base64.b64encode(password.encode("utf-8"))
                student.password = password
                os.system("cls")
            elif choice == "3":
                if not student.get_scores():
                    os.system("cls")
                    color.print_RED("该学生暂无成绩信息，修改失败！！！")
                    return
                print("请输入要修改的科目：")
                print("1、英语")
                print("2、语文")
                print("3、数学")
                print("4、全部")
                key = input()
                if key == "1":
                    try:
                        student.scores.english = eval(input("请输入新的英语成绩："))
                    except Exception as e:
                        color.print_RED("输入有误，修改失败！！！")
                        print(e)
                        pass
                elif key == "2":
                    try:
                        student.scores.chinese = eval(input("请输入新的语文成绩："))
                    except Exception as e:
                        color.print_RED("输入有误，修改失败！！！")
                        print(e)
                        pass
                elif key == "3":
                    try:
                        student.scores.math = eval(input("请输入新的数学成绩："))
                    except Exception as e:
                        color.print_RED("输入有误，修改失败！！！")
                        print(e)
                        pass
                elif key == "4":
                    try:
                        student.scores.english = eval(input("请输入新的英语成绩："))
                        student.scores.chinese = eval(input("请输入新的语文成绩："))
                        student.scores.math = eval(input("请输入新的数学成绩："))
                    except Exception as e:
                        color.print_RED("输入有误，修改失败！！！")
                        print(e)
                        pass
                else:
                    os.system("cls")
                    color.print_RED("输入错误，请重新输入")
        else:
            os.system("cls")
            color.print_RED(f"该学生不存在，修改失败！！！")

    # 修改学生数据
    def modify(self):
        print("请输入你要通过学生的姓名修改还是学号修改：(1.学号 2.姓名)")
        choice = input()
        if choice == "1":
            id = input("请输入学生的学号：")
            if not id.isdigit():
                os.system("cls")
                color.print_RED("学号输入有误，修改失败，请输入数字！！！")

                return

            student = self.get_student_id(id)
            if not student:
                os.system("cls")
                color.print_RED(f"该学生不存在，修改失败！！！")
                return
            self.modify2(student)
            os.system("cls")
            color.print_GRREN(f"{student.get_name()}的信息修改成功！！！")
        elif choice == "2":
            name = input("请输入学生的姓名：")
            if not name.isalpha():
                os.system("cls")
                color.print_RED("姓名输入有误，修改失败，请输入字符！！！")
                return
            student = self.get_student_name(name)
            if not student:
                os.system("cls")
                color.print_RED(f"该学生不存在，修改失败！！！")
                return
            self.modify2(student)
            os.system("cls")
            color.print_GRREN(f"{student.get_name()}的信息修改成功！！！")
        else:
            os.system("cls")
            color.print_RED("输入错误，请重新输入")

        pass

    # 给学生用的系统，用于登录查询、修改个人信息。


class systemForStudent:
    def __init__(self, systemAdmin):
        self.color = color()
        self.systemAdmin = systemAdmin
        self.student = self.login()
        if not self.student:
            return
        self.show_menu()

    def login(self):
        id = input("请输入学号：")
        if not id.isdigit():
            color.print_RED("出现错误，请输入数字")
            return
        student = self.systemAdmin.get_student_id(id)
        if not student:
            color.print_RED("未查询到学生相关信息")
            return
        password = input("请输入密码：")
        # 对密码进行编码
        password = base64.b64encode(password.encode("utf-8"))
        if student.get_password() != password:
            color.print_RED("密码错误")
            return
        color.print_GRREN("登录成功")
        return student

    def show_menu(self):
        while True:
            print("请输入选择您的选择：")
            print("1、查询个人信息")
            print("2、修改个人信息")
            print("3、保存并退出系统")
            choice = input("请输入您的选择")
            if choice == "1":
                self.systemAdmin.show_student2(self.student)
                pass
            elif choice == "2":
                self.systemAdmin.modify2(self.student)
                pass
            elif choice == "3":
                self.systemAdmin.save_data()
                color.print_GRREN("数据保存成功，系统退出！！！")
                os._exit(0)


if __name__ == "__main__":
    colorama.init()
    diver = color()
    # sysAdmin = systemForAdmin()
    # sysAdmin.show_menu()
    # 打印欢迎字符
    print(Fore.BLUE + "Welcome to the student manawigement system")
    print(
        Fore.BLUE
        + """
                                   \ ' /
                                   - (\  /
     (\      (\      (\      (\    / | ) -   (\      (\      (\      (\\
     | )     | )     | )     | )     `|      | )     | )     | )     | )
     `|      `|      `|      `|      |~|     `|      `|      `|      `|
     |~|     |~|     |~|     |~|     | |     |~|     |~|     |~|     |~|
     | |     | |     | |     | |     | |     | |     | |     | |     | |
     | |     | |     | |     | |     | |     | |     | |     | |     | |
     | |     | |     | |     | |     | |     | |     | |     | |     | |
     | |     | |     | |     | |    \~~~/    | |     | |     | |     | |
    \~~~/   \~~~/   \~~~/   \~~~/    (_)    \~~~/   \~~~/   \~~~/   \~~~/
     (_)     (_)     (_)     (_)_____(_)_____(_)     (_)     (_)     (_)
     (_)     (_)     (_)      \======(_)======/      (_)     (_)     (_)
     (_)     (_)     (_)_____________(_)_____________(_)     (_)     (_)
     (_)     (_)      \==============(_)==============/      (_)     (_)
     (_)     (_)_____________________(_)_____________________(_)     (_)
     (_)      \======================(_)======================/      (_)
     (_)_____________________________(_)_____________________________(_)
      \==============================(_)==============================/
                                   __(_)__
                                __(=======)__
                               (=============)Lev Lawrence

"""
    )
    Style.RESET_ALL
    if os.path.exists("systemAdmin.txt"):
        file_systemAdmin = open("systemAdmin.txt", "rb")
        sysAdmin = pickle.load(file_systemAdmin)
    else:
        sysAdmin = systemForAdmin()
    while True:
        choice = input("请输入您要进入教师系统(1)or学生系统(2)")
        if not choice.isalpha():
            print("您的输入存在问题请重新输入！")
            os.system("cls")
            pass
        if choice == "1":
            sysAdmin.show_menu()
            pass
        elif choice == "2":
            sysStudent = systemForStudent(sysAdmin)
            # sysStudent.show_menu()
            pass
    # if not os.path.exists("systemAdmin.txt"):
    #     sysAdmin = systemForAdmin()
    #     sysAdmin.show_menu()
    # file_systemAdmin = open("systemAdmin.txt", "rb")
    # sysAdmin = pickle.load(file_systemAdmin)
    # sysAdmin.show_menu()
    # colorama.deinit()
