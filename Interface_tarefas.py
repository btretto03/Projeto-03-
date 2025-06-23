import datetime as dt

dia = dt.date.today()           
dia_formatado = dia.strftime("%d/%m/%Y")
leo = input()
if len(leo) > 30:
    leo = list(leo)
    leo1 = leo [:30]
    leo2 = leo[30:len(leo)]
    leo = f"{"".join(leo1)} \n {"".join(leo2)}" 

print("—" * 81)
print("|                            |                                      ",dia_formatado,"|")
print(f"|{leo}                      |                                                  |")