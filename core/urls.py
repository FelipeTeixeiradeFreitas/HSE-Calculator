from django.urls import path
from .views import tabela_dados, AjaxNextLevel, AjaxNextLevel2

urlpatterns = [
    path('tabela_dados/', tabela_dados.as_view(), name='tabela_dados'),
    path('tabela_dados/next_level1/', AjaxNextLevel.as_view(), name='next_level1'),
    path('tabela_dados/next_level2/', AjaxNextLevel2.as_view(), name='next_level2'),
]