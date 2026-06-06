import requests
import pandas as pd 
from tabulate import tabulate
url = "https://jsonplaceholder.typicode.com/posts"
my_headers = {
    'User-Agent': "Mozilla/"
}
h=requests.get(url,headers=my_headers)
j=h.json()
df=pd.DataFrame(j)
print(df)
df.to_excel("df.xlsx",index=False)
print("load the data to xlsx1")



csv_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
csv=pd.read_csv(csv_url)
h=csv[["PassengerId","Survived","Name","Sex"]]
print(tabulate(h.head(),headers="keys",tablefmt="grid"))
h.head().to_excel("h.xlsx",index=False)
print("load the data to xlsx2")

xlsx="https://go.microsoft.com/fwlink/?LinkID=521962"
x=pd.read_excel(xlsx)
print(tabulate(x.iloc[:5,:6],headers="keys",tablefmt="grid"))
x.iloc[:5,:6].to_excel("x.xlsx")
print("load the data to xlsx3")


twitter_url = "https://raw.githubusercontent.com/zfz/twitter_corpus/master/full-corpus.csv"
c=pd.read_csv(twitter_url)
print(tabulate(c.iloc[:5,:4],headers="keys",tablefmt="grid"))
c.iloc[:5,:4].to_excel("c.xlsx")
print("load the data to xlsx4")