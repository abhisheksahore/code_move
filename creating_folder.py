import os
folder = input()
os.mkdir(folder)
os.chdir(folder)
fol = ''
for i in range(0, len(folder)):
    if folder[i] != " ":
        fol= fol+folder[i]
    else:
        print(folder[i])
fol = fol.lower()
print(fol)
for i in range(0,len(fol)):
    f= open(fol[i],"w")
    s = fol[i]
    count = fol.count(s)
    f.write(str(count))
    f.close    
