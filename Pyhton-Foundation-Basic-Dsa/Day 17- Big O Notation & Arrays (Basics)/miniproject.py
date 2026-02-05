# Student Marks Analyzer
arr=[11,12,13,14,15]

highest=arr[0]
lowest=arr[0]
avg=0
sum=0
for x in arr:
    if x>highest:
        highest=x
    if x<lowest:
        lowest=x
    sum=sum+x
avg=(sum)/len(arr)   

print("Higest marks :",highest)
print("Lowest :",lowest)
print("Average :",avg)   