from  django.http import JsonResponse

def not_found_404(request):
    return JsonResponse({
            'error': 'Not found',
            'message': 'Not found'
        }, status=404
    )