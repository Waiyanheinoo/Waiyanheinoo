def main():
    plate = input("Input: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(i):
    if i.isalpha() and 2<=len(i)<=6:
        return True
    if len(i) < 2 or len(i) > 6:
        return False
    if i[0:2].isdigit():
        return False
    if not i.isalnum():
        return False
    if zero(i) == False:
        return False
    if alpha(i) == False:
        return False
    else:
        return True

def zero(i):
    for char in i:
        if char.isdigit():
           if int(char) == 0:
               return False
           else:
               return True
           
def alpha(i):
    for char in i:
        if char.isdigit():
            index = i.index(char)
            for n in i[index:len(i)]:
                if n.isalpha():
                    return False
main()
