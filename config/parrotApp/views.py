from django.http import HttpResponse
from django.views import View


class GeneralView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('птичик')
