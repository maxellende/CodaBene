# -*- coding: utf-8 -*-

"""
Created on Tue Nov  8 10:35:00 2022

@author: maxel
"""

import numpy as np
import pandas as pd


def main():
    
    retailer_extract = pd.read_csv('retailer extract.csv', sep = ';')
    references = pd.read_csv('references initialized in shop.csv', sep = ';')
    
    missing_ref(retailer_extract,references) # challenge 1
    
    rev_missing_ref = relevant_missing_ref(retailer_extract,references) # challenge 2
    
    tot = len(rev_missing_ref)
    print(' total size of the list of relevant but not tracked products : ', tot) # challenge 3
    
    aisle_suggestion(retailer_extract,references) # challenge 4
    
    
# challenge 1
def missing_ref(retailer_extract,references):
    
    reference_id = np.unique(references['reference_id'].str.replace(',','.').astype('float')) # product referenced
    ean = retailer_extract.dropna(how = 'all')[retailer_extract['Stock en quantité'].str.replace(',','.').astype('float')> 0]['EAN'].astype('float') # products in shop 
    nb = sum(~np.isin(ean,reference_id)) # number of products in shop but not tracked

    print(' total number of references not tracked in the app but present in the shop assortment : ', nb) # number of product in shop - number of product referenced


# challenge 2
def relevant_missing_ref(retailer_extract,references):
   
    df = retailer_extract.dropna(how = 'all')[retailer_extract['Stock en quantité'].str.replace(',','').astype('float')> 0] # present in shop
   
    df = df.iloc[~np.isin(df['EAN'].astype('float'),references['reference_id'].str.replace(',','').astype('float'))] # not tracked
   
    df = df.loc[pd.isnull(df['Date déréf.'])] # It is not “dereferenced”
    
    
    for i in range(len(df)) : 
        sub_fam = df['Libellé  Sous-Famille '].iloc[i]
        ean = df.loc[df['Libellé  Sous-Famille ']==sub_fam]
        if np.isin(ean,references['reference_id']).any() :  # The sub family is tracked in at least one aisle in the shop : there exists one product of this sub-family tracked in the shop
            continue
        else : 
            df.drop(df.index[i]) 
        
    print('list (EAN and Reference Name) of products which are not tracked by the app, but are relevant : \n',df['EAN'])
    return df['EAN']


    
# challenge 3
def relevant_missing_ref_total(retailer_extract,references):
    missing_ref = relevant_missing_ref(retailer_extract,references)
    tot = len(missing_ref)
    print(' total size of the list of relevant but not tracked products : ', tot)
    
# challenge 4
def aisle_suggestion(retailer_extract,references) : 
    
    h = hashtable(retailer_extract,references)
    
    missing_ref = relevant_missing_ref(retailer_extract,references).astype('float')
    m_df = retailer_extract.dropna(how = 'all')
    m_df = m_df.iloc[np.isin(retailer_extract['EAN'].astype('float'), missing_ref)]
    m_df = pd.DataFrame(columns = retailer_extract.columns)
    m_h = pd.DataFrame()
    m_h['reference'] = missing_ref
    m_h['Code Groupe de Famille '] = m_df['Code Groupe de Famille ']
    m_h['Code Famille '] = m_df['Code Famille ']
    m_h['Code Sous-Famille '] = m_df['Code Sous-Famille ']
    m_allee = []
    for i in range(len(missing_ref)):
        m_allee.append(h[m_h['Code Groupe de Famille ', 'Code Famille ', 'Code Sous-Famille ']==h['Code Groupe de Famille ', 'Code Famille ', 'Code Sous-Famille '].iloc[i]]['allee'])
    m_h['allee'] = m_allee
    print('suggestion of an aisle where the reference could be found : \n', m_h['reference', 'allee'])
    
def hashtable(retailer_extract,references):
    df = retailer_extract.dropna(how = 'all')
    known_ref = references['reference_id'].str.replace(',','').astype('float')
    df = df[np.isin(retailer_extract['EAN'].astype('float') == known_ref.iloc)]
    h = pd.DataFrame() # hashtable
    h['Code Groupe de Famille '] = df['Code Groupe de Famille ']
    h['Code Famille '] = df['Code Famille ']
    h['Code Sous-Famille '] = df['Code Sous-Famille ']
    h['allee'] = references['allee']
    return h

if __name__ == "__main__":
    main()