from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View

from accounts.forms import RegisterForm
from profiles.models import UserProfile


class RegisterView(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            try:
                user = form.save()

                if user:
                    UserProfile.objects.create(user=user)
                    messages.success(request, 'Registro realizado com sucesso! Faça o login.')
                    return redirect('accounts:login')
                else:
                    messages.error(request, 'Ocorreu um erro inesperado ao criar o usuário.')
            except Exception as e:
                messages.error(request, f'Erro durante o registro: {e}')
                # Logar 'e'
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')

        # Renderiza novamente em caso de erro no try ou form inválido
        return render(request, self.template_name, {'form': form})
