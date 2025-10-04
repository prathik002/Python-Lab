y1=int(input("Enter Starting Year: "))
y2=int(input("Enter Ending Year: "))

if y1>y2:
    print("End year must be greater than or equal to starting year")
else:
    print(f"The leap years from {y1} to {y2} are")
    for year in  range(y1,y2+1):
        if(year%4==0 and year%100!=0) or (year%400==0):
            print(year)
