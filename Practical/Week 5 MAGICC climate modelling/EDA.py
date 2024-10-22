import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

SSP5_85 = pd.read_csv('/Users/yangyangxiayule/Documents/GitHub/Environmental-Modelling/Practical/Week 5 MAGICC climate modelling/Practical/TEMPLATES/SSP5-8.5_templ.csv')
SSP1_19 = pd.read_csv('/Users/yangyangxiayule/Documents/GitHub/Environmental-Modelling/Practical/Week 5 MAGICC climate modelling/Practical/TEMPLATES/SSP1-1.9_templ.csv')

print(SSP5_85.columns.to_list())

joint_df = pd.concat([SSP5_85, SSP1_19])
joint_df.to_csv('/Users/yangyangxiayule/Documents/GitHub/Environmental-Modelling/Practical/Week 5 MAGICC climate modelling/Practical/joint_df.csv')

year_columns = ['2015', '2020', '2030', '2040', '2050', '2060', '2070', '2080', '2090', '2100']
df_melted = pd.melt(joint_df, id_vars=['model', 'region', 'scenario', 'unit', 'variable'], 
                    value_vars = year_columns, 
                    var_name = 'Year', 
                    value_name = 'Emissions')

df_melted['Year'] = df_melted['Year'].astype(int)

print(df_melted)
df_melted.to_csv('/Users/yangyangxiayule/Documents/GitHub/Environmental-Modelling/Practical/Week 5 MAGICC climate modelling/Practical/joint_melted_df.csv')

ssp119 = df_melted.query('scenario == "ssp119"')
ssp585 = df_melted.query('scenario == "ssp585"')


ssp119.to_csv('/Users/yangyangxiayule/Documents/GitHub/Environmental-Modelling/Practical/Week 5 MAGICC climate modelling/Practical/ssp119.csv')
ssp585.to_csv('/Users/yangyangxiayule/Documents/GitHub/Environmental-Modelling/Practical/Week 5 MAGICC climate modelling/Practical/ssp585.csv')

#EDA
sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))

sns.lineplot(data=ssp585, x='Year', y='Emissions', hue='variable')
sns.lineplot(data=ssp119, x='Year', y='Emissions', hue='variable', linestyle="--")

plt.title('Comparison of Emissions Trends: SSP5-8.5 vs SSP1-1.9', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Emissions', fontsize=12)
plt.legend(title='Gas Type')
plt.show()
plt.savefig('/Users/yangyangxiayule/Documents/GitHub/Environmental-Modelling/Practical/Week 5 MAGICC climate modelling/Practical/all_data.png')