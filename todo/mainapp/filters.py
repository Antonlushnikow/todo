import django_filters
import django_filters.rest_framework as filters

from mainapp.models import Project, Todo


class ProjectFilter(filters.FilterSet):
    """
    Фильтрация для проектов
    """
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    """
    Фильтрация для тикетов
    """
    created_date = filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'yyyy/mm/dd'}),
    )

    class Meta:
        model = Todo
        fields = ['project', 'created_date']
