from django.conf.urls import patterns, url

from src.app.views import (
    BonusCardListCreateView,
    BonusCardDeleteView
)

urlpatterns = patterns('',
    url(r'^list/$', BonusCardListCreateView.as_view(), name='bonus_cards'),
    url(r'^list/(?P<pk>)/$', BonusCardDeleteView.as_view(), name='bonus_card_delete'),
)