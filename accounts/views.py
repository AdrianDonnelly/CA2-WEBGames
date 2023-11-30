from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        try:
            customer_group = Group.objects.get(name='Customer')
        except Group.DoesNotExist:
            customer_group = Group.objects.create(name='Customer')

        # Validate age if its above 18 to make account
        age = form.cleaned_data.get('age')
        if age is not None and age < 18:
            form.add_error('age', 'You must be at least 18 years old to register.')
            return self.form_invalid(form)

        signup_user = form.save()
        username = form.cleaned_data.get('username')
        signup_user = CustomUser.objects.get(username=username)
        customer_group.user_set.add(signup_user)
        return super().form_valid(form)
