#!/usr/bin/env python3

# Importing Libraries
from pyvirtualdisplay import Display
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import re


'''

Comment out the below 4 lines if system environment is Windows.

'''


def mens_fashion():

    # Locating the presence of elements on category page.

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()
        

    xpath_generator ='//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[2]/ul/li[2]/a'

    split_cat_xpath=xpath_generator.split('li[2]')



    for i in range(1,17):

    # Generating xpath for all sub categories
    
        sub_category=split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
        print(sub_category)

        mens_fashion=driver.find_element_by_xpath(sub_category)
        driver.execute_script('arguments[0].click();',mens_fashion)

        page=1

        xpath='//*[@id="result_i"]/div/div[3]/div[1]/a'

        prod_xpath=xpath.split('_i')

        page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

        while(page<int(page_number)):
            
            product_ids=[]
            
            print("Done: {:.2f}%".format(page/int(page_number) * 100), end='\r')

            li_tags_in_page=driver.find_elements_by_tag_name('li')
            time.sleep(2)

            for i in range(0,len(li_tags_in_page)):
                tags_with_id=li_tags_in_page[i].get_attribute('id')
                if tags_with_id!='':
                    e=tags_with_id.split('result_')
                    product_ids.append(int(e[1]))

            for i in range(product_ids[0],product_ids[-1]):
                xpath_each_product=prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                try:
                    link=driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                    new_link=re.sub('/ref.*','',link)
                    thefile.writelines(new_link)
                    thefile.write('\n')


                except(NoSuchElementException or StaleElementReferenceException):
                    
                    print('Unable to find products on page')
                    
                    print(end='\r')
                    
            print(len(product_ids))
            
            page+=1

            try:

                next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                driver.execute_script('arguments[0].click();', next_page)
                time.sleep(2)

            except(NoSuchElementException or StaleElementReferenceException):
                
                print('Failed to load Current page. Proceeding to next.')
                
                continue

        print('\n')
        print('Catergory over.......\n Changing to new sub-category......')
        print('\n')
        driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

def women_fashion():
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[3]'))
        WebDriverWait(driver, timeout).until(element_present)
    
    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[3]/ul/li[1]/a'
    
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(2, 17):

        if i==15 or i==3:
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            womens = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',womens)
            page = 1
            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'
            prod_xpath = xpath.split('_i')
            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text
            while (page < int(page_number)):
                product_ids = []

                print("Done: {:.2f}%".format(page/int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)
                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id != '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]
                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')
                    except(NoSuchElementException or StaleElementReferenceException):
                        
                        print('Unable to find products on page')
                        print(end='\r')
                        
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):

                    print('Failed to load Current page. Proceeding to next.')

                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

def global_store():
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr/td[4]/div[5]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[4]/div[5]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')

    selected_categories=[1,2,3,4,8,9,10,11,12,13]
    for i in selected_categories:
        sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
        glob_store = driver.find_element_by_xpath(sub_category)
        driver.execute_script('arguments[0].click();',glob_store)

        page = 1

        xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'
        prod_xpath = xpath.split('_i')
        page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text
        while (page < int(page_number)):
            product_ids = []
            print("Done: {:.2f}%".format(page/int(page_number)*100), end='\r')
            li_tags_in_page= driver.find_elements_by_tag_name('li')
            time.sleep(2)
            for i in range(0, len(li_tags_in_page)):
                tags_with_id = li_tags_in_page[i].get_attribute('id')
                if tags_with_id != '':
                    e = tags_with_id.split('result_')
                    product_ids.append(int(e[1]))
            for i in range(product_ids[0], product_ids[-1]):
                xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]
                try:
                    link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                    new_link = re.sub('/ref.*', '', link)
                    thefile.writelines(new_link)
                    thefile.write('\n')
                except(NoSuchElementException or StaleElementReferenceException):
                    print(end='\r')
                    print('Unable to find products on page.')
            print(len(product_ids))
            page += 1

            try:

                next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                driver.execute_script('arguments[0].click();', next_page)
                time.sleep(2)

            except(NoSuchElementException or StaleElementReferenceException):
                print('Failed to load Current page. Proceeding to next.')
                continue

        print('\n')
        print('Catergory over.......\n Changing to new sub-category......')
        print('\n')
        driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')


def Sports_fitness():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[3]/div[3]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 19):

        if i==5 or i==12:
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            sports_fitness = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',sports_fitness)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id != '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')


                    except(NoSuchElementException or StaleElementReferenceException):
                        print(end='\r')
                        print('Unable to find products on page')
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')



def Tv_Appliancs_Electronics():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[1]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 18):

        selected_category=[7,9,11,12]

        if i in selected_category:
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            electronics = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',electronics)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id!= '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')


                    except(NoSuchElementException or StaleElementReferenceException):
                        print(end='\r')
                        print('Unable to find products on page')
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')


