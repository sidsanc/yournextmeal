import datetime

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DbOperationsApp.models import Donor, Recipient, DonorLoginCredentials, RecipientLoginCredentials, RequestStatus, DonationRequest
from DbOperationsApp.serializers import DonorSerializer, RecipientSerializer, DonorLoginCredentialsSerializer, RecipientLoginCredentialsSerializer, DonorRequestSerializer, RequestStatusSerializer

# structure into classes

# get email and usertype from session and if session does not exist, redirect to login
usertype = 'donor'
email = 'xyz@gmail.com'

# make non editable once session is created
def createSession(request, email, usertype='donor'):
    request.session['username'] = email
    request.session['usertype'] = usertype


def accessSession(request):
    username = request.session['username']
    usertype = request.session['usertype']

    return username, usertype


def sessionExist(request, email):
    if email in request.session:
        return True

    return False


def logout(request):
    request.session.flush()


@csrf_exempt
def signup(request, **kwargs):
    # add validations for all fields + check if email id already exists
    data = JSONParser().parse(request)
    signup_data = {k:v for k,v in data.items() if k!= 'Password'} 
    login_data = {k:v for k,v in data.items() if k in ['Email', 'Password']}

    if kwargs['user'] == 'donor':
        signup_serializer = DonorSerializer(data=signup_data)
        login_serializer = DonorLoginCredentialsSerializer(data=login_data)
    else:
        signup_serializer = RecipientSerializer(data=signup_data)
        login_serializer = RecipientLoginCredentialsSerializer(data=login_data)

    # add exisiting email checks and output correct failure messages
    if signup_serializer.is_valid():
        signup_serializer.save()
        if login_serializer.is_valid():
            login_serializer.save()
        return JsonResponse("Sign Up Successful", safe=False)
    return JsonResponse("Sign up failed", safe=False)


@csrf_exempt
def login(request, **kwargs):
    login_data = JSONParser().parse(request)
    email = login_data['Email']
    pwd = login_data['Password']

    if kwargs['user'] == 'donor':
        try:
            user = DonorLoginCredentials.objects.get(Email=email)
        except DonorLoginCredentials.DoesNotExist:
            return JsonResponse("User does not exist. Please sign up!", safe=False)
    else:
        try:
            user = RecipientLoginCredentials.objects.get(Email=email)
        except RecipientLoginCredentials.DoesNotExist:
            return JsonResponse("Username incorrect or does not exist!", safe=False)
        
    # create session and set session variables if username and password are correct
    if pwd == user.Password:
        createSession(request, email, kwargs['user'])
        print(request.session)
        return JsonResponse("User login successful", safe=False)
    else:
        return JsonResponse("Incorrect Password. Please try again", safe=False)


@csrf_exempt
def resetPassword(request, **kwargs):
    reset_data = JSONParser().parse(request)
    email = reset_data['Email']
    pwd = reset_data['Password']
    reenter_pwd = reset_data['Reenter_Password']

    #add email validation. if valid, then proceed.

    if kwargs['user'] == 'donor':
        try:
            user = DonorLoginCredentials.objects.get(Email=email)
        except DonorLoginCredentials.DoesNotExist:
            return JsonResponse("User does not exist. Please sign up!", safe=False)
    else:
        try:
            user = RecipientLoginCredentials.objects.get(Email=email)
        except RecipientLoginCredentials.DoesNotExist:
            return JsonResponse("User does not exist. Please sign up!", safe=False)

    if pwd == reenter_pwd:
        user.Password = pwd
        user.save(update_fields=['Password'])
        return JsonResponse('Password reset. Login to continue', safe=False)
    else:
        return JsonResponse('Passwords do not match. Try again!', safe=False)


def getProfile(self):
    if usertype == 'donor':
        profile = DonorSerializer(Donor.objects.get(Email=email)).data
    else:
        profile = RecipientSerializer(Recipient.objects.get(Email=email)).data
    
    return JsonResponse(profile, safe=False)


@csrf_exempt
def deleteProfile(self):
    if usertype == 'donor':
        user = Donor.objects.get(Email=email)
    else:
        user = Recipient.objects.get(Email=email)

    user.delete()

    return JsonResponse('User deleted successfully', safe=False)


@csrf_exempt
def updateProfile(request):
    user_updates = JSONParser().parse(request) ## type and email fields are frozen so that entire record can be overwritten in one go
    if usertype == 'donor':
        user = Donor.objects.get(Email=email)
        serializer = DonorSerializer(user, data=user_updates)
    else:
        user = Recipient.objects.get(Email=email)
        serializer = RecipientSerializer(user, data=user_updates)

    # add check for validating contact field
    if serializer.is_valid():
        serializer.save()
        return JsonResponse('Details updated Successfully', safe=False)


@csrf_exempt
def createDonationRquest(request):
    # allow for user to upload images and store directly in database
    # email id has to come from session 
    request_data = JSONParser().parse(request)
    request_serializer = DonorRequestSerializer(data=request_data)
    if request_serializer.is_valid():
        request_serializer.save()

        latest_created_request = DonationRequest.objects.latest('RequestId')
        request_status = RequestStatus.objects.create(RequestId=latest_created_request, RequestCreatedBy=request_data['Email'], \
            RequestCreationDateTime=datetime.datetime.now())
        request_status_serializer = RequestStatusSerializer(data=request_status)
        if request_status_serializer.is_valid():
            request_status_serializer.save()
        return JsonResponse("Request created!", safe=False)

    return JsonResponse("Error in creating donation request", safe=False)


@csrf_exempt
def updateDonationRquest(request):
    donation_request_updates = JSONParser().parse(request) ## email field is frozen so that entire record can be overwritten in one go
    user = DonationRequest.objects.get(Email=email)
    serializer = DonorRequestSerializer(user, data=donation_request_updates)

    # add check for validating contact field
    if serializer.is_valid():
        serializer.save()
        return JsonResponse('Details updated Successfully', safe=False)


def viewCurrentRequests(self):
    user_requests = DonationRequest.objects.filter(Email=email)

    if user_requests:
        user_requests_serializer = DonorRequestSerializer(user_requests, many=True)

        l = len(user_requests_serializer.data)
        for i in range(l):
            request_status = RequestStatus.objects.get(RequestId_id=user_requests_serializer.data[i]['RequestId'])
            user_requests_serializer.data[i]['RequestCreationDateTime'] = request_status.RequestCreationDateTime
            user_requests_serializer.data[i]['RequestAcceptedBy'] = request_status.RequestAcceptedBy
            user_requests_serializer.data[i]['RequestAcceptDateTime'] = request_status.RequestAcceptDateTime
            user_requests_serializer.data[i]['RequestCurrentStatus'] = request_status.RequestCurrentStatus
        
        return JsonResponse(user_requests_serializer.data, safe=False)
    
    return JsonResponse("No requests found!", safe=False)


def viewActiveRequests(self):
    active_requests = RequestStatus.objects.filter(RequestCurrentStatus='Active')

    if active_requests:
        active_requests_serializer = RequestStatusSerializer(active_requests, many=True)
        l = len(active_requests_serializer.data)
        active_request_id_list = []
        for i in range(l):
            active_request_id_list.append(active_requests_serializer.data[i]['RequestId'])

        requests_to_display = DonationRequest.objects.filter(RequestId__in=active_request_id_list)
        if requests_to_display:
            requests_to_display_serializer = DonorRequestSerializer(requests_to_display, many=True)
            return JsonResponse(requests_to_display_serializer.data, safe=False)
        
    return JsonResponse('No active requests found', safe=False)


#def cancelDonationRequest(request):


