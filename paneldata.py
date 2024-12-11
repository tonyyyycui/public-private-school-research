import pandas as pd
import matplotlib.pyplot as plt
from linearmodels.panel import PanelOLS


# Load datasets
path_0003 = 'data/income_2005-9.csv'
data_0003 = pd.read_csv(path_0003)

path_0004 = 'data/ed_2005-9.csv'
data_0004 = pd.read_csv(path_0004)

path_0005 = 'data/ed_2010-14-0006_ds207_20145_county.csv'
data_0005 = pd.read_csv(path_0005)

path_0006 = 'data/income_2010-14-20145_county_E.csv'
data_0006 = pd.read_csv(path_0006)

path_0007 = 'data/income_2015-19-20195_county_E.csv'
data_0007 = pd.read_csv(path_0007)

path_0008 = 'data/income_2015-19-20195_county_E.csv'
data_0008 = pd.read_csv(path_0008)

path_0009 = 'data/ed_2015-19-_2015-19-20195_county_E.csv'
data_0009 = pd.read_csv(path_0009)




# Simplify column names for consistency
data_0003.columns = [col.strip().lower().replace(' ', '_') for col in data_0003.columns]
data_0004.columns = [col.strip().lower().replace(' ', '_') for col in data_0004.columns]
data_0005.columns = [col.strip().lower().replace(' ', '_') for col in data_0005.columns]
data_0006.columns = [col.strip().lower().replace(' ', '_') for col in data_0006.columns]

data_0007.columns = [col.strip().lower().replace(' ', '_') for col in data_0007.columns]
data_0008.columns = [col.strip().lower().replace(' ', '_') for col in data_0008.columns]
data_0009.columns = [col.strip().lower().replace(' ', '_') for col in data_0009.columns]

# Remove empty columns
data_0003.dropna(axis=1, how='all', inplace=True)
data_0004.dropna(axis=1, how='all', inplace=True)
data_0005.dropna(axis=1, how='all', inplace=True)
data_0006.dropna(axis=1, how='all', inplace=True)

data_0007.dropna(axis=1, how='all', inplace=True)
data_0008.dropna(axis=1, how='all', inplace=True)
data_0009.dropna(axis=1, how='all', inplace=True)



# Ensure county and state names are clean for joining
data_0003['county'] = data_0003['county'].str.strip().str.lower()
data_0003['state'] = data_0003['state'].str.strip().str.lower()

data_0004['county'] = data_0004['county'].str.strip().str.lower()
data_0004['state'] = data_0004['state'].str.strip().str.lower()

data_0005['county'] = data_0005['county'].str.strip().str.lower()
data_0005['state'] = data_0005['state'].str.strip().str.lower()

data_0006['county'] = data_0006['county'].str.strip().str.lower()
data_0006['state'] = data_0006['state'].str.strip().str.lower()

data_0007['county'] = data_0007['county'].str.strip().str.lower()
data_0007['state'] = data_0007['state'].str.strip().str.lower()

data_0008['county'] = data_0008['county'].str.strip().str.lower()
data_0008['state'] = data_0008['state'].str.strip().str.lower()


data_0009['county'] = data_0009['county'].str.strip().str.lower()
data_0009['state'] = data_0009['state'].str.strip().str.lower()


# Southern states list
southern_states = ['alabama', 'arkansas', 'florida', 'georgia', 'kentucky', 'louisiana', 'misssissippi', 'north carolina', 'oklahoma', 'south carolina', 'tennessee', 'texas', 'virginia', 'west virginia']
# Merge on county and state
merged_data = pd.merge(data_0004, data_0003[['county', 'state', 'rnhe001']], on=['county', 'state'], how='inner')

# Rename median income column for clarity
merged_data.rename(columns={'rnhe001': 'median_income'}, inplace=True)

# Aggregate private and public school enrollments
merged_data['private_school_enrollment'] = (
    merged_data[['rmxe006', 'rmxe030', 'rmxe012', 'rmxe036', 'rmxe018', 'rmxe042']].sum(axis=1)
)
merged_data['public_school_enrollment'] = (
    merged_data[['rmxe005', 'rmxe029', 'rmxe011', 'rmxe035', 'rmxe017', 'rmxe041']].sum(axis=1)
)

# Calculate private to public enrollment ratio
merged_data['private_to_public_ratio'] = (
    merged_data['private_school_enrollment'] / merged_data['public_school_enrollment']
)


# ------------------Merge on county and state------------------------
merged_data2 = pd.merge(data_0005, data_0006[['county', 'state', 'abdpe001']], on=['county', 'state'], how='inner')

# Rename median income column for clarity
merged_data2.rename(columns={'abdpe001': 'median_income'}, inplace=True)

# Aggregate private and public school enrollments
merged_data2['private_school_enrollment'] = (
    merged_data2[['abrke012', 'abrke040']].sum(axis=1)
)
merged_data2['public_school_enrollment'] = (
    merged_data2[['abrke031', 'abrke030']].sum(axis=1)
)

