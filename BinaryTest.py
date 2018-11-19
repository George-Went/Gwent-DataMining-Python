#!/usr/bin/python


import pandas as pd 
import numpy as np


#Reading CSV Data
df = pd.read_csv(
    '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/test.csv'
    )

#For pt4 - adds binary columns denoting which instrumnets are playing 


#Playmethod Binary
df['struck'] = np.where((df['playmethod'] == 'struck_Hrm'),'yes','no')

df['string'] = np.where((df['playmethod'] == 'string'),'yes','no')

df['blown'] = np.where((df['playmethod'] == 'blown'),'yes','no')


#Class 1  Binary
df['chordophone'] = np.where((df['class1'] == 'chordophone'),'yes','no')

df['aerophone'] = np.where((df['class1'] == 'aerophone'),'yes','no')

#Class 2 Binary
df['chrd_composite'] = np.where((df['class2'] == 'chrd_composite'),'yes','no')

df['chrd_simple'] = np.where((df['class2'] == 'chrd_simple'),'yes','no')

df['aero_lip-vibrated'] = np.where((df['class2'] == 'aero_lip-vibrated'),'yes','no')

df['aero_single-reed'] = np.where((df['class2'] == 'aero_single-reed'),'yes','no')

df['aero_double-reed'] = np.where((df['class2'] == 'aero_double-reed'),'yes','no')

df['aero_free-reed'] = np.where((df['class2'] == 'aero_free-reed'),'yes','no')

df['aero_side'] = np.where((df['class2'] == 'aero_side'),'yes','no')



print df.loc[:,['playmethod','class1','class2','struck','string','blown',
                'chordophone','aerophone',]]


df.to_csv(
  '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/testBinary.csv'
  )

