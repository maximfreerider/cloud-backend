from django.db import models
import datetime
# Create your models here.

""""
- рейс літака(BA81)
- маршрут(London-Accra)
- швидкість(523)
- авіакомпанію(British Airways)
- попередні рейси({date: 21 october, 
                    from: Miami, 
                    to: London}, 
                    {date: 22 october, 
                    from: Miami, 
                    to: London})
- загальний наліт
- реєстраційну інформацію


Створіть сайт, яка дозволяє зберігати інформацію про поточне розташування літака 
(його рейс, маршрут, швидкість, авіакомпанію, попередні рейси, загальний наліт, 
реєстраційну інформацію
"""


class Flight(models.Model):
    name = models.CharField(max_length=15)  # рейс
    come_from = models.CharField(max_length=15)
    come_to = models.CharField(max_length=15)
    avia_company = models.CharField(max_length=15)
    speed = models.FloatField()
    registration_info = models.CharField(max_length=15)
    flight_distance = models.IntegerField()


class History(models.Model):
    start = models.DateTimeField(blank=True, null=True)
    finish = models.DateTimeField(blank=True, null=True)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)


#    previous_flight = models.ForeignKey('PreviousFlights', on_delete=models.CASCADE)
#
#
# class PreviousFlights(models.Model):
#     date_of_flight = models.DateTimeField()
#     come_from = models.CharField(max_length=15)
#     come_to = models.CharField(max_length=15)
#     flight_of_previous = models.CharField(max_length=15)
#     previous_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, blank=True, null=True)


# {
#     "flight": "",
#     "come_from": "",
#     "come_to": "",
#     "avia_company": "",
#     "speed": 123,
#     "registration_info": "",
#     "flight_distance": 1234,
#     "previous_routes": [
#         {
#             "date_of_flight": 10.05.2019,
#             "come_from": "",
#             "come_to": "",
#             "flight": ""
#         },
#         {
#             "date_of_flight": 10.05.2019,
#             "come_from": "",
#             "come_to": "",
#             "flight": ""
#         },
#     ]
# }






# {
#     "farmer": {
#         "name": "Vasya",
#         "dilyalis": [
#             {   "id": 1,
#                 "location": "Lviv, village",
#                 "level_of_vologist": 2,
#                 "level_of_light": 12,
#             }
#         ]
#     }
# }
#
#
# {
#     "dilyanka": {
#         "farmer": "Vasya",
#         "location": "Lviv, village",
#         "level_of_vologist": 2,
#         "level_of_light": 12,
#     }
#
# }
#
#































