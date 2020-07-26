from django.urls import path
from board.views import (
    PublicationCreateView,
    PublicationsListView,
    PublicationUpdateDestroyView,
    CommentCreateView,
    CommentDetailView,
    comments,
    CommentUpdateDestroyView,
    AmountOfUpvotesResetView,
)

app_name = "board"
urlpatterns = [
    path("publication/create/", PublicationCreateView.as_view()),
    path("all/", PublicationsListView.as_view()),
    path(
        "publication/<int:pk>/reset_amount_of_upvotes",
        AmountOfUpvotesResetView.as_view(),
    ),
    path("publication/detail/<int:pk>/", PublicationUpdateDestroyView.as_view()),
    path(
        "publication/detail/comments/correction/<int:pk>/",
        CommentUpdateDestroyView.as_view(),
    ),
    path("publication/comments/create/", CommentCreateView.as_view()),
    path("publication/detail/<int:pk>/comments/", comments),
    path("publication/comment/<int:pk>/", CommentDetailView.as_view()),
]
