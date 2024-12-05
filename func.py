import pandas as pd
vct_df = pd.read_csv("vct_data.csv")
# vct_df.dropna(axis=0, inplace=True) > Drop Null(MissingValue)
# vct_df.gun.fillna(value="vandal", inplace=True) > Imputation(MissingValue)
print(vct_df.isna().sum())
print(pd.DataFrame(vct_df))







### Cntoh IQR

# q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
# iqr = q75 - q25
# cut_off = iqr * 1.5
# minimum, maximum = q25 - cut_off, q75 + cut_off
 
# outliers = [x for x in data if x < minimum or x > maximum]

###