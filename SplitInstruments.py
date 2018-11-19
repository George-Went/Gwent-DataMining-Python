#!/usr/bin/python


import pandas as pd 
import numpy as np


#Reading CSV Data
df = pd.read_csv(
    '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/train.csv'
    )

#For pt4 - adds binary columns denoting which instrumnets are playing 
df['Cello'] = np.where((df['mix2_instrument'] == "Cello"),1,0)

df['Trumpet'] = np.where((df['mix1_instrument'] == "CTrumpet") | 
                         (df['mix1_instrument'] == "DTrumpet") | 
                         (df['mix2_instrument'] == "B-FlatTrumpet"),1,0)

df['Piano'] = np.where((df['mix1_instrument'] == "Piano"),1,0)

df['DoubleBass'] = np.where((df['mix1_instrument'] == "DoubleBass") | 
                         (df['mix2_instrument'] == "AcousticBass"),1,0)

df['Clarinet'] = np.where((df['mix1_instrument'] == "BFlatClarinet"),1,0)

df['Oboe'] = np.where((df['mix1_instrument'] == "Oboe"),1,0)

df['Trombone'] = np.where((df['mix1_instrument'] == "TenorTrombone"),1,0)

df['Saxophone'] = np.where((df['mix1_instrument'] == "TenorSaxophone") | 
                         (df['mix2_instrument'] == "SopranoSaxophone") | 
                         (df['mix2_instrument'] == "AltoSaxophone")    |
                         (df['mix2_instrument'] == "BaratoneSaxophone")|
                         (df['mix2_instrument'] == "BassSaxophone"),1,0)

df['Vibraphone'] = np.where((df['mix2_instrument'] == "Vibraphone"),1,0)

df['Accordian'] = np.where((df['mix1_instrument'] == "Accordion") | 
                          (df['mix2_instrument'] == "Accordion"),1,0)

df['Viola'] = np.where((df['mix1_instrument'] == "Viola"),1,0)

df['Violin'] = np.where((df['mix1_instrument'] == "Violin"),1,0)

df['ElectricGuitar'] = np.where((df['mix1_instrument'] == "ElectricGuitar"),1,0)

df['Marimba'] = np.where((df['mix2_instrument'] == "Marimba"),1,0)

print (df.loc[:,['mix1_instrument','mix2_instrument','Cello','Trumpet','Piano','DoubleBass','Clarinet'
                ,'Oboe','Trombone','Saxophone','Vibraphone','Accordian','Viola','Violin','ElectricGuitar','Marimba']])

#Playmethod Binary
df['struck'] = np.where((df['Piano'] == 1)       |
                    (df['Vibraphone'] == 1)      |
                    (df['ElectricGuitar'] == 1)  |
                    (df['Marimba'] == 1),1,0)

df['string'] = np.where((df['Cello'] == 1) |
                    (df['DoubleBass'] == 1)|
                    (df['Viola'] == 1)     |
                    (df['Violin'] == 1),1,0)

df['blown'] = np.where((df['Trumpet'] == 1)   |
                    (df['Clarinet'] == 1)     |
                    (df['Oboe'] == 1)         |
                    (df['Trombone'] == 1)     |
                    (df['Saxophone'] == 1)    |
                    (df['Accordian'] == 1),1,0)

#Class 1  Binary
df['chordophone'] = np.where((df['Cello'] == 1)   |
                    (df['Piano'] == 1)            |
                    (df['DoubleBass'] == 1)       |
                    (df['Viola'] == 1)            |
                    (df['Violin'] == 1)           |
                    (df['ElectricGuitar'] == 1),1,0)

df['aerophone'] = np.where((df['Trumpet'] == 1)   |
                    (df['Clarinet'] == 1)     |
                    (df['Oboe'] == 1)         |
                    (df['Trombone'] == 1)     |
                    (df['Saxophone'] == 1)    |
                    (df['Accordian'] == 1),1,0)

#Class 2 Binary
df['chrd_composite'] = np.where((df['Cello'] == 1) |
                    (df['DoubleBass'] == 1)|
                    (df['Viola'] == 1)     |
                    (df['Violin'] == 1)    |
                    (df['ElectricGuitar'] == 1),1,0)

df['chrd_simple'] = np.where((df['Piano'] == 1),1,0)

df['aero_lip-vibrated'] = np.where((df['Trumpet'] == 1) |
                                    (df['Trombone'] == 1),1,0)

df['aero_single-reed'] = np.where((df['Clarinet'] == 1),1,0)

df['aero_double-reed'] = np.where((df['Oboe'] == 1),1,0)

df['aero_free-reed'] = np.where((df['Accordian'] == 1),1,0)

#df['aero_slide'] = np.where((df['Flute'] == 1),1,0)



print df.loc[:,['mix1_instrument','mix2_instrument','struck','string','blown']]
print df.loc[:,['mix1_instrument','mix2_instrument','chordophone','aerophone',
                'chrd_composite','chrd_simple','aero_lip-vibrated','aero_single-reed','aero_double-reed',
                'aero_free-reed']]
#df.to_csv(
#   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/trainBinary.csv'
#  )





















#Cello
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Trumpet
df = df.loc[(df['Trumpet'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#English horn
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#piano
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#tuba
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#SynthBass
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Double
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Clarinet
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Oboe
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#French Horn
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Flute
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Trombone
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Piccalo
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Saxophone
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Accordion
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Viola
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Basson
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
#Violin
df = df.loc[(df['Cello'] == 1 )]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/cello.csv'
  )
