import pandas as pd
from tabulate import tabulate

de=pd.read_csv("data enger.csv",sep=";")
sh=de.groupby("Country").agg(
    Avarge_profit=("Total Profit","mean"),
    number_of_purchase=("Country","count"),
    Total_cost=("Total Cost","sum"),
    Total_Revenue=("Total Revenue","sum")
)
print(sh)
sh["Return on profit"]=(sh["Total_Revenue"]/sh["Total_cost"])*100
highest_profit=sh.sort_values("Avarge_profit",ascending=False)
Top_20=highest_profit.head(20)
active_countries=sh[sh["number_of_purchase"]>=30]
active_countries=active_countries.assign(Status = "Active")
print(tabulate(active_countries,headers="keys",tablefmt="grid"))
data=pd.DataFrame(Top_20)
data = data.reset_index().merge(active_countries.reset_index())
print(tabulate(data, headers='keys', tablefmt='grid'))
with pd.ExcelWriter("Sales analysis.xlsx") as writer:
 Top_20.to_excel(writer,sheet_name="Top 20 highest-earning countries")

 active_countries.to_excel(writer,sheet_name="active_countries.")
 
 data.to_excel(writer,sheet_name="Top")
print("Data uploaded successfully")