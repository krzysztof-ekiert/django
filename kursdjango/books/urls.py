from django.urls import path

from books.views import biblioteka

urlpatterns= [


    path('', biblioteka, name="books"),

]