from django.http import JsonResponse


def not_found(request, *args, **kwargs):
    return JsonResponse(data={"message": "Not Found"}, status=404)


def app_error(request, *args, **kwargs):
    return JsonResponse(data={"message": "Server Error"}, status=500)
