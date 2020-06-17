import sys,os
import time
from selenium.webdriver.common.by import By
sys.path.append(os.getcwd())
from Page.Page_obj import Page_Obj
from Base.init_driver import get_driver
from Base.Read_Data import return_yaml
import pytest
import allure
#异常账号数据
def testaccount_data():
    data = return_yaml('account.yaml')
    a = data.get('testaccount')
    x = []
    for i in a.keys():
        b = a.get(i)
        x.append(((i, b.get('phone'), b.get('passwd'),b.get('assert'))))
    return x
#正常账号数据
def rightaccount_data():
    data = return_yaml('account.yaml')
    a = data.get('rightaccount')
    x = []
    for i in a.keys():
        b = a.get(i)
        x.append(((b.get('phone'), b.get('passwd'),b.get('assert'))))
    return x
class Test_Login_Page:
    def setup_class(self):
        self.driver=get_driver()
        self.obj=Page_Obj(self.driver).login_page_obj()
        self.obj.click_layout_my()
        self.obj.click_login()

    @allure.step(title='测试账号密码异常情况')
    #测试账号密码异常情况
    @pytest.mark.parametrize('index,phone,passwd,asser',testaccount_data())
    def test_login_failed(self,index,phone,passwd,asser):
        allure.attach('%s,%s,%s'%(index,phone,passwd))
        self.obj.input_et_username(phone)
        self.obj.input_et_password(passwd)
        self.obj.click_btn_login()
        self.obj.clean_et_username()
        self.obj.clean_et_password()
        value='//*[contains(@text,\"'+asser+'\")]'
        assert self.obj.find_element((By.XPATH,value),timeout=5,poll=0.1)
    @allure.step(title='测试注册按钮')
    #测试注册按钮
    def test_btb_register(self):
        self.obj.click_btb_register()
        self.obj.click_rl_Back()

    @allure.step(title='测试同意萌股协议按钮')
    #测试同意萌股协议按钮
    def test_ckbox_login_icon(self):
        self.obj.click_ckbox_login_icon()
        self.obj.click_ckbox_login_icon()

    @allure.step(title='测试萌股协议')
    #测试萌股协议
    def test_txt_login_agree(self):
        self.obj.click_txt_login_agree()
        self.obj.click_rl_Back()

    @allure.step(title='测试正常登陆')
    #测试正常登陆
    @pytest.mark.parametrize('phone,passwd,asser',rightaccount_data())
    def test_login_success(self,phone,passwd,asser):
        self.obj.input_et_username(phone)
        self.obj.click_ivCleanphone()
        self.obj.input_et_username(phone)
        self.obj.input_et_password(passwd)
        self.obj.click_iv_show_pwd()
        self.obj.click_btn_login()
        value='//*[contains(@text,\"'+asser+'\")]'
        assert self.obj.find_element((By.XPATH,value),timeout=3,poll=0.1)