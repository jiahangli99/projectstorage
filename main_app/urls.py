from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('projects/', views.projects_index, name='projects'),
path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
path('project/<int:project_id>/', views.project_detail, name='detail'),
path('project/<int:pk>/update', views.ProjectUpdate.as_view(), name='project_update'),
path('project/<int:pk>/delete', views.ProjectDelete.as_view(), name='project_delete'),
path('project/<int:project_id>/add_date/', views.add_date, name='add_date'),
path('status/', views.StatusList.as_view(), name='status_index'),
path('status/<int:pk>/', views.StatusDetail.as_view(), name='status_detail'),
path('status/create/', views.StatusCreate.as_view(), name='status_create'),
path('status/<int:pk>/update/', views.StatusUpdate.as_view(), name='status_update'),
path('status/<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),
 path('project/<int:project_id>/assoc_status/<int:status_id>/', views.assoc_status, name='assoc_status'),
]

