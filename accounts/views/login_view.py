from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import View

from accounts.forms import LoginForm


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        data = {'form': LoginForm, 'error': None}
        return render(request, self.template_name, data)

    def post(self, request):
        data = LoginForm(request.POST or None)

        if data is not None:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Check if the user is active
                if user.is_active:
                    # Log the user in
                    login(request, user)
                    return redirect('tickets:ticket_list')

        return render(
            request,
            self.template_name,
            {
                'form': data,
                'error': 'A autenticação falhou. Verifique o login, a senha e tente novamente.',
            },
        )
