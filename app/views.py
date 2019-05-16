import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import BaseDeleteView

from src.app.models import BonusCard


class JsonResponse(HttpResponse):
    def __init__(self, data, encoder=json.JSONEncoder, safe=True,
                 json_dumps_params=None, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError(
                'In order to allow non-dict objects to be serialized set the '
                'safe parameter to False.'
            )
        if json_dumps_params is None:
            json_dumps_params = {}
        kwargs.setdefault('content_type', 'application/json')
        data = json.dumps(data, cls=encoder, **json_dumps_params)
        super().__init__(content=data, **kwargs)


class BonusCardListCreateView(View):

    def __init__(self, **kwargs):
        super(BonusCardListCreateView, self).__init__(**kwargs)
        self.fields = ['serial', 'number', 'issue_date', 'expiration_date', 'status']

    def get_queryset(self):
        return BonusCard.objects.filter(**self.get_search_query())

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            [obj.to_representation(self.fields) for obj in self.get_queryset()]
        )

    def post(self, request, *args, **kwargs):
        obj, created = BonusCard.objects.create(**request.POST)
        return JsonResponse(obj.to_representation(self.fields))

    def get_search_query(self):
        postfix = '__icontains'
        search = self.request.GET.get('search')
        search_query = {'%s%s' % (x, postfix): search for x in self.fields}
        return search_query


class BonusCardDeleteView(BaseDeleteView):

    def get_success_url(self):
        return reverse('bonus_cards')
