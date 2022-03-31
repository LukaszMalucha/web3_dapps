from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

app_name = "api"

router = DefaultRouter()
router.register("tokens", views.TokenModelViewSet, basename="tokens")


urlpatterns = [
    path("", include(router.urls)),
    path("account-balance/", views.AccountBalanceView.as_view(), name="account-balance"),
    path("token-supply/", views.TokenSupplyView.as_view(), name="token-supply"),
]
