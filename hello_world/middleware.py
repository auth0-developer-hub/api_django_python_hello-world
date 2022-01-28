from django.utils.cache import add_never_cache_headers


class Auth0Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Expires'] = 0
        add_never_cache_headers(response)
        response['X-XSS-Protection'] = 0
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
