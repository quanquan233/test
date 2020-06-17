from Page.Me_Page import Me_Page
from Page.Login_Page import Login_Page
class Page_Obj():
    def __init__(self,driver):
        self.driver=driver
   #返回我页面对象
    def me_page_obj(self):
        return Me_Page(self.driver)
    #返回登录页面对象
    def login_page_obj(self):
        return Login_Page(self.driver)