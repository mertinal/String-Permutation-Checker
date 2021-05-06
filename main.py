def checkStrings(str1 , str2):
    status = False
    str1 = ''.join(sorted("".join(str1)))
    str2 = ''.join(sorted("".join(str2)))
    if(str1 == str2):
        status = True
    else:
        status = True
        if(len(str1) > len(str2)):
            for i in str2:
                if(i not in str1):
                    status = False
                    break
        else:
            for i in str1:
                if(i not in str2):
                    status = False
                    break
        
    return status

print(checkStrings("baba","abab"))
        
