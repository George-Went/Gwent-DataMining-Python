#!/usr/bin/python


import pandas as pd 
import numpy as np


#Array of instruments 
instrumentList = ['Cello'
                ,'Piano' 
                ,'DoubleBass'
                ,'AcousticBass'
                ,'SynthBass'
                ,'Viola'
                ,'Violin'
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

#Read Test instrument data
testInstrument = pd.read_csv(
    '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/PT4/testInstrumentsBinary.csv'
    )

print instrumentList

for instrument in instrumentList:
    print("Reading: " + instrument)
    # Grabs instrments preictions results 
    prediction_df = pd.read_csv(
    '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/PredictionOutputs/J48/' + instrument + 'Predictions.csv'
    )

    print prediction_df 
    
    #formats the predicted and prediction columns and 
    # places results into testInstruments file
    testInstrument[instrument] = np.where((prediction_df['predicted'] == '2:yes'),'yes','no')
    testInstrument[instrument + '_accuracy'] = prediction_df['prediction']
    
    print testInstrument.loc[:,[instrument,instrument + '_accuracy']]


  
print testInstrument 

print testInstrument.loc[:,[
                'Cello_accuracy'
                ,'Piano_accuracy' 
                ,'DoubleBass_accuracy'
                ,'AcousticBass_accuracy'
                ,'SynthBass_accuracy'
                ,'Viola_accuracy'
                ,'Violin_accuracy'
                ,'Trumpet_accuracy'
                ,'Clarinet_accuracy'
                ,'Piccalo_accuracy'
                ,'Flute_accuracy'
                ,'Oboe_accuracy'
                ,'Bassoon_accuracy'
                ,'EnglishHorn_accuracy'
                ,'FrenchHorn_accuracy'
                ,'Trombone_accuracy'
                ,'Tuba_accuracy'
                ,'Saxophone_accuracy'
                ,'Accordian_accuracy'
                ]]

testInstrument.to_csv(
        '/home/george//Programs/WEKA/weka-3-8-3/data/assignmentData/PT4/testInstrumentsPredictions.csv'
    )


  


