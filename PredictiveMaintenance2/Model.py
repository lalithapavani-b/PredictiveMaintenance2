# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Library Notebooks/04_Model.ipynb.

# %% auto 0
__all__ = ['train_test_split', 'build_test_train']

# %% ../nbs/Library Notebooks/04_Model.ipynb 4
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

# %% ../nbs/Library Notebooks/04_Model.ipynb 5
def train_test_split(dataset_df : pd.DataFrame, # Pandas DataFrame object of dataset
                     machine_Unique_Identifer :str, # a unique ID to identify machine
                     failure : str, # event of failute, failure = 0 means not failed yet, failure=1 means equipment is failed
                    ):
    try:
        # get unique machine ID s
        split_df = dataset_df[[machine_Unique_Identifer]]
        
        
        # Create a new variable with a random number between 0 and 1
        np.random.seed(42)
        split_df['temp'] = (np.random.randint(0, 10000, pd_id.shape[0]))/10000
        split_df = split_df[[machine_Unique_Identifer,'temp']]
        
        
        # Give each record 30% chance of being validation, 35% chance of being in testing, 
        # and 35% chance of being in the training data set.
        split_df['MODELING_GROUP'] = np.where(((split_df.temp <= 0.35)), 'TRAINING', np.where(((split_df.temp <= 0.65)), 'VALIDATION', 'TESTING'))
        
        
        # number of machines under each category
        machines_per_category = split_df.groupby(['MODELING_GROUP'])['temp'].count()
        print(f"Number of machines in each group \n{machines_per_category}\n")
        
        #Append the Group of each id to each individual record.
        dataset_df = dataset_df.sort_values(by=['ID'], ascending=[True])
        split_df =split_df.sort_values(by=['ID'], ascending=[True])
        
        dataset_df = dataset_df.merge(split_df, on=['ID'], how='inner')
        
        # number of records under each category
        records_per_category = dataset_df.groupby(['MODELING_GROUP'])['temp'].count()
        print(f"Number of record in each group \n{machines_per_category}\n")
        
        
        # number of failure targets under each category
        failures_in_category = dataset_df.groupby(['MODELING_GROUP'])[failure].count()
        print(f"Number of record in each group \n{failures_in_category}\n")
        
        # create seperate dataframes for training,testing and validation data
        
        
        
    except Exception as e:
        print(e)
        return None
    
    else:
        pass

# %% ../nbs/Library Notebooks/04_Model.ipynb 6
def build_test_train(dataset_df : pd.DataFrame, # Pandas DataFrame object of dataset
                     test_part:float # split criteria
                    ):
    try:
        N =  dataset_df.shape[0]
        num = range(N)
        index_train, index_test = train_test_split(num,test_size=test_part,random_state=42)
        data_train = dataset_df.loc[index_train].reset_index( drop = True )
        data_test  = dataset_df.loc[index_test].reset_index( drop = True )

        # Creating the X, T and E inputs
        X_train, X_test = data_train[features], data_test[features]
        T_train, T_test = data_train[rul_time], data_test[rul_time]
        E_train, E_test = data_train[failure_event], data_test[failure_event]
        
    except Exception as e:
        print(e)
        return None
    
    else:
        return X_train,T_train,E_train,X_test,T_test,E_test
