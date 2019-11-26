from rest_framework.views import APIView
from rest_framework import mixins, generics, status
from .serializer import FlightSerializer, HistorySerializer
from .models import Flight, History
from rest_framework.response import Response


class HistoryView(generics.ListAPIView,
                  mixins.CreateModelMixin):
    """return a list of  previous and post for create a new previous"""
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = HistorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        a = self.create(request, *args, **kwargs)
        print(a)
        return self.create(request, *args, **kwargs)


class HistoryDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FlightAndPreviousView(APIView):

    def get(self, request):
        flights = Flight.objects.all()
        flights_serializer = FlightSerializer(flights, many=True)
        histories = History.objects.all()
        history_serializer = HistorySerializer(histories, many=True)
        return Response({"flights": flights_serializer.data, "previous": history_serializer.data})

    # def post(self, request, format=None):
    #     serializer = FlightSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightView(generics.GenericAPIView, mixins.CreateModelMixin):
    """return a list of flights, and a post method for creation it"""
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get(self, request):
        flights = Flight.objects.all()
        flights_serializer = FlightSerializer(flights, many=True)
        return Response({"flights": flights_serializer.data})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FlightDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
