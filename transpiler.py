########################################################################
#                                                                      #
#                   Welcome to (not) transpiler                        #
#                                                                      #
########################################################################
import sys
####################################
#                                  #
# Check for python file            #
#                                  #
####################################


def is_python(filename):
    ending = ('.py')
    if filename.endswith(ending):
        return True
    return False
####################################
#                                  #
# Check for c file                 #
#                                  #
####################################


def is_c(filename):
    ending = ('.c')
    if filename.endswith(ending):
        return True
    return False

####################################
#                                  #
# store white space for each line  #
#                                  #
####################################


def store_whitespace(line):
    whitespace = 0
    for i in line:
        if i == ' ':
            whitespace += 1
        else:
            return whitespace
####################################
#                                  #
# store white space for do   line  #
#                                  #
####################################

def store_whitespace_do(line):
    whitespace = 0
    for i in line:
        if i == ' ':
            whitespace += 1
        else:
            return whitespace
####################################
#                                  #
# remove perentensis and semicolon #
#                                  #
####################################


def check_bracket(line):
    no_whitespace = line.strip()
    if len(no_whitespace) == 1:
        if no_whitespace == '}' or no_whitespace == '{':
            return "\n"
    if len(no_whitespace) > 1:
        if no_whitespace[0] == '}' or no_whitespace[0] == '{':
            return no_whitespace[1:] + "\n"
        elif no_whitespace[-1] == '}' or no_whitespace[-1] == '{' or no_whitespace[-1] == ';':
            return no_whitespace[:-1] + "\n"
    return False

####################################
#                                  #
# check end brakcer                #
#                                  #
####################################
def check_end_bracket(line):
    no_whitespace =line.strip()
    if len(no_whitespace) == 1:
        if no_whitespace == '}':
            return True
####################################
#                                  #
# convert --,++ to -=1 +=1         #
#                                  #
####################################


def check_indecrement(line):
    no_whitespace = line.strip()
    new = ""
    newer = ""
    for i in range(len(no_whitespace)):
        if i > 0 and no_whitespace[i] == "+" and no_whitespace[i - 1] == "+":
            new += "=1"
        elif i > 0 and no_whitespace[i] == "-" and no_whitespace[i - 1] == "-":
            new += "=1"
        else:
            new += no_whitespace[i]
    for i in range(len(new)):
        if i > 0 and new[i-1] == "1" and new[i-2] == "=" and new[i-3] == "-" and (new[i-4]== " " or new[i-4]==";" or new[i-4]=="("):
            newer = newer.replace("-=1","") + new[i] +"-=1"
        elif i > 0 and new[i-1] == "1" and new[i-2] == "=" and new[i-3] == "+" and (new[i-4]== " " or new[i-4]==";"):
            newer = newer.replace("+=1","") + new[i] +"+=1"
        else:
            newer += new[i]
    return newer + "\n"
####################################
#                                  #
# Check for main function          #
#                                  #
####################################

def check_main(line):

    first_chars = line[0:5]

    if first_chars == "main(":
        return True
    return False
#####################################################################
##                                                                 ##
##                                  Preposesor                     ##
##                                                                 ##
#####################################################################

####################################
#                                  #
# convert for define               #
#                                  #
####################################


def check_define(line):
    first_chars = line[0:7]
    if first_chars == "#define":
        line = line.replace("#define ", "").split()
        return line[0] + " = " + line[1] + "\n"

####################################
#                                  #
# convert for include              #
#                                  #
####################################


def check_include(line):
    first_chars = line[0:9]
    if first_chars == "#include ":
        line = line.replace("#include ", "")
        if line == "<stdio.h>":
            return "import sys\n\n"
        elif line[0] == '"':
            line = line.strip('"\n') + "\n"
            return "import " + line
        else:
            return False
    return False





    #####################
    ## CHECK VARIABLES ##
    #####################

####################################
#                                  #
# Check for integer                #
#                                  #
####################################


def check_int(line):
    first_chars = line[0:4]
    if first_chars == "int ":
        return line[4:]
    return False
####################################
#                                  #
# Check for integer                #
#                                  #
####################################


def check_float(line):
    first_chars = line[0:6]
    if first_chars == "float ":
        return line[6:]
    return False
