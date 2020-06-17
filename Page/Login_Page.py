import Page
from Base.Base import Base

class Login_Page(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击我按钮
    def click_layout_my(self):
        self.click_element(Page.layout_my)
    # 点击登录按钮
    def click_login(self):
        self.click_element(Page.login)
    #输入手机号
    def input_et_username(self,phone):
        self.input_element(Page.et_username,phone)
    #清除手机号
    def clean_et_username(self):
        self.find_element(Page.et_username).clear()
    #输入密码
    def input_et_password(self,passwd):
        self.input_element(Page.et_password,passwd)
    #清除密码
    def clean_et_password(self):
        self.find_element(Page.et_password).clear()
    #清除手机号
    def click_ivCleanphone(self):
        self.click_element(Page.ivCleanphone)
    #展示密码
    def click_iv_show_pwd(self):
        self.click_element(Page.iv_show_pwd)
    #点击登录按钮
    def click_btn_login(self):
        self.click_element(Page.btn_login)
    #点击注册按钮
    def click_btb_register(self):
        self.click_element(Page.btn_register)
    #点击QQ按钮
    def click_iv_qq_login(self):
        self.click_element(Page.iv_qq_login)
    #点击微信按钮
    def click_iv_weixin_login(self):
        self.click_element(Page.iv_weixin_login)
    #点击微博按钮
    def click_iv_sina_login(self):
        self.click_element(Page.iv_sina_login)
    #点击萌股协议选择按钮
    def click_ckbox_login_icon(self):
        self.click_element(Page.ckbox_login_icon)
    #点击萌股协议文字
    def click_txt_login_agree(self):
        self.click_element(Page.txt_login_agree)
    #点击注册页返回按钮
    def click_rl_Back(self):
        self.click_element(Page.rl_Back,timeout=20)
    #