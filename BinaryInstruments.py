#!/usr/bin/python


import pandas as pd 
import numpy as np


#Reading CSV Data
df = pd.read_csv(
    '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/trainFullInstrument.csv'
    )

#For pt4 - adds binary columns denoting which instrumnets are playing 

df['Bassoon'] = np.where((df['mix1_instrument'] == "Bassoon"),'yes','no')

df['Cello'] = np.where((df['mix2_instrument'] == "Cello"),'yes','no')

df['Trumpet'] = np.where((df['mix1_instrument'] == "CTrumpet") | 
                         (df['mix1_instrument'] == "DTrumpet") | 
                         (df['mix2_instrument'] == "B-FlatTrumpet"),'yes','no')

df['Piano'] = np.where((df['mix1_instrument'] == "Piano"),'yes','no')

df['Flute'] = np.where((df['mix1_instrument'] == "Flute"),'yes','no')

df['Piccalo'] = np.where((df['mix1_instrument'] == "Piccalo"),'yes','no')

df['DoubleBass'] = np.where((df['mix1_instrument'] == "DoubleBass"),'yes','no')

df['AcousticBass'] = np.where((df['mix2_instrument'] == "AcousticBass"),'yes','no')

df['SynthBass'] = np.where((df['mix1_instrument'] == "SynthBass"),'yes','no')

df['Clarinet'] = np.where((df['mix1_instrument'] == "B-flatclarinet"),'yes','no')

df['EnglishHorn'] = np.where((df['mix1_instrument'] == "English_Horn"),'yes','no')

df['FrenchHorn'] = np.where((df['mix1_instrument'] == "FrenchHorn"),'yes','no')

df['Oboe'] = np.where((df['mix1_instrument'] == "Oboe"),'yes','no')

df['Trombone'] = np.where((df['mix1_instrument'] == "TenorTrombone"),'yes','no')

df['Tuba'] = np.where((df['mix2_instrument'] == "Tuba"),'yes','no')

df['Saxophone'] = np.where((df['mix1_instrument'] == "TenorSaxophone") | 
                         (df['mix2_instrument'] == "SopranoSaxophone") | 
                         (df['mix2_instrument'] == "AltoSaxophone")    |
                         (df['mix2_instrument'] == "BaratoneSaxophone")|
                         (df['mix2_instrument'] == "BassSaxophone"),'yes','no')

df['Vibraphone'] = np.where((df['mix2_instrument'] == "Vibraphone"),'yes','no')

df['Accordian'] = np.where((df['mix1_instrument'] == "Accordian") | 
                          (df['mix2_instrument'] == "Accordian"),'yes','no')

df['Viola'] = np.where((df['mix2_instrument'] == "Viola"),'yes','no')

df['Violin'] = np.where((df['mix1_instrument'] == "Violin"),'yes','no')


df['ElectricGuitar'] = np.where((df['mix1_instrument'] == "ElectricGuitar"),'yes','no')

df['Marimba'] = np.where((df['mix2_instrument'] == "Marimba"),'yes','no')
#22

print (df.loc[:,['mix1_instrument','mix2_instrument','Cello','Trumpet','Piano','DoubleBass','Clarinet'
                ,'Oboe','Trombone','Saxophone','Vibraphone','Accordian','Viola','Violin','ElectricGuitar','Marimba']])

#Playmethod Binary
df['struck'] = np.where((df['Piano'] == 'yes')       |
                    (df['Vibraphone'] == 'yes')      |
                    (df['DoubleBass'] == 'yes')      |
                    (df['AcousticBass'] == 'yes')     |                    
                    (df['ElectricGuitar'] == 'yes')  |
                    (df['SynthBass'] == 'yes')       |
                    (df['Marimba'] == 'yes'),'yes','no')
                    #7

df['string'] = np.where((df['Cello'] == 'yes') |
                    (df['Viola'] == 'yes')     |
                    (df['Violin'] == 'yes'),'yes','no')
                    #3

df['blown'] = np.where((df['Trumpet'] == 'yes')   |
                    (df['Clarinet'] == 'yes')     |
                    (df['Piccalo'] == 'yes')      |
                    (df['Flute'] == 'yes')        |
                    (df['Oboe'] == 'yes')         |
                    (df['EnglishHorn'] == 'yes')  |
                    (df['FrenchHorn'] == 'yes')   |
                    (df['Trombone'] == 'yes')     |
                    (df['Saxophone'] == 'yes')    |
                    (df['Bassoon'] == 'yes')      |
                    (df['Tuba'] == 'yes')     |
                    (df['Accordian'] == 'yes'),'yes','no')
                    #12

