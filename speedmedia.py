from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import sys


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


driver = webdriver.Chrome('chromedriver', options=options)
currentPath = os.getcwd()

url = sys.argv[1]

driver.get(url)

seasons = driver.find_elements_by_css_selector("body > div.body > article > div > div > section > div > div > a")
seasonsLinks = []

showName = driver.find_element_by_css_selector("body > div.body > article > div > div > div.media-body > header > h1").text
showName = showName.replace(" ","-")
os.system("mkdir " + " '" + showName + "'")
print("Downloading %s show" % showName)
n=1
for seasonLink in seasons:
    seasonsLinks.append(seasonLink.get_attribute("href"))
    # os.system("cd " + currentPath + "/"+showName)
    os.system("mkdir " + currentPath+"/"+showName+"/"+"Season" + str(n))
    n+=1


i = 1
for seasonLink in seasonsLinks:
    print("Downloading Season", i)
    driver.get(seasonLink)
    episodes = driver.find_elements_by_css_selector("body > div.body > article > div > div > section > div > div > a")

    links = []
    for iii in episodes:
        links.append(iii.get_attribute("href"))


    epiNum = 1
    for link in links:
        print("Starting Episode Number: ", epiNum)
        epiNum += 1
        print(link)
        driver.get(link)
        downloadButton = driver.find_element_by_css_selector('body > div.body > article > div > div > div.media-left > div > a.action-link.action-download')
        downloadLink = downloadButton.get_attribute("href")
        # downloadLink = downloadLink.replace(" ", "%20")
        os.system("wget " + "'" +str(downloadLink) + "'"  + " -P " + currentPath +"/"+showName+ "/Season"+str(i))

    i+=1

# driver.close()
