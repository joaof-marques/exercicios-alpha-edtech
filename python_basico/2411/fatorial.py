def calcFatorial (num):
    if num==1:
        return 1
    return num*calcFatorial(num-1)



fatorialTeste = calcFatorial(20)