#Class 1  Binary --------------------------------------------------
df['chordophone'] = np.where((df['Cello'] == 'yes')   |
                    (df['Piano'] == 'yes')            |
                    (df['DoubleBass'] == 'yes')       |
                    (df['AcousticBass'] == 'yes')     |
                    (df['SynthBass'] == 'yes')        |
                    (df['Viola'] == 'yes')            |
                    (df['Violin'] == 'yes')           |
                    (df['ElectricGuitar'] == 'yes'),'yes','no')
                    #7

df['aerophone'] = np.where((df['Trumpet'] == 'yes')   |
                    (df['Clarinet'] == 'yes')         |
                    (df['Piccalo'] == 'yes')          |
                    (df['Flute'] == 'yes')            |
                    (df['Oboe'] == 'yes')             |
                    (df['Bassoon'] == 'yes')          |
                    (df['EnglishHorn'] == 'yes')      |
                    (df['FrenchHorn'] == 'yes')       |
                    (df['Trombone'] == 'yes')         |
                    (df['Tuba'] == 'yes')             |
                    (df['Saxophone'] == 'yes')        |
                    (df['Accordian'] == 'yes'),'yes','no')
                    #1'no'

#Class 2 Binary --------------------------------------------------
df['chrd_composite'] = np.where((df['Cello'] == 'yes') |
                    (df['DoubleBass'] == 'yes')        |
                    (df['AcousticBass'] == 'yes')      |
                    (df['Viola'] == 'yes')             |
                    (df['Violin'] == 'yes')            |
                    (df['ElectricGuitar'] == 'yes'),'yes','no')

df['chrd_simple'] = np.where((df['Piano'] == 'yes')           |
                                (df['SynthBass'] == 'yes'),'yes','no')

df['aero_lip-vibrated'] = np.where((df['Trumpet'] == 'yes'),'yes','no')

df['aero_lip-valved'] = np.where((df['FrenchHorn'] == 'yes')   |
                                (df['Tuba'] == 'yes')          |
                                (df['Saxophone'] == 'yes'),'yes','no')

df['aero_side'] = np.where((df['Trombone'] == 'yes'),'yes','no')

df['aero_single-reed'] = np.where((df['Clarinet'] == 'yes')    |
                                    (df['Piccalo'] == 'yes')   |
                                    (df['Flute'] == 'yes'),'yes','no')

df['aero_double-reed'] = np.where((df['Oboe'] == 'yes')           |
                                    (df['Bassoon'] == 'yes')      |
                                    (df['EnglishHorn'] == 'yes'),'yes','no')

df['aero_free-reed'] = np.where((df['Accordian'] == 'yes'),'yes','no')



print df.loc[:,['mix1_instrument','mix2_instrument'
                ,'Cello'
                ,'Piano'
                ,'DoubleBass'
                ,'AcousticBass'
                ,'SynthBass'
                ,'Viola'
                ,'Violin'
                ,'ElectricGuitar'
                ,'Trumpet'
                ,'Clarinet'
                ,'Piccalo'
                ,'Flute'
                ,'Oboe'
                ,'Bassoon'
                ,'EnglishHorn'
                ,'FrenchHorn'
                ,'Trombone'
                ,'Tuba'
                ,'Saxophone'
                ,'Accordian']]


print df.loc[:,['mix1_instrument','mix2_instrument','struck','string','blown']]
print df.loc[:,['mix1_instrument','mix2_instrument','chordophone','aerophone',
                'chrd_composite','chrd_simple','aero_lip-vibrated','aero_single-reed','aero_double-reed',
                'aero_free-reed']]
df.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/trainBinary.csv',index = False
  )

#seperating all instruments by type into csv's
instrumentList = ['Cello'
                ,'Piano' 
                ,'DoubleBass'
                ,'AcousticBass'
                ,'SynthBass'
                ,'Viola'
                ,'Violin'
                ,'ElectricGuitar'
                ,'Trumpet'
                ,'Clarinet'
                ,'Piccalo'
                ,'Flute'
                ,'Oboe'
                ,'Bassoon'
                ,'EnglishHorn'
                ,'FrenchHorn'
                ,'Trombone'
                ,'Tuba'
                ,'Saxophone'
                ,'Accordian']


for instrument in instrumentList:
    print(instrument)
    dfInstrument = df.loc[(df[instrument] == 'yes')]
    dfInstrument.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/PT4/InstrumentList/' + instrument + 'Data.csv',index = False
  )

