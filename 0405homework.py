import pandas as pd
a='./data/beijing_tianqi_2018.csv'
df=pd.read_csv(a)
df
df.loc[:,"bWendu"]=df["bWendu"].str.replace("℃","").astype('int32')
df.loc[:,"yWendu"]=df["yWendu"].str.replace("℃","").astype('int32')
df
df.loc[(df['bWendu']<30)&(df['yWendu']>15)&(df['tianqi']=='晴')&(df['aqiInfo']=='优'),:]
