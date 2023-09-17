import sqlite3
import pandas as pd
import os

def extract_data():
    current_file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(os.path.dirname(current_file_path))
    data_directory = os.path.join(parent_directory, 'data')

    cr_post_path = os.path.join(data_directory,'cruise_post.db')
    cr_pre_path = os.path.join(data_directory,'cruise_pre.db')


    cr_post_table = sqlite3.connect(cr_post_path)
    cr_pre_table = sqlite3.connect(cr_pre_path)

    query = "SELECT * FROM cruise_post"
    dfpost = pd.read_sql_query(query, cr_post_table)

    query = "SELECT * FROM cruise_pre"
    dfpre = pd.read_sql_query(query, cr_pre_table)

    dfpre.drop('index', axis=1, inplace=True)
    dfpost.drop('index', axis=1, inplace=True)

    common_columns = set(dfpre.columns) & set(dfpost.columns)

    df = pd.merge(dfpre, dfpost, on='Ext_Intcode', how='inner')

    return df

