from django.contrib.auth import get_user_model
from django.db.models import F


def url_count_changer(request, is_increase: bool):
    count_number = 1 if is_increase else -1
    user = get_user_model().objects.filter(pk=request.user.pk)

    # 더한값이 0보다 작으면 0, 그렇지 않으면 update
    if user.first().url_count + count_number < 0:
        user.update(url_count=0)
    else:
        user.update(url_count=F("url_count") + count_number)