####################################
#                                  #
# Check for char                   #
#                                  #
####################################


def check_char(line):
    first_chars = line[0:5]
    if first_chars == "char ":
        a = line[5:]

        return a

    return False

####################################
#                                  #
# array     char                   #
#                                  #
####################################


def array_char(line):
    braket = 0
    first_chars = line[0:5]
    out = ""
    if first_chars == "char ":
        a = line[5:]

    for char in a:
        if braket == 0:
            if char != '[':

                out += char
            elif char == '[':
                braket += 1
                out += " = ["
        else:
            if char == ']':
                out += char
    return out +"\n"


####################################
#                                  #
# Check for string                 #
#                                  #
####################################


def check_string(line):
    first_chars = line[0:6]
    if first_chars == "char* ":
        a = line[6:]

        return a

    return False

####################################
#                                  #
# Check for unassign value         #
#                                  #
####################################


def check_notvalue(line):
    assign = True
    for i in line:
        if i == "=":
            assign = False
    return assign

####################################
#                                  #
# check array                      #
#                                  #
####################################


def check_array(line):
    if line[-2] == ']':

        return True
####################################
#                                  #
# Variable                         #
#                                  #
####################################
def check_variables(line):

    if check_char(line):
        line_temp = check_char(line)
        check_array(line)

        if check_main(line_temp):
            line = line.lstrip("char")
            line = line.rstrip("\n")
            line = "def" + line + ":" + "\n"
            return line
        if check_notvalue(line_temp):
            if check_array(line):
                line = array_char(line)
                return line
            else:
                line = check_char(line).rstrip(";\n") + " = 0\n"
                return line

        line = check_char(line).rstrip(";\n") + "\n"
        return line

    if check_string(line):
        line_temp = check_string(line)
        if check_main(line_temp):
            line = line.lstrip("char*")
            line = line.rstrip("\n")
            line = "def" + line + ":" + "\n"
            return line
        if check_notvalue(line_temp):
            line = check_string(line).rstrip(";\n") + " = 0\n"
            return line

        line = check_string(line).rstrip(";\n") + "\n"
        return line

    elif check_int(line):
        line_temp = check_int(line)
        if check_main(line_temp):
            line = line.lstrip("int")
            line = line.rstrip("\n")
            line = "def" + " main()" + ":" + "\n"
            return line
        if check_notvalue(line_temp):
            line = check_int(line).rstrip(";\n") + " = 0\n"
            return line
        line = check_int(line).rstrip(";\n") + "\n"
        return line

    elif check_float(line):
        line_temp = check_float(line)
        if check_main(line_temp):
            line = line.lstrip("float")
            line = line.rstrip("\n")
            line = "def" + line + ":" + "\n"
            return line
        if check_notvalue(line_temp):
            line = check_float(line).rstrip(";\n") + " = 0\n"
            return line
        line = check_float(line).rstrip(";\n") + "\n"
        return line
    return False


####################################
#                                  #
# Check for print function         #
#                                  #
####################################

####################################
#                                  #
# Check for newline                #
#                                  #
####################################


def check_notnewline(line):
    for i in range(len(line)):
        if line[i] == "n" and line[i - 1] == "\\":
            return False
    return True

####################################
#                                  #
# Check for print function         #
#                                  #
####################################


def check_print(line):
    no_whitespace = line.strip()
    if no_whitespace[:7] == "printf(":
        no_whitespace = "print(" + no_whitespace.lstrip("printf(")
        new = ""
        format_string = False
        comma = True
        newline = False
        for i in range(len(no_whitespace)):
            if no_whitespace[i - 1] == "%":
                pass
            elif no_whitespace[i] == '%':
                if no_whitespace[i + 1] == 'd':
                    format_string = True
                    new += "{}"
                elif no_whitespace[i + 1] == 'f':
                    format_string = True
                    new += "{}"
                elif no_whitespace[i + 1] == 'c':
                    format_string = True
                    new += "{}"
                elif no_whitespace[i + 1] == 's':
                    format_string = True
                    new += "{}"
                elif no_whitespace[i + 1] == '%':
                    new += "%"

            elif no_whitespace[i] == '"' and no_whitespace[i + 1] == ',' and format_string:
                comma = False
                new += '".format('
            elif no_whitespace[i] == ',':
                if comma == False:
                    comma = True
                else:
                    new += no_whitespace[i]
            elif no_whitespace[i] == '\\' and no_whitespace[i - 1] != '\\':
                pass

            elif no_whitespace[i] == 'n' and no_whitespace[i - 1] == '\\' and newline == False:
                newline = True

            else:
                new += no_whitespace[i]
        if check_notnewline(line):
            new += ',end=""'
        if format_string == True:
            new += ")"

        new += "\n"
        return new
    return False

