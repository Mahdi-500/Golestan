import os
import time
import datetime as DT
import error
import information as info

student = {'0312764839': ('mahdi', 'wrehfg'), '03124569': ('ali', 'egr')}
professor = dict()
Class = {}
add_student = {}
add_professor = {}
id_list = list()
mark = {'0312764839':('031', '1111111111', '20'), '03124569': ('031', '1111111111', '19.5')}
mark_list = list()
average_student_mark = dict()

# all while true loops are for Real-Time checking so if the user enters a wrong input it wom't
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


    #################################################


    def register_student(self) -> None:

        # name

        while True:

            name, flag = info.name()

            if not flag:
                break
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # id number

        while True:

            id_number, flag = info.id(id_name= 'id number')

            if self.student != {}:
                if id_number in self.student.keys():
                    error.message("student with this id number is already registered \n")
                    return
            if not flag:
                break
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        while True:

            # entry year

            entry_year = ''
            flag, entry_year = error.try_except(entry_year, "enter the entry year: ")

            if flag:
                error.message("enter a valid value")

            if error.just_number(entry_year):
                error.message("only numbers are allowed")

            elif error.length(entry_year, 4):
                error.message("entry year must be 4 digits")

            elif int(entry_year) < 1300 or int(entry_year) > 1500:
                error.message("entry year must be a year between 1300 till 1500")
            
            else:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # field

        while True:

            field, flag = info.field()
        
            if not flag:
                break

        self.student[id_number] = name, entry_year, field, DT.datetime.now()
        print("welcome to Golestan")    # successful


    ################################################


    def register_professor(self) -> None:

        # name

        while True:

            name, flag = info.name()

            if not flag:
                break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # id number

        while True:

            id_number, flag = info.id(id_name= 'id number')

            if not flag:
                break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # field

        while True:

            field, flag = info.field()

            if not flag:
                break

        self.professor[id_number] = name, id_number, field
        print("welcome to Golestan")        # success


    ################################################


    def make_class(self) -> None:

        # name

        while True:

            name, flag = info.name()

            if not flag:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # class id

        while True:

            class_id, flag = info.id(id_name= 'class id')

            if not flag:
                break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # field

        while True:

            field, flag = info.field()

            if not flag:
                break

        self.Class[class_id] = name, field
        print("class added successfuly")    # success



    ################################################


    def add_student(self) -> None:  # add student to a class

        # id number

        while True:

            student_id, flag = info.id(id_name= 'student id')

            if self.student != {}:
                if student_id not in self.student.keys():
                    error.message("No student with this id number exist")  # error message

            elif not flag:
                break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # class id

        while True:
            
            class_id, flag = info.id(id_name= ' class id')

            if self.Class != {}:
                if class_id not in self.Class.keys():
                    error.message("no class found with the given class id")  # error message

            if self.Class[class_id][1] != self.student[student_id][2]:
                error.message("student field does not match")  # error message

            if self.add_st != {}:
                if class_id in self.add_st[student_id]:
                    error.message("studnet is already registered to this class")  # error message
                    return
                
            elif not flag:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
            
        """
        here it'll add student id to the dictionary if it doesn't exist in dict keys
        then it saves class ids in a list why?
        because if we wnat to add more class for this student in future we can easilly do it just by appending it
        """

        if student_id not in self.add_st.keys():
            self.add_st[student_id] = [class_id]
            error.message("student added successfully")  # success

        elif student_id in self.add_st.keys():
            self.add_st[student_id].append(class_id)
            error.message("student added successfully")  # success


    ################################################


    def add_professor(self) -> None:    # assign a professor to a class

        # id number

        while True:
            
            professor_id, flag = info.id(id_name= 'id number')        

            if professor_id not in self.professor.keys():
                error.message("no professor with given id number exist")  # error message

            elif not flag:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # class id

        while True:

            class_id, flag = info.id(id_name= 'class_id')


            if class_id not in self.Class.keys():
                error.message("no class found with given class id")  # error message

            if self.Class[class_id][1] != self.professor[professor_id][1]:
                error.message("professor field does not match")  # error message

            elif not flag:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
            
        """
        the idea here is that if this professor has no class
        it'll assign a class to the professor and saves the class id number in a list 
        beacause in future if you want to add more classes to this professor 
        you can easily do it by just appending it
        """

        if professor_id not in self.add_pr.keys():
            self.add_pr[professor_id] = [class_id]
        
        # here if this professor already have at least one class
        # it'll check if this professor have this class already or not
        # if it doesn't; it'll append the class id to list
        # otherwise, it will show an error message
            
        elif professor_id in self.add_pr.keys():
            for i in range(0, len(self.add_pr[professor_id])):
                if class_id != self.add_pr[professor_id][i]:
                    self.add_pr[professor_id].append(class_id)
                    error.message("prodessor added to class successfully")  # success

                else:
                    error.message("this class is already assigned to this professor")  # error 


    ################################################


    def student_status(self) -> None:   # shows student name, entering year, field and clsses

        # id number

        while True:

            id_number, flag = info.id(id_name= 'id number')

            if self.student != {}:
                if id_number not in self.student.keys():
                    error.message("no student found with given id number")

            else:   # shows an error message if dict is empty
                error.message("there are no students")  # error message
                return
            
            if not flag:
                break

        # show time

        os.system('cls')
        print('name: ', self.student[id_number][0])
        print('entering year: ', self.student[id_number][1])
        print('field: ', self.student[id_number][2])
        print('class:')
        for i in range(0, len(self.add_st[id_number])):
            class_id = self.add_st[id_number][i]    # save the class id number i
            print(self.Class[class_id][0])      # shows the class id number i name
        
        time.sleep(2)
        os.system('cls')


    ################################################


    def professor_status(self) -> None:  # shows professor name, field and classes

        # id number

        while True:

            professor_id, flag = info.id(id_name='id number')

            if self.professor != {}:
                if professor_id not in self.professor.keys():
                    error.message("no professor founded with given id number")
            
            else:   # shows an error message if dict is empty
                error.message("there are no professor")  # error message
                return
            
            if not flag:
                break

        # show time
            
        os.system('cls')
        print('name: ', self.professor[professor_id][0])
        print('field: ', self.professor[professor_id][1])
        print('class: ')
        for i in range(0, len(self.add_pr[professor_id])):
            class_id = self.add_pr[professor_id][i]   # save the class id, number i
            print(self.Class[class_id][0])  # shows the class id number i's name - success

        time.sleep(2)
        os.system('cls')


    ################################################


    def class_status(self) -> None:     # shows a class students

        # class id

        while True:

            class_id, flag= info.id(id_name= 'class id')

            if self.Class != {}:
                if class_id not in self.Class.keys():
                    error.message("no class founded with given class id")  # error message

            elif not flag:
                break

        # iterates on add_pr keys and checks if professor have this class or not

        for i in self.add_pr.keys():
            if class_id in self.add_pr[i]:
                print(f"teacher: {self.professor[i][0]}")  # success
                break
        
        # it iterates on add_st keys and checks if the student have this class or not

        print("students: ")
        for i in self.add_st.keys():
            if class_id in self.add_st[i]:
                print(self.student[i][0])  # success

        time.sleep(2)
        os.system('cls')


    ################################################


    def set_final_mark(self) -> None:  # assigning grade for students

        # professor id number

        while True:

            professor_id, flag = info.id(id_name= 'professor id')

            if professor_id not in self.professor.keys():
                error.message("no professor found with given id")  # error message

            elif not flag:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # student id number

        while True:

            student_id, flag = info.id(id_name= student_id)

            if student_id not in self.student.keys():
                error.message("no student found with given id")  # error message
            
            elif not flag:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # class id

        while True:

            class_id, flag = info.id(id_name= 'class id')

            if class_id not in self.Class.keys():
                error.message("no class found with given id")  # error message
        
            # does professor have this class?
            
            if class_id not in self.add_pr[professor_id]:
                error.message("this professor isn't registered on this class")  # error message
            
            # is the student registered on class?

            if student_id not in self.add_st[class_id]:
                error.message("this student isn't registered on this class")  # error message

            elif not flag:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # entering grade

        while True:

            grade = input('enter grade: ')

            if grade == '':
                grade = None

            elif error.just_number(grade):
                error.message("only numbers are allowed")  #error message

            elif int(grade) < 0 or int(grade) > 20:
                error.message("grade must be a number between 0 and 20")  # error message
            
            else:
                break
        
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
            
        """
        the idea in here is that if this student doesn't have any grade
        it'll assign grade with class id and professor id to that student using 2D array
        because in future if we wanted to add more grades to this student we can easily do it by appending the list
        """

        if student_id not in self.mark.keys():
            self.mark[student_id] = [[professor_id, class_id, grade]]

        
        # here if it has a student with given student id in dict keys 
        # it will check if that student have grade for that class
        # if it does have grade asks for confirmation to change the grade 
        # to do that it will remove the old array and apped a new one
        # if it does not have grade it will add a new array
        
        elif student_id in self.mark.keys():
            
            for i in range(0, len(self.mark[student_id])):
                if class_id != self.mark[student_id][i][1]:
                    self.mark[student_id].append([professor_id, class_id, grade])
                    error.message("student grade added successfully")  # success

                else:
                    while True:

                        flag, x = error.try_except(x, "this student already have a grade do you want to change it? (y/n)")
                        if flag:
                            error.message("enter a valid character")  # error message
                        
                        elif error.just_str(x) == True:
                            error.message("letters only")  # error message

                        else:
                            if x == 'y':
                                self.mark[student_id].remove(self.mark[student_id][i])
                                self.mark[student_id].append([professor_id, class_id, grade])
                                error.message("grade changed successfully")  # success

                            elif x == 'n':
                                break
    

    ################################################


    def mark_student(self) -> None:  # shows a student grade for a class
        
        # id number

        while True:

            student_id, flag = info.id(id_name= 'student id')
            
            if student_id not in self.student.keys():
                error.message("no student found with given id number")  # error messsage

            elif not flag:
                break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
          
        # class id

        while True:

            class_id, flag = info.id(id_name= 'class id')

            if class_id not in self.Class.keys():
                error.message("no class found with given class id")  # error message
                
            if class_id not in self.add_st[student_id]:
                error.message("student is not registered in this class")  # error message
            
            elif not flag:
                break
        
        # show time
            
        class_name = self.Class[class_id][0]
        student_name = self.student[student_id][0]
        for i in range(0,len(self.mark[student_id])):  # saving grade
            if self.mark[student_id][i][1] == class_id:
                grade = self.mark[student_id][i][2]
                break

        os.system('cls')
        print(f"class name: {class_name}")
        print(f"name: {student_name}")
        print(f"grade: {grade}")  # success
        

    ################################################


    def mark_list(self) -> None:  # shows a grade list for the class

        # class id

        while True:

            class_id, flag = info.id(id_name= 'class id')

            temp = Student()
            if class_id not in self.Class.keys():
                error.message("no lass found with given class id")  # error meesage

            elif not flag:
                break

        # checking if a professor have any class with this class id

        for i in self.add_pr.keys():
            if class_id not in self.add_pr[i][0]:
                error.message("this class has no professor")  # error message
                temp.mark_list()

        # checking if this class has any student

        for i in self.add_st.keys():
            if class_id not in self.add_st[i]:
                error.message("this class has no student")  # error message
                temp.mark_list()

        for i in self.mark.keys():
            if class_id in self.mark[i]:
                print(f"name: {self.student[i][0]}      {self.mark[i][2]}")  # success


    ################################################


    def average_mark_professor(self) -> None:  # shows the avrage assigned mark by one professor

        # professor id number

        while True:

            professor_id, flag = info.id(id_name= 'professor id')

            if professor_id not in self.professor.keys():
                error.message("no professor found with given id number")

            elif not flag:
                break
        
        sum = 0
        count = 0   # counts how many students are graded by this professor
        for i in self.mark.keys():
            if professor_id in self.mark[i]:
                if self.mark[i][2] != None:
                    sum += int(self.mark[i][2])
                    count += 1

        if sum != 0:
            os.system("cls")
            print(f"average grade: {round(sum/count, 2)}")
        else:
            print(None)

        
    ################################################


    def average_mark_student(self) -> None:  # shows the average mark of a student

        # id number

        while True:

            student_id, flag = info.id(id_name= 'id number')

            if self.student != {}:
                if student_id not in self.student.keys():
                    error.message("no student found with given id number")  #error message

                elif student_id not in self.mark.keys():
                    error.message("this student has no grade")  # error message

                elif not flag:
                    break

        # calculates average

        """
        here we iterate on self.mark with given student id number to find the grade
        and calculate sum.
        with every sum; count value will be increased by one unit
        it also saves the field and the entery year to for easier search in future
        """

        sum = count = 0
        for i in range(0, len(self.mark[student_id])):
            if self.mark[student_id][i][2] != None:
                sum += float(self.mark[student_id][i][2])
                count += 1

        if sum != 0:
            os.system('cls')
            print('average student mark is ' + str(round((sum / count), 2)) + '\n')  #success
            self.average_st_mark[student_id].append([str(round((sum / count), 2)), 
                                                     self.student[student_id][1], 
                                                     self.student[student_id][2]])

        else:
            error.message(None)  # success


    ################################################


    def top_student(self) -> None:  # shows the top student of a class
        
        # field

        while True:

            field, flag = info.field()

            if not flag:
                break
                
        while True:

            # entry year

            entry_year = ''
            flag, entry_year = error.try_except(entry_year, "enter the entry year: ")

            if flag:
                error.message("enter a valid value")

            if error.just_number(entry_year):
                error.message("only numbers are allowed")

            elif error.length(entry_year, 4):
                error.message("entry year must be 4 digits")

            elif int(entry_year) < 1300 or int(entry_year) > 1500:
                error.message("entry year must be a year between 1300 till 1500")
            
            else:
                break
        
        """
        in here due to the saving method we used in average mark student
        we can check both entry year and field with one loop and find maximum grade
        """

        max = 0
        id = ''
        for i in self.average_st_mark.keys():
            if self.average_st_mark[i][1] == entry_year and self.average_st_mark[i][2] == field:
                if float(self.average_st_mark[i][0]) > max:
                    max = float(self.average_st_mark[i][0])
                    id = i
                elif float(self.average_st_mark[i][0]) == max:
                    if self.student[i][3] < self.student[id][3]:
                        max = float(self.average_st_mark[i][0])


    ################################################   


    def top_mark(self) -> None:  # shows the highest mark of a class

        # class id

        while True:

            class_id, flag = info.id(id_name= 'class id')

            if not flag:
                break
        
        max = 0
        for i in self.mark.keys():  # iterated on keys
            for j in range(0, len(self.mark[i])):  # iterates on values of key i

                if self.mark[i][j][1] == class_id:
                    if self.mark[i][j][2] != None and self.mark[i][j][2] > max:
                        max = self.mark[i][j][2]

        if max == 0:
            error.message("this class students doesn't have any mark")  # success
        else:
            os.system("cls")
            print(f'maximum grade for this calss is {max}')
            time.sleep(3)
            return
        

################################################################################################
            
    
# main menu
            
while True:

    print('1 - register student \t\t 2 - register professor \n3 - make class \t\t         4 - add student')
    print('5 - add professor \t\t 6 - student status \n7 - professor status \t\t 8 - class status')
    print('9 - set final mark \t\t 10 - mark student \n11 - average professor mark \t 12 - average student mark')
    print('13 - top student \t\t 14 - top mark \n15 - mark list')
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
    elif x == 15:
        a = Student()
        a.mark_list()