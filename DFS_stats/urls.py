from django.conf.urls import include, url
from rest_framework import routers
from playerAPI import views
from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'QB', views.QuarterBackViewSet)
router.register(r'RB', views.RunningBackViewSet)
router.register(r'WR', views.WideReceiverViewSet)
router.register(r'TE', views.TightEndViewSet)
router.register(r'DEF', views.DefenseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