# Calculate private to public enrollment ratio
merged_data2['private_to_public_ratio'] = (
    merged_data2['private_school_enrollment'] / merged_data2['public_school_enrollment']
)




# ------------------Merge on county and state------------------------
merged_data3 = pd.merge(data_0009, data_0008[['county', 'state', 'alw1e001']], on=['county', 'state'], how='inner')


# Rename median income column for clarity
merged_data3.rename(columns={'alw1e001': 'median_income'}, inplace=True)

# Aggregate private and public school enrollments
merged_data3['private_school_enrollment'] = (
    merged_data3[['amaxe040', 'amaxe012']].sum(axis=1)
)
merged_data3['public_school_enrollment'] = (
    merged_data3[['amaxe003', 'amaxe031']].sum(axis=1)
)

# Calculate private to public enrollment ratio
merged_data3['private_to_public_ratio'] = (
    merged_data3['private_school_enrollment'] / merged_data3['public_school_enrollment']
)

# Filter data for Southern states
southern_data = merged_data[merged_data['state'].isin(southern_states)]

southern_data2 = merged_data2[merged_data2['state'].isin(southern_states)]

southern_data3 = merged_data3[merged_data3['state'].isin(southern_states)]



# Print the number of observations
print(f"Number of observations in all data: {len(merged_data)}")
print(f"Number of observations in Southern states: {len(southern_data)}")

print(f"Number of observations in second data: {len(merged_data2)}")

print(f"Number of observations in third data: {len(merged_data3)}")


# Plot the filtered data (Southern states)
plt.figure(figsize=(10, 6))
plt.scatter(southern_data['private_to_public_ratio'], southern_data['median_income'], alpha=0.5, label='Southern States')

# plt.scatter(southern_data2['private_to_public_ratio'], southern_data2['median_income'], alpha=0.5, label='Southern States 2')


plt.title('Private to Public School Enrollment Ratio vs Median Income (Southern States)')
plt.ylabel('Median Income ($)')
plt.xlabel('Private/Public Enrollment Ratio')
plt.text(0.45, -0.2, 'Figure 1.1', transform=plt.gca().transAxes, fontsize=12, fontweight='bold')

plt.grid(True)
plt.legend()
# plt.show()


import pandas as pd
from linearmodels import PanelOLS

# Assuming you already have merged_data, merged_data2, and merged_data3
# Concatenate the datasets
southern_data['time'] = 2005
southern_data2['time'] = 2010
southern_data3['time'] = 2015

# Concatenate all data into one panel dataset
panel_data = pd.concat([southern_data, southern_data2, southern_data3], ignore_index=True)

# Check for missing values before processing
print(panel_data.isna().sum())  # Total missing values per column
print(panel_data.isna().mean())  # Proportion of missing values per column

# Clean and preprocess the data
panel_data.replace([float('inf'), float('-inf')], float('nan'), inplace=True)

# Fill missing values for columns before dropping rows
panel_data['private_to_public_ratio'].fillna(panel_data['private_to_public_ratio'].mean(), inplace=True)
panel_data['median_income'].fillna(panel_data['median_income'].mean(), inplace=True)

# Drop rows with NaN values in key columns
panel_data.dropna(subset=['private_to_public_ratio', 'median_income'], inplace=True)

# Take a random sample of 10% of the data
# sampled_data = panel_data.sample(frac=0.1, random_state=42)

# Ensure sampled data has a multi-index for panel regression
panel_data.set_index(['county', 'time'], inplace=True)

# Check the cleaned data
print(panel_data[['private_to_public_ratio', 'median_income']].isna().sum())
print(panel_data[['private_to_public_ratio', 'median_income']].head())

# Panel OLS with fixed effects
model = PanelOLS.from_formula('median_income ~ private_to_public_ratio + EntityEffects + TimeEffects', data=panel_data)

# Fit and summarize the model, using check_rank=False if needed
results = model.fit()
print(results.summary)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'panel_data' is the data you have after merging and cleaning

# Calculate the differences for each county across time
panel_data['median_income_diff'] = panel_data.groupby('county')['median_income'].diff()
panel_data['private_to_public_diff'] = panel_data.groupby('county')['private_to_public_ratio'].diff()

# Drop NaN values caused by the diff() operation (first time period will have NaN)
panel_data.dropna(subset=['median_income_diff', 'private_to_public_diff'], inplace=True)

# Plot the boxplot for differences in 'median_income' and 'private_to_public_ratio'
plt.figure(figsize=(12, 6))

# Boxplot for Median Income differences
plt.subplot(1, 2, 1)
sns.boxplot(data=panel_data, y='median_income_diff')
plt.title('Box Plot of Median Income Differences Across Time')
plt.ylabel('Difference in Median Income')
plt.grid(True)

# Boxplot for Private to Public Ratio differences
plt.subplot(1, 2, 2)
sns.boxplot(data=panel_data, y='private_to_public_diff')
plt.title('Box Plot of Private to Public Ratio Differences Across Time')
plt.ylabel('Difference in Private to Public Ratio')
plt.grid(True)

plt.tight_layout()
plt.show()
