year1=int(input("Enter the year:"))
if(year1%4==0 and year1%100!=0):
    print(year1,"is leap year")
elif(year1%4==0 and year1%100==0 and year1%400==0):
    print(year1, "is leap year")
else:
    print(year1,"is not leap year")
