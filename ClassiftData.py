#!/usr/bin/python


import pandas as pd 
import numpy as np


#Reading CSV Data
data = pd.read_csv(
    '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/train.csv'
    )

#Printing Data
print data #prints out all the data


#Printing specific Rows
print (data[0:5]['MFCC1'])
#prints the MFCC1 for the first 5 rows 

#Printing Specific Columns 
print (data.loc[:,['mix1_instrument','MFCC1']])

#Reading specfic Columns and rows
print (data.loc[[1,4,67],['mix1_instrument','MFCC1']])