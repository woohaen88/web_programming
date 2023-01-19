from tags.models import Tag



def tag_list(request):
    qs = Tag.objects.all()
    return dict(tags=qs)