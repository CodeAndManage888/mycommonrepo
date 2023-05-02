import csv
# with open('Program Files/Input/business-employment-data-032022.csv', 'r') as csv_file00:
#     csv_reader = csv.reader(csv_file00)
    
#     with open('Program Files/Output/new-business-employment-data-032022.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
    
#         for line00 in csv_reader:
#             csv_writer.writerow(line00)
           
with open('Program Files/Output/new-business-employment-data-032022.csv', 'r') as csv_file01:
   csv_reader = csv.reader(csv_file01, delimiter='\t')
   
   for line01 in csv_reader:
       print(line01)
        
#-----------------------------------------------------------------
# Notes:
#   a.) 
#
