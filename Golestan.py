import os
import time

n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '/', ';', ':', '"', '\\', '\'',
     '<', '>', '?', '*', '-', '_', '+', '=', '`', '~', '!', '@', '#', '$', '%', '^', '&', '(', ')', '[', ']', '{', '}']

student = dict()
professor = dict()
Class = dict()
add_student = dict()
add_professor = dict()
id_list = list()
mark = dict()
mark_list = list()
average_student_mark = dict()


class Student:
    def __init__(self) -> None:
        self.student = student
        self.Class = Class
        self.professor = professor
        self.add_st = add_student
        self.add_pr = add_professor
        self.id_list = id_list
        self.mark = mark
        self.average_st_mark = average_student_mark



    # register student



    def register_student(self) -> None:

        # name

        name = input('enter your full name: ').lower()

        if len(name) < 1 or len(name) > 20:
            os.system('cls')
            print('enter a valid name')
            return
        else:
            for i in range(0, len(name)):
                if name[i] in n:
                    print('enter a valid name')
                    return

        # id number

        id_number = input('enter your id number: ')

        if len(id_number) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(id_number)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if self.student != {}:
            if id_number in self.student.keys():
                os.system('cls')
                print('student with this id number is already registered \n')
                return

        # entering year

        entering_year = input('enter your entery year: ')

        try:
            int(entering_year)
        except ValueError:
            os.system('cls')
            print('eentering year have to be ONLY numbers \n')
            return

        if int(entering_year) < 1300 or int(entering_year) > 1500:
            os.system('cls')
            print('enter a year between 1300 till 1500 \n')
            return

        # field

        field = input('enter your field: ').lower()

        if len(field) < 1 or len(field) > 20:
            os.system('cls')
            print('field have to be ONLY contain letters \n')
            return
        else:
            for i in range(0, len(field)):
                if field[i] in n:
                    os.system('cls')
                    print('enter a valid field \n')
                    return

        self.student[id_number] = name, entering_year, field
        os.system('cls')
        print('** welcome to golestan :) **')
        time.sleep(2)
        os.system('cls')



    # register professor



    def register_professor(self) -> None:

        # name

        name = input('enter your full name: ').lower()

        if len(name) < 1 or len(name) > 20:
            os.system('cls')
            print('enter a valid name \n')
            return
        else:
            for i in range(0, len(name)):
                if name[i] in n:
                    os.system('cls')
                    print('enter a valid name \n')
                    return

        # id number

        id_number = input('enter your id number: ')

        if len(id_number) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(id_number)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if self.professor != {}:
            if id_number in professor.keys():
                os.system('cls')
                print('professor with this id number is already registered \n')
                return

        # field

        field = input('enter your field: ').lower()

        if len(field) < 1 or len(field) > 20:
            os.system('cls')
            print('enter a valid field \n')
            return
        else:
            for i in range(0, len(field)):
                if field[i] in n:
                    os.system('cls')
                    print('enter a valid field \n')
                    return

        self.professor[id_number] = name, 
        os.system('cls')
        print('** welcome to golestan :) **')
        time.sleep(2)
        os.system('cls')



    # make class



    def make_class(self) -> None:

        # name

        name = input('enter class name: ').lower()

        if len(name) < 1 or len(name) > 20:
            os.system('cls')
            print('enter a valid name \n')
            return
        else:
            for i in range(0, len(name)):
                if name[i] in n:
                    os.system('cls')
                    print('enter a valid name \n')
                    return

        # class id

        class_id = input('enter class id number: ')

        if len(class_id) != 10:
            os.system('cls')
            print('id number have to be contain ONLY numbers \n')
            return
        else:
            try:
                int(class_id)
            except ValueError:
                os.system('cls')
                print('enter valid id number \n')
                return

        if self.Class != {}:
            if class_id in self.Class.keys():
                os.system('cls')
                print('class with this id number is already in use \n')
                return

        # field

        field = input('enter class field: ').lower()

        if len(field) < 1 or len(field) > 20:
            os.system('cls')
            print('enter a valid field \n')
            return
        else:
            for i in range(0, len(field)):
                if field[i] in n:
                    os.system('cls')
                    print('enter a valid field \n')
                    return

        self.Class[class_id] = name, field
        os.system('cls')
        print('class added successfully')
        time.sleep(2)
        os.system('cls')



    # add student



    def add_student(self) -> None:

        # id number

        id_number = input('enter student id number: ')

        if len(id_number) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(id_number)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if self.student != {}:
            if id_number not in self.student.keys():
                os.system('cls')
                print('invalid student \n')
                return

        # class id

        class_id = input('enter class id number: ')

        if len(class_id) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(class_id)
            except ValueError:
                os.system('cls')
                print('enter valid id number \n')
                return

        if self.Class != {}:
            if class_id not in self.Class.keys():
                os.system('cls')
                print('invalid class \n')
                return

        if self.Class[class_id][1] != self.student[id_number][2]:
            os.system('cls')
            print('student field is not match \n')
            return

        if self.add_st != {}:
            if id_number == self.add_st[class_id][0]:
                os.system('cls')
                print('student is alredy registered \n')
                return

        
        self.id_list.append(id_number)
        self.add_st[class_id] = self.id_list
        os.system('cls')
        print('student added successfully')
        time.sleep(2)
        os.system('cls')



    # add professor



    def add_professor(self) -> None:

        # id number

        id_number = input('enter professor id number: ')

        if len(id_number) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(id_number)
            except ValueError:
                os.system('cls')
                print('enter valid id number \n')
                return

        if id_number not in self.professor.keys():
            os.system('cls')
            print('invalid professor \n')
            return
        
        # class id

        class_id = input('enter class id number: ')

        if len(class_id) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(class_id)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return


        if class_id not in self.Class.keys():
            os.system('cls')
            print('invalid class \n')
            return

        if self.Class[class_id][1] != self.professor[id_number][1]:
            os.system('cls')
            print('professor field is not match \n')
            return

        if self.add_pr != {}:
            try:
                self.add_pr[class_id][0]
            except KeyError:
                pass
            else:
                os.system('cls')
                print('this class has professor \n')
                return
            
        self.add_pr[class_id] = id_number
        os.system('cls')
        print('professor successfully added to the class')
        time.sleep(2)
        os.system('cls')



    # student status


    def student_status(self) -> None:

        # id number

        id_number = input('enter student id number: ')

        if len(id_number) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(id_number)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if self.student != {}:
            if id_number not in self.student.keys():
                os.system('cls')
                print('invalid student \n')
                return

        add_student_key_list = list(self.add_st.keys())
        add_student_value_list = list(self.add_st.values())

        flag = False
        class_id = []
        if id_number in add_student_value_list:
            flag = True
            for i in range(0, len(add_student_value_list)):
                if add_student_value_list[i] == id_number:
                    position = i
                    class_id.append(add_student_key_list[position])
        

        class_name = []
        for i in range(0, len(class_id)):
            if class_id[i] in self.Class.keys():
                class_name.append(self.Class[class_id[i]][0])

        os.system('cls')
        print('name: ', self.student[id_number][0])
        print('entering year: ', self.student[id_number][1])
        print('field: ', self.student[id_number][2])

        if flag:
            print('class: ')
            for i in range(0, len(class_name)):
                print(class_name[i])
        
        time.sleep(2)
        os.system('cls')



    # professor status



    def professor_status(self) -> None:

        # id number

        id_number = input('enter professor id number: ')

        if len(id_number) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(id_number)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if id_number not in self.professor.keys():
            os.system('cls')
            print('invalid professor \n')
            return
        
       
        add_professor_key_list = list(self.add_pr.keys())
        add_professor_value_list = list(self.add_pr.values())

        flag = False
        class_id = []
        if id_number in add_professor_value_list:
            flag = True
            for i in range(0, len(add_professor_value_list)):
                if add_professor_value_list[i] == id_number:
                    position = i
                    class_id.append(add_professor_key_list[position])
        

        class_name = []
        for i in range(0, len(class_id)):
            if class_id[i] in self.Class.keys():
                class_name.append(self.Class[class_id[i]][0])

        os.system('cls')
        print('name: ', self.professor[id_number][0])
        print('field: ', self.professor[id_number][1])

        if flag:
            print('class: ')
            for i in range(0, len(class_name)):
                print(class_name[i])

        time.sleep(2)
        os.system('cls')


    # class status



    def class_status(self) -> None:

        # class id

        class_id = input('enter class id number: ')

        if len(class_id) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(class_id)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if self.Class != {}:
            if class_id not in self.Class.keys():
                os.system('cls')
                print('invalid class \n')
                return

        try:
            self.add_pr[class_id]
        except KeyError:
            print(None)
        else:
            pr_id = self.add_pr[class_id]
            print('professor name:', self.professor[pr_id][0])

        st_id = self.add_st[class_id]
        os.system('cls')
        print('student name: ')
        for i in range(0, len(st_id)):
            print(self.student[st_id[i]][0])

        time.sleep(2)
        os.system('cls')



    # set final marks



    def set_final_mark(self) -> None:

        # professor id number

        professor_id = input('enter professor id number: ')

        if len (professor_id) != 10:
            os.system('cls')
            print('enter a valid id number \n')
            return
        try:
            int(professor_id)
        except ValueError:
            os.system('cls')
            print('id number have to be contain ONLY numbers \n')
            return

        if professor_id not in self.professor.keys():
            os.system('cls')
            print('invalid professor \n')
            return
        
        # student id number

        student_id = input('enter student id number: ')

        if len(student_id) != 10:
            os.system('cls')
            print('enter a valid id number \n')
            return
        
        try:
            int(student_id)
        except ValueError:
            os.system('cls')
            print('id number have to be contain ONLY numbers \n')
            return

        if student_id not in self.student.keys():
            os.system('cls')
            print('invalid student \n')
            return
        
        # class id

        class_id = input('enter class id: ')

        try:
            int(class_id)
        except ValueError:
            os.system('cls')
            print('id number have to be contain ONLY numbers \n')
            return

        if class_id not in self.Class.keys():
            os.system('cls')
            print('invalid class \n')
            return
        
        # if len(class_id) != 10:
        #     os.system('cls')
        #     print('enter a valid class number \n')
        #     return
        
        # does professor have this class?
        
        if self.add_pr[class_id] != professor_id:
            os.system('cls')
            print('professor class is not match \n')
            return
        
        # is the student registered in class?

        if student_id not in self.add_st[class_id]:
            os.system('cls')
            print('student did not registered \n')
            return
        
        # entering grade

        grade = input('enter grade: ')

        if grade == '':
            grade = 'None'

        else:
            try:
                float(grade)
            except ValueError:
                os.system('cls')
                print('grade have to be contain ONLY numbers \n')
                return

            if float(grade) < 0 or float(grade) > 20:
                os.system('cls')
                print('gade have to be a number between 0 and 20 \n')
                return

        
        mark_list.append([professor_id, class_id, grade])
        self.mark[student_id] = mark_list
        os.system('cls')
        print('student final mark added or changed \n')
        time.sleep(2)
        os.system('cls')



    # mark student



    def mark_student(self) -> None:
        
        # id number

        id_number = input('enter student id number: ')

        if len(id_number) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(id_number)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if self.student != {}:
            if id_number not in self.student.keys():
                os.system('cls')
                print('invalid student \n')
                return
            
        # class id

        class_id = input('enter class id number: ')

        if len(class_id) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(class_id)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if self.Class != {}:
            if class_id not in self.Class.keys():
                os.system('cls')
                print('invalid class \n')
                return
            
        if id_number not in self.add_st[class_id]:
            os.system('cls')
            print('student not registered \n')
            return
        
        name_class = self.Class[class_id][0]
        student_name = self.student[id_number][0]

        os.system('cls')
        print('class name: ' + name_class)
        print('name: ' + student_name)
        print('grade: ' + self.mark[id_number][2] + '\n')
        


    # mark list



    def mark_list(self) -> None:

        # class id

        class_id = input('enter class id: ')

        if len(class_id) != 10:
            os.system('cls')
            print('enter a valid class id \n')
            return

        try:
            int(class_id)
        except ValueError:
            os.system('cls')
            print('id number have to be contain ONLY numbers \n')
            return

        if class_id not in self.Class.keys():
            os.system('cls')
            print('invalid class \n')
            return

        try:
            self.add_pr[class_id][0]
        except KeyError:
            os.system('cls')
            print('no professor \n')
            return
        
        try:
            self.add_st[class_id][0]
        except KeyError:
            os.system('cls')
            print('no student')
            return

        os.system('cls')
        id_list = self.add_st[class_id]
        for i in range(0, len(id_list)):
            student_name = self.student[id_list[i]][0]
            student_grade = self.mark[id_list[i]][2]
            print('name: ' + student_name, '\tgrade: ' + student_grade)




    # average mark professor



    def average_mark_professor(self) -> None:

        # professor id number

        professor_id = input('enter professor id number: ')

        if len (professor_id) != 10:
            os.system('cls')
            print('enter a valid id number \n')
            return
        try:
            int(professor_id)
        except ValueError:
            os.system('cls')
            print('id number have to be contain ONLY numbers \n')
            return

        if professor_id not in self.professor.keys():
            os.system('cls')
            print('invalid professor \n')
            return
        
        # finding professor classes

        key_list = list(self.add_pr.keys())

        class_list = []
        for i in range(0, len(key_list)):
            if professor_id == self.add_pr[key_list[i]]:
                class_list.append(key_list[i])

        # finding student id number for each class code & calculates average

        sum = 0
        count = 0
        for i in range(0, len(class_list)):
            student_list = self.add_st[class_list[i]]
            for j in range(0, len(student_list)):
                if self.mark[student_list[j]] != 'None':
                    sum += float(self.mark[student_list[j]][2])
                    count += 1

        if sum == 0:
            os.system('cls')
            print(None + '\n')
            return
        
        os.system('cls')
        print('average grade for this professor is ' + str(round((sum / count), 2))+ '\n')
        


    # average student mark



    def average_mark_student(self) -> None:

        # id number

        id_number = input('enter student id number: ')

        if len(id_number) != 10:
            os.system('cls')
            print('enter valid id number \n')
            return
        else:
            try:
                int(id_number)
            except ValueError:
                os.system('cls')
                print('id number have to be contain ONLY numbers \n')
                return

        if self.student != {}:
            if id_number not in self.student.keys():
                os.system('cls')
                print('invalid student \n')
                return

        # calculates average

        key_list = list(self.mark.keys())
        sum = 0
        count = 0
        for i in range(0, len(list(self.mark.keys()))):
            for j in range(0, len(self.mark[key_list[i]])):
                if self.mark[key_list[i]][j][2] != 'None':
                    sum += float(self.mark[key_list[i]][j][2])
                    count += 1

        if sum == 0:
            os.system('cls')
            print(None + '\n')
            return
        
        os.system('cls')
        print('average student mark is ' + str(round((sum / count), 2)) + '\n')
        self.average_st_mark[id_number] = str(round((sum / count), 2))



    # top student



    def top_student(self) -> None:
        
        # field

        field = input('enter your field: ').lower()

        if len(field) < 1 or len(field) > 20:
            os.system('cls')
            print('enter a valid field \n')
            return
        else:
            for i in range(0, len(field)):
                if field[i] in n:
                    os.system('cls')
                    print('field have to be ONLY contain letters \n')
                    return
                
        # entering year

        entering_year = input('enter your entery year: ')

        try:
            int(entering_year)
        except ValueError:
            os.system('cls')
            print('eentering year have to be ONLY numbers \n')
            return

        if int(entering_year) < 1300 or int(entering_year) > 1500:
            os.system('cls')
            print('enter a year between 1300 till 1500 \n')
            return
        
        key_list = list(self.student.keys())
        
        for i in range (0, len(key_list)):
            if self.student[key_list[i]][1] == entering_year and self.student[key_list[i]][2] == field:
                id_list.append(key_list[i])
                break
            else:
                os.system('cls')
                print(None + '\n')
                return

        max = float(self.average_st_mark[key_list[0]])

        for i in range(1, len(key_list)):
            if float(self.average_st_mark[key_list[i]]) > max:
                max = self.average_st_mark[key_list[i]]
                id_number = key_list[i]
        
        os.system('cls')
        print(self.student[id_number][0] + '\n')



    # top mark    



    def top_mark(self) -> None:

        # class id

        class_id = input('enter class id: ')

        if len(class_id) != 10:
            os.system('cls')
            print('enter a valid class id \n')
            return

        try:
            int(class_id)
        except ValueError:
            os.system('cls')
            print('id number have to be contain ONLY numbers \n')
            return

        if class_id not in self.Class.keys():
            os.system('cls')
            print('invalid class \n')
            return
        
        
        if list(self.mark.values())[0][0][2] != 'None':
            id_list = self.add_st[class_id]
            max = 0
            for i in range(0, len(id_list)):
                value_list = self.mark[id_list[i]]
                for j in range(0, len(value_list)):
                    if self.mark[id_list[i]][j][1] == class_id:
                        if float(self.mark[id_list[i]][j][2]) > max and self.mark[id_list[i]][j][2] != 'None':
                            max = float(self.mark[id_list[i]][j][2])
            os.system('cls')
            print('maximum garde is ' + str(max) + '\n')
            
        else:
            flag = False
            value_list = list(self.mark.values())
            for i in range(0, len(value_list)):
                for j in range(0, len(list(self.mark.values())[i])):
                    if list(self.mark.values())[i][j][2] == 'None':
                        flag = True
                    else:
                        flag = False
            if flag:
                print(None + '\n')
                return
