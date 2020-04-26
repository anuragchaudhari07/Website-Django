from django.urls import path
from . import views

app_name = "divorce"

urlpatterns = [
	path('', views.CreateDivorceView.as_view(), name = "new_d"),
	path('complaints/',views.DivorceListView.as_view(),name='list_d'),
    path('<uuid:pk>/', views.DivorceDetailView.as_view(), name='detail_d'),
	path('<uuid:pk>/payment/',views.payment, name='payment'),
    path('<uuid:pk>/handlerequest/', views.handlerequest, name = "HandleRequest"),
	path('<uuid:pk>/update/', views.UpdateDivorceView.as_view(), name='update_d'),

]
