k = open("blocks.in")
blocks = int(k.readline())
r = 0
counts = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
count1 = 0
count2 = 0
for i in range(blocks):
    words = [i for i in k.readline().split()]
    for j in counts:
        count1 = 0
        count2 = 0
        for x in words[0]:
            if x == j:
                count1 += 1
        for x in words[1]:
            if x == j:
                count2 += 1
        if count1 == 0 and count2 == 0:
            continue
        elif count1 >= count2:
            counts[j] += count1
        else:
            counts[j] += count2
        r+=1


y = open("blocks.out","w")
for i in counts.values():
    y.write(f"{i}\n")
y.close
