
from django.urls import path
from accounts.views import registration,login
app_name='accounts'


urlpatterns=[
    path("",registration,name="registration"),
    path("accounts/",login,name="login"),

]

    