from django.contrib.auth.forms import UserCreationForm

# 덮어씌우기 = 오버라이밍?
class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True