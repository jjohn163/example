#from inspect import getouterframes, currentframe, stack

def bears(n):
    #print(len(stack()))
    if n < 42:
        return False
    if n == 42:
        return True
    win = False
    if n % 2 == 0:
        win = bears(n//2)
    if not win and (n % 3 == 0 or n % 4 == 0):
        give = n%10 * (n%100//10)
        if give > 0:
            win = bears(n - give)
    if not win and n % 5 == 0:
        win = bears(n-42)
    return win

'''values = []
for val in range(10000, 20000):
    if bears(val) and val not in values:
        values.append(val)
values.sort()
out = open('out2.txt', "w")
out.write('[')
for i in range(len(values)):
    out.write('%4d' % values[i] + ', ')
    if (i+1)%100 == 0:
        out.write('\n')
out.write(']')'''