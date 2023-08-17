from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  Customer, Vehicle, Rental, RentalStation, VehicleAtRentalStation
from .serializers import  CustomerSerializer, VehicleSerializer, RentalSerializers, RentalStationSerializers
from rest_framework.permissions import AllowAny

      
class RentalAPIView(APIView):
    permission_classes = [AllowAny]
    # Get with or without ID
    def get(self, request, **kwargs):
        id = kwargs.get("pk", None)
        if id is not None:
            try:
                rental = Rental.objects.get(id=id)
                serializer = RentalSerializers(rental)

            except Rental.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            rentals = Rental.objects.order_by('return_date', 'rental_date')
            serializer = RentalSerializers(rentals, many=True)
            return Response(serializer.data)

    #Post
    def post (self, request, format=None):
        serializer = RentalSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, *args, **kwargs):
        rental = Rental.objects.get(id=pk)
        serializer = RentalSerializers(instance=rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        rental = Rental.objects.get(id=pk)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        id = kwargs.get("pk", None)
        if id is not None:
            try:
                customer = Customer.objects.get(id=id)
                serializer = CustomerSerializer(customer)

            except Customer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            customers = Customer.objects.order_by('first_name')
            serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post (self, request, format=None):
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# GET specific vehicle or it will group by type
class VehicleAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        id = kwargs.get("pk", None)
        if id is not None:
            try:
                vehicle = Vehicle.objects.get(id=id)
                serializer = RentalSerializers(vehicle)

            except Rental.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            vehicles = Vehicle.objects.order_by('vehicle_type')
            serializer = RentalSerializers(vehicles, many=True)

            # group vehicles by type
            grouped_vehicles = {}
            for vehicle in serializer.data:
                type_id = vehicle['vehicle_type']['id']
                if type_id not in grouped_vehicles:
                    grouped_vehicles[type_id] = {
                        'vehicle_type': vehicle['vehicle_type'],
                        'vehicles': [vehicle]
                    }
                else:
                    grouped_vehicles[type_id]['vehicles'].append(vehicle)
            
            return Response(list(grouped_vehicles.values()))
                     

# GET/POST /rent/vehicle/add: Allows for adding a new vehicle.
    def post (self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT/DELETE /rent/vehicle/<pk>: Displays, updates, or deletes a specific vehicle.
    def put(self, request, pk, *args, **kwargs):
        vehicle = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializer(instance=vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        vehicle = Vehicle.objects.get(id=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all the rental stations, and also filter by ID with the vehicles on it

class RentalStationAPIView(APIView):
    def get(self, request, **kwargs):
        id = kwargs.get("pk", None)
        if id is not None:
            try:
                rental_station = RentalStation.objects.get(id=id)
                vehicles_at_station = VehicleAtRentalStation.objects.filter(station=rental_station)
                
                #GET distribution stats
                rental_station_data = RentalStationSerializers(rental_station).data
                vehicles_data = VehicleAtRentalStation(vehicles_at_station, many =True).data
                
                return Response({"rental_station": rental_station_data,
                                 "vehicles_at_station": vehicles_data})

            except RentalStation.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            rental_stations = Rental.objects.all()
            serializer = RentalSerializers(rental_stations, many=True)
            return Response(serializer.data) 

# POST /rent/station/add: Allows for creating a new rental station.
    def post (self, request, action):
        if action == 'add':
            serializer = RentalStationSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif action == 'distribute':
            # Distribute vehicles among stations
            try:
                total_capacity = sum(station.capacity for station in RentalStation.objects.all())
                total_vehicles = VehicleAtRentalStation.objects.count()

                if total_capacity >= total_vehicles:
                    # Calculate the average number of vehicles to distribute to each station
                    avg_vehicles_per_station = total_vehicles // RentalStation.objects.count()

                    # Distribute vehicles evenly among stations
                    for station in RentalStation.objects.all():
                        vehicles_to_distribute = VehicleAtRentalStation.objects.filter(station=None)[:avg_vehicles_per_station]
                        for vehicle in vehicles_to_distribute:
                            vehicle.station = station
                            vehicle.save()

                    return Response({"message": "Vehicles distributed successfully"})
                else:
                    return Response({"error": "Not enough capacity to distribute vehicles"}, status =status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
