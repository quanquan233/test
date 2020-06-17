from  appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))


    def find_elements(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def click_element(self,loc,timeout=5,poll=0.5):
        WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc)).click()

    def input_element(self,loc,text,timeout=5,poll=0.5,):
        WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc)).send_keys(text)
    def get_size(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y
    #左滑
    def swipe_left(self,duration=500):
        x,y=self.get_size()
        y1=y * 0.5
        x1=x * 0.8
        x2=x * 0.2
        self.driver.swipe(x1,y1,x2,y1,duration=duration)
    #上滑
    def swipe_up(self,duration=500):
        x, y = self.get_size()
        y1 = y * 0.8
        y2 = y * 0.2
        x1 = x * 0.5
        self.driver.swipe(x1, y1, x1, y2, duration=duration)
