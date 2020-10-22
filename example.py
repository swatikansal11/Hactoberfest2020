import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\HP\Desktop\Matter\python\machinelearning\House_Price.csv', header=0)
pd.set_option('display.expand_frame_repr', False)
print(df.head())
print(df.shape)
print(df.describe())
"""
print(sns.jointplot(x='n_hot_rooms',y='price',data=df))
plt.show()
print(sns.jointplot(x='rainfall',y='price',data=df))
plt.show()
print(df.head())
print(sns.countplot(x='airport',data=df))
plt.show()
print(sns.countplot(x='waterbody',data=df))
plt.show()
print(sns.countplot(x='bus_ter',data=df))
plt.show()
#Missing values in n_hos_beds
#Skewness or outliers in crime_rate
#Outliers in n_hot_rooms and rainfall
#Bus_ter has only one value
print(df.info())
print(np.percentile(df.n_hot_rooms,[99]))
print(np.percentile(df.n_hot_rooms,[99])[0])
uv=np.percentile(df.n_hot_rooms,[99])[0]
print(df[(df.n_hot_rooms>uv)])
print(df.n_hot_rooms[(df.n_hot_rooms> 3*uv)])
t=df.n_hot_rooms[(df.n_hot_rooms> 3*uv)]=3*uv
print(t)
print(df[(df.n_hot_rooms>uv)])
print(np.percentile(df.rainfall,[1])[0])
lv=np.percentile(df.rainfall,[1])[0]
da=df[(df.rainfall<lv)]
print(da)
df.rainfall[(df.rainfall< 0.3*lv)]=0.3*lv
dte=df[df.rainfall<lv]
print(dte)
print(sns.jointplot(x="crime_rate",y="price",data=df))
plt.show()
print(df.describe())

print(df.info())
df.n_hos_beds=df.n_hos_beds.fillna(df.n_hos_beds.mean())
print(df.info())
"""
print(sns.jointplot(x="crime_rate",y="price",data=df))
plt.show()
df.crime_rate=np.log(1+df.crime_rate)
print(sns.jointplot(x="crime_rate",y="price",data=df))
plt.show()
df['avg_dist']=(df.dist1+df.dist2+df.dist3+df.dist4)/4
print(df.describe())
del df['dist1']
print(df.describe())
del df['dist2']
del df['dist3']
del df['dist4']
print(df.describe())
del df['bus_ter']
print(df.head())