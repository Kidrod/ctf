def solve():
    s = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
    arr = s.split()
    a=[]
    for i in range(1,27):
        a.append(str(i))
    d = {}
    for i in range (26):
        d[a[i]] = chr(65 + i)
    print("".join([d.get(c,c) for c in arr])) 
if(__name__ == "__main__"):
    solve()