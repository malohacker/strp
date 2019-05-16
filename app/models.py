from django.db import models
from django.utils.translation import gettext_lazy as _


class BonusCard(models.Model):
    """
    Bonus card model
    """
    STATUS = (
        (1, _('Not active')),
        (2, _('Active')),
        (3, _('Expired'))
    )
    serial = models.CharField(_('Serial'), max_length=10)
    number = models.CharField(_('Number'), max_length=10)
    issue_date = models.DateTimeField(_('Date of issue'))
    expiration_date = models.DateTimeField(_('Date of expiration'))
    date_of_use = models.DateTimeField(_('Date of use'))
    amount = models.IntegerField(_('Amount'))
    status = models.CharField(_('Status'), max_length=1, choices=STATUS)

    class Meta:
        verbose_name = _('Bonus card')
        verbose_name_plural = _('Bonus cards')

    def to_representation(self, fields):
        return dict(getattr(self, field) for field in fields)

    def __str__(self):
        return self.serial

