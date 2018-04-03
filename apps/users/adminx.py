import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _


from .models import EmailVerifyRecord, Banner, UserProfile







"""

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
"""





class BannerAdmin(object):



    # list_display = ['image', 'index', 'title']
    # search_fields =['image', 'index', 'title']
    list_filter = ['image', 'index', 'title']
    # model_icon = 'fa fa-address-book-o'


xadmin.site.register(Banner, BannerAdmin)
#
# class UserProfileAdmin(UserAdmin):
#     def get_form_layout(self):
#         if self.org_obj:
#             self.form_layout = (
#                 Main(
#                     Fieldset('',
#                              'username', 'password',
#                              css_class='unsort no_title'
#                              ),
#                     Fieldset(_('Personal info'),
#                              Row('first_name', 'last_name'),
#                              'email'
#                              ),
#                     Fieldset(_('Permissions'),
#                              'groups', 'user_permissions'
#                              ),
#                     Fieldset(_('Important dates'),
#                              'last_login', 'date_joined'
#                              ),
#                 ),
#                 Side(
#                     Fieldset(_('Status'),
#                              'is_active', 'is_staff', 'is_superuser',
#                              ),
#                 )
#             )
#         return super(UserAdmin, self).get_form_layout()
#
# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True
#
# class GlobalSettings(object):
#     site_title = "慕学后台管理系统"
#     site_footer = "慕学在线网"
#     # menu_style = "accordion"
#
# class EmailVerifyRecordAdmin(object):
#     list_display = ['code', 'email', 'send_type', 'send_time']
#     search_fields = ['code', 'email', 'send_type']
#     list_filter = ['code', 'email', 'send_type', 'send_time']
#     model_icon = 'fa fa-address-book-o'
#
# class BannerAdmin(object):
#     list_display = ['title', 'image', 'url', 'index', 'add_time']
#     search_fields = ['title', 'image', 'url', 'index']
#     list_filter = ['title', 'image', 'url', 'index', 'add_time']


# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
# xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# xadmin.site.register(Banner, BannerAdmin)
# # xadmin.site.register(UserProfile, UserProfileAdmin)
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSettings)
#








