#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
#với mức ý nghĩa 5%
#%%
#Giữa giá nhà và diện tích có tương quan với nhau?
df = pd.read_csv('house_price_Dống-Da_Hà-Nội_subdata.csv')
df.info()
#%%
df
# %%
df_1 = df[['area','price']]
df_1 = df_1.dropna()
df_1.sort_values(by=['area'])
df_1
#%%
plt.plot(df_1['price'],df_1['area'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()
# %%
r, p = scipy.stats.pearsonr(df_1.price,df_1.area)
print("r =", r, "p =", p)

# %%
print("Nhận xét: Do pvalue ~0, và hệ số tương quan =0.22 nên giữa giá nhà và diện tích có mối tương quan thuận rất chặt với nhau")
#%%
#Giữa giá nhà và tọa độ địa lý (lat, long) có tương quan với nhau
df_lat = df[['lat','price']]
df_lat = df_lat.dropna()
df_lat.sort_values(by=['lat'])
df_lat
#%%
plt.plot(df_lat['price'],df_lat['lat'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()
# %%
r, p = scipy.stats.pearsonr(df_lat.price,df_lat.lat)
print("r =", r, "p =", p)

# %%
print("Nhận xét: Do pvalue ~0.2, và hệ số tương quan <<0 nên giữa giá nhà và tọa độ lat có mối tương quan thuận không chặt với nhau")
#%%
df_long = df[['long','price']]
df_long = df_long.dropna()
df_long.sort_values(by=['long'])
df_long
#%%
plt.plot(df_long['price'],df_long['long'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()
# %%
r, p = scipy.stats.pearsonr(df_long.price,df_long.long)
print("r =", r, "p =", p)

# %%
print("Nhận xét: Do pvalue ~0, và hệ số tương quan ~0 nên giữa giá nhà và tọa độ long có mối tương quan thuận rất chặt với nhau")
#%%
contigency = pd.crosstab(df['land_certificate'], df['property_type'])
contigency

# %%
c, p, dof, expected = scipy.stats.chi2_contingency(contigency)
print("c = ", c)
print("p = ", p)

# %%
print("Với mức ý nghĩa là alpha = 5% = 0,05 < p , kết luận không có tính tương quan giữa land_certificate và property_type")