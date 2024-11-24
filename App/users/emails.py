from djoser.email import ActivationEmail, PasswordResetEmail

class CustomActivationEmail(ActivationEmail):
    template_name = 'email/Activation.html'

class CustomResetPasswordEmail(PasswordResetEmail):
    template_name = 'email/ResetPass.html'