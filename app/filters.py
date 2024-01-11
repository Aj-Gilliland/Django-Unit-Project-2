# import django_filters
# from django_filters import DateFilter, CharFilter

# from .models import *
		
# class BugReportFilter(django_filters.FilterSet):
# 	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
# 	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
# 	prompt = CharFilter(field_name='prompt', lookup_expr='icontains')

# 	class Meta:
# 		model = BugReport
# 		fields = '__all__'
# 		exclude = ['account', 'messages', 'most_correct' 'date_created']