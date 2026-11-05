import os
import numpy as np 
special_char = "~`!@#$%^&*)(_+-=][}{:;<>,.?/\\ \'\' \"\""

def counter(p) :
    if not p.isnumeric() :
        s = [i for i in p if i in special_char]
        n = [i for i in p if i.isdigit()]
        u = [i for i in p if i.isupper()]
        l = [i for i in p if i.islower()]
        r = [True if p.count(i) >= 3 else False for i in p]
        return {
            "el" : np.array([(len(s) * 2), (len(n) * 1.5), (len(u) * 1.5), (len(l))]),
            "repeat" : r.count(True),
            "lenth" : len(p)
        }
    else :
        return False

def cheker(p) :
    lst = counter(p)
    if lst == False :
        return "Weak"
    else :
        return "Strong" if lst["lenth"] >= 8 and lst["el"].mean() >= (lst["lenth"] / 3) and lst["repeat"] <= lst["lenth"]  / 3  else "Weak"

def main() :
    while True :
        password = input("Enter your password (\'\' For break): ")
        os.system("cls")
        if password == "" : break
        password = password.replace(" ","")
        print(f"\n- Your password is {cheker(password)} !\n")
        print(">>>",password,"\n")

if __name__ == "__main__" :
    main()
    os.system("cls")
    print("\n>> Thanks for choosing us ;)\n")
