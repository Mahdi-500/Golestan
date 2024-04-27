import error

flag_info = False
def name() -> str:

    while True:

        # name

        name = ''
        flag, name = error.try_except(name, "enter name: ")
        name = name.lower()
    
        if flag:
            error.message("enter a valid character")
            flag_info = True

        if len(name) < 1 or len(name) > 20:     
            error.message("not enough or more than enough characters")
            flag_info = True
      
        elif error.just_str(name):
            error.message("only letters is allowed")
            flag_info = True
            
        else:
            # break
            return name, flag_info

def id(id_name) -> str:

    while True:

        # id number

        var_name = ''
        flag, var_name = error.try_except(var_name, f"enter {id_name} number: ")

        if flag:
            error.message("enter a valid integer")
            flag_info = True

        if error.just_number(var_name):
            error.message("only numbers are allowed")
            flag_info = True

        elif error.length(var_name, 10) == True:
            error.message(f"not enough digits for {id_name}")
            flag_info = True
        
        else:
            return var_name, flag_info
        
def field() -> str:
        
    while True:

        # field

        field = ''
        flag, field = error.try_except(field, "enter field: ")
        field = field.lower()

        if flag:
            error.message("enter a valid value")
            flag_info = True

        if error.just_str(field):
            error.message("only letters are allowed")
            flag_info = True
        
        elif len(field) < 1 or len(field) > 20:
            error.message("field must have minimum 1 chracter and maximum 20 characters")
            flag_info = True

        else:
            return field, flag_info