def repeatedString(a:str,x:int):
    if len(a) ==1:
        return n
    else:
        daa = a.count("a")*(x//len(a)) + (a[:x//len(a)].count('a'))
        return daa
    
if __name__ == '__main__':

    s =input()
    n =int(input())
 
    result = repeatedString(s, n)
    print(result)