####################################
#                                  #
#           if/else                #
#                                  #
####################################


def check_if(line):
    no_whitespace = line.strip()
    if no_whitespace[:8] == "else if ":
        no_whitespace = "elif " + no_whitespace.lstrip("else if (")
        no_whitespace = no_whitespace.rstrip(")\n")
        no_whitespace = no_whitespace + ":\n"
        return no_whitespace
    elif no_whitespace[:3] == "if ":
        no_whitespace = "if " + no_whitespace.lstrip("if (") + "\n"
        no_whitespace = no_whitespace.rstrip(")\n")
        no_whitespace = no_whitespace + ":\n"
        return no_whitespace
    elif no_whitespace[:4] == "else":
        no_whitespace = no_whitespace.rstrip("\n")
        no_whitespace = no_whitespace + ":\n"
        return no_whitespace
    return False
####################################
#                                  #
#              for infinite        #
#                                  #
####################################

def check_for_infinite(line):
    no_whitespace = line.strip()
    if no_whitespace[:8] == "for (;;)":
        return "while True:\n"

####################################
#                                  #
#              for                 #
#                                  #
####################################


def check_for(line):
    no_whitespace = line.strip()
    if no_whitespace[:3] == "for":
        string = no_whitespace.split(";")
        new_string = ""
        if len(string) == 3:
            variable = ""
            value = ""
            string[0] = string[0].lstrip("for (")
            count_equal = 0
            for i in range(len(string)):
                string[i] = string[i].strip()

            for i in range(len(string[0])):
                if string[0][i] == '=':
                    count_equal += 1
                elif string[0][i] != "=" and count_equal == 0:
                    variable += string[0][i]
                elif string[0][i] != "=" and count_equal > 0:
                    value += string[0][i]
                else:
                    break
            variable = variable.lstrip("int")
            variable = variable.strip()
            new_string += "for " + variable + " in range( " + value + ", "
            value2 = ""
            count_lessthan = 0
            for i in range(len(string[1])):
                if string[1][i] == "<" or string[1][i] == ">":
                    count_lessthan += 1
                elif (string[1][i] != "<" or string[1][i] == ">") and count_lessthan > 0:
                    value2 += string[1][i]
            value2 = value2.strip()
            new_string += value2 + ", "
            value3 = ""

            check_notincrement_decrement = True
            for i in range(len(string[2])):

                if string[2][i] == "+" and string[2][i + 1] == "+":
                    value3 += "1"
                    check_notincrement_decrement = False
                    break

                elif string[2][i] == "-" and string[2][i + 1] == "-":
                    value3 += "-1"
                    check_notincrement_decrement = False
                    break

            if check_notincrement_decrement:
                string[2] = string[2].strip(variable)

                for i in range(len(string[2])):
                    if string[2][i] == "=":
                        pass
                    else:
                        value3 += string[2][i]

                value3 = value3.rstrip(")")

            new_string += value3 + "):\n"
            return new_string

####################################
#                                  #
#     process_line_do              #
#                                  #
####################################

def process_line_do(line):
    no_whitespace =line.strip()
    if no_whitespace[:5] == "while":
        no_whitespace = "if " + no_whitespace.replace("while (","")
        no_whitespace = no_whitespace.rstrip(");\n")
        no_whitespace = no_whitespace + ":\n"
        return no_whitespace
    else:
        return ""
####################################
#                                  #
#           while check function   #
#                                  #
####################################
def while_check_function (line):

    if line [:5] == "while":
        line = line.replace("while (","")
        line = line.rstrip(");\n")
    for i in line:
        if i == "=":
            return True
    return False

