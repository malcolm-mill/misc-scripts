import datetime
from astral import Astral

city_name = 'Glasgow'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]

current_date = datetime.date(2019, 1, 1)

print("*")
for d in range(1, 366):
#    sun = city.sun(current_date)
    print(current_date.strftime("** [%Y-%m-%d %a]"))
    print(current_date.strftime("Week:%W Day:%j"))
#    print("Dawn: " + str(sun['dawn']))
#    print(sun['dawn'].strftime("Dawn: %X"))
#    print(sun['sunrise'].strftime("Sunrise: %X"))
#    print(sun['noon'].strftime("Noon: %X"))
#    print(sun['sunset'].strftime("Sunset: %X"))
#    print(sun['dusk'].strftime("Dusk: %X"))    
    current_date = current_date + datetime.timedelta(days=1)

input("press enter to continue ... ")
