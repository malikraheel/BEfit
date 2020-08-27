from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# ------------ Admin Page text show ------------
admin.site.site_header = "Befit Admin"
admin.site.site_title = "Befit Admin Portal"
admin.site.index_title = "Welcome to Befit Researcher Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    # django-registration-redux  setting add
    path('accounts/', include('registration.backends.default.urls')),
    path('register/', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
         name='registration_register'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    path('gym/', include('gym.urls')),
    path('', RedirectView.as_view(url="gym/")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       # image upload  path