####################################
#                                  #
#           while                  #
#                                  #
####################################


def check_while(line,whitespace):
    no_whitespace = line.strip()
    if no_whitespace[:5] == "while":

        if while_check_function(line):
            var = ""
            no_whitespace = no_whitespace.replace("while", "")
            no_whitespace = no_whitespace.strip()
            if no_whitespace[0] =="(" and no_whitespace[-1] ==")":
                no_whitespace = no_whitespace[1:]
                no_whitespace = no_whitespace[:-1]
                for i in no_whitespace:
                    if i != '=' and i != '-' and i != '+' and i !='*' and i !='/':
                        var += i
                    else:
                        break
            new = whitespace * " " + no_whitespace +"\n"
            new += whitespace * " " + "tmp = " + var + '\n'
            new += whitespace * " " + "while tmp:\n"


            return new
        else:


            no_whitespace = no_whitespace.replace("while","")

            no_whitespace = no_whitespace.strip()

            no_whitespace = no_whitespace.replace("(","")
            no_whitespace = "while " + no_whitespace


            no_whitespace = no_whitespace.rstrip(")\n{ \t")
            no_whitespace = no_whitespace + ":\n"
            return whitespace * " " + no_whitespace

####################################
#                                  #
#               scanf              #
#                                  #
####################################
def check_scanf(line, whitespace):

    string_activate = 0
    output = ""
    string_left = ""
    no_whitespace = line.strip()
    if no_whitespace[:6] == "scanf(":
        new = ""
        variables_check = False
        arraynumber = ""
        fasttrack = 0
        for i in range(len(no_whitespace)):
            string_activate = string_check(no_whitespace[i], string_activate)
            if fasttrack >0:
                fasttrack -= 1
            elif no_whitespace[i] == ',' and no_whitespace[i - 1] == '"':
                variables_check = True

            elif string_activate:
                if no_whitespace[i] == '%':
                    if no_whitespace[i+1] != 's' and  no_whitespace[i+1] != 'c' and no_whitespace[i+1] != 'd':
                        if no_whitespace[i+2] == 's' or no_whitespace[i+2] == 'c' or no_whitespace[i+2] == 'd':
                            arraynumber += no_whitespace[i+1]
                            fasttrack += 2

                    elif no_whitespace[i+1] == 's' or  no_whitespace[i+1] == 'c' or no_whitespace[i+1] == 'd':
                        fasttrack += 1

                else:
                    string_left += no_whitespace[i]

            elif variables_check:
                new += no_whitespace[i]
        string_left += '"'
        new = new.split(',')
        for i in range(len(new)):
            new[i] = new[i].strip()
            new[i] = new[i].lstrip("&")
            new[i] = new[i].rstrip(")")

        variables = no_whitespace.split

        output += whitespace * " " + "tmp = input()\n"

        output += whitespace * " " + "tmp = tmp[:" + arraynumber + "]\n"
        output += whitespace * " " + "tmp = tmp.split()\n"
        for i in range(len(new)):
            """
            if string_left != "":
                output += whitespace * " " + \
                    new[i] + " = " + "tmp[" + str(i) + "] + " + string_left +"\n"
            """

            output += whitespace * " " + \
                new[i] + " = " + "tmp[" + str(i) + "]\n"
        return output
    return False

####################################
#                                  #
#   struct                         #
#                                  #
####################################


def check_structs(line):
    line = line.strip()
    if line[:6] == "struct" or line[:5] == "union":
        line = line.replace("struct", "")
        line = line.replace("union", "")
        line = line.split()
        if len(line) == 1:
            return True
        return False
    return False


def process_struct(line):
    line = line.strip()

    line = line.strip("\n;")

    line = line.replace("int ", "")
    line = line.replace("char ", "")
    if line == "{":
        return "{"
    elif line == "}":
        return "}"
    else:
        return line


def get_class(line):
    line = line.strip()

    line = line.split()

    return line[1]


def set_struct(line):
    no_whitespace = line.strip()
    no_whitespace = line.strip(';')
    if no_whitespace[:7] == "struct " or no_whitespace[:6] == "union ":
        no_whitespace = no_whitespace.split()
        if len(no_whitespace) > 2:
            return no_whitespace[2] + " = " + no_whitespace[1] + "()\n"


