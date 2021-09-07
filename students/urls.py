from rest_framework.routers import DefaultRouter
from .views import StudentViewset
router = DefaultRouter()
router.register(r'students', StudentViewset, basename='students')
urlpatterns = router.urls