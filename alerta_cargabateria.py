import psutil
import pynotifier


bateria = psutil.sensors_battery() #nivel de bateria
percentual_bateria = int(bateria.percent) # percentual de bateria
plugado = bateria.power_plugged #se esta plugado ou não


if percentual_bateria <=30 and plugado == False:
    pynotifier.Notification(
    title = "Lembrete",
    description= "Sua bateria está fraca, CARREGUE!",
    duration =15,
    ).send()
    
elif percentual_bateria >=100 and plugado != False:
    pynotifier.Notification(
    title = "Lembrete",
    description= "Carga Completa!\nRetire da tomada",
    duration =10,
    
).send()

else:
    print("nada a fazer")



    

 