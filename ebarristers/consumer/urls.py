from django.urls import path
from . import views

app_name = "consumer"

urlpatterns = [
	path('', views.CreateConsumerView.as_view(), name = "new_c"),
	path('complaints/',views.ConsumerListView.as_view(),name='list_c'),
    path('<uuid:pk>/', views.ConsumerDetailView.as_view(), name='detail_c'),
	path('<uuid:pk>/payment/',views.payment, name='payment'),
    path('<uuid:pk>/handlerequest/', views.handlerequest, name = "HandleRequest"),
	path('<uuid:pk>/update/', views.UpdateConsumerView.as_view(), name='update_c'),

]