def Mobiles_Computers():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[1]/div[6]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 19):

        if i == 8 or i == 17 :
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            mobile = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',mobile)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id!= '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')


                    except(NoSuchElementException or StaleElementReferenceException):
                        print(end='\r')
                        print('Unable to find products on page')
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

def Home_Kitchen():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[3]/div[1]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 18):

        selected_category=[3,5,7,8,9,13,14,15,16]

        if i in selected_category :
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            home_kitchen = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',home_kitchen)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id!= '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')


                    except(NoSuchElementException or StaleElementReferenceException):
                        print('Unable to find products on page')
                        print(end='\r')
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

def Toys_Baby_kids():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[3]/div[4]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 18):

        selected_category=[1,2,4,5,11,12,13,14]
        if i in selected_category :
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            toy_baby = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',toy_baby)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id!= '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')


                    except(NoSuchElementException or StaleElementReferenceException):
                        print('Unable to find products on page')
                        print(end='\r')
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')


def Cars_Motorbikes():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[4]/div[1]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 11):

        if i == 6 or i == 7 :
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            car_bike = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',car_bike)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id!= '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')


                    except(NoSuchElementException or StaleElementReferenceException):
                        print('Unable to find products on page')
                        print(end='\r')
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

def Books():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[4]/div[2]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 11):

        if i == 1:
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            Books = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',Books)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id!= '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')


                    except(NoSuchElementException or StaleElementReferenceException):
                        print('Unable to find products on page')
                        print(end='\r')
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')


def Movies_Music_Videogames():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[4]/div[3]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 16):

        if i == 1 or i==10 or i==11:
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            movies_games = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',movies_games)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id!= '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')


                    except(NoSuchElementException or StaleElementReferenceException):
                        print('Unable to find products on page')
                        print(end='\r')
                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

def Giftcards():

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("May be you are not connected to internet")
        driver.quit()

    xpath_generator = '//*[@id="shopAllLinks"]/tbody/tr/td[4]/div[4]/ul/li[1]/a'
    split_cat_xpath = xpath_generator.split('li[1]')
    for i in range(1, 8):

        if i == 1 :
            continue
        else:
            sub_category = split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
            gift = driver.find_element_by_xpath(sub_category)
            driver.execute_script('arguments[0].click();',gift)

            page = 1

            xpath = '//*[@id="result_i"]/div/div[3]/div[1]/a'

            prod_xpath = xpath.split('_i')

            page_number = driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text

            while (page < int(page_number)):
                product_ids = []
                print("Done: {:.2f}%".format(page / int(page_number) * 100), end='\r')

                li_tags_in_page = driver.find_elements_by_tag_name('li')
                time.sleep(2)

                for i in range(0, len(li_tags_in_page)):
                    tags_with_id = li_tags_in_page[i].get_attribute('id')
                    if tags_with_id!= '':
                        e = tags_with_id.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    xpath_each_product = prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                    try:
                        link = driver.find_element_by_xpath(xpath_each_product).get_attribute('href')
                        new_link = re.sub('/ref.*', '', link)
                        thefile.writelines(new_link)
                        thefile.write('\n')

                    except(NoSuchElementException or StaleElementReferenceException):
                        print('Unable to find products on page')
                        print(end='\r')

                print(len(product_ids))
                page += 1

                try:

                    next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                    driver.execute_script('arguments[0].click();', next_page)
                    time.sleep(2)

                except(NoSuchElementException or StaleElementReferenceException):
                    print('Failed to load Current page. Proceeding to next.')
                    continue

            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')




if __name__ == '__main__':

    display = Display(visible = 0, size = (800, 800))
    display.start()
    driver = webdriver.Chrome()

    url='https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820'
    driver=webdriver.Chrome()
    driver.get(url)
    timeout=200

    filepath='crawl_categories.txt'
    thefile = open('product-links', 'w')

    with open(filepath) as fp:
        line=fp.readlines()


    dict_category_function={
                            'Mens Fashion': mens_fashion,
                            'Womens Fashion': women_fashion,
                            'Global Store': global_store,
                            'Sports and Fitness': Sports_fitness,
                            'Electronics': Tv_Appliancs_Electronics,
                            'Mobiles and Computers': Mobiles_Computers,
                            'Home and Kitchen': Home_Kitchen,
                            'Baby toys, fashion,kids': Toys_Baby_kids,
                            'Cars and MotorBikes': Cars_Motorbikes,
                            'Books': Books,
                            'Movies, music and games': Movies_Music_Videogames,
                            'Gift Cards': Giftcards
                            }


    for i in range(len(line)):
        choice=str(line[i]).replace('\n','')
        
        

        try:

            dict_category_function[choice]()
            print(str(choice) + ': Done')

        except(KeyError):

            print('Please check the category you entered')

    driver.quit()

    thefile.close()
