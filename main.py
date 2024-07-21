import requests
from bs4 import BeautifulSoup
import pandas as pd

Product_name=[]
Prices=[]
Description=[]
Reviews=[]

# for i in range(2, 12):
url="https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(1)
                
r=requests.get(url)
            
soup=BeautifulSoup(r.text, "html.parser")
box = soup.find("div", class_ = "DOjaWF gdgoEp")
            
         
# Extract the names of the products 
names = box.find_all("div", class_ = "KzDlHZ")
       
for i in names:
    name=i.text
    Product_name.append(name)
print(Product_name) 
    
            
# Extracts the price of the products 
prices = box.find_all("div", class_ = "Nx9bqj _4b5DiR")

for i in prices:
    name=i.text
    Prices.append(name)
print(Prices) 
    
    
# Extracts the description of the products
desc = box.find_all("ul", class_ = "G4BRas")
            
for i in desc:
    name=i.text
    Description.append(name)
print(Description)
    
    
# Extracts the description of the products
reviews = box.find_all("div", class_="XQDdHH")
            
for i in reviews:
    name=i.text
    Reviews.append(name)
print(Reviews)  

df=pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})

df.to_csv("C:/Users/Victus0424/OneDrive/Desktop/Laptops.csv")
            
