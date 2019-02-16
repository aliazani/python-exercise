f = open('numbers.txt')
g = f.read()
print(type(f))
for i in g.split():
    print(i)
f.close()


