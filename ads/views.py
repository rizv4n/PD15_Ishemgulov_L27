import json

from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import ADS


def main_page(request):
    return HttpResponse("{'status': 'ok'}", 200)


@method_decorator(csrf_exempt, name='dispatch')
class ADSView(View):
    def get(self, request):
        ads = ADS.objects.all()
        response = []
        for i in ads:
            response.append({
                'id': i.id,
                'name': i.name,
                'author': i.author,
                'price': i.price,
                'description': i.description,
                'address': i.address,
                'is_published': i.is_published
            })

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = ADS()
        ads.name = ads_data['name']
        ads.author = ads_data['author']
        ads.price = ads_data['price']
        ads.description = ads_data['description']
        ads.address = ads_data['address']
        ads.is_published = ads_data['is_published']
        ads.save()

        return JsonResponse({
                'id': ads.id,
                'name': ads.name,
                'author': ads.author,
                'price': ads.price,
                'description': ads.description,
                'address': ads.address,
                'is_published': ads.is_published
            }, json_dumps_params={'ensure_ascii': False}, status=200)


class ADSDetailView(DetailView):
    model = ADS

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except ADS.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
                'id': ads.id,
                'name': ads.name,
                'author': ads.author,
                'price': ads.price,
                'description': ads.description,
                'address': ads.address,
                'is_published': ads.is_published
            }, json_dumps_params={'ensure_ascii': False}, status=200)