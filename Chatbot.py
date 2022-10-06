i=list(input(""))
i.append(" ")
b=""
inp=[]
for a in i:
    asc=ord(a)
    if asc >= 65 and asc <= 90:
        asc=asc+32
        a=chr(asc)
    if a != " ":
        b=b+a
    else:
        inp.append(b)
        b=""
print (inp)
stop=["a","an","the","is","are","am","any","at","has","have","had","was","were","will","shall","to","be","being","been","but","!","?",".",","]
for i in inp:
    if i in stop:
        inp.remove(i)
print(inp)
