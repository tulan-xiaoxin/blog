from django.conf.urls import url

from App import views

urlpatterns = [

    url(r'^homeblog/',views.homeBlog,name='homeblog'),
    url(r'^addblog/',views.addBlog,name='addblog'),
    url(r'^addcontent/',views.addContent,name='addcontent'),
    url(r'^homecontent/(.*)',views.homeContent,name='homecontent'),
    url(r'^index/',views.index,name='index'),
    url(r'^detail/(.*)',views.detail,name='detail'),
    url(r'^add/',views.add,name='add'),
]
