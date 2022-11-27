from django.urls import re_path
from DbOperationsApp import views

urlpatterns = [
    re_path(r'^signup/(?P<user>\D+)',views.signup),
    re_path(r'^login/(?P<user>\D+)', views.login),
    re_path(r'^resetpassword/(?P<user>\D+)', views.resetPassword),

    re_path(r'^viewprofile', views.getProfile),
    re_path(r'^deleteprofile', views.deleteProfile),
    re_path(r'^updateprofile', views.updateProfile),

    re_path(r'^createdonationrequest', views.createDonationRquest),
    re_path(r'^updatedonationrequest', views.updateDonationRquest),
    re_path(r'^viewcurrentrequests', views.viewCurrentRequests),

    re_path(r'^viewactiverequests', views.viewActiveRequests),
]