####################################
#                                  #
#           Process line           #
#                                  #
####################################

def process_line(line):
    whitespace = store_whitespace(line)

    while check_bracket(line):
        line = check_bracket(line)

    if check_include(line):
        return check_include(line)

    if check_define(line):
        return check_define(line)
    if check_for_infinite(line):
        return whitespace *" " + check_for_infinite(line)
    if check_print(line):
        return whitespace * " " + check_print(line)

    if check_variables(line):
        return whitespace * " " + check_variables(line)
    if check_if(line):
        return whitespace * " " + check_if(line)
    if check_for(line):
        return whitespace * " " + check_for(line)

    if check_scanf(line, whitespace):
        return check_scanf(line, whitespace)
    if set_struct(line):
        return whitespace * " " + set_struct(line)

    return whitespace * " " + line

####################################
#                                  #
#           while check            #
#                                  #
####################################

def while_check(line):
    no_whitespace =line.strip()
    #print(no_whitespace+ "__________________")
    if no_whitespace[:5] == "while":

        return True
    else:

        return False
####################################
#                                  #
#           do check               #
#                                  #
####################################

def do_check(line, mode):
    no_whitespace =line.strip()
    if no_whitespace[:2] == "do":
        return 1
    else:
        return 0

####################################
#                                  #
#           string check           #
#                                  #
####################################


def string_check(char, mode):
    if char == '"':
        return int(not mode)
    else:
        return mode
####################################
#                                  #
#           bracket count          #
#                                  #
####################################


def bracket_counts(char):
    if char == '{':
        return 1
    elif char == '}':
        return -1
    else:
        return 0
####################################
#                                  #
#   Process file                   #
#                                  #
####################################


def process_file(c_file, python_file):
    string_activate = 0  # 0 = off , 1 = on
    special_no_brace = 0
    bracket_count = 0
    struct_variables = []
    do_switch = 0
    store_do_whitespace = []
    store_while_whitespace = 0
    while_switch = 0
    struct_activate = False


    store_while_func = []

    cf = open(c_file, 'r')
    pf = open(python_file, 'w')