for instrument in instrumentList:
    print("Reading: " + instrument)
    # Grabs instrments preictions results 
    
    instrument_df_Format = (df.loc[:,['temporalCentroid',
                                            'LogSpecCentroid',	
                                            'LogSpecSpread',
                                            'MFCC1',
                                            'MFCC2',
                                            'MFCC3',
                                            'MFCC4',	
                                            'MFCC5',	
                                            'MFCC6',	
                                            'MFCC7',	
                                            'MFCC8',
                                            'MFCC9',
                                            'MFCC10',	
                                            'MFCC11',
                                            'MFCC12',
                                            'MFCC13',
                                            'Energy',
                                            'ZeroCrossings',	
                                            'SpecCentroid',	
                                            'SpecSpread',	
                                            'Rolloff',
                                            'Flux',	
                                            'bandsCoef1',
                                            'bandsCoef2',
                                            'bandsCoef3',
                                            'bandsCoef4',	
                                            'bandsCoef5',	
                                            'bandsCoef6',
                                            'bandsCoef7',
                                            'bandsCoef8',
                                            'bandsCoef9',
                                            'bandsCoef10',
                                            'bandsCoef11',	
                                            'bandsCoef12',	
                                            'bandsCoef13',
                                            'bandsCoef14',	
                                            'bandsCoef15',	
                                            'bandsCoef16',	
                                            'bandsCoef17',
                                            'bandsCoef18',	
                                            'bandsCoef19',	
                                            'bandsCoef20',	
                                            'bandsCoef21',	
                                            'bandsCoef22',
                                            'bandsCoef23',	
                                            'bandsCoef24',
                                            'bandsCoef25',
                                            'bandsCoef26',
                                            'bandsCoef27',
                                            'bandsCoef28',
                                            'bandsCoef29',
                                            'bandsCoef30',	
                                            'bandsCoef31',	
                                            'bandsCoef32',
                                            'bandsCoef33',
                                            'bandsCoefSum',
                                            'prj1',
                                            'prj2',
                                            'prj3',
                                            'prj4',
                                            'prj5',
                                            'prj6',
                                            'prj7',
                                            'prj8',
                                            'prj9',
                                            'prj10',
                                            'prj11',
                                            'prj12',
                                            'prj13',
                                            'prj14',
                                            'prj15',
                                            'prj16',
                                            'prj17',	
                                            'prj18',
                                            'prj19',	
                                            'prj20',	
                                            'prj21',	
                                            'prj22',
                                            'prj23',	
                                            'prj24',
                                            'prj25',	
                                            'prj26',
                                            'prj27',
                                            'prj28',
                                            'prj29',
                                            'prj30',	
                                            'prj31',
                                            'prj32',	
                                            'prj33',	
                                            'prjmin',
                                            'prjmax',
                                            'prjsum',
                                            'prjdis',
                                            'prjstd',
                                            'LogAttackTime',
                                            'HamoPk1',
                                            'HamoPk2',	
                                            'HamoPk3',
                                            'HamoPk4',
                                            'HamoPk5',
                                            'HamoPk6',
                                            'HamoPk7',
                                            'HamoPk8',
                                            'HamoPk9',
                                            'HamoPk10',
                                            'HamoPk11',	
                                            'struck',
                                            'string',
                                            'blown',
                                            'chordophone',	
                                            'aerophone',
                                            'chrd_composite',	
                                            'chrd_simple',
                                            'aero_lip-vibrated',
                                            'aero_lip-valved',	
                                            'aero_side',	
                                            'aero_single-reed',
                                            'aero_double-reed',
                                            'aero_free-reed',
                                            instrument]])



    print instrument_df_Format.keys() 
    instrument_df_Format.to_csv(  '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/PT4/InstrumentListData/' + instrument + 'Data.csv',index = False)


#seperating all instruments by playmethod 
playmethodList = ['struck','string','blown']

for playmethod in playmethodList:
    print(playmethod)
    dfplaymethod = df.loc[(df[playmethod] == 'yes')]
    dfplaymethod.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/PT4/Playmethod/' + playmethod + 'Data.csv',index = False
  )
#Seperating all instruments by class 1
class1List = ['chordophone','aerophone']

for class1 in class1List:
    print(class1)
    dfclass1 = df.loc[(df[class1] == 'yes')]
    dfclass1.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/PT4/Class1/' + class1 + 'Data.csv',index = False
  )
#seperating all instruments by class 2
class2List = ['chrd_composite'
                ,'chrd_simple'
                ,'aero_lip-vibrated'
                ,'aero_lip-valved'
                ,'aero_side'
                ,'aero_single-reed'
                ,'aero_double-reed'
                ,'aero_free-reed']

for class2 in class2List:
    print(class2)
    dfclass2 = df.loc[(df[class2] == 'yes')]
    dfclass2.to_csv(
   '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/PT4/Class2/' + class2 + 'Data.csv',index = False
  )                