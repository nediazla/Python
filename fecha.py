from datetime import datetime

date_str = input("Introduce una fecha en formato dd/mm/yy HH:MM:SS: ")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

d = datetime.strptime(date_str, "%d/%m/%y %H:%M:%S")
print(days[d.weekday()]+"day")