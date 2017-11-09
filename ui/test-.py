a=(1,3,5,7,9,11,13,15)
for i in range (len(a)):
    for n in range (len(a)):
        for k in range (len(a)):
            if (a[i]+a[n]+a[k]) == 30 :
                print a[i],a[n],a[k]