#### PREPROCESS FILE ####
    lines = []
    raw_c_lines = cf.readlines()
    check_empty_while = 0
    check_empty_for = 0
    for line in raw_c_lines:

        tidy_c_line = "" + bracket_count * 4 * " "
        line = line.strip()
        line = check_indecrement(line)
        if check_empty_for == 1:
            if line.strip() != "":
                line = line.strip()
                line = line.rstrip("\n")
                lines[-1] = lines[-1].rstrip("\n") + line
                check_empty_for =0

                continue
        if line == "for\n":
            check_empty_for =1

        if check_empty_while == 1:
            if line.strip() != "":
                line = line.strip()
                line = line.rstrip("\n")
                lines[-1] = lines[-1].rstrip("\n") + line
                check_empty_while =0

                continue

        if line == "while\n":
            check_empty_while =1


        check_ending = 0
        for char in line:
            string_activate = string_check(char, string_activate)
            bracket_count += bracket_counts(char)
            if int(not string_activate):
                if char == '{':
                    lines.append(tidy_c_line + '\n')
                    tidy_c_line = (bracket_count - 1) * 4 * " " + char
                    lines.append(tidy_c_line + '\n')
                    tidy_c_line = " " * bracket_count * 4
                    check_ending = 0
                elif char == '}':
                    lines.append(tidy_c_line + '\n')
                    tidy_c_line = (bracket_count) * 4 * " " + char
                    lines.append(tidy_c_line + '\n')
                    tidy_c_line = bracket_count * " " *4
                    check_ending = 1
                elif char == " ":
                    if check_ending:
                        tidy_c_line += ""
                        check_ending = 0

                    else:
                        tidy_c_line += char
                        check_ending = 0
                else:
                    tidy_c_line += char
                    check_ending =0
            elif string_activate:

                tidy_c_line += char

        lines.append(tidy_c_line + '\n')

    for i in range(0,len(lines)):
        lines[i] = lines[i].strip('\n')
    lines = list(filter(None, lines))
    value =0
    for i in range(0, len(lines)):
        for char in lines[i]:
            if char == ' ':
                value += 0
            else:
                value += 1
        if value == 0:
            lines[i] = ""
        value = 0
    lines = list(filter(None, lines))

    extra_bracket_activate = 0
    news_lines =[]
    extra_whitespace = 0
    for i in range (0,len(lines)):
        news_lines.append(extra_whitespace * " " + lines[i])
        tidy_c_line = "" + bracket_count * 4 * " "


        if extra_bracket_activate == 1 and lines[i][-1] == ';':
            extra_whitespace -= 4
            extra_bracket_activate =0
        elif lines[i].strip() == "else":
            extra_whitespace += 4
            extra_bracket_activate = 1

        elif lines[i][-1] == ')' and lines[i+1][-1] !='{':
            extra_whitespace += 4
            extra_bracket_activate = 1

    for i in range (0,len(news_lines)):
        if news_lines[i] == ';':
            news_lines[i] = ""
    news_lines = list(filter(None, news_lines))

    for i in range (0,len(news_lines)):
        news_lines[i] = news_lines[i].replace("argv","sys.argv")

    for line in news_lines:
        print(line)
        do_switch += do_check(line, do_switch)
        check_struct = False
        check_struct = check_structs(line)
        if check_struct:
            whitespace = store_whitespace(line)
            struct_activate = True
            pf.write("class " + get_class(line) + ":\n")
        elif struct_activate == True:

            if process_struct(line) == "}":
                pf.write("):\n")
                for i in struct_variables:
                    pf.write(whitespace * " " + "        " + "self." + i +
                             " = " + i + "\n")

                struct_activate = False
                struct_variables = []

            elif process_struct(line) == "{":
                pf.write(whitespace * " " + "    " + "def __init__(self")
            else:
                struct_variables.append(process_struct(line))
                pf.write(", " + process_struct(line) + " = 0")

        elif struct_activate == False:
            if do_switch == 0:
                if check_while(line, store_while_whitespace):

                    while_switch = 1
                    store_while_whitespace = store_whitespace(line)
                    store_while_func_string = check_while(line , store_while_whitespace)
                    store_while_func = store_while_func_string.split('\n')
                    if len(store_while_func) ==2 :
                        store_while_func = []
                        while_switch = 0
                    pf.write(check_while(line, store_while_whitespace))
                elif while_switch ==1 and check_end_bracket(line):

                    pf.write(store_while_whitespace*" " +store_while_func[0]+'\n')
                    pf.write(store_while_whitespace*" "+store_while_func[1]+'\n')
                    while_switch =0
                elif check_end_bracket(line):
                    while_switch = 0

                else:
                    pf.write(process_line(line))


            else:
                if do_check(line, 0):
                    whitespace = store_whitespace(line)
                    store_do_whitespace.append(store_whitespace_do(line))
                    pf.write(whitespace * " " + "while True:\n")

                elif while_check(line):
                    whitespace = store_do_whitespace.pop()
                    pf.write((whitespace + 4) * " " + process_line_do(line))
                    pf.write((whitespace + 8) * " " + "continue\n")
                    pf.write((whitespace + 4) * " " + "else:\n")
                    pf.write((whitespace + 8) * " " + "break\n")
                    do_switch -= 1

                elif while_switch == 1 and check_end_bracket(line):
                    pf.write(store_while_func[0]+"\n")
                    pf.write(store_while_func[1]+"\n")
                else:
                    pf.write(process_line(line))



    pf.write("\nif __name__ == '__main__':\n")
    pf.write("    main()")
    pf.close()
    cf.close()

########################################
########################################
###                                  ###
###          Main function           ###
###                                  ###
########################################
########################################
def main():

    if len(sys.argv) != 3:
        print('Invalid Arguments, First is Path to C file, Second is Path to Pyhthon file')
        exit(1)

    python_file = sys.argv[2]
    c_file = sys.argv[1]

    if is_python(python_file) == False:
        print('Invalid source file')
        exit(1)

    if is_c(c_file) == False:
        print('Invalid source file')
        exit(1)

    process_file(c_file, python_file)


if __name__ == '__main__':
    main()
