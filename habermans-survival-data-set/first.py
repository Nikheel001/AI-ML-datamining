# understanding the dataset

from pandas import read_csv

cs =read_csv('haberman.csv')

print(cs.columns)
print(cs.head)

'''
findings

Age - age of the patient
Op_year - year of the operation
axil_nodes - number of positive axillary nodes detected
Surv_status - survival status 
    1 means the patient survived 5 years or longer
    2 means the patient died within 5 year
'''