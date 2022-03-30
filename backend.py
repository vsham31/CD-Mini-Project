#backend

lines=""

keywords    = ["void", "main", "int", "float", "bool", "if", "for", "else", "while", "char", "return"]
operators   = ["=", "==", "+", "-", "*", "/", "++", "--", "+=", "-=", "!=", "||", "&&"]
punctuations= [";", "(", ")", "{", "}", "[", "]"]

def is_int(x):
    try:
        int(x)
        return True
    except:
        return False

def parsefn(b):
    a=""
    for line in b:
        for i in line.strip().split(" "):
            a+="\n"
            if i in keywords:
                a=a+i+" is a keyword"
            elif i in operators:
                a=a+i+" is an operator"
            elif i in punctuations:
                a=a+i+" is a punctuation"
            elif is_int(i):
                a=a+i+" is a number"
            else:
                a=a+i+" is an identifier"
    return(a)
