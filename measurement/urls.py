from django.urls import path

from .views import SensorView, MeasurementView, SensorViewQ

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorViewQ.as_view()),
]
