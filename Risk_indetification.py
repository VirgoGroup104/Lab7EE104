# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:54:08 2022

#Quang Khai Le 
"""

# Factor Analysis package
import pandas as pd

# Read the source file
risk = pd.read_csv("ratings.csv")
# Calculate the risk rating w/ own formula
risk['Total Rating']= risk['COMMEQTA']*0.4 + risk['LLPLOANS']*0.1 +risk['COSTTOINCOME']*0.05 +risk['ROE']*0.7 +risk['LIQASSTA']*0.65
risk['risk']=''
# Set the boundary of different risking level
risk.loc[risk['Total Rating']>0.2,['risk']]='low'
risk.loc[(risk['Total Rating']<=0.2) & (risk['Total Rating'] >= 0.12), ['risk']]='medium'
risk.loc[risk['Total Rating']<0.12,['risk']]='high'
# Save it to another csv file
# Add a new column for recommendation
risk['Recommendation'] = ''

# Set the boundary of different risking levels
risk.loc[risk['Total Rating'] > 0.2, ['Recommendation']] = 'APPROVED'
risk.loc[(risk['Total Rating'] <= 0.2) & (risk['Total Rating'] >= 0.12), ['Recommendation']] = 'CONDITIONAL APPROVED'
risk.loc[risk['Total Rating'] < 0.12, ['Recommendation']] = 'REJECT'
#save to file
risk.to_csv('ratings.csv')
