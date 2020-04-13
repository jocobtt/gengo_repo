import pandas as pd 
import seaborn as sns 
import os 
import numpy as np 

# read in airlines dataset from github
df = pd.read_table('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv',sep=',')

# list the unique airlines in our dataset 
df.airline.unique()

# get info for the dataset ie variable type etc. 
df.info()

# describe the count etc. of the dataset 
df.describe()

# list the value counts of each data type 
df.dtypes.value_counts()

# unique values of object 
df.select_dtypes('object').apply(lambda x: pd.Series.nunique(x))

# unique values of int types 
df.select_dtypes('int64').apply(lambda x: pd.Series.nunique(x))

# check for missing values 
def missing_vals_table(my_df):
    if my_df.isnull().sum().sum() > 0:
        miss_val = my_df.isnull().sum()
        miss_val_pct = 100 * miss_val / len(my_df)
        table = pd.concat([miss_val, miss_val_pct], axis=1)
        table = table[table.loc[:, table.columns[0]] != 0].sort_values(table.columns[0],
                                                                      ascending=False).round(3)
        table = table.rename(columns = {0: "missing values", 1: "% of Missing Values"})
        return table 
    else:
        return "there are no missing values"
missing_vals_table(df)

# find max fatal accidents for 00-14
df.fatal_accidents_00_14.max()

# find where incidents is greater than 4 
sns.countplot(df.loc[df.fatalities_00_14 > 4, 'fatalities_00_14'], palette = 'coolwarm')

# count plot of all fatalities for 00-14
sns.countplot(df['fatalities_00_14'], palette = 'coolwarm')

# barplot of fatalities by airline for 85-99 - only pull off top values for this viz 
sns.countplot(df.loc[df.fatalities_85_99 < 6, 'fatalities_85_99'])

# correlation heatmap
sns.heatmap(df.corr(method='pearson'))

# line plot of incidents for 00-14 and available seats per week
sns.lineplot(df.avail_seat_km_per_week, df.incidents_00_14)

# filter out higher fatality airlines 

# check histogram of fatalities overall to see where a good spot to filter them out would be 
sns.distplot(df.fatalities_00_14)

# split dataset where fatalities from 00-14 is greater than 200 
df_2 = df.loc[df.fatalities_00_14 > 200]


# bar plot of airlines by fatalities
sns.barplot(x=df_2.airline, y= df_2.fatalities_00_14)

# pairplot of the dataset 
sns.pairplot(df)

# pairplot of the correlation of the dataset
sns.pairplot(df.corr())
