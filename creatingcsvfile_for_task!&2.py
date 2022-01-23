import csv 
    
# field names 
fields = ['Name', 'Volunteer', 'Date', 'Payed'] 
    
# data rows of csv file 
rows = [['Jack Barnard', 'no', '06/01/22', 'yes'],
['Lisa Gross', 'entrance gate', '04/01/22', 'yes']] 
    
# name of csv file 
filename = "member_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)


#creates csv file
#adds some memeber info
