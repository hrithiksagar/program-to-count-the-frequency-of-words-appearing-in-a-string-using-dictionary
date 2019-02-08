# write a program to count the frequency of words appearing in a string  using dictionary

x = input("enter a paragraph: ")
y = []
y = x.split()
freq = [y.count(i) for i in y]
d = dict(zip(y, freq))
print(d)

# other way

s = input("enter a string")
l = (s.lower()).split()
d = {}
for i in l:
    if i in d.keys():
        d[i] = d[i] + l
    else:
        d[i] = l
d[i] = d.get(i, 0) + 1
print(d)