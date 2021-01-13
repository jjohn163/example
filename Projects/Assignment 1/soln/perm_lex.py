def perm_gen_lex(a): 
    if len(a) == 0:
        return []
    if len(a) == 1:
        return [a]
    strlist = []
    for i in range(len(a)):
        remstring = a[0:i] + a[i+1:len(a)]
        perm = perm_gen_lex(remstring)
        for s in perm:
            #strlist.append(a[i] + s)
            strlist = strlist + [(a[i] + s)]
    return strlist
