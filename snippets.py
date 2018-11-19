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

#Reading specific Columns and rows based on cell data
print (data.loc[(data['mix1_instrument'] == 'DTrumpet' )])

##Object Creation

#Creating a series (attribute)
s = pd.Series([1,3,5,np.nan,6,8])

print s

#Creating a DataFrame (dataset)
dates = pd.date_range('20130101', periods=6)

print dates

dataFrame = pd.DataFrame(np.random.rand(6,4), index=dates, columns=list('ABCD'))

print dataFrame

#You can also create a dataFrame by passing in objects
df2 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

print df2
#looking at the types of data in a dataFrame
print df2.dtypes



#functions 
DTrumpet = data['mix1_instrument'] == 'DTrumpet'

#adding attributes 
df['Trumpet'] = (DTrumpet)

#dropping columns 
df.drop('mix1_instrument', axis='columns', inplace=True)


def conditions(x):
    if x == "CTrumpet":
        return "1"
    elif x ==  "DTrumpet":
        return "1"
    elif x ==  "B-FlatTrumpet":
        return "1"
    else:
        return "0"

func = np.vectorize(conditions)
trumpet = func(df["mix1_instrument"]) & (df["mix2_instrument"])
df["Trumpet"] = trumpet

print (df.loc[:,['mix1_instrument','mix2_instrument','Trumpet']])


df['trumpet']=np.where((df['mix1_instrument']=='f')| )