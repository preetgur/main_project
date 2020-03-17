import django_filters
from ems.models import Register_Employee


class Employee_filter(django_filters.FilterSet):

    #field_name => set to the 'order' table field value
    # lookup_expr => set the expression 

    class Meta:
        model = Register_Employee
        fields = ['first_name','emp_id']
        # exclude = ['placed_by','placed_on']