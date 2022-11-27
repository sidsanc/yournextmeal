from djongo import models

class Address(models.Model):
    _id = models.ObjectIdField()
    Street1 = models.CharField(max_length=200)
    Street2 = models.CharField(max_length=200, blank=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zipcode = models.CharField(max_length=10)


class Donor(models.Model):
    Type = models.CharField(max_length=20)
    Name = models.CharField(max_length=200)
    PocName = models.CharField(max_length=200, blank=True)
    Address = models.EmbeddedField(
        model_container=Address
        )
    Contact = models.BigIntegerField(blank=True)
    Email = models.EmailField(primary_key=True)


class Recipient(models.Model):
    Type = models.CharField(max_length=20)
    Name = models.CharField(max_length=200)
    PocName = models.CharField(max_length=200, blank=True)
    Address = models.EmbeddedField(
        model_container=Address
        )
    Contact = models.BigIntegerField(blank=True)
    Email = models.EmailField(primary_key=True)


class DonorLoginCredentials(models.Model):
    Email = models.ForeignKey(
        "Donor", on_delete=models.CASCADE
        )
    Password = models.CharField(max_length=30)


class RecipientLoginCredentials(models.Model):
    Email = models.ForeignKey(
        "Recipient", on_delete=models.CASCADE
        )
    Password = models.CharField(max_length=30)


class DropOffLocations(models.Model):
    LocationName = models.CharField(max_length=200)
    LocationAddress = models.EmbeddedField(
        model_container=Address
        )
    LocationContact = models.BigIntegerField(blank=True)
    LocationHours = models.DateTimeField()


class DonationRequest(models.Model):
    RequestId = models.AutoField(primary_key=True)
    Email = models.ForeignKey(
        "Donor", on_delete=models.CASCADE
        )
    DonationType = models.CharField(max_length=100)
    # Convert to dictionary type {grocery:x pounds, meals:50 boxes}
    DonationQty = models.TextField()
    DonationAllergies = models.TextField(blank=True)
    DonationDescription = models.TextField()
    DonationPickupDate = models.DateField()
    DonationPickupTime = models.TimeField()
    DonorContact = models.BigIntegerField()
    DonorAddress = models.EmbeddedField(
        model_container=Address
        )
    # store file in mongo
    DonationPhotoLink = models.URLField(blank=True)


class RequestStatus(models.Model):
    RequestId = models.ForeignKey(
        "DonationRequest", to_field='RequestId', on_delete=models.CASCADE
        )
    RequestCreatedBy = models.EmailField()
    RequestCreationDateTime = models.DateTimeField(auto_now=True)
    # Many to one relationship
    RequestAcceptedBy = models.ForeignKey(
        "Recipient", to_field='Email', on_delete = models.CASCADE, default=None
        )
    # Datetime when request is accepted
    RequestAcceptDateTime = models.DateTimeField(default=None)
    RequestCurrentStatus = models.CharField(max_length=20, default='Active')

