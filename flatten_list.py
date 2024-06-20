a = [1,2,3,[4,5,6],[[7,8,9]],10,11]

final = []

def flatten(l):
    for i in l:
        if isinstance(i,list):
            flatten(i)
        else:
            final.append((i))

flatten(a)
print(final)
