import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



def get_driver():
    caps = {}
    caps['platformName'] = 'Android'
    caps['automationName'] = 'uiautomator2'
    # caps['platformVersion'] = '10'
    caps['platformVersion'] = '5.1.1'
    caps['unicodeKeyboard'] = True
    caps['resetKeyboard'] = True
    caps['noReset']=True
    caps['deviceName'] = '172.0.0.1:62025'
    # caps['deviceName'] = 'a7da3f26'
    caps['appPackage'] = 'com.hoolai.moego'
    caps['appActivity'] = '.ui.activity.login.WelcomPageActivity'
    caps['newCommandTimeout']=6000
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    y0 = y * 0.5
    x1 = x * 0.8
    x2 = x * 0.2

    try:
        WebDriverWait(driver,5,0.5).until(lambda x:x.find_element_by_id('com.hoolai.moego:id/swipe'))
        driver.swipe(x1, y0, x2, y0, duration=500)
        time.sleep(2)
        driver.swipe(x1, y0, x2, y0, duration=500)
        WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_id('com.hoolai.moego:id/btn_guide_enter')).click()
        try:
            loc = ("xpath", "//*[@text='始终允许']")
            WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located(loc)).click()
        except Exception:
            pass
        finally:

            WebDriverWait(driver, 3, 0.5).until(lambda x: x.find_element_by_xpath('//*[contains(@text,"我知道")]')).click()
            a=WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_elements_by_id('com.hoolai.moego:id/iv_close'))
            a[1].click()
            # b=a[1].location
            # print(b)
            # TouchAction(driver).press(a[1]).release().perform()
            # TouchAction(driver).tap(x=b.get('x'),y=b.get('y')).release().perform()

    except Exception:
        pass
    return driver
if __name__ == '__main__':
    get_driver()