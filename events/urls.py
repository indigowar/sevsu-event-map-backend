from django.urls import path

from events import views

urlpatterns = [
    # Organizer levels
    path('organizer_levels/', views.OrganizerLevelListView.as_view()),

    # Organizers
    path('organizer/', views.OrganizerListCreateView.as_view()),
    path('organizer/<int:pk>', views.OrganizerRetrieveUpdateDestroyView.as_view()),

    # Competitor Types
    path('competitors/', views.CompetitorsListView.as_view()),

    # Founding Types
    path('founding_types/', views.FoundingTypeListView.as_view()),

    # Founding Range
    path('founding_range/', views.FoundingRangeListCreateAPIView.as_view()),
    path('founding_range/<int:pk>', views.FoundingRangeRetrieveUpdateDestroyView.as_view()),

    path('event/<int:pk>/', views.EventView.as_view()),
    path('event/<int:pk>/minimal', views.MinimalEventView.as_view())
]
