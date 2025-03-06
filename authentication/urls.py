from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('authentication/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('authentication/token/verify',TokenVerifyView.as_view(), name='token_verify')
]

# testar esse endpoint usando o mthod http POST passando o username e password para vermos o request e response de token, se o username e paassword for válido no bd, ele gerará um token que deverá ser usado para acessar o entpoints protegidos, se inválido devolverá uma menssagem com status code 401
''' 
{
   "username":"teste1",
    "password":"testenever123"
} '''