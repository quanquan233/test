from  Base.Base import Base
import Page

class Me_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击我按钮
    def click_layout_my(self):
        self.click_element(Page.layout_my)
    #点击登录按钮
    def click_login(self):
        self.click_element(Page.login)
    #点击注册按钮
    def click_register(self):
        self.click_element(Page.register)
    #点击关注按钮
    def click_rlAttention(self):
        self.click_element(Page.rlAttention)
    #点击粉丝按钮
    def click_rlFans(self):
        self.click_element(Page.rlFans)
    #点击动态按钮
    def click_rlCard(self):
        self.click_element(Page.rlCard)
    #点击banner
    def click_vp_banner(self):
        self.click_element(Page.vp_banner)
    #点击萌股会员按钮
    def click_vip(self):
        self.click_element(Page.vip)
    #点击萌股商城
    def click_shopping(self):
        self.click_element(Page.shopping)
    #点击真爱标签
    def click_label(self):
        self.click_element(Page.label)
    #点击信誉分
    def click_credit(self):
        self.click_element(Page.credit)
    #点击我的收藏
    def click_collection(self):
        self.click_element(Page.collection)
    #点击浏览历史
    def click_history(self):
        self.click_element(Page.history)
    #点击联系客服
    def click_start_customerservice(self):
        self.click_element(Page.start_customerservice)
    #点击设置
    def click_more_setup(self):
        self.click_element(Page.more_setup)
    #点击登录页的返回按钮
    def click_ly_return(self):
        self.click_element(Page.ly_return)
    #点击注册页的返回按钮
    def click_rl_Back(self):
        self.click_element(Page.rl_Back)