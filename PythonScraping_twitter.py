#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the libraries

import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


# In[2]:


# calling the drivers 

driver = Chrome()


# In[3]:


# Accessing the website

driver.get('https://twitter.com/whatsapp')


# In[4]:


# Calling the first link

bio_1 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_1 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_1 = driver.find_element('xpath', '//a[@href="/WhatsApp/following"]').text
Follower_1 = driver.find_element('xpath', '//a[@href="/WhatsApp/verified_followers"]').text
Website_1 = '-'


# In[5]:


# Creating an CSV File

header = ['Bio', 'Following Count','Followers Count','Location', 'Website']
data_1 = [bio_1,Following_1, Follower_1,location_1,Website_1]

with open('PythonScraping_twitter.csv','w',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data_1)


# In[6]:


# Calling the second link

driver.get('https://twitter.com/GTNUK1')


# In[7]:


bio_2 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_2 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_2 = driver.find_element('xpath', '//a[@href="/GTNUK1/following"]').text
Follower_2 = driver.find_element('xpath', '//a[@href="/GTNUK1/verified_followers"]').text
Website_2 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_2 = [bio_2,Following_2, Follower_2,location_2,Website_2]

# Appending the details from second link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_2)


# In[8]:


# Calling the third link

driver.get('https://twitter.com/aacb_CBPTrade')


# In[9]:


bio_3 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_3 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_3 = driver.find_element('xpath', '//a[@href="/aacb_CBPTrade/following"]').text
Follower_3 = driver.find_element('xpath', '//a[@href="/aacb_CBPTrade/verified_followers"]').text
Website_3 = '-'
data_3 = [bio_3,Following_3, Follower_3,location_3,Website_3]

# Appending the details from third link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_3)


# In[10]:


# Calling the fourth link

driver.get('https://twitter.com/aacbdotcom')


# In[11]:


bio_4 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_4 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_4 = driver.find_element('xpath', '//a[@href="/aacbdotcom/following"]').text
Follower_4 = driver.find_element('xpath', '//a[@href="/aacbdotcom/verified_followers"]').text
Website_4 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_4 = [bio_4,Following_4, Follower_4,location_4,Website_4]

# Appending the details from fourth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_4)


# In[12]:


# Calling the fifth link

driver.get('https://twitter.com/@AAWindowPRODUCT')


# In[13]:


bio_5 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_5 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_5 = driver.find_element('xpath', '//a[@href="/AAWindowPRODUCT/following"]').text
Follower_5 = driver.find_element('xpath', '//a[@href="/AAWindowPRODUCT/verified_followers"]').text
Website_5 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_5 = [bio_5,Following_5, Follower_5,location_5,Website_5]

# Appending the details from fifth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_5)


# In[14]:


# Calling the sixth link

driver.get('https://www.twitter.com/aandb_kia')


# In[15]:


bio_6 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_6 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_6 = driver.find_element('xpath', '//a[@href="/AandB_Kia/following"]').text
Follower_6 = driver.find_element('xpath', '//a[@href="/AandB_Kia/verified_followers"]').text
Website_6 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_6 = [bio_6,Following_6, Follower_6,location_6,Website_6]

# Appending the details from sixth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_6)


# In[16]:


# Calling the seventh link

driver.get('https://twitter.com/ABHomeInc')


# In[17]:


bio_7 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_7 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_7 = driver.find_element('xpath', '//a[@href="/ABHomeInc/following"]').text
Follower_7 = driver.find_element('xpath', '//a[@href="/ABHomeInc/verified_followers"]').text
Website_7 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_7 = [bio_7,Following_7, Follower_7,location_7,Website_7]

# Appending the details from seventh link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_7)


# In[18]:


# Calling the eighth link

driver.get('https://twitter.com/Abrepro')


# In[19]:


bio_8 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_8 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_8 = driver.find_element('xpath', '//a[@href="/Abrepro/following"]').text
Follower_8 = driver.find_element('xpath', '//a[@href="/Abrepro/verified_followers"]').text
Website_8 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_8 = [bio_8,Following_8, Follower_8,location_8,Website_8]

