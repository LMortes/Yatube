from django.core.paginator import Paginator


def pg_views(request, arg_objects, count):
    page_number = request.GET.get('page')
    paginator = Paginator(arg_objects, count)
    result = paginator.get_page(page_number)
    return result
