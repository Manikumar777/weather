import requests 
from django.contrib.auth import logout
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password
from .forms import CityForm
from .models import WeatherData
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
class LoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, self.template_name, {'error_message': 'Invalid login'})
class IndexView(View):
    template_name = 'index.html'
    api_key = '285eca87582862d3869dd9c23baacab3'  # Replace with your actual API key
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + api_key

    def get(self, request):
        myForm = CityForm()
        context = {'form': myForm, 'test': 123}
        return render(request, self.template_name, context)

    def post(self, request):
        myForm = CityForm(request.POST)
        weather_data = None

        if myForm.is_valid():
            city_name = myForm.cleaned_data["name"]
            response = requests.get(self.url.format(city_name))

            if response.status_code == 200:
                weather_data = response.json()

                WeatherData.objects.create(
                    city=city_name,
                    temperature=(weather_data['main']['temp']),
                    humidity=weather_data['main']['humidity']
                )
                print("Weather data saved successfully")
            else:
                print("Failed to fetch data:", response.status_code)

        # Implement logout functionality
        if 'logout' in request.POST:
            logout(request)
            return redirect('login')  # Redirect to the login page after logout

        context = {'weather_data': weather_data, 'form': myForm}
        return render(request, self.template_name, context)
class SearchView( View):
    template_name = 'registration/search.html'
    def get(self, request):
        myForm = CityForm()
        weather_data = WeatherData.objects.all()
        context = {'form': myForm,  'weather_data': weather_data}
        return render(request, self.template_name, context)
class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login_view')  # Redirect to a success page

        return render(request, self.template_name, {'form': form})



