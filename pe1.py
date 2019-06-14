n=int(input())
l=[]
s=0
tp=1
fp=1
while(True):
    k=min(3*tp,5*fp)
    
    if(k<n):
        l.append(k)
        if(k==3*tp):
            tp+=1
        else:
            fp+=1
        
    else:
        break

print(sum(list(set(l))))
    
