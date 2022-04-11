from django.urls import path
from helloapp.views import HelloWorldView, HelloView 

urlpatterns = [
    # helloapp/
    path('helloapp/', HelloWorldView.as_view(), name='hello_world'),
    path('<name>', HelloView.as_view(), name='hello_name'),
]