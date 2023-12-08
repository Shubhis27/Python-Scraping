#!/usr/bin/env python
# coding: utf-8

# In[35]:


#importing the libraries

from bs4 import BeautifulSoup
import requests
import smtplib


# In[36]:


# Website Access and calling for first product
 

URL_1 = 'https://www.amazon.in/20000mAh-Sandstone-Triple-Charging-Delivery/dp/B08HV83HL3/ref=sr_1_1?qid=1701980499&s=electronics&sr=1-1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_1 = requests.get(URL_1 , headers=headers)

soup1_1 = BeautifulSoup(page_1.content, "html.parser")

soup1 = BeautifulSoup(soup1_1.prettify(),'html.parser')

title_1 = soup1.find(id='productTitle').get_text()
seller_1 = soup1.find(id='bylineInfo').get_text()
Rating_1 = soup1.find(id='acrCustomerReviewText').get_text()
price_1 = 2149


# In[37]:


# Creating an CSV File
import csv
header = ['Product Name', 'Price','Rating','Seller Name']
data_1 = [title_1,price_1,Rating_1,seller_1]

with open('PythonScraping.csv','w',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data_1)


# In[38]:


# repeating for second product
 
URL_2 = 'https://www.amazon.in/10000mAH-Li-Polymer-Power-Charging-Midnight/dp/B08HVL8QN3/ref=sr_1_2?qid=1701980499&s=electronics&sr=1-2'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_2 = requests.get(URL_2 , headers=headers)

soup2_1 = BeautifulSoup(page_2.content, "html.parser")

soup2 = BeautifulSoup(soup2_1.prettify(),'html.parser')

title_2 = soup2.find(id='productTitle').get_text()
seller_2 = soup2.find(id='bylineInfo').get_text()
Rating_2 = soup2.find(id='acrCustomerReviewText').get_text()
Price_2= 1299
data_2 = [title_2,Price_2,Rating_2,seller_2]

# Appending the details from second product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_2)


# In[39]:


# 4 product

URL_4 = 'https://www.amazon.in/Ambrane-20000mAh-Lithium-Polymer-Stylo-20K/dp/B07RD611Z8/ref=sr_1_7?qid=1702025373&s=electronics&sr=1-7&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_4 = requests.get(URL_4 , headers=headers)

soup4_1 = BeautifulSoup(page_4.content, "html.parser")

soup4= BeautifulSoup(soup4_1.prettify(),'html.parser')

title_4 = soup4.find(id='productTitle').get_text()
seller_4 = soup4.find(id='bylineInfo').get_text()
Rating_4 = soup4.find(id='acrCustomerReviewText').get_text()
Price_4= 1599
data_4 = [title_4,Price_4,Rating_4,seller_4]

# Appending the details from fourth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_4)


# In[40]:


# 5 product

URL_5 = 'https://www.amazon.in/Ambrane-Multi-Layer-Protection-Li-Polymer-Stylo-20k/dp/B09MZDVQCC/ref=sr_1_8?qid=1702025373&s=electronics&sr=1-8&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_5 = requests.get(URL_5 , headers=headers)

soup5_1 = BeautifulSoup(page_5.content, "html.parser")

soup5 = BeautifulSoup(soup5_1.prettify(),'html.parser')

title_5 = soup5.find(id='productTitle').get_text()
seller_5 = soup5.find(id='bylineInfo').get_text()
Rating_5 = soup5.find(id='acrCustomerReviewText').get_text()
Price_5= 1599
data_5 = [title_5,Price_5,Rating_5,seller_5]

# Appending the details from fifth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_5)


# In[41]:


# 6 product

URL_6 = 'https://www.amazon.in/Ambrane-Multi-Layer-Protection-Li-Polymer-Stylo-20k/dp/B09MZDVQCC/ref=sr_1_8?qid=1702025373&s=electronics&sr=1-8&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_6 = requests.get(URL_6 , headers=headers)

soup6_1 = BeautifulSoup(page_6.content, "html.parser")

soup6 = BeautifulSoup(soup6_1.prettify(),'html.parser')

title_6 = soup6.find(id='productTitle').get_text()
seller_6 = soup6.find(id='bylineInfo').get_text()
Rating_6 = soup6.find(id='acrCustomerReviewText').get_text()
Price_6= 1599
data_6 = [title_6,Price_6,Rating_6,seller_6]

# Appending the details from sixth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_6)


# In[42]:


# 7 product

URL_7 = 'https://www.amazon.in/Duracell-Slimmest-Charging-Portable-Simultaneously/dp/B0BJV4L36G/ref=sr_1_9?qid=1702025373&s=electronics&sr=1-9&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_7 = requests.get(URL_7 , headers=headers)

soup7_1 = BeautifulSoup(page_7.content, "html.parser")

