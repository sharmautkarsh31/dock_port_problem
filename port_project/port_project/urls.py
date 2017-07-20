from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from test1.views import PortViewset, ContainerPositionViewset

router= routers.DefaultRouter()
router.register(r'port', PortViewset)
router.register(r'container_naming', ContainerPositionViewset)
urlpatterns = (
    # Examples:
    # url(r'^$', 'port_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
