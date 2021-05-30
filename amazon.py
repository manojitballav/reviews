import re,time

from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# database connections
client = MongoClient('127.0.0.1',27017)
db = client['amazon']
col  = db['record']

# method to get the total number of reviews avilable for each rating
def number(devdata):
    data = devdata
    print(devdata)
    name = data[0]
    pc = data[1]
    ram = data[2]
    rom = data[3]
    color = data[4]
    driver = webdriver.Chrome()
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=one_star&pageNumber=1&sortBy=recent')
        # driver.implicitly_wait(3)
        oner = driver.find_element_by_xpath('//*[@id="filter-info-section"]/div[2]/span').text
        oner = oner.replace('|','')
        oner = oner.replace(',','')
        tmp1 = re.findall(r'\d+',oner)
        res1 = list(map(int,tmp1))
        oner = int(res1[1])
        # one_star_scrap(pc,oner,ram,rom,color)
    except NoSuchElementException:
        pass

    # getting the number of two_star reviews
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=two_star&pageNumber=1&sortBy=recent')
        twor = driver.find_element_by_xpath('//*[@id="filter-info-section"]/div[2]/span').text
        twor = twor.replace('|','')
        twor = twor.replace(',','')
        tmp2 = re.findall(r'\d+',twor)
        res2 = list(map(int,tmp2))
        twor = int(res2[1])
        # two_star_scrap(pc,twor,ram,rom,color)
    except NoSuchElementException:
        pass

    # getting the number of three_star reviews
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=three_star&pageNumber=1&sortBy=recent')
        threer = driver.find_element_by_xpath('//*[@id="filter-info-section"]/div[2]/span').text
        threer = threer.replace('|','')
        threer = threer.replace(',','')
        tmp3 = re.findall(r'\d+',threer)
        res3 = list(map(int,tmp3))
        threer = int(res3[1])
        # three_star_scrap(pc,threer,ram,rom,color)
    except NoSuchElementException:
        pass

    # getting the number of four_star reviews
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=four_star&pageNumber=1&sortBy=recent')
        fourr = driver.find_element_by_xpath('//*[@id="filter-info-section"]/div[2]/span').text
        fourr = fourr.replace('|','')
        fourr = fourr.replace(',','')
        tmp4 = re.findall(r'\d+',fourr)
        res4 = list(map(int,tmp4))
        fourr = int(res4[1])
        # four_star_scrap(pc,fourr,ram,rom,color)
    except NoSuchElementException:
        pass
    # getting the number of five_star reviews
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=five_star&pageNumber=1&sortBy=recent')
        fiver = driver.find_element_by_xpath('//*[@id="filter-info-section"]/div[2]/span').text
        fiver = fiver.replace('|','')
        fiver = fiver.replace(',','')
        tmp5 = re.findall(r'\d+',fiver)
        res5 = list(map(int,tmp5))
        fiver = int(res5[1])
        # five_star_scrap(pc,fiver,ram,rom,color)
    except NoSuchElementException:
        pass
    driver.quit()

    # printing the breakup of reviews along ratings
    try:
        print('1 Star: '+str(oner))
    except Exception as e:
        print(e)
        pass
    try:
        print('2 Star: '+str(twor))
    except Exception as e:
        print(e)
        pass
    try:
        print('3 Star: '+str(threer))
    except Exception as e:
        print(e)
        pass
    try:
        print('4 Star: '+str(fourr))
    except Exception as e:
        print(e)
        pass
    try:
        print('5 Star: '+str(fiver))
    except Exception as e:
        print(e)
        pass
    reviewnumber = [oner,twor,threer,fourr,fiver]
    return(reviewnumber)