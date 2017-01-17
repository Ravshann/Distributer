from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext as _
from location_field.models.plain import PlainLocationField
from solo.models import SingletonModel


def phone_validation(phone):
    if not phone.startswith('+998'):
        raise ValidationError(_('The phone number is incorrect'))


class Time(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(SingletonModel, Time):
    token = models.CharField(max_length=64, blank=True)
    companyName = models.CharField(_('Company name'), max_length=255)
    companyAddress = PlainLocationField(verbose_name=_('Company address'), based_fields=['city'], zoom=7,
                                        max_length=255, default='41.313918406594375, 69.24613952636719')
    companyPhone = models.CharField(_('Company phone number'), max_length=13, validators=[phone_validation])
    companyLogo = models.ImageField(_('Company logo'), upload_to='logos')

    def __str__(self):
        return self.companyName

    def get_products(self):
        return self.products.all()

    def get_product_count(self):
        return self.products.all().count()

    class Meta:
        verbose_name = _('Nestle')


class Product(Time):
    CHOICES = (
        ('food', _('Food')),
        ('tech', _('Technology'))
    )
    relatedCompany = models.ForeignKey(Company, related_name='products', default=1)
    productName = models.CharField(_('Product name'), max_length=255)
    productType = models.CharField(_('Product type'), max_length=255, choices=CHOICES)
    productDefinition = models.TextField(_('Product definition'))
    productCost = models.PositiveIntegerField(_('Product cost'))

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Order(Time):
    order_id = models.CharField(verbose_name=_('Order ID'), max_length=255)
    shop = models.CharField(verbose_name=_('Shop'), max_length=255)
    due_date = models.DateTimeField(_('Due date'))
    quantity = models.PositiveIntegerField(_('Quantity'))
    product = models.CharField(verbose_name=_('Product'), max_length=255)
    address = PlainLocationField(verbose_name=_('Address'), based_fields=['city'], zoom=7,
                                 default='41.313918406594375, 69.24613952636719', max_length=255)

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
