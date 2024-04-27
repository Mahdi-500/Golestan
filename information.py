import error


def first_name() -> str:

    while True:

        # ? first name

        flag_info = False
        f_name = ''  # first name
        flag, f_name = error.try_except(f_name, "enter first name: ")
        f_name = f_name.lower()
    
        if flag:
            error.message("enter a valid character")
            flag_info = True

        if len(f_name) < 1 or len(f_name) > 20:     
            error.message("not enough or more than enough characters")
            flag_info = True

        elif error.just_str(f_name):
            error.message("only letters is allowed")
            flag_info = True
            
        else:
            # break
            return f_name, flag_info
        
def last_name() -> str:

    while True:

        # ? last name

        flag_info = False
        l_name = ''  # last name
        flag, l_name = error.try_except(l_name, "enter last name: ")
        l_name = l_name.lower()
    
        if flag:
            error.message("enter a valid character")
            flag_info = True

        if len(l_name) < 1 or len(l_name) > 20:     
            error.message("not enough or more than enough characters")
            flag_info = True

        elif error.just_str(l_name):
            error.message("only letters is allowed")
            flag_info = True
            
        else:
            # break
            return l_name, flag_info

def id(id_name) -> str:

    while True:

        # ? id number

        flag_info = False
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

        # ? field

        flag_info = False
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