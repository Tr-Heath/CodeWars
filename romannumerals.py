def solution(n):
    # TODO convert int to roman string
    print(n / 5)
    print(n / 10)
    print(n / 50)
    print(n / 100)
    print(n / 1000)
    
    r = ""
    match n:
        case 1:
            return "I"
        case 4:
            return "IV"

    if(n / 1000 > 1):
        print(n / 1000)
        r = r + "M"
        n = n - 1000
    if(n / 100 > 1):
        print(n / 100)
        r = r + "C"
        n = n - 100
    if(n / 50 > 1):
        print(n / 50)
        r = r + "L"
        n = n - 50
    if(n / 10 > 1):
        print(n / 10)
        r = r + "X"
        n = n - 10
    if(n / 5 > 1):
        print(n / 5)
        r = r + "V"
        n = n - 5
    

    return r