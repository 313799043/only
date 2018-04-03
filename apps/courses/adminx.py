import xadmin
from xadmin import views
class GlobalSettings(object):
    site_title = "xadmin.py文件GlobalSettings..site_title"
    site_footer = "xadmin.py文件GlobalSettings..site_footer"
# menu_style = "accordion" #是否收藏起来APP库
# 结局收起来显示名称为英文，解决方法：
# 1.APP项目目录里，appsAPP项目目录里，apps.py 添加行 verbose_name=u"名称"
# 2.同路径下__init__.py 文件下添加default_app_config = "项目.apps.OperationConfig"
# xadmin.site.register(views.CommAdminView, GlobalSettings)
