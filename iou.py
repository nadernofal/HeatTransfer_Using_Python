strr="""
100 3.945 0.962 76.4 1.94 9.25 2.44 0.796
150 2.585 0.921 114.8 4.44 13.8 5.80 0.766
200 1.930 0.915 147.5 7.64 18.3 10.4 0.737
250 1.542 0.915 178.6 11.58 22.6 16.0 0.723
300 1.284 0.920 207.2 16.14 26.8 22.7 0.711
"""
lis=["temp","Density","Cp","Vis","kyn_vis","conductivity","diff","Pr"]
for i in strr.split('\n'):
    x=0
    print("{",end="")
    for j in i.split(' '):
        print(f"'{lis[x]}':{j},",end="")
        x+=1
    print("},\n",end="")