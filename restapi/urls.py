from rest_framework import routers
from django.urls import (
    path,
    include
)

from rest_framework.routers import DefaultRouter
from .views import (
    some_function, sample_view,
    BanksDetails, BankInfo,
    BanksViewSet, BanksDetail,
    BanksList, BanksListGenerics,
    BanksDetailGenerics, LoginView,
    Logout, SignUp,
    StudentListGenerics, SendUrl,
    StudentDetailGenerics,
    StudentDetails, ResetPassword,
)

#
# router = routers.SimpleRouter()
# router.register('classview', BanksDateils)

urlpatterns = [
    path('', some_function),
    path('data/<int:id>/', sample_view),
    path('classview/', BanksDetails.as_view()),
    path('classview/<int:pk>/', BankInfo.as_view())
]

router = DefaultRouter()
router.register('viewset', BanksViewSet, basename='viewsetclass')

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns += [
    path('mixins/', BanksList.as_view()),
    path('mixins/<int:pk>/', BanksDetail.as_view())
]

urlpatterns += [
    path('generic/', BanksListGenerics.as_view()),
    path('generic/<int:pk>/', BanksDetailGenerics.as_view())
]

urlpatterns += [
    path('login/', LoginView.as_view()),
    path('logout/', Logout.as_view()),
    path('signup/', SignUp.as_view())
]

urlpatterns += [
    path('student/', StudentListGenerics.as_view()),
    path('student/<int:id>/', StudentDetailGenerics.as_view())
]

urlpatterns += [
    path('resetpassword/', SendUrl.as_view()),
    path('resetpassword/<str:token>/', ResetPassword.as_view())
]
