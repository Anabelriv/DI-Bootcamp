from rest_framework import serializers
from .models import Address, Customer, Vehicle, VehicleAtRentalStation, VehicleSize, VehicleType, Rental, RentalRate, RentalStation

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
    
class VehicleAtRentalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAtRentalStation
        fields = "__all__"

class VehicleSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSize
        fields = "__all__"

class VehicleTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = "__all__"

class RentalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = "__all__"
    
class RentalRateSerializers(serializers.ModelSerializer):
    class Meta:
        model = RentalRate
        fields = "__all__"

class RentalStationSerializers(serializers.ModelSerializer):
    class Meta:
        model = RentalStation
        fields = "__all__"