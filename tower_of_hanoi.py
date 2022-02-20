def TOH(n,s,d,h):
    if n==1:
        print(f"MOVING PLATE {n} FROM {s} to {d}")
        return
    TOH(n-1,s,h,d)
    print(f"MOVING PLATE {n} FROM {s} to {d}")
    TOH(n-1,h,d,s)
    return
    




n=int(input("Enter the input: "))
s=1
h=2
d=3
TOH(n,s,d,h)
