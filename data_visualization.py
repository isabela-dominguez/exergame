from config import * 

# import data from CSV
df = pd.read_csv('data/ziads_data/Walking.csv', engine="python",index_col=False, sep=";", header= 1, encoding='utf-8' )

print(df.size)
print(df.dtypes)


print(df)
# Take a look at all sensor outputs
df.plot(subplots=True,sharex=True,layout=(6,6))
plt.show()