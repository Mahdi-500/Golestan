import os
import time
import datetime as DT
import pandas as pd
import error
import information as info

student = dict()
professor = dict()
Class = dict()
add_student = dict()
add_professor = dict()
mark = dict()
average_student_mark = dict()

# ? all while true loops are for Real-Time checking so if the user enters a wrong input it wom't
class Student:
    
    def __init__(self) -> None:
        self.student = student
        self.Class = Class
        self.professor = professor
        self.add_st = add_student
        self.add_pr = add_professor
        self.mark = mark
        self.average_st_mark = average_student_mark


    #################################################


    def register_student(self) -> None:

        # ? name

        while True:

            f_name, flag1 = info.first_name()
            l_name, flag2 = info.last_name()

            if not flag1 and not flag2:
                break

    
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? id number

        while True:

            id_number, flag = info.id(id_name= 'id number')

            if self.student != {}:
                if id_number in self.student.keys():
                    error.message("student with this id number is already registered \n")
                    return
            if not flag:
                break

        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? entry year

        while True:


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
        
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? field

        while True:

            field, flag = info.field()
        
            if not flag:
                break

        self.student = {'first name': [f_name], 'last name': [l_name], 'id number': [id_number], 
                        'entry year': [entry_year], 'field': [field], 'date and time': [DT.datetime.now()]}
        data_student = pd.DataFrame(self.student)
        
        if os.path.isfile(r'your saving location\Golestan\Student.csv'):  # to avoid overwriting we check if the file exist or not
            data_student.to_csv(r'your saving location\Golestan\Student.csv', sep=',', mode='a', index=False, header=False)  # adding new datas to existing csv file

        else:
            data_student.to_csv(r'your saving location\Golestan\Student.csv', sep=',', mode='w', index=False, header=True)  # creating a new csv file for datas

        print("\nwelcome to Golestan\n")    # + successful


    ################################################



    def register_professor(self) -> None:

        # ? name

        while True:

            f_name, flag1 = info.first_name()
            l_name, flag2 = info.last_name()

            if not flag1 and not flag2:
                break

        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? id number

        while True:

            id_number, flag = info.id(id_name= 'id number')

            if not flag:
                break

        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? field

        while True:

            field, flag = info.field()

            if not flag:
                break

        self.professor ={'first name': [f_name], ' last name': [l_name], 'id number':[id_number],'field of study':[field]}
        data_professor = pd.DataFrame(self.professor)
        
        if os.path.isfile(r'your saving location\Golestan\Professor.csv'):  # to avoid overwriting we check if the file exist or not
            data_professor.to_csv(r'your saving location\Golestan\Professor.csv', sep=',', mode='a', index=False, header=False)  # adding new datas to existing csv file

        else:
            data_professor.to_csv(r'your saving location\Golestan\Professor.csv', sep=',', mode='w', index=False, header=True)  # creating a new csv file for datas
        
        print("\nwelcome to Golestan\n")        # + successful


    ################################################


    def make_class(self) -> None:

        # ? name

        while True:

            name, flag = info.first_name()

            if not flag:
                break
        
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? class id

        while True:

            class_id, flag = info.id(id_name= 'class id')

            if not flag:
                break

        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? field

        while True:

            field, flag = info.field()

            if not flag:
                break

        self.Class = {'name': [name], 'class id': [class_id], 'class field': [field]}
        data_class = pd.DataFrame(self.Class)
        
        if os.path.isfile(r'your saving location\Golestan\Class.csv'):  # to avoid overwriting we check if the file exist or not
            data_class.to_csv(r'your saving location\Golestan\Class.csv', sep=',', mode='a', index=False, header=False)  # adding new datas to existing csv file

        else:
            data_class.to_csv(r'your saving location\Golestan\Class.csv', sep=',', mode='w', index=False, header=True)  # creating a new csv file for datas
        
        print("\nclass added successfully\n")    # + successful



    ################################################


    def add_student(self) -> None:  # todo - add student to a class

        # ? id number

        while True:

            student_id, flag = info.id(id_name= 'student id')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Student.csv')  # checking if file is empty or does not exist or not
            
            if not flag:
                if not flag1:  # file is not empty and exist
                    data_student = pd.read_csv(r"your saving location\Golestan\Student.csv")
                    data_student['id number'] = data_student['id number'].astype(str).str.zfill(10)  # add leading zero in id number
                    
                    if student_id not in data_student['id number'].values:
                        error.message("No student found with given id number")  # ! error message

                    else:
                        break

                else:
                    error.message("student csv file is empty or does not exist")  # ! error message
                    return
            

        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                
        
        # ? class id

        while True:
            
            class_id, flag = info.id(id_name= 'class id')
            flag1 = error.try_except_pd(r"your saving location\Golestan\Class.csv")  # checking if file is empty or does not exist or not

            if not flag:
                if not flag1:  # file is not empty and exist
                    
                    flag2 = False
                    data_class = pd.read_csv(r"your saving location\Golestan\Class.csv")
                    data_class['class id'] = data_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if class_id not in data_class["class id"].values:
                        error.message("no class found with the given class id")  # ! error message
                        flag2 = True

                    else:
                        
                        # ? checking the field

                        index_class = data_class.index[data_class['class id'] == class_id][0]
                        index_student = data_student.index[data_student['id number'] == student_id][0]

                        if data_class.iloc[index_class, 2] != data_student.iloc[index_student, 4]:
                            error.message("student field does not match")  # ! error message
                            flag2 = True
                else:
                    error.message("class csv file is empty or does not exist")  # ! error message
                    return

            if not flag2:
                break

        self.add_st = {'student id': [student_id], 'class id': [class_id]}
        dataframe_class_student = pd.DataFrame(self.add_st)

        if os.path.isfile(r"your saving location\Golestan\Class-Student.csv"):  # to avoid overwriting we check if the file exist or not

            data_class_student = pd.read_csv(r"your saving location\Golestan\Class-Student.csv")

            data_class_student['student id'] = data_class_student['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
            data_class_student['class id'] = data_class_student['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

            index_student = data_class_student.index[data_class_student['student id'] == student_id]

            for i in index_student:
                if data_class_student['class id'][i] == class_id:
                    error.message("student is already registered to this class")  # ! error message
                    return
                
            dataframe_class_student.to_csv(r'your saving location\Golestan\Class-Student.csv', sep=',', mode='a', index=False, header=False)  # adding new datas to existing csv file 
            error.message("student added successfully")  # + successful
                
        else:
            dataframe_class_student.to_csv(r'your saving location\Golestan\Class-Student.csv', sep=',', mode='w', index=False, header=True)  # creating a new csv file for datas
            error.message("student added successfully")  # + successful


    ################################################


    def add_professor(self) -> None:    # todo - assign a professor to a class

        # ? id number

        while True:
            
            professor_id, flag = info.id(id_name= 'professor id')        
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Professor.csv')  # checking if file is empty or does not exist or not

            if not flag:
                if not flag1:  # file is not empty and exist

                    data_professor = pd.read_csv(r"your saving location\Golestan\Professor.csv")
                    data_professor["id number"] = data_professor['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if professor_id not in data_professor['id number'].values:
                        error.message("no professor found with given id number")  # ! error message

                    else:
                        break
                
                else:
                    error.message("the professor csv file is empty or does not exist")  # ! error message
                    return
            
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? class id

        while True:

            class_id, flag = info.id(id_name= 'class id')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Class.csv')  # check if the file is empty or does not exist or not

            if not flag:
                if not flag1:  # file is not empty and exist

                    data_class = pd.read_csv(r'your saving location\Golestan\Class.csv')
                    data_class['class id'] = data_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if class_id not in data_class['class id'].values:
                        error.message("no class found with given class id")  # ! error message

                    class_index = data_class.index[data_class['class id'] == class_id][0]
                    professor_index = data_professor.index[data_professor['id number'] == professor_id][0]

                    if data_class.iloc[class_index, 2] != data_professor.iloc[professor_index, 3]:
                        error.message("professor field does not match")  # ! error message

                    elif not flag:
                        break
                
                else:
                    error.message("class csv file is empty or does not exist")
                    return
                
        
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        
        self.add_pr = {'professor id': [professor_id], 'class id': [class_id]}
        dataframe_professor_class = pd.DataFrame(self.add_pr)

        if os.path.isfile(r'your saving location\Golestan\Class-professor.csv'):  # to avoid overwriting we check if the file exist or not

            data_professor_class = pd.read_csv(r"your saving location\Golestan\Class-professor.csv")
            
            data_professor_class['professor id'] = data_professor_class['professor id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
            data_professor_class['class id'] = data_professor_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

            index_professor = data_professor_class.index[data_professor_class['professor id'] == professor_id]

            for i in index_professor:
                if data_professor_class['class id'][i] == class_id:
                    error.message("this class is already assigned to this professor")  # ! error message 
                    return

            dataframe_professor_class.to_csv(r"your saving location\Golestan\Class-professor.csv", sep=',', mode='a', index= False, header= False)  # add new data to csv file
            error.message("professor added successfully")  # + successful
            
        else:
            dataframe_professor_class.to_csv(r"your saving location\Golestan\Class-professor.csv", sep=',', mode='w', header= True, index= False)  # creates a new csv file and adds the data
            error.message("professor added successfully")  # + successful


    ################################################


    def student_status(self) -> None:   # todo - shows student name, entering year, field and clsses

        # ? id number

        while True:

            id_number, flag = info.id(id_name= 'id number')

            if os.path.isfile(r'your saving location\Golestan\Student.csv'):
                flag1 = error.try_except_pd(path=r"your saving location\Golestan\Student.csv")

            else:
                error.message("student.csv file does not exist")  # ! error message
                return

            if not flag:
                if not flag1:  # file is not empty and exist

                    data_student = pd.read_csv(r"your saving location\Golestan\Student.csv")
                    data_student['id number'] = data_student['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if id_number not in data_student['id number'].values:
                        error.message("no student found with given id number")  # ! error message
                    
                    else:
                        break
                
                else:
                    error.message("student.csv file is empty or does not exist")  # ! error message

        # ? show time

        """
        the problem was when it shows the data it also shows the data type and the name (again) when it just uses data_student.iloc ...
        to solve that; first the data is converted to string and after that we can use string ability to filter those things  
        """

        os.system('cls')
        student_index = data_student.index[data_student['id number'] == id_number]
        name = str(data_student.iloc[student_index, 0])
        l_name = str(data_student.iloc[student_index, 1])
        year = str(data_student.iloc[student_index, 3])
        field = str(data_student.iloc[student_index, 4])

        print("first name:", name[5:name.find("N")])
        print("last name:", l_name[5:l_name.find("N")])
        print("entery year:", year[5:year.find("N")])
        print("field: ", field[5:field.find("N")])

        # ? showing the classes

        if not os.path.isfile(r"your saving location\Golestan\Class-Student.csv"):  # to avoid overwriting we check if the file exist or not
            error.message("there is no file for students classes") # ! error message
        else:
            flag = error.try_except_pd(path=r"your saving location\Golestan\Class-Student.csv")
            if not flag:  # file is not empty and exist

                data_class_student = pd.read_csv(r"your saving location\Golestan\Class-Student.csv")
                data_class_student['student id'] = data_class_student['student id'].astype(str).str.zfill(10) # adds the leading zero to those id's which length is less than 10
                data_class_student['class id'] = data_class_student['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                if id_number not in data_class_student['student id'].values:
                    error.message("this student has no class")  # + successful
                    return

                # ? first of all we save the index of that student id; therefor we can use that to find the class id
                # ? after saving the first class id; it immedietly goes for finding that class id name

                else:
                    index_id = data_class_student.index[data_class_student['student id'] == id_number]
                
                    print("class: ")
                    for i in range(0, len(index_id)):
                        class_id = data_class_student.iloc[i, 1]

                        data_class = pd.read_csv(r"your saving location\Golestan\Class.csv")
                        data_class['class id'] = data_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                        index_class = data_class.index[data_class['class id'] == class_id]
                        classes = str(data_class.iloc[index_class, 0])
                        print(classes[5:classes.find("N")])  # + successful

            else:
                error.message("class - student csv file is empty or does not exist")  # ! error message


    ################################################


    def professor_status(self) -> None:  # todo - shows professor name, field and classes

        # id number

        while True:

            professor_id, flag = info.id(id_name='professor id')

            if os.path.isfile(r'your saving location\Golestan\Professor.csv'):  # to avoid overwriting we check if the file exist or not
                flag1 = error.try_except_pd(path=r"your saving location\Golestan\Professor.csv")
            
            else:
                error.message("professor.csv file does not exist")  # ! error message
                return

            if not flag:
                if not flag1:  #file is not empty and exist
                    data_professor = pd.read_csv(r"your saving location\Golestan\Professor.csv")
                    data_professor['id number'] = data_professor['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if professor_id not in data_professor['id number'].values:
                        error.message("no professor founded with given id number")  # ! error message
                    
                    else:
                        break
            
                else:
                    error.message("professor.csv file is empty or does not exist")  # ! error message
                    return

        # ? show time
            
        os.system('cls')
        professor_index = data_professor.index[data_professor['id number'] == professor_id]
        f_name = str(data_professor.iloc[professor_index, 0])
        l_name = str(data_professor.iloc[professor_index, 1])
        field = str(data_professor.iloc[professor_index, 3])

        print('first name:', f_name[5:f_name.find("N")])
        print("last name:", l_name[5:l_name.find("N")])
        print('field:', field[5:field.find("N")])
        
        # ? showing the classes

        if os.path.isfile(r'your saving location\Golestan\Class-professor.csv'):
            flag = error.try_except_pd(path=r'your saving location\Golestan\Class-professor.csv')

            
            if not flag:  # file is not empty and exist

                data_class_professor = pd.read_csv(r'your saving location\Golestan\Class-professor.csv')
                data_class_professor['professor id'] = data_class_professor['professor id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                data_class_professor['class id'] = data_class_professor['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                # ? first of all we save the index of that student id; therefor we can use that to find the class id
                # ? after saving the first class id; it immedietly goes for finding that class id name
                
                if professor_id not in data_class_professor['professor id'].values:
                    error.message("this professor has no class")  # + successful
                    return
                
                else:
                    index_id = data_class_professor.index[data_class_professor['professor id'] == professor_id]

                    print("class:")
                    for i in range(0, len(index_id)):
                        class_id = data_class_professor.iloc[i, 1]
                        
                        data_class = pd.read_csv(r'your saving location\Golestan\Class.csv')
                        data_class['class id'] = data_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                        index_class = data_class.index[data_class['class id'] == class_id]
                        classes = str(data_class.iloc[index_class, 0])
                        print(classes[5:classes.find("N")])  # + successful
            
            else:
                error.message("class - professor csv file is empty or does not exist")  # ! error message


    ################################################


    def class_status(self) -> None:     # todo - shows a class students

        # ? class id

        while True:

            class_id, flag = info.id(id_name= 'class id')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Class.csv')

            if not flag:
                if not flag1:  # file is not empty and exist
                    data_class = pd.read_csv(r'your saving location\Golestan\Class.csv')
                    data_class['class id'] = data_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if class_id not in data_class['class id'].values:
                        error.message("no class found with given class id")  # ! error message
                    else:
                        break
                
                else:
                    error.message("class.csv file is empty or does not exist") # ! error message

        # ? showing the professor name
                    
        if os.path.isfile(r"your saving location\Golestan\Professor.csv"):  # professor file must exist
            if os.path.isfile(r"your saving location\Golestan\Class-professor.csv"):  # class professor file must exist

                flag = error.try_except_pd(path=r"your saving location\Golestan\Class-professor.csv")
                flag1 = error.try_except_pd(path=r"your saving location\Golestan\Professor.csv")
            
                if not flag and not flag1:  # files are not empty and exist

                    data_class_professor = pd.read_csv(r'your saving location\Golestan\Class-professor.csv')
                    data_professor = pd.read_csv(r'your saving location\Golestan\Professor.csv')

                    data_professor['id number'] = data_professor['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_class_professor['professor id'] = data_class_professor['professor id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_class_professor['class id'] = data_class_professor['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    index_class = data_class_professor.index[data_class_professor['class id'] == class_id][0]
                    professor_id = data_class_professor.iloc[index_class, 0]
                    index_professor = data_professor.index[data_professor['id number'] == str(professor_id)]
                    professor_f_name = str(data_professor.iloc[index_professor, 0])
                    professor_l_name = str(data_professor.iloc[index_professor, 1])

                    print(f"\nteacher: \n{professor_f_name[5:professor_f_name.find("N")] + professor_l_name[5:professor_l_name.find("N")]}")  # + successful


                elif flag1:
                    error.message("professor.csv file is empty or does not exist")  # ! error message
                    return

                elif flag:
                    error.message("class - professor csv file is empty or does not exist")  # ! error message
                    return
            
            else:
                error.message("class - professor csv file does not exist")  # ! error message
                return
            
        else:
            error.message("professor.csv file does not exist")  # ! error message
            return
        
        # ? showing the students

        if os.path.isfile(r'your saving location\Golestan\Student.csv'):  # student file must exist
            if os.path.isfile(r'your saving location\Golestan\Class-Student.csv'):  # class - student file must exist

                flag = error.try_except_pd(r'your saving location\Golestan\Class-Student.csv')
                flag1 = error.try_except_pd(r'your saving location\Golestan\Student.csv')

                if not flag and not flag1:  # files are not empty and exist

                    data_class_student = pd.read_csv(r'your saving location\Golestan\Class-Student.csv')
                    data_student = pd.read_csv(r'your saving location\Golestan\Student.csv')

                    data_class_student['student id'] = data_class_student['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_class_student['class id'] = data_class_student['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_student['id number'] = data_student['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    class_student_index = data_class_student.index[data_class_student['class id'] == class_id]
                    print("students:")
                    for i in class_student_index:
                        student_id = data_class_student.iloc[int(i), 0]

                        student_index = data_student.index[data_student['id number'] == student_id]
                        student_f_name = str(data_student.iloc[student_index, 0])
                        student_l_name = str(data_student.iloc[student_index, 1])

                        print(student_f_name[5:student_f_name.find("N")] + student_l_name[5:student_l_name.find("N")])  # + successful

                elif flag:
                    error.message("class - student csv file is empty or does not exist")  # ! error message
                    return
                
                elif flag1:
                    error.message("student.csv file is empty or does not exist") # ! error message
                    return
            
            else:
                error.message("class - stundent csv file does not exist")  # ! error message
                return
        
        else:
            error.message("stundent.csv file does not exist") # ! error message
            return


    ################################################


    def set_final_mark(self) -> None:  # todo - assigning grade for students

        # ? professor id number

        while True:

            professor_id, flag = info.id(id_name= 'professor id')
            flag1 = error.try_except_pd(path= r'your saving location\Golestan\Professor.csv')
            
            if not flag:
                if not flag1:  # file is not empty and exist
                    data_professor = pd.read_csv(r'your saving location\Golestan\Professor.csv')
                    data_professor['id number'] = data_professor['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if professor_id not in data_professor['id number'].values:
                        error.message("no professor found with given id")  # ! error message

                    else:
                        break  # + successful
                else:
                    error.message("the professor.csv file is empty or does not exist")  # ! error messgae
        
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? student id number

        while True:

            student_id, flag = info.id(id_name= 'student id')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Student.csv')

            if not flag:
                if not flag1:  # file is not empty and exist
                    data_student = pd.read_csv(r'your saving location\Golestan\Student.csv')
                    data_student['id number'] = data_student['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if student_id not in data_student['id number'].values:
                        error.message("no student found with given id")  # ! error message

                    else:
                        break  # + successful

                else:
                    error.message("the student.csv file is empty or does not exist")  # ! error message
        
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? class id

        while True:

            class_id, flag = info.id(id_name= 'class id')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Class.csv')
            flag2 = error.try_except_pd(path=r'your saving location\Golestan\Class-professor.csv')
            flag3 = error.try_except_pd(path=r'your saving location\Golestan\Class-Student.csv')

            if not flag:
                if not flag1 and not flag2 and not flag3:  # class, class - professor, class - student files are not empty and exist

                    data_class = pd.read_csv(r'your saving location\Golestan\Class.csv')
                    data_class['class id'] = data_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    data_class_student = pd.read_csv(r'your saving location\Golestan\Class-Student.csv')
                    data_class_student['class id'] = data_class_student['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    data_class_professor = pd.read_csv(r'your saving location\Golestan\Class-professor.csv')
                    data_class_professor['class id'] = data_class_professor['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    

                    if class_id not in data_class['class id'].values:
                        error.message("no class found wih given class id")  # ! error message

                    elif class_id not in data_class_professor['class id'].values:
                        error.message("this class has no professor")  # ! error message

                    elif class_id not in data_class_student['class id'].values:
                        error.message("this class has no student")  # ! error message
                    
                    else:
                        break  # + successful
                
                elif flag1:
                    error.message("class.csv file is empty or does not exist")  # ! error message

                elif flag2:
                    error.message("class - professor.csv file is empty or does not exist")  # ! error message

                elif flag3:
                    error.message("class - student.csv file is empty or does not exist")  # ! error message
        
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


        # ? checking if the professor and the student have this class


        # professor

        data_class_professor['professor id'] = data_class_professor['professor id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
        professor_index = data_class_professor.index[data_class_professor['professor id'] == professor_id][0]

        if data_class_professor.iloc[professor_index, 1] != class_id:
            error.message("this class is not assigned to this professor")  # ! error message
            return
        
        # student

        data_class_student['student id'] = data_class_student['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
        student_index = data_class_student.index[data_class_student['student id'] == student_id]
        
        for i in student_index:
            if data_class_student.iloc[i, 1] != class_id:
                error.message("this student is not assigned to this class")  # ! error message
                return

        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? entering grade

        while True:

            grade = input('enter grade: ')

            if grade == '':
                grade = None

            elif error.just_number(grade) and '.' not in grade:
                error.message("only numbers are allowed")  # ! error message

            elif float(grade) < 0 or float(grade) > 20:
                error.message("grade must be a number between 0 and 20")  # ! error message
            
            else:
                break
        
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        self.mark = {'student id': [student_id], 'grade': [grade], 'professor id': [professor_id], 'class id':[class_id]}
        data_mark = pd.DataFrame(self.mark)

        if os.path.isfile(r'your saving location\Golestan\Grade.csv'):

            data_grade = pd.read_csv(r"your saving location\Golestan\Grade.csv")
            data_grade['student id'] = data_grade['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
            data_grade['class id'] = data_grade['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

            if student_id not in data_grade['student id'].values:
                data_mark.to_csv(r"your saving location\Golestan\Grade.csv", sep=',', mode='a', index=False, header=False)  # adding new data to exisitng csv file
                error.message("student garde added successfully")  # + successful

            elif class_id not in data_grade['class id'].values:
                data_mark.to_csv(r'your saving location\Golestan\Grade.csv', sep=',', mode='a', index=False, header=False)  # adding neew data to existing csv file
                error.message("student grade added successfully")  # + successful

            else:
                while True:
                    x = input("this student already have a grade do you want to change it? (y/n)")
                    x = x.lower()
                    flag = error.just_str(x)

                    if not flag:
                        if x == 'y':
                            
                            # because a student can have more than one class we have to find the index of the class by using the list of stundent id indexes

                            data_student_index = data_grade.index[data_student['student id'] == student_id]

                            for i in data_student_index:  
                                if data_grade['class id'][i] == class_id:
                                    index_id = i
                                    break
                            data_grade.iat[index_id, 1] = grade  # + successful
                            error.message("student grade successfully changed")  # + successful

                        elif x == 'n':
                            return  # + successful
                        
                    else:
                        error.message("only letters y and n are allowed")
                        
                

        else:
            data_mark.to_csv(r'your saving location\Golestan\Grade.csv', sep=',', mode='w', index=False, header=True)  # creating new csv file for datas
            error.message("grade added successfully")  # + success


    ################################################


    def mark_student(self) -> None:  # todo - shows a student grade for a class
        
        # ? id number

        while True:

            student_id, flag = info.id(id_name= 'student id')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Student.csv')

            if not flag:  
                if not flag1:  # file is not empty and exist
                    data_student = pd.read_csv(r"your saving location\Golestan\Student.csv")
                    data_student['id number'] = data_student['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if student_id not in data_student['id number'].values:
                        error.message("no student found with given id number")  # ! error message

                    else:
                        break  # + successful
                else:
                    error.message("student.csv file is empty or does not exist")  # ! error message

        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        
        # ? class id

        while True:

            class_id, flag = info.id(id_name= 'class id')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Class.csv')
            flag2 = error.try_except_pd(path=r'your saving location\Golestan\Class-Student.csv')
            flag3 = False

            if not flag:
                if not flag1 and not flag2:  # files are not empty and exist

                    data_class = pd.read_csv(r"your saving location\Golestan\Class.csv")
                    data_class_student = pd.read_csv(r"your saving location\Golestan\Class-Student.csv")

                    data_class_student['student id'] = data_class_student['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_class_student['class id'] = data_class_student['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_class['class id'] = data_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    student_index = data_class_student.index[data_class_student['student id'] == student_id]

                    for i in student_index:
                        if data_class_student.iloc[i, 1] != class_id:
                            error.message("this student is not registered to this class")  # ! error message
                            flag3 = True
                            break
                    
                    if class_id not in data_class['class id'].values:
                        error.message("no class found with given class id")  # ! error message
                    
                    elif not flag3:
                        break  # + successful
                
                elif flag1:
                    error.message("class.csv file is empty or does not exist")  # ! error message

                elif flag2:
                    error.message("class - student csv file is empty or does not exist")  # ! error message

        
        # ? show time
            
        # class name

        class_index = data_class.index[data_class['class id'] == class_id][0]
        class_name = data_class.iloc[class_index, 0]

        # student name
        
        student_index = data_student.index[data_student['id number'] == student_id][0]
        student_f_name = data_student.iloc[student_index, 0]
        student_l_name = data_student.iloc[student_index, 1]

        # grade

        flag = error.try_except_pd(path=r'your saving location\Golestan\Grade.csv')

        if not flag:  # file is not empty and exist

            data_grade = pd.read_csv(r'your saving location\Golestan\Grade.csv')
            data_grade['student id'] = data_grade['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
            data_grade['class id'] = data_grade['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

            student_index = data_grade.index[data_grade['student id'] == student_id]

            for i in student_index: 
                if data_grade.iloc[i, 3] == class_id:
                    grade = data_grade.iloc[i, 1]
                    break  # + successful
        else:
            error.message("Grade.csv file does not exist")  # ! error message

        os.system('cls')
        print(f"class name: {class_name}")
        print(f"name: {student_f_name} {student_l_name}")
        print(f"grade: {grade}\n\n")  # + successful
        

    ################################################


    def mark_list(self) -> None:  # todo - shows a grade list for the class

        # ? class id

        while True:

            class_id, flag = info.id(id_name= 'class id')
            flag1 = error.try_except_pd(r'your saving location\Golestan\Grade.csv')

            if not flag:
                if not flag1:  # file is not empty and exist

                    data_grade = pd.read_csv(r'your saving location\Golestan\Grade.csv')
                    data_student = pd.read_csv(r'your saving location\Golestan\Student.csv')
                    data_grade['student id'] = data_grade['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_grade['class id'] = data_grade['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_student['id number'] = data_student['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if class_id not in data_grade['class id'].values:
                        error.message("no class found with given class id")  # ! error message meesage

                    else:
                        break  # + successful
                else:
                    error.message("grade.csv file is empty or does not exist")  # ! error message

        # ? show time

        index_class = data_grade.index[data_grade['class id'] == class_id]

        for i in index_class:
            if data_grade['class id'][i] == class_id:
                index_student = data_student.index[data_student['id number'] == data_grade.iloc[i, 0]][0]
                print(f"name: {data_student.iloc[index_student, 0]}  {data_student.iloc[index_student, 1]}      {data_grade.iloc[i, 1]}\n\n")  # + successful


    ################################################


    def average_mark_professor(self) -> None:  # todo - shows the avrage assigned mark by one professor

        # ? professor id number

        while True:

            professor_id, flag = info.id(id_name= 'professor id')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Professor.csv')
            flag2 = error.try_except_pd(path=r"your saving location\Golestan\Grade.csv")

            if not flag:
                if not flag1 and not flag2:  # files are not empty and exist

                    data_professor = pd.read_csv(r'your saving location\Golestan\Professor.csv')  
                    data_grade = pd.read_csv(r"your saving location\Golestan\Grade.csv")

                    data_professor['id number'] = data_professor['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_grade['professor id'] = data_grade['professor id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if professor_id not in data_professor['id number'].values:
                        error.message("no professor found with given id number")  # ! error message

                    else:
                        break  # + successful
                elif flag1:
                    error.message('professor.csv file is empty or does not exist')  # ! error message

                elif flag2:
                    error.message("grade.csv file is empty or does not exist")  # ! error message
        
        sum = 0
        count = 0   # counts how many students are graded by this professor
        professor_index = data_grade.index[data_grade['professor id'] == professor_id]

        for i in professor_index:
            sum += float(data_grade.iloc[i, 1])
            count += 1

        if sum != 0:
            os.system("cls")
            print(f"average grade: {round(sum/count, 2)}")  # + successful
            error.message("")
        else:
            print(None)

        
    ################################################


    def average_mark_student(self) -> None:  # todo - shows the average mark of a student

        # ? id number

        while True:

            student_id, flag = info.id(id_name= 'id number')
            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Student.csv')
            flag2 = error.try_except_pd(path=r"your saving location\Golestan\Grade.csv")

            if not flag:
                if not flag1 and not flag2:  # files are not empty and exist
                    
                    data_student = pd.read_csv(r"your saving location\Golestan\Student.csv")
                    data_grade = pd.read_csv(r'your saving location\Golestan\Grade.csv')

                    data_student['id number'] = data_student['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_grade['student id'] = data_grade['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if student_id not in data_student['id number'].values:
                        error.message('no student found with given id number')  # ! error message
                    else:
                        break  # + successful
                
                elif flag1:
                    error.message("student.csv file is empty or does not exist")  # ! error message

                elif flag2:
                    error.message("grade.csv file is empty or does not exist")  # ! error message

        # calculates average

        sum = 0
        count = 0
        student_index = data_grade.index[data_grade['student id'] == student_id]
        for i in student_index:
            sum += float(data_grade.iloc[i, 1])
            count += 1

        if sum != 0:
            os.system('cls')
            print('average student mark is ' + str(round((sum / count), 2)) + '\n')  # + successful
            error.message("")

        else:
            error.message(None)  # + successful
        
        # saving these information for next function

        student_index = data_student.index[data_student['id number'] == student_id][0]

        self.average_st_mark = {'student id': [data_student.iloc[student_index, 2]],
                                'entry year': [data_student.iloc[student_index, 3]], 
                                'field': [data_student.iloc[student_index, 4]],
                                'grade':[str(round((sum / count), 2))]}
        data_average = pd.DataFrame(self.average_st_mark)

        if os.path.isfile(r'your saving location\Golestan\Average-mark.csv'):  # to avoid overwriting we check if the file exist or not
            data_average.to_csv(r'your saving location\Golestan\Average-mark.csv', sep=',', mode='a', index=False, header=False)  # adding new datas to existing csv file

        else:
            data_average.to_csv(r'your saving location\Golestan\Average-mark.csv', sep=',', mode='w', index=False, header=True)  # creating a new csv file for datas



    ################################################


    def top_student(self) -> None:  # todo - shows the top student of a specific field and entry year
        
        # ? field

        while True:

            field, flag = info.field()

            if not flag:
                break
        
        # $ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        # ? entry year

        while True:


            entry_year = ''
            flag, entry_year = error.try_except(entry_year, "enter the entry year: ")

            if not flag:
                error.message("enter a valid value")

            if error.just_number(entry_year):
                error.message("only numbers are allowed")

            elif error.length(entry_year, 4):
                error.message("entry year must be 4 digits")

            elif int(entry_year) < 1300 or int(entry_year) > 1500:
                error.message("entry year must be a year between 1300 till 1500")
            
            else:
                break

        flag = error.try_except_pd(path=r'your saving location\Golestan\Average-mark.csv')
        flag1 = error.try_except_pd(path=r'your saving location\Golestan\Student.csv')

        if not flag and not flag1:  # files are not empty and exist and exist

            data_av_grade = pd.read_csv(r'your saving location\Golestan\Average-mark.csv')
            data_student = pd.read_csv(r"your saving location\Golestan\Student.csv")
            
            data_av_grade['student id'] = data_av_grade['student id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
            data_student['id number'] = data_student['id number'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
            
            grade_index = data_av_grade.index[data_av_grade['entry year'] == entry_year]

            # ? finding maximum
            max = 0
            id = ''
            for i in grade_index:
                if data_av_grade.iloc[i, 2] == field:
                    if float(data_av_grade[i, 3]) > max:
                        max = float(data_av_grade[i, 3])
                        id = data_av_grade[i, 0]

            student_index = data_student.index[data_student['id number'] == id][0]
            print(f'name: {data_student[student_index, 0]} {data_student[student_index, 1]} \ngrade: {max}\n')  # + successful
        
        elif flag:
            error.message("average - mark.csv file is empty or doesn't exist")  # ! error message

        elif flag1:
            error.message("student.csv file is empt or doesn't exist")  # ! error message


    ################################################   


    def top_mark(self) -> None:  # todo - shows the highest mark of a class

        # ? class id

        while True:

            class_id, flag = info.id(id_name= 'class id')

            flag1 = error.try_except_pd(path=r'your saving location\Golestan\Class.csv')
            flag2 = error.try_except_pd(path=r'your saving location\Golestan\Grade.csv')
            

            if not flag:
                if not flag1 and not flag2:  # files are not empty and exist

                    data_class = pd.read_csv(r'your saving location\Golestan\Class.csv')
                    data_grade = pd.read_csv(r"your saving location\Golestan\Grade.csv")

                    data_class['class id'] = data_class['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10
                    data_grade['class id'] = data_grade['class id'].astype(str).str.zfill(10)  # adds the leading zero to those id's which length is less than 10

                    if class_id not in data_class['class id'].values:
                        error.message("no class found with given id number")  # ! error message

                    if class_id not in data_grade['class id'].values:
                        error.message(None)  # + successful
                        return
                    
                    else:
                        break

                elif flag1:
                    error.message("class.csv file is empty or doesn't exist")  # ! error message

                elif flag2:
                    error.message("grade.csv file is empty or doesn't exist")  # ! error message
        
        class_index = data_grade.index[data_grade['class id'] == class_id]
        max = 0
        for i in class_index:
            if float(data_grade.iloc[i, 1]) > max:
                max = float(data_grade.iloc[i, 1])

        os.system("cls")
        print(f'maximum grade for this class is {max}')  # + successful
        time.sleep(3)
        return
        

################################################################################################
            
    
# ? main menu
            
while True:

    while True:
        print('1 - register student \t\t 2 - register professor \n\n3 - make class \t\t         4 - add student')
        print('\n5 - add professor \t\t 6 - student status \n\n7 - professor status \t\t 8 - class status')
        print('\n9 - set final mark \t\t 10 - mark student \n\n11 - average professor mark \t 12 - average student mark')
        print('\n13 - top student \t\t 14 - top mark \n\n15 - mark list')
        x = int(input(''))
        flag = error.just_number(x)

        if flag:
            error.message("only number")  # ! error message
        else:
            break
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
    else:
        error.message("select correct number")  # ! error message