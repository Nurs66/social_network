from django.utils import timezone

from apps.users.models import User


class UserLastActivityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user.last_activity = timezone.now()
            user.save()
