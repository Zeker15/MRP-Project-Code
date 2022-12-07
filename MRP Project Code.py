#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from bs4 import BeautifulSoup
import time
# import numpy

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium. webdriver. chrome. options import Options
options = Options()
options. add_experimental_option("detach", True)

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
#browser = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
#browser.set_window_size(1800, 900)

global driver
driver = webdriver.Chrome ('C:\\Users\\robgo\\Downloads\\chromedriver_win32\\chromedriver.exe'), ('options=options')
options = Options()
options.add_argument("--start-maximized");
options.add_argument("--window-position=1367,0");

driver = webdriver.Chrome('C:\\Users\\robgo\\Downloads\\chromedriver_win32\\chromedriver.exe', 
                                  options = options)
# driver.set_window_size(1800,900)
driver.get('https://linkedin.com/uas/login')

# waiting for the page to load
time.sleep(5)
 
# entering username
username = driver.find_element_by_id("username")
 
# Enter Your Email Address
username.send_keys("enter user_name here") 
 
# entering password
pword = driver.find_element_by_id("password")
 
# Enter Your Password - enter your password
pword.send_keys("enter password here")       
 
# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# XPath used here.
 
# Opening my LinkedIn Profile
profile_url = "https://www.linkedin.com/in/rob-goudis-bba61b13/"
 
driver.get(profile_url)

start = time.time()
 
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
 
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")                     
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
 
    # we will stop the script for 3 seconds so that
    # the data can load
    time.sleep(3)

 
    end = time.time()
 
    # We will scroll for 20 seconds.
    if round(end - start) > 15:
        break
        
src = driver.page_source
 
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
 
print(intro)

# In case of an error, try changing the tags used here.
 
name_loc = intro.find("h1")
 
# Extracting the Name
name = name_loc.get_text().strip()
 
works_at_loc = intro.find("div", {'class': 'text-body-medium'})

# Extracting the Company Name
works_at = works_at_loc.get_text().strip()
 
location_loc = intro.find_all("div", {'class': 'text-body-small'})
 
# Extracting the Location
# The 2nd element in the location_loc variable has the location

#location_loc = location_loc[1].get_text().strip()

#location_loc = intro.find("span", 'class': 'text-body-small inline t-black--light break-words'})
 
print("Name -->", name,
      "\nWorks At -->", works_at)
#     "\nLocation -->", location)

# Getting the HTML of the Experience section in the profile
experience = soup.find("experience", {"id": "experience-section"}).find('ul')
 
print(experience)
 
li_tags = experience.find('div')
a_tags = li_tags.find("a")
job_title = a_tags.find("h3").get_text().strip()
 
print(job_title)
 
company_name = a_tags.find_all("p")[1].get_text().strip()
print(company_name)
 
joining_date = a_tags.find_all("h4")[0].find_all("span")[1].get_text().strip()
 
employment_duration = a_tags.find_all("h4")[1].find_all(
    "span")[1].get_text().strip()
 
print(joining_date + ", " + employment_duration)

jobs = driver.find_element_by_xpath("//a[@data-link-to='jobs']/span")
# In case of an error, try changing the XPath.
 
jobs.click()

job_src = driver.page_source
 
soup = BeautifulSoup(job_src, 'lxml')

jobs_html = soup.find_all('a', {'class': 'job-card-list__title'})
# In case of an error, try changing the XPath.
 
job_titles = []
 
for title in jobs_html:
    job_titles.append(title.text.strip())
 
print(job_titles)

company_name_html = soup.find_all(
  'div', {'class': 'job-card-container__company-name'})
company_names = []
 
for name in company_name_html:
    company_names.append(name.text.strip())
 
print(company_names)

import re   # for removing the extra blank spaces
 
location_html = soup.find_all(
    'ul', {'class': 'job-card-container__metadata-wrapper'})
 
location_list = []
 
for loc in location_html:
    res = re.sub('\n\n +', ' ', loc.text.strip())
 
    location_list.append(res)
 
print(location_list)


# In[ ]:





# In[ ]:





# In[ ]:




