import csv 
    
# field names 
fields = ['Name', 'Message'] 
    
# data rows of csv file 
rows = [['Jack Barnard','Hello World'],]
    
# name of csv file 
filename = "sponsor_records.csv"
    
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
