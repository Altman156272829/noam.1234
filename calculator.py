def negative_binary_calculator(a):
    b = ''
    c = ''
    d = ''
    first = True
    count = 0
    for i in a:
        if i == "0":
            b += "1"
        else:
            b+= "0"

    for item in reversed(b):
        if item =="0" and first :
            c +="1"
            first = False
        elif first:
            c += "0"
        else:
            c += item

    for gg in reversed(c):
        d += gg
    print(d)
        
    

        


    