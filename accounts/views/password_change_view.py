from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View

from accounts.forms import ChangePasswordForm
from accounts.models import CustomUser


class ChangePasswordView(View):
    template_name = 'accounts/password_change.html'

    def get(self, request):
        form = ChangePasswordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            print('Formulário válido, processando...')
            try:
                user = form.cleaned_data.get('user_name')
                custom_user = CustomUser.objects.get(username=user)

                user = form.save(custom_user)

                if user:
                    return redirect('accounts:login')
                else:
                    print('Erro inesperado ao criar o usuário.')
                    messages.error(request, 'Ocorreu um erro inesperado ao criar o usuário.')
            except Exception as e:
                print(f'Erro durante o registro: {e}')
                messages.error(request, f'Erro durante o registro: {e}')
                # Logar 'e'
        else:
            print('Por favor, corrija os erros no formulário.')
            messages.error(request, 'Por favor, corrija os erros no formulário.')

        # Renderiza novamente em caso de erro no try ou form inválido
        return render(request, self.template_name, {'form': form})
