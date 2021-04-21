from rest_framework import routers
from testapp.views import EmailTestingViews,TestEmailViews
router = routers.SimpleRouter()
router.register(r'', EmailTestingViews, basename='email')
router.register(r'email', TestEmailViews, basename='insert-email')

urlpatterns = router.urls
