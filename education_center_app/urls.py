from django.urls import path, include
from rest_framework import routers

from education_center_app.views import StudentViewSet, CourceViewSet, MarkViewSet

router = routers.DefaultRouter()
router.register("students", StudentViewSet, "students")
router.register("courses", CourceViewSet, "courses")
router.register("marks", MarkViewSet, "marks")

urlpatterns = [
    path('', include(router.urls)),
]
 