while True:

    print('1 - register student \t\t 2 - register professor \n3 - make class \t\t         4 - add student')
    print('5 - add professor \t\t 6 - student status \n7 - professor status \t\t 8 - class status')
    print('9 - set final mark \t\t 10 - mark student \n11 - average professor mark \t 12 - average student mark')
    print('13 - top student \t\t 14 - top mark')
    x = int(input(''))
    os.system('cls')

    if x == 1:
        a = Student()
        a.register_student()
    elif x == 2:
        a = Student()
        a.register_professor()
    elif x == 3:
        a = Student()
        a.make_class()
    elif x == 4:
        a = Student()
        a.add_student()
    elif x == 5:
        a = Student()
        a.add_professor()
    elif x == 6:
        a = Student()
        a.student_status()
    elif x == 7:
        a = Student()
        a.professor_status()
    elif x == 8:
        a = Student()
        a.class_status()
    elif x == 9:
        a = Student()
        a.set_final_mark()
    elif x == 10:
        a = Student()
        a.mark_student()
    elif x == 11:
        a = Student()
        a.average_mark_professor()
    elif x == 12:
        a = Student()
        a.average_mark_student()
    elif x == 13:
        a = Student()
        a.top_student()
    elif x == 14:
        a= Student()
        a.top_mark()

