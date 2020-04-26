from django.urls import path
from . import views

app_name = "domestic"

urlpatterns = [
	path('', views.CreateDomesticView.as_view(), name = "new_do"),
	path('complaints/',views.DomesticListView.as_view(),name='list_do'),
    path('<uuid:pk>/', views.DomesticDetailView.as_view(), name='detail_do'),
	path('<uuid:pk>/payment/',views.payment, name='payment'),
    path('<uuid:pk>/handlerequest/', views.handlerequest, name = "HandleRequest"),
	path('<uuid:pk>/update/', views.UpdateDomesticView.as_view(), name='update_do'),

]
