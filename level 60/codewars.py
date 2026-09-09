def flick_switch(lst):
    boo = True
    array = []
    for i in range(len(lst)):
        if lst[i] == "flick":
            if boo == True:
                boo = False
            else:
                boo = True
        array.append(boo)
    return array