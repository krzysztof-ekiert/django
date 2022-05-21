from django.urls import path

from main.views import hello
from main.views import custom_greetings
from books.views import biblioteka

urlpatterns= [


    path('', hello, name="hello"),
    path('<text>/', hello, name="hello2"),
    path('<s1>/<s2>', custom_greetings, name="cg"),
    path('books', biblioteka, name="biblioteka"),

]