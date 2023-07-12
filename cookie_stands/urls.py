from django.urls import path
from .views import CookieStandList, CookieStandDetail

urlpatterns = [
    path("", CookieStandList.as_view(), name="Cookie_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="Cookie_detail"),
]
