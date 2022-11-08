from django.urls import path

from .views import event, organizer, competitor, foundings, subjects

urlpatterns = [
    # Organizer levels
    path('organizer_levels/', organizer.LevelsListAPIView.as_view()),

    # Organizers
    path('organizer/', organizer.ListCreateAPIView.as_view()),
    path('organizer/<int:pk>', organizer.RetrieveUpdateDestroyAPIView.as_view()),

    # Competitor Types
    path('competitors/', competitor.ListView.as_view()),

    # Founding Types
    path('founding_types/', foundings.TypeListView.as_view()),

    # Founding Range
    path('founding_range/', foundings.FoundingRangeListCreateAPIView.as_view()),
    path('founding_range/<int:pk>', foundings.FoundingRangeRetrieveUpdateDestroyView.as_view()),

    path('co_founding_range/', foundings.CoFoundingCreateAPIView.as_view()),
    path('co_founding_range/<int:pk>', foundings.CoFoundingRangeRetrieveUpdateDestroyAPIView.as_view()),

    # Event
    path('event/', event.ListCreateAPIView.as_view()),
    path('event/<int:pk>/', event.RetrieveUpdateDestroyAPIView.as_view()),
    path('event/<int:pk>/minimal', event.MinimalRetrieveAPIView.as_view()),

    # Subjects
    path('subject/event/<int:event>/', subjects.ListByEventAPIView.as_view()),
    path('subject/id/<int:pk>/', subjects.RetrieveUpdateDestroyAPIView.as_view())
]
