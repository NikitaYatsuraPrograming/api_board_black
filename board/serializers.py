from rest_framework import serializers

from board.models import Publications, Comments


class CommentDetailSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comments
        fields = "__all__"


class PublicationDetailSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # amount_of_upvotes = serializers.HiddenField(default='0')

    class Meta:
        model = Publications
        fields = "__all__"


class AmountOfUpvotesResetSerializer(serializers.ModelSerializer):
    amount_of_upvotes = serializers.HiddenField(default="0")

    class Meta:
        model = Publications
        fields = ("amount_of_upvotes",)
