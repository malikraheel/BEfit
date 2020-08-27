from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from gym.models import Profile, Message, Exercise
from django.views.generic.list import ListView
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import UpdateView, CreateView


def home(request):
    if request.user.is_authenticated:
        ti = Profile.objects.get(name=request.user.username)
        if ti.time == 1:
            ti.time = 2
            ti.save()
            return render(request, 'price.html')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def feature(request):
    return render(request, 'feature.html')


def contact(request):
    request.session['id'] = request.user.id
    return render(request, 'contact.html')


@login_required(login_url='/accounts/login')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='/accounts/login')
def videos(request, id):
    info5 = list(Exercise.objects.values(id).filter(name=request.user.id))
    v = Profile.objects.get(user_id=request.user.id)
    print(v.gender)
    if len(info5) == 0 and v.gender == 'female':
        info5 = list(Exercise.objects.values(id).filter(category='reguler_f'))
        return render(request, 'videos.html', {'id': id, 'info5': info5, 'l': len(info5)})
    elif len(info5) == 0 and v.gender == 'male':
        info5 = list(Exercise.objects.values(id).filter(category='reguler_m'))
        return render(request, 'videos.html', {'id': id, 'info5': info5, 'l': len(info5)})

    return render(request, 'videos.html', {'id': id, 'info5': info5, 'l': len(info5)})


@ login_required(login_url='/accounts/login')
def schedule(request):
    return render(request, 'schedule.html')


@ login_required(login_url='/accounts/login')
def price(request):
    return render(request, 'price.html')


@ login_required(login_url='/accounts/login')
def bmi(request):
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        result = weight / (height * height)
        output = round(result * 100) / 100
        if output < 18.5:
            res = "Underweight"
        elif output >= 18.5 and output <= 25:
            res = "Normal"
        elif output >= 25 and output <= 30:
            res = "Obese"
        elif output > 30:
            res = "Overweight"
        return render(request, 'bmi.html', {'weight': weight, 'height': height, 'res': res})

    return render(request, 'bmi.html')


@ method_decorator(login_required, name="dispatch")
class ProfileListView(ListView):
    model = Profile


@ method_decorator(login_required, name="dispatch")
class ProfileDetailView(DetailView):
    model = Profile


@ method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile

    fields = ['age', 'address', 'status',  # fields inside update column names
              'gender', 'phone_no', 'description', 'pic']


# @ method_decorator(login_required, name='dispatch')
class MessageCreate(CreateView):

    model = Message
    fields = ['subject', "msg", "phone_no", "email"]

#    -----------------before save form run ------------
    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
