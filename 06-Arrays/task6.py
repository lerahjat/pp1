import statistics as st

ar=[15,8,31,47,2,19]
sum=0
for i in ar:
    sum=sum+i
mean=sum/(len(ar))
print(mean)



print(st.mean(ar))