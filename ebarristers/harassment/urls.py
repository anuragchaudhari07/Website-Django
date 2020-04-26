from django.urls import path
from . import views

app_name = "harassment"

urlpatterns = [
	path('', views.CreateHarassmentView.as_view(), name = "new_h"),
	path('complaints/',views.HarassmentListView.as_view(),name='list_h'),
    path('<uuid:pk>/', views.HarassmentDetailView.as_view(), name='detail_h'),
	path('<uuid:pk>/payment/',views.payment, name='payment'),
    path('<uuid:pk>/handlerequest/', views.handlerequest, name = "HandleRequest"),
	path('<uuid:pk>/update/', views.UpdateHarassmentView.as_view(), name='update_h'),


]
