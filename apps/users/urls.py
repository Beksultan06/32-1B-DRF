from rest_framework.routers import SimpleRouter
from apps.users.views import AuthViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
router = SimpleRouter()
router.register(r"users", AuthViewSet, basename='users')


urlpatterns = [
    path('users/refresh', TokenRefreshView.as_view())
]

urlpatterns = router.urls