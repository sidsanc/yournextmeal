from rest_framework import serializers
import DbOperationsApp.models

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbOperationsApp.models.Donor
        fields = "__all__"


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbOperationsApp.models.Recipient
        fields = "__all__"


class DonorLoginCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbOperationsApp.models.DonorLoginCredentials
        fields = "__all__"


class RecipientLoginCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbOperationsApp.models.RecipientLoginCredentials
        fields = "__all__"
        

class DropOffLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbOperationsApp.models.DropOffLocations
        fields = ('LocationName', 'LocationAddress', 'LocationContact', 'LocationHours')


class DonorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbOperationsApp.models.DonationRequest
        DonationPickupDate = serializers.DateField()
        DonationPickupTime = serializers.TimeField()
        fields = "__all__"


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbOperationsApp.models.RequestStatus
        RequestCreationDateTime = serializers.DateTimeField()
        RequestAcceptDateTime = serializers.DateTimeField()
        fields = "__all__"
