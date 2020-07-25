from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from board.serializers import (
    PublicationDetailSerializer,
    CommentDetailSerializer,
    AmountOfUpvotesResetSerializer,
)

from board.models import Publications, Comments
from board.permissons import IsOwnerOrAdminReadOnly


class PublicationsListView(generics.ListAPIView):
    """
    Вывод всех публикаций
    """

    serializer_class = PublicationDetailSerializer
    queryset = Publications.objects.all().order_by("-create_date")


class PublicationCreateView(generics.CreateAPIView):
    """
    Создание публикации
    """

    serializer_class = PublicationDetailSerializer
    permission_classes = (IsAuthenticated,)


class PublicationDetailView(generics.RetrieveAPIView):
    """
    Вывод одной публикации по id
    """

    serializer_class = PublicationDetailSerializer
    queryset = Publications.objects.all()


class PublicationUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Обновление, удаление данных публикации
    """

    serializer_class = PublicationDetailSerializer
    queryset = Publications.objects.all()
    permission_classes = (IsOwnerOrAdminReadOnly,)


class CommentCreateView(generics.CreateAPIView):
    """
    Создание комментария
    """

    serializer_class = CommentDetailSerializer
    permission_classes = (IsAuthenticated,)


class CommentDetailView(generics.RetrieveAPIView):
    """
    Вывод одного комментария по id
    """

    serializer_class = CommentDetailSerializer
    queryset = Comments.objects.filter()


@api_view(["GET"])
def comments(request, pk):
    """
    Вывод комментариев которые относятся к определенному посту

    :param request:
    :param pk:
    :return:
    """
    comment = Comments.objects.filter(publication=pk)
    print(comment)
    serializer = CommentDetailSerializer(comment, many=True)

    return Response(serializer.data)


class CommentUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Обновление, удаление данных комментария
    """

    serializer_class = CommentDetailSerializer
    queryset = Comments.objects.all()
    permission_classes = (IsOwnerOrAdminReadOnly,)


class AmountOfUpvotesResetView(generics.RetrieveUpdateAPIView):
    """
    Ресетим голоса при отправки PUT запроса на адресс
    """

    serializer_class = AmountOfUpvotesResetSerializer
    queryset = Publications.objects.all()
    permission_classes = (IsOwnerOrAdminReadOnly,)