# Appending the details from eighth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_8)


# In[20]:


# Calling the ninth link

driver.get('https://twitter.com/X')


# In[21]:


bio_9 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_9 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_9 = driver.find_element('xpath', '//a[@href="/X/following"]').text
Follower_9 = driver.find_element('xpath', '//a[@href="/X/verified_followers"]').text
Website_9 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_9 = [bio_9,Following_9, Follower_9,location_9,Website_9]

# Appending the details from ninth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_9)


# In[22]:


# Calling the tenth link

driver.get('https://twitter.com/ACChristofiLtd')


# In[23]:


bio_10 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_10 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_10 = driver.find_element('xpath', '//a[@href="/ACChristofiLtd/following"]').text
Follower_10 = driver.find_element('xpath', '//a[@href="/ACChristofiLtd/verified_followers"]').text
Website_10 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_10 = [bio_10,Following_10, Follower_10,location_10,Website_10]

# Appending the details from tenth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_10)


# In[24]:


# Calling the eleventh link

driver.get('https://twitter.com/aeclothing1')


# In[25]:


bio_11 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_11 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_11 = driver.find_element('xpath', '//a[@href="/aeclothing1/following"]').text
Follower_11 = driver.find_element('xpath', '//a[@href="/aeclothing1/verified_followers"]').text
Website_11 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_11 = [bio_11,Following_11, Follower_11,location_11,Website_11]

# Appending the details from eleventh link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_11)


# In[26]:


# Calling the twelfth link

driver.get('https://twitter.com/ShubhamS_2795')


# In[27]:


bio_12 = '-'
location_12 = '-'
Following_12 = driver.find_element('xpath', '//a[@href="/ShubhamS_2795/following"]').text
Follower_12 =  driver.find_element('xpath', '//a[@href="/ShubhamS_2795/verified_followers"]').text
Website_12 = '-'
data_12 = [bio_12,Following_12, Follower_12,location_12,Website_12]

# Appending the details from twelfth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_12)


# In[28]:


# Calling the thirteenth link

driver.get('https://twitter.com/AETechnologies1')


# In[29]:


bio_13 = '-'
location_13 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_13 = driver.find_element('xpath', '//a[@href="/AETechnologies1/following"]').text
Follower_13 = driver.find_element('xpath', '//a[@href="/AETechnologies1/verified_followers"]').text
Website_13 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_13 = [bio_13,Following_13, Follower_13,location_13,Website_13]

# Appending the details from thirteenth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_13)


# In[30]:


# Calling the fourteenth link

driver.get('http://www.twitter.com/wix')


# In[31]:


bio_14 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_14 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_14 = driver.find_element('xpath', '//a[@href="/Wix/following"]').text
Follower_14 = driver.find_element('xpath', '//a[@href="/Wix/verified_followers"]').text
Website_14 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_14 = [bio_14,Following_14, Follower_14,location_14,Website_14]

# Appending the details from fourteenth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_14)


# In[32]:


# Calling the fifteenth link

driver.get('https://twitter.com/AGInsuranceLLC')


# In[33]:


bio_15 = driver.find_element('xpath', '//div[@data-testid="UserDescription"]').text
location_15 = driver.find_element('xpath', '//span[@data-testid="UserLocation"]').text
Following_15 = driver.find_element('xpath', '//a[@href="/AGInsuranceLLC/following"]').text
Follower_15 = driver.find_element('xpath', '//a[@href="/AGInsuranceLLC/verified_followers"]').text
Website_15 = driver.find_element('xpath', '//a[@data-testid="UserUrl"]').text
data_15 = [bio_15,Following_15, Follower_15,location_15,Website_15]

# Appending the details from fifteenth link in the csv file

with open('PythonScraping_twitter.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data_15)


# In[34]:


# Opening the CSV File

import pandas as pd
df = pd.read_csv(r'C:\Users\Administrator\PythonScraping_twitter.csv')
print(df)


# In[ ]:




