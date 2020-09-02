# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
def myAtoi(str: str) -> int:
    l = len(str)
    str = str.strip()#.replace(" ","")
    i = 0
    sign = ""
    num = ""
    for i in range(len(str)):
        if (str[i] > "a" and str[i] < "z") or (str[i] > "A" and str[i] < "Z"):
            return 0            
        elif ((str[i] =="+" or str[i] == "-") and sign == ""):
            sign = str[i]
        elif(str[i] >= "0" and str[i] <= "9"):
            while(i <= len(str)-1 and (str[i] >= "0" and str[i] <= "9")):
                num+=str[i]
                i += 1
            break;
        else:
            return 0                

    if(num != ""):
        res = int(sign + num)
        if res > pow(2,31) - 1 or res < -pow(2, 31):
            return -pow(2, 31) if res < 0 else pow(2,31) - 1
        else:
            return res
    else:
        return 0

print(myAtoi(str="        +0 123"))
#%%