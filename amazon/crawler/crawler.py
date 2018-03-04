from selenium import webdriver
from urllib.error import HTTPError
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

url='https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820'
driver=webdriver.Chrome()
driver.get(url)
timeout=100

thefile = open('data_new.txt', 'w')

def mens_fashion():
    x='//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[2]/ul/li[2]/a'

    split_cat_xpath=x.split('li[2]')


    for i in range(1,17):

        sub_category=split_cat_xpath[0] + 'li[' + str(i) + ']' + split_cat_xpath[1]
        mens_fashion=driver.find_element_by_xpath(sub_category).click()

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
                c=li_tags_in_page[i].get_attribute('id')
                if c!='':
                    e=c.split('result_')
                    product_ids.append(int(e[1]))

            for i in range(product_ids[0],product_ids[-1]):
                abc=prod_xpath[0] + '_' + str(i) + prod_xpath[1]

                try:
                    link=driver.find_element_by_xpath(abc).get_attribute('href')
                    thefile.writelines(link)
                    thefile.write('\n')


                except(NoSuchElementException):
                    print(end='\r')
            print(len(product_ids))
            page+=1

            next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
            driver.execute_script('arguments[0].click();', next_page)
            time.sleep(2)

        print('\n')
        print('Catergory over.......\n Changing to new sub-category......')
        print('\n')
        driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

def women_fashion():
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[3]'))
        WebDriverWait(driver, timeout).until(element_present)
    
    except TimeoutException:
        print("Timed out waiting for page to load")
    
    x = '//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[3]/ul/li[1]/a'
    
    split_cat_xpath = x.split('li[1]')
    for i in range(1, 17):
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
            print(page_number)
            while (page < int(page_number)):
                product_ids = []

                print("Done: {:.2f}%".format(page/int(page_number) * 100), end='\r')

                b = driver.find_elements_by_tag_name('li')
                time.sleep(2)
                for i in range(0, len(b)):
                    c = b[i].get_attribute('id')
                    if c != '':
                        e = c.split('result_')
                        product_ids.append(int(e[1]))

                for i in range(product_ids[0], product_ids[-1]):
                    abc = prod_xpath[0] + '_' + str(i) + prod_xpath[1]
                    try:
                        link = driver.find_element_by_xpath(abc).get_attribute('href')
                        thefile.writelines(link)
                        thefile.write('\n')
                    except(NoSuchElementException):
                        print("Sponsored Links")
                print(len(product_ids))
                page += 1
                next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
                driver.execute_script('arguments[0].click();', next_page)
                time.sleep(2)
            print('\n')
            print('Catergory over.......\n Changing to new sub-category......')
            print('\n')
            driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

def global_store():
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="shopAllLinks"]/tbody/tr/td[4]/div[5]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    x = '//*[@id="shopAllLinks"]/tbody/tr/td[4]/div[5]/ul/li[1]/a'
    split_cat_xpath = x.split('li[1]')
    selected_categories=[1,2,4,9,11]
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
            b = driver.find_elements_by_tag_name('li')
            time.sleep(2)
            for i in range(0, len(b)):
                c = b[i].get_attribute('id')
                if c != '':
                    e = c.split('result_')
                    product_ids.append(int(e[1]))
            for i in range(product_ids[0], product_ids[-1]):
                abc = prod_xpath[0] + '_' + str(i) + prod_xpath[1]
                try:
                    link = driver.find_element_by_xpath(abc).get_attribute('href')
                    thefile.writelines(link)
                    thefile.write('\n')
                except(NoSuchElementException):
                    print('Sponsored Link')
             print(len(product_ids))
#            print(len(product_ids))
            page += 1
            next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
            driver.execute_script('arguments[0].click();', next_page)
            time.sleep(2)
        print('\n')
        print('Catergory over.......\n Changing to new sub-category......')
        print('\n')
        driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')

mens_fashion()
women_fashion()
global_store()

driver.quit()


thefile.close()

