def check(s,n):
    for i in range(len(s)-n):
        a = s[i:(i+n)]
        b = s[i+n]
        l = set([a.count(item) for item in a])
        if((l=={1}) and (b not in a)):
            return i+n+1

with open('day6/input.txt','r') as f:
    s = f.read()
    print("P1: ", check(s,3)) #Part-1
    print("P2: ", check(s,13)) #Part-2