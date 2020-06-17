import allure
import sys,os
from time import sleep

sys.path.append(os.getcwd())
from Page.Page_obj import Page_Obj
from Base.init_driver import get_driver

class Test_Me_Page:
    def setup_class(self):
        self.driver=get_driver()
        self.obj=Page_Obj(self.driver).me_page_obj()
        self.obj.click_layout_my()
    def teardown_class(self):
        self.driver.quit()
    @allure.step('测试未登录登录按钮')
    #测试未登录登录按钮
    def test_login(self):
        self.obj.click_login()
        self.obj.click_ly_return()
    @allure.step('测试未登录注册按钮')
    #测试未登录注册按钮
    def test_register(self):
        self.obj.click_register()
        self.obj.click_rl_Back()

    @allure.step('测试未登录关注按钮')
    # 测试未登录关注按钮
    def test_rlAttention(self):
        self.obj.click_rlAttention()
        self.obj.click_ly_return()

    @allure.step('测试未登录粉丝按钮')
    #测试未登录粉丝
    def test_rlFans(self):
        self.obj.click_rlFans()
        self.obj.click_ly_return()

    @allure.step('测试未登录动态按钮')
    #测试未登录动态按钮
    def test_rlCard(self):
        self.obj.click_rlCard()
        self.obj.click_ly_return()

    @allure.step('测试未登录banner跳转')
    # 测试未登录banner跳转
    def test_vp_banner(self):
        self.obj.click_vp_banner()
        self.obj.click_ly_return()

    @allure.step('测试未登录萌股会员按钮')
    #测试未登录萌股会员按钮
    def test_vip(self):
        self.obj.click_vip()
        self.obj.click_ly_return()

    @allure.step('测试未登录萌股商城按钮')
    #测试未登录萌股商城按钮
    def test_shopping(self):
        self.obj.click_shopping()
        self.obj.click_ly_return()

    @allure.step('测试未登录真爱标签按钮')
    #测试未登录真爱标签按钮
    def test_label(self):
        self.obj.click_label()
        self.obj.click_ly_return()
        sleep(1)
        self.obj.swipe_up()
        sleep(1)

    @allure.step('测试未登录信誉分按钮')
    #测试未登录信誉分按钮
    def test_credit(self):
        self.obj.click_credit()
        self.obj.click_ly_return()

    @allure.step('测试未登录我的收藏按钮')
    #测试未登录我的收藏按钮
    def test_collectio(self):
        self.obj.click_collection()
        self.obj.click_ly_return()

    @allure.step('测试未登录浏览历史按钮')
    #测试未登录浏览历史按钮
    def test_history(self):
        self.obj.click_history()
        self.obj.click_ly_return()

    @allure.step('测试未登录联系客服按钮')
    #测试未登录联系客服按钮
    def test_customerservice(self):
        self.obj.click_start_customerservice()
        self.obj.click_ly_return()

    @allure.step('测试未登录设置按钮按钮')
    #测试未登录设置按钮按钮
    def test_more_setup(self):
        self.obj.click_more_setup()
        self.obj.click_rl_Back()

