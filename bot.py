from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import sub
from decimal import Decimal
import selenium.common.exceptions
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs


class Instabot:
    def __init__(self, username, password, OtherUserId,):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(5)
        self.driver.get("https://www.instagram.com/"+OtherUserId)
        pic = self.driver.find_element_by_class_name("_9AhH0")
        pic.click()
        sleep(2)
        like = self.driver.find_element_by_class_name('fr66n')
        soup = bs(like.get_attribute('innerHTML'), 'html.parser')
        if(soup.find('svg')['aria-label'] == 'Like'):
            like.click()
        sleep(1)
       # next = self.driver.find_element_by_class_name(
        #   "coreSpriteRightPaginationArrow")
       # sleep(1)
        while(True):
            next_element = self.driver.find_element_by_class_name(
                "coreSpriteRightPaginationArrow")
            if next_element != False:
                next_element.click()
                sleep(2)
                like_button = self.driver.find_element_by_class_name('fr66n')
                soup = bs(like_button.get_attribute(
                    'innerHTML'), 'html.parser')
                if(soup.find('svg')['aria-label'] == 'Like'):
                    like_button.click()
                sleep(2)

            else:
                print('not found')
                break
    sleep(20)


Instabot('username', 'password', 'AnyInstaUserID')
