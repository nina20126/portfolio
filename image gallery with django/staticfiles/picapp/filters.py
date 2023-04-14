import django_filters
from .models import Photo


class SnippetFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(
        label="", choices=CHOICES, method='filter_by_order')

    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)