soup7 = BeautifulSoup(soup7_1.prettify(),'html.parser')

title_7 = soup7.find(id='productTitle').get_text()
seller_7 = soup7.find(id='bylineInfo').get_text()
Rating_7 = soup7.find(id='acrCustomerReviewText').get_text()
Price_7= 3099
data_7 = [title_7,Price_7,Rating_7,seller_7]

# Appending the details from seventh product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_7)


# In[43]:


# 8 product

URL_8 = 'https://www.amazon.in/Ambrane-Multi-Layer-Protection-Li-Polymer-Stylo-10k/dp/B0993BB11X/ref=sr_1_10?qid=1702025373&s=electronics&sr=1-10&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_8 = requests.get(URL_8 , headers=headers)

soup8_1 = BeautifulSoup(page_8.content, "html.parser")

soup8 = BeautifulSoup(soup8_1.prettify(),'html.parser')

title_8 = soup8.find(id='productTitle').get_text()
seller_8 = soup8.find(id='bylineInfo').get_text()
Rating_8 = soup8.find(id='acrCustomerReviewText').get_text()
Price_8= 999
data_8 = [title_8,Price_8,Rating_8,seller_8]

# Appending the details from Eighth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_8)


# In[44]:


# 9 product

URL_9 = 'https://www.amazon.in/Ambrane-Multi-Layer-Protection-Li-Polymer-Stylo-20k/dp/B09779CSV6/ref=sr_1_11?qid=1702025373&s=electronics&sr=1-11&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_9 = requests.get(URL_9 , headers=headers)

soup9_1 = BeautifulSoup(page_9.content, "html.parser")

soup9 = BeautifulSoup(soup9_1.prettify(),'html.parser')

title_9 = soup9.find(id='productTitle').get_text()
seller_9 = soup9.find(id='bylineInfo').get_text()
Rating_9 = soup9.find(id='acrCustomerReviewText').get_text()
Price_9= 1599
data_9 = [title_9,Price_9,Rating_9,seller_9]

# Appending the details from Ninth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_9)


# In[45]:


# 10 product

URL_10 = 'https://www.amazon.in/URBN-20000-22-5W-Charging-Output/dp/B08JW1GVS7/ref=sr_1_12?qid=1702025373&s=electronics&sr=1-12'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_10 = requests.get(URL_10 , headers=headers)

soup10_1 = BeautifulSoup(page_10.content, "html.parser")

soup10 = BeautifulSoup(soup10_1.prettify(),'html.parser')

title_10 = soup10.find(id='productTitle').get_text()
seller_10 = soup10.find(id='bylineInfo').get_text()
Rating_10 = soup10.find(id='acrCustomerReviewText').get_text()
Price_10= 1499
data_10 = [title_10,Price_10,Rating_10,seller_10]

# Appending the details from tenth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_10)


# In[46]:


# 11 product

URL_11 = 'https://www.amazon.in/Power-10000mAh-Metallic-Output-Charging/dp/B08HVJCW95/ref=sr_1_16?qid=1702025373&s=electronics&sr=1-16'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_11 = requests.get(URL_11 , headers=headers)

soup11_1 = BeautifulSoup(page_11.content, "html.parser")

soup11 = BeautifulSoup(soup11_1.prettify(),'html.parser')

title_11 = soup11.find(id='productTitle').get_text()
seller_11 = soup11.find(id='bylineInfo').get_text()
Rating_11 = soup11.find(id='acrCustomerReviewText').get_text()
Price_11= 1299
data_11 = [title_11,Price_11,Rating_11,seller_11]

# Appending the details from Eleventh product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_11)


# In[47]:


# 12 product

URL_12 = 'https://www.amazon.in/Ambrane-Multi-Layer-Protection-Li-Polymer-Stylo-10k/dp/B09MZCQYHZ/ref=sr_1_17?qid=1702025373&s=electronics&sr=1-17&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_12 = requests.get(URL_12 , headers=headers)

soup12_1 = BeautifulSoup(page_12.content, "html.parser")

soup12 = BeautifulSoup(soup12_1.prettify(),'html.parser')

title_12 = soup12.find(id='productTitle').get_text()
seller_12 = soup12.find(id='bylineInfo').get_text()
Rating_12 = soup12.find(id='acrCustomerReviewText').get_text()
Price_12= 999
data_12 = [title_12,Price_12,Rating_12,seller_12]

# Appending the details from Twelfth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_12)


# In[48]:


# 13 product

URL_13 = 'https://www.amazon.in/FLiX-PowerXtreme-Compatible-Samsung-Black-P10/dp/B0C8CY5TD9/ref=sr_1_18?qid=1702025373&s=electronics&sr=1-18&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_13 = requests.get(URL_13 , headers=headers)

