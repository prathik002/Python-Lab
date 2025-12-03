import csv
csv_col=['Roll no','Name','Place']
dict_data=[{'Roll no':1,'Name':'Anjela','Place':'Idukki'},
           {'Roll no':2,'Name':'Theja','Place':'Thrissur'},
           {'Roll no':3,'Name':'Prathik','Place':'Thrissur'},
           {'Roll no':4,'Name':'Thasni','Place':'Thrissur'},
           {'Roll no':5,'Name':'Arya','Place':'Palakkad'}]
csv_file="student.csv"
try:
    with open(csv_file,'w')as file1:
        writer=csv.DictWriter(file1,fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)
except IOError:
    print("I/O error")
data1=csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
           
         
