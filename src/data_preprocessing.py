import numpy as np
import pandas as pd


def convert(entry):
    try:
        n = entry.split()
        if len(n) == 2:
            value, unit = float(n[0]), n[1].lower()
            if unit == 'km':
                return value
            elif unit == 'miles':
                return value * 1.60934
    except:
        return

def fill_mode(s):
    m = s.mode().iloc[0] if not s.mode().empty else None
    return s.fillna(m)


def pre_processing_data(df):

    df.drop('Ext_Intcode', axis=1, inplace=True)
    mapping = {'Not at all important': 1, 'A little important': 2, 'Somewhat important': 3,
               'Very important': 4, 'Extremely important': 5}
    cols = df.columns[df.isin(['Somewhat important']).any()].tolist()
    for i in cols:
        df[i] = df[i].replace(mapping)

    df.drop('Logging', axis=1, inplace=True)



    df['Gender'].fillna("na", inplace=True)

    df = pd.get_dummies(df, columns=['Gender'], prefix=['gender'], drop_first=True)
    df = pd.get_dummies(df, columns=['Source of Traffic'], prefix=['traffic'], drop_first=True)

    df[['traffic_Direct - Email Marketing',
        'gender_Male', 'traffic_Indirect - Search Engine',
        'traffic_Indirect - Social Media']] = df[['traffic_Direct - Email Marketing',
                                                  'gender_Male', 'traffic_Indirect - Search Engine',
                                                  'traffic_Indirect - Social Media']].astype(float)


    mapping2 = {'Deluxe': 3, 'Luxury': 2, 'Standard': 1}
    df['Ticket Type'] = df['Ticket Type'].replace(mapping2)



    df['Cruise Name'] = df['Cruise Name'].str.lower()
    df['Cruise Name'] = df['Cruise Name'].str.replace('blast0ise', 'blastoise')
    df['Cruise Name'] = df['Cruise Name'].str.replace(r'\bblast\b', 'blastoise', regex=True)
    df['Cruise Name'] = df['Cruise Name'].str.replace('iapras', 'lapras')
    df['Cruise Name'] = df['Cruise Name'].str.replace(r'\blap\b', 'lapras', regex=True)





    df['Cruise Distance'] = df['Cruise Distance'].apply(convert)

    df.loc[df['Cruise Distance'] < 0, 'Cruise Distance'] = np.nan
    means_cruisetype = df.groupby('Cruise Name')['Cruise Distance'].transform('mean')
    df['Cruise Distance'].fillna(means_cruisetype, inplace=True)

    df['Cruise Name'].fillna(0, inplace=True)
    mapping = {"lapras": 1.0, "blastoise": 2.0}
    df['Cruise Name'] = df['Cruise Name'].replace(mapping)

    avg_m = df['Cruise Distance'][df['Cruise Name'] == 0].mean()
    df['Cruise Distance'].fillna(avg_m, inplace=True)



    df['Ticket Type'] = df.groupby('Cruise Name')['Ticket Type'].transform(fill_mode)



    df0 = df.loc[df['Age'] < 122]

    avg = df0['Age'].mean()
    df['Age'] = df['Age'].apply(lambda x: avg if x > 122 else x)
    df['Age'].fillna(avg, inplace=True)


    df['WiFi'].fillna(2, inplace=True)
    df['Entertainment'].fillna(2, inplace=True)
    df = pd.get_dummies(df, columns=['WiFi'], prefix=['Wifi'], drop_first=True)
    df = pd.get_dummies(df, columns=['Entertainment'], prefix=['Entertainment'], drop_first=True)



    cols5 = df.columns[df.max() == 5]
    m = df[cols5].median()
    df[cols5] = df[cols5].fillna(m)

    df = pd.get_dummies(df, columns=['Cruise Name'], prefix=['Cruise_Name'], drop_first=True)

    return df