soup13_1 = BeautifulSoup(page_13.content, "html.parser")

soup13 = BeautifulSoup(soup13_1.prettify(),'html.parser')

title_13 = soup13.find(id='productTitle').get_text()
seller_13 = soup13.find(id='bylineInfo').get_text()
Rating_13 = soup13.find(id='acrCustomerReviewText').get_text()
Price_13= 599
data_13 = [title_13,Price_13,Rating_13,seller_13]

# Appending the details from Thirteenth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_13)


# In[49]:


# 14 product

URL_14 = 'https://www.amazon.in/URBN-Premium-Charging-Delivery-Two-Way/dp/B0BXSR4ZBD/ref=sr_1_20?qid=1702025373&s=electronics&sr=1-20&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_14 = requests.get(URL_14 , headers=headers)

soup14_1 = BeautifulSoup(page_14.content, "html.parser")

soup14 = BeautifulSoup(soup14_1.prettify(),'html.parser')

title_14 = soup14.find(id='productTitle').get_text()
seller_14 = soup14.find(id='bylineInfo').get_text()
Rating_14 = soup14.find(id='acrCustomerReviewText').get_text()
Price_14= 2499
data_14 = [title_14,Price_14,Rating_14,seller_14]

# Appending the details from Fourteenth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_14)


# In[50]:


# 15 product

URL_15 = 'https://www.amazon.in/Amazon-20000mAh-Lithium-Polymer-Charging-Included/dp/B0C37KY7LH/ref=sr_1_21?qid=1702025373&s=electronics&sr=1-21'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_15 = requests.get(URL_15 , headers=headers)

soup15_1 = BeautifulSoup(page_15.content, "html.parser")

soup15 = BeautifulSoup(soup15_1.prettify(),'html.parser')

title_15 = soup15.find(id='productTitle').get_text()
seller_15 = soup15.find(id='bylineInfo').get_text()
Rating_15 = soup15.find(id='acrCustomerReviewText').get_text()
Price_15= 1579
data_15 = [title_15,Price_15,Rating_15,seller_15]

# Appending the details from Fifteenth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_15)


# In[51]:


# 16 product

URL_16 = 'https://www.amazon.in/5000mAh-Li-Polymer-Wireless-Two-Way-Charging/dp/B0CGZY677H/ref=sr_1_22?qid=1702025373&s=electronics&sr=1-22'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_16 = requests.get(URL_16 , headers=headers)

soup16_1 = BeautifulSoup(page_16.content, "html.parser")

soup16 = BeautifulSoup(soup16_1.prettify(),'html.parser')

title_16 = soup16.find(id='productTitle').get_text()
seller_16 = soup16.find(id='bylineInfo').get_text()
Rating_16 = soup16.find(id='acrCustomerReviewText').get_text()
Price_16= 1099
data_16 = [title_16,Price_16,Rating_16,seller_16]

# Appending the details from Sixtteenth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_16)


# In[52]:


# 17 product

URL_17 = 'https://www.amazon.in/Amazon-Basics-20000mAh-Lithium-Polymer-Included/dp/B0C37L2B32/ref=sr_1_23?qid=1702025373&s=electronics&sr=1-23'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_17 = requests.get(URL_17 , headers=headers)

soup17_1 = BeautifulSoup(page_17.content, "html.parser")

soup17 = BeautifulSoup(soup17_1.prettify(),'html.parser')

title_17 = soup17.find(id='productTitle').get_text()
seller_17 = soup17.find(id='bylineInfo').get_text()
Rating_17 = soup17.find(id='acrCustomerReviewText').get_text()
Price_17= 1219
data_17 = [title_17,Price_17,Rating_17,seller_17]

# Appending the details from Seventeenth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_17)


# In[53]:


# 18 product

URL_18 = 'https://www.amazon.in/FLiX-PowerXtreme-Compatible-Lightning-Blue-P10/dp/B0CJBVNZ7V/ref=sr_1_24?qid=1702025373&s=electronics&sr=1-24&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_18 = requests.get(URL_18 , headers=headers)

soup18_1 = BeautifulSoup(page_18.content, "html.parser")

soup18 = BeautifulSoup(soup18_1.prettify(),'html.parser')

title_18 = soup18.find(id='productTitle').get_text()
seller_18 = soup18.find(id='bylineInfo').get_text()
Rating_18 = soup18.find(id='acrCustomerReviewText').get_text()
Price_18= 499
data_18 = [title_18,Price_18,Rating_18,seller_18]

# Appending the details from Eighteenth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_18)


# In[54]:


# 19 product

URL_19 = 'https://www.amazon.in/URBN-10000-22-5W-Charging-Output/dp/B08JVY8LGD/ref=sr_1_25?qid=1702025373&s=electronics&sr=1-25'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_19 = requests.get(URL_19 , headers=headers)

