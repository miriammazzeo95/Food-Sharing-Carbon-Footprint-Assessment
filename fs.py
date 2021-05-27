# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:58:13 2021

@author: Miriam
"""
import pandas as pd
import numpy as np
import inflection as inf
# import recordlinkage
# import pandas_dedupe
# import unidecode
# import re
# import string
# import random
from spellchecker import SpellChecker
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


##############################################################################
############################# USEFUL CODE #################################
##############################################################################

# def checker(wrong_options,correct_options):
#     names_array=[]
#     ratio_array=[]    
#     for wrong_option in wrong_options:
#         if wrong_option in correct_options:
#            names_array.append(wrong_option)
#            ratio_array.append('100')
#         else:   
#             x=process.extractOne(wrong_option,correct_options,scorer=fuzz.token_set_ratio)
#             names_array.append(x[0])
#             ratio_array.append(x[1])
#             return names_array,ratio_array
        
        
##find those words that may be misspelled
# misspelled = spell.unknown(['aple', 'meat', 'beans'])
# for word in misspelled:
#     # Get the one `most likely` answer
#     print(spell.correction(word))

#     # Get a list of `likely` options
#     print(spell.candidates(word))

####Dropping a df raw
# df_reg[~df_reg.productName.astype(str).str.isdigit()]
# df_reg=df_reg.drop([4137,4608,4610,4612])

####Listing attempts
# foodtype = df_reg['productName']
# foodtype_l = foodtype.values.tolist() 
# for i in range(len(foodtype_l)):
# #     # Get the one `most likely` answer
# #     print(spell.correction(word))
#     foodtype_l[i]=foodtype_l[i].split()

####Python String Methods
# DTUfood=DTUfood[DTUfood['Name'].apply(lambda x: str(x).isalpha())]

# import difflib 
# difflib.get_close_matches
# df3 = df2.Product.map(lambda x: difflib.get_close_matches(x, df1)[0])

##############################################################################
######################## CREATION OF FOOD CATALOG #################################
##############################################################################

# filename = "DTUfood_eng.xlsx"
# DTUfood = pd.read_excel(
#   filename,
#   sheet_name='catalog',
#   header=1,
#   index_col=0,
#    sep = ';',
#   # usecols=["text"],
#   # na_filter = False,
#     encoding ="ISO-8859-1"
#     )

# DTUfood=DTUfood.reset_index(drop=True)
# DTUfood= DTUfood.iloc[:, 0:2]
    
# DTUfood.drop(DTUfood[DTUfood['Name'].apply(lambda x: str(x).isnumeric())].index, inplace=True)
# DTUfood=DTUfood.reset_index(drop=True)

# for i in range(len(DTUfood.Name)):
#     DTUfood.Name[i] = DTUfood.Name[i].split()[0].replace(",", "")

# ###convert colum to lowrcases
# DTUfood['Name']=DTUfood['Name'].str.lower()
# DTUfood['Group']=DTUfood['Group'].str.lower()

# DTUfood= DTUfood.sort_values(by='Name')
# DTUfood=DTUfood.reset_index(drop=True)


# ##### Cleaning of Groups Names
# groups =  DTUfood.Group.unique()
# groups.sort()

# match="vegetable"
# DTUfood=DTUfood.replace(DTUfood.Group[DTUfood['Group'].str.contains(match)].to_numpy(),'vegetables')
# match="vegetables"
# DTUfood=DTUfood.replace(DTUfood.Group[DTUfood['Group'].str.contains(match)].to_numpy(),'vegetables')

# match="fruit"
# DTUfood=DTUfood.replace(DTUfood.Group[DTUfood['Group'].str.contains(match)].to_numpy(),'fruit')

# match="cheese"
# DTUfood=DTUfood.replace(DTUfood.Group[DTUfood['Group'].str.contains(match)].to_numpy(),match)

# #### Delete identical raws
# DTUfood.drop_duplicates(keep=False,inplace=True)

##############################################################################
######################### CLEANING REGISTRATION DATA ##################################
##############################################################################

# filename = "food.xlsx"
# raw_data = pd.read_excel(
#   filename,
#     sep = ';',
#   header="infer",
#   index_col= None,
#   # usecols=["text"],
#   # na_filter = False,
#     encoding ="ISO-8859-1"
#     )


# df_reg= raw_data.copy()
# ###convert colum to lowrcases
# df_reg['productName']=df_reg['productName'].str.lower()


# misspelled=[]
# spell = SpellChecker()

###delete non string values
# for i in range(len(df_reg.productName)):
#     if type(df_reg.productName[i]) != str:
#         df_reg.drop(i,inplace=True)
#         i+=1
#     df_reg.reset_index(drop=True)
    
#     ##spell correction
#     words= df_reg.productName[i].split()
#     misspelled = spell.unknown(words)
#     for word in misspelled:
#             corrected=spell.correction(word)
#             idx= words.index(word)
#             words[idx]=corrected
#             df_reg['productName'][i]=' '.join(words)


## Save new dataframe in Excel sheet
# df_reg.to_excel('df_reg.xlsx', index = None)




##############################################################################
################################ READING DATA #################################
##############################################################################
spellcheck = False


if spellcheck == True:
    filename = "df_reg_spellcheck.xlsx"
    df_reg = pd.read_excel(
      filename,
       sep = ';',
      header="infer",
      index_col= None,
      # usecols=["text"],
      # na_filter = False,
        # encoding ="ISO-8859-1"
        )

else:
    filename = "df_reg.xlsx"
    df_reg = pd.read_excel(
      filename,
       sep = ';',
      header="infer",
      index_col= None,
      # usecols=["text"],
      # na_filter = False,
        # encoding ="ISO-8859-1"
        )
        
#Singularize words
df_reg['productName'] = df_reg['productName'].apply(lambda x: ' '.join([inf.singularize(item) for item in x.split()]))

#adjust values that are too high
# df_reg.loc[(df_reg['Total Kg'] >30), 'Total Kg']=df_reg.loc[(df_reg['Total Kg'] >30), 'Total Kg']/100




###############################################################################
############################# CO2 DATA ########################################
##############################################################################

# filename = "BASE_calculation2.xlsx"
# basecalc = pd.read_excel(
#   filename,
#   sheet_name='Summary DISCOUNTED',
#   header=[0,1,2,3,4],
#   index_col=None,
#    sep = ';',
#   # usecols=["text"],
#  # na_filter = True,
#     encoding ="ISO-8859-1"
#     )

# co2base = pd.concat([basecalc.iloc[:,:5], basecalc.iloc[:,41:49].copy()], axis=1)

# co2base=co2base.dropna(how='all')
# co2base=co2base.fillna(0)
# # group=co2base.iloc[0:4]
# # co2base = co2base.iloc[4:,:] 


# filename = "dataS2.xlsx"
# co2s2 = pd.read_excel(
#   filename,
#   sheet_name='Results - Retail Weight',
#   header=[0,1,2],
#   index_col=None,
#    sep = ';',
#   # usecols=["text"],
#  # na_filter = True,
#     encoding ="ISO-8859-1"
#     )
# co2s2 = co2s2.dropna(how='all')




filename = "co2calculator.xlsx"
co2calculator = pd.read_excel(
  filename,
  sheet_name='global',
  header=0,
  index_col=None,
   sep = ';',
  # usecols=["text"],
 # na_filter = True,
    encoding ="ISO-8859-1"
    )
# co2calculator=co2calculator.dropna(how='all')
co2calculator=co2calculator.where(co2calculator.notnull(), 'n')

# co2calculator.assign(Right="")

# df_reg['newcol']=""


# a=df_reg.merge(co2calculator, left_on = df_reg.productName.str.extract('(\d+)', expand = False), right_on = co2calculator.Product.str.extract('(\d+)', expand = False), how = 'inner').rename(columns = {'Address_y': 'Right_Address'})

# df1 = df_reg.copy()
# df2 = co2calculator.copy()
# #initiate matching
# df_final = pandas_dedupe.link_dataframes(df1, df2, ['Name'])
# # reset index
# df_final = df_final.reset_index(drop=True)


# df1 = df_reg.copy()
# df2 = co2calculator.copy()
# indexer = recordlinkage.Index()
 #using url as intersection
# indexer = indexer.block('id')
# candidate_links = indexer.index(df1, df2)
# c = recordlinkage.Compare()


##########decapitalize
#find rows matching word 
#create empty columns
#add values to empty colums

df_co2 = df_reg.productName.copy()
df_co2=df_co2.to_frame(name=None)
co2calculator.Product = co2calculator.Product.str.lower()
co2calculator.Product2 = co2calculator.Product2.str.lower()
co2calculator.Group = co2calculator.Group.str.lower()
co2calculator['Sub-group'] = co2calculator['Sub-group'].str.lower()

# df2[df2['Product'].str.contains('Apple')]

df_co2['Class'] = ""
df_co2['Group'] = ""
df_co2['Sub-group'] = ""
df_co2['kgCO2e Carbon Opportunity Cost per tot fresh weight [Kg]'] = ""
df_co2['kgCO2e Carbon Opportunity Cost per tot retail weight [Kg]'] = ""


food=[]
fuzzymatch=[]
match=[]
l=[]
for i in range(len(df_co2.productName)):
    food = df_co2.productName[i]
    match=co2calculator[co2calculator['Product'].str.contains(fr'\b{food}\b', regex=True)].reset_index(drop=True)
    if match.empty == True:
        match=co2calculator[co2calculator['Product2'].str.contains(fr'\b{food}\b', regex=True)].reset_index(drop=True)
   
    if match.empty == True:
        match=co2calculator[co2calculator['Product'].str.contains(r'\b{}\b'.format('|'.join(food.split())))].reset_index(drop=True)
         
    if match.empty == True:
        match=co2calculator[co2calculator['Product2'].str.contains(r'\b{}\b'.format('|'.join(food.split())))].reset_index(drop=True)
         
    if match.empty == True:
        # print('product: ' + food)
        df_co2.iloc[i,1:]= list([0,0,0,0,0])
        fuzzymatch=process.extractOne(food, co2calculator.Product.values.tolist())
        if fuzzymatch[1]> 70:
             match=co2calculator[co2calculator['Product'].str.contains(fuzzymatch[0])].reset_index(drop=True)
             l= pd.concat([match.Product.reset_index(drop=True), match.iloc[:,2:].reset_index(drop=True)], axis=1)
             l=l.loc[0]
             df_co2.iloc[i,1:]= l.values.tolist()
    if match.empty == True:
       # print('product: ' + food)
       df_co2.iloc[i,1:]= list([0,0,0,0,0])
       fuzzymatch=process.extractOne(food, co2calculator.Product2.values.tolist())
       if fuzzymatch[1]> 60:
            match=co2calculator[co2calculator['Product2'].str.contains(fuzzymatch[0])].reset_index(drop=True)
            l= pd.concat([match.Product.reset_index(drop=True), match.iloc[:,2:].reset_index(drop=True)], axis=1)
            l=l.loc[0]
            df_co2.iloc[i,1:]= l.values.tolist()
    else:
          
        l= pd.concat([match.Product.reset_index(drop=True), match.iloc[:,2:].reset_index(drop=True)], axis=1)
        l=l.loc[0]
        df_co2.iloc[i,1:]= l.values.tolist()
        
        
#####    other not-successful trials    
# for index, row in co2calculator.iterrows():
#     # if fuzz.partial_ratio(food, row[0])>70:
#       if fuzz.token_sort_ratio(food, row[0])>70:  
#           print(row[0])
#           df_co2.iloc[i,1:]= row[1:].values.tolist()

             

df_co2['Date'] = pd.Series(df_reg['Date'])
df_co2['Tot Kg'] = pd.Series(df_reg['Tot Kg corrected'])
df_co2['kgCO2e Carbon Opportunity Cost per tot fresh weight [Kg]'] = pd.Series(df_co2.iloc[:,4]*df_co2.iloc[:,7])
df_co2['kgCO2e Carbon Opportunity Cost per tot retail weight [Kg]'] = pd.Series(df_co2.iloc[:,5]*df_co2.iloc[:,7])

filename = "food per shop.xlsx"
shoplist = pd.read_excel(
  filename,
  sheet_name='list',
  header=0,
  index_col=None,
   sep = ';',
  # usecols=["text"],
 # na_filter = True,
    encoding ="ISO-8859-1"
    )


df1 = df_reg.shop.copy()
df1=df1.to_frame(name=None)
df1.shop = df1.shop.str.lower()
shoplist.SHOP = shoplist.SHOP.str.lower()



entry=[]
for i in range(len(df1)):
    entry = df1.shop[i]
    match= shoplist[shoplist['SHOP'].str.contains('|'.join(entry.split()))].reset_index(drop=True)
    if match.empty == False:
        l= match.iloc[0,:].reset_index(drop=True)
        df1.iloc[i,:]= l.values.tolist()
    
    else:
        # print('product: ' + food)
        df1.iloc[i,:]= 0
        fuzzymatch=process.extractOne(entry, shoplist.SHOP.values.tolist())
        if fuzzymatch[1]> 55:
             match=shoplist[shoplist['SHOP'].str.contains(fuzzymatch[0])].reset_index(drop=True)
             l= match.iloc[0,:].reset_index(drop=True)
             df1.iloc[i,:]= l.values.tolist()
            
food_notcount=df_co2[df_co2.Group==0]
food_notcount= food_notcount.productName


df_co2['Shops'] = pd.Series(df1['shop'])

##wrong attemps
### df_co2[df_co2.Group==0].iloc[:,1]=pd.Series(['other']*48)
### df_co2[df_co2.Group==0]['Group']='other'

df_co2.loc[df_co2.Group==0, 'Group']='other'
df_co2.loc[df_co2['Sub-group']==0, 'Sub-group']='other'

####Save new dataframe in Excel sheet
df_co2.to_excel('df_co2.xlsx', index = None)

shop_notcount_idx=df_co2[df_co2.Shops==0].index
shop_notcount= df_reg.shop[shop_notcount_idx]





