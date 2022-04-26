from rest_framework import viewsets, views, status
from rest_framework.response import Response
from django.db.models import Q

from apps.posts import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = models.Like.objects.all()
    serializer_class = serializers.LikeSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AnalyticAPIView(views.APIView):
    def get(self, request):
        try:
            dates = dict(request.query_params)

            like_count = models.Like.objects.filter(Q(
                date__range=[
                    dates['date_from'][0],
                    dates['date_to'][0]]
            )
            ).count()

            return Response(
                {'date_from': dates['date_from'][0],
                 'date_to':  dates['date_to'][0],
                 'like_by_period': f'{like_count}'},
                status=status.HTTP_200_OK)

        except:
            return Response(
                {'status': 'any problems with Analytics features'},
                status=status.HTTP_400_BAD_REQUEST)