soup19_1 = BeautifulSoup(page_19.content, "html.parser")

soup19 = BeautifulSoup(soup19_1.prettify(),'html.parser')

title_19 = soup19.find(id='productTitle').get_text()
seller_19 = soup19.find(id='bylineInfo').get_text()
Rating_19 = soup19.find(id='acrCustomerReviewText').get_text()
Price_19= 1199
data_19 = [title_19,Price_19,Rating_19,seller_19]

# Appending the details from Ninteenth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_19)


# In[55]:


# 20 product

URL_20 = 'https://www.amazon.in/URBN-20000-22-5W-Charging-Output/dp/B08JVY7QYC/ref=sr_1_26?qid=1702025373&s=electronics&sr=1-26'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_20 = requests.get(URL_20 , headers=headers)

soup20_1 = BeautifulSoup(page_20.content, "html.parser")

soup20 = BeautifulSoup(soup20_1.prettify(),'html.parser')

title_20 = soup20.find(id='productTitle').get_text()
seller_20 = soup20.find(id='bylineInfo').get_text()
Rating_20 = soup20.find(id='acrCustomerReviewText').get_text()
Price_20= 1499
data_20 = [title_20,Price_20,Rating_20,seller_20]

# Appending the details from Twentieth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_20)


# In[56]:


# 21 product

URL_21 = 'https://www.amazon.in/URBN-Premium-Charging-Smallest-Delivery/dp/B0BXSTYMZ7/ref=sr_1_27?qid=1702025373&s=electronics&sr=1-27&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_21 = requests.get(URL_21 , headers=headers)

soup21_1 = BeautifulSoup(page_21.content, "html.parser")

soup21 = BeautifulSoup(soup21_1.prettify(),'html.parser')

title_21 = soup21.find(id='productTitle').get_text()
seller_21 = soup21.find(id='bylineInfo').get_text()
Rating_21 = soup21.find(id='acrCustomerReviewText').get_text()
Price_21= 2499
data_21 = [title_21,Price_21,Rating_21,seller_21]

# Appending the details from Twenty-first product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_21)


# In[57]:


# 22 product

URL_22 = 'https://www.amazon.in/Ambrane-Multi-Layer-Protection-Li-Polymer-Stylo/dp/B098QV28F7/ref=sr_1_28?qid=1702025373&s=electronics&sr=1-28'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_22 = requests.get(URL_22 , headers=headers)

soup22_1 = BeautifulSoup(page_22.content, "html.parser")

soup22 = BeautifulSoup(soup22_1.prettify(),'html.parser')

title_22 = soup22.find(id='productTitle').get_text()
seller_22 = soup22.find(id='bylineInfo').get_text()
Rating_22 = soup22.find(id='acrCustomerReviewText').get_text()
Price_22= 2499
data_22 = [title_22,Price_22,Rating_22,seller_22]

# Appending the details from Twenty-second product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_22)


# In[58]:


# 23 product

URL_23 = 'https://www.amazon.in/URBN-Charging-Lithium_ion-Delivery-Included/dp/B0B4DHLVTQ/ref=sr_1_29?qid=1702025373&s=electronics&sr=1-29&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_23 = requests.get(URL_23 , headers=headers)

soup23_1 = BeautifulSoup(page_23.content, "html.parser")

soup23 = BeautifulSoup(soup23_1.prettify(),'html.parser')

title_23 = soup23.find(id='productTitle').get_text()
seller_23 = soup23.find(id='bylineInfo').get_text()
Rating_23 = soup23.find(id='acrCustomerReviewText').get_text()
Price_23= 1499
data_23 = [title_23,Price_23,Rating_23,seller_23]

# Appending the details from Twenty-third product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_23)


# In[59]:


# 24 product

URL_24 = 'https://www.amazon.in/Redmi-20000mAh-Li-Polymer-Power-Charging/dp/B0851WWXJC/ref=sr_1_30?qid=1702025373&s=electronics&sr=1-30'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-65722b27-5ddfd33e3e458c2f2a896cf6"} 
page_24 = requests.get(URL_24 , headers=headers)

soup24_1 = BeautifulSoup(page_24.content, "html.parser")

soup24 = BeautifulSoup(soup24_1.prettify(),'html.parser')

title_24 = soup24.find(id='productTitle').get_text()
seller_24 = soup24.find(id='bylineInfo').get_text()
Rating_24 = soup24.find(id='acrCustomerReviewText').get_text()
Price_24= 2049
data_24 = [title_24,Price_24,Rating_24,seller_24]

# Appending the details from Twenty-fourth product in the csv file
with open('PythonScraping.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_24)


# In[63]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Administrator\PythonScraping.csv')
print(df)


# In[ ]:




