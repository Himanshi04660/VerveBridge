# Importing modules
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Creating an empty list to store the data of the products
phn_nm=[] 
phn_pr=[]
phn_desc=[]

# Taking input of no. of pages from user
page_num=input("Enter number of pages")

for i in range(1,int(page_num)+1):
    url="https://www.flipkart.com/search?q=mi+phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    # request the server for the url
    req=requests.get(url)

    # Fetch the content of the url using BeautifulSoup
    content=BeautifulSoup(req.content, 'html.parser')



    # Scrap product name data
    name=content.find_all('div', {"class":"KzDlHZ"})

    for i in name:
        phn_nm.append(i.text)


    
    # Scrap product price data
    price=content.find_all('div', {"class":"Nx9bqj _4b5DiR"})

    for i in price:
        phn_pr.append(i.text)


  
    # Scrap product description data
    description=content.find_all('ul', {"class":"G4BRas"})

    for i in description:
        phn_desc.append(i.text)


   
    # Prints no. of phones on each page
    print("Phones in page"+str(i))
    print(len(name)) 

# Creating dataframe
data={"Product name":phn_nm, "Product price": phn_pr, "Product Description":phn_desc}
df=pd.DataFrame(data)
print(df)

# Export to CSV file
csv_file = 'Laptops.csv'
df.to_csv(csv_file, index=False)
    
print(f"Scraping and exporting completed. Data saved to {csv_file}.")
