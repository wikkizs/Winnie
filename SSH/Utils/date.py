import datetime 

# Renvoie la date et l'heure actuelle
def get_current_time() :
    date = datetime.datetime.now()
    jour = date.strftime('%Y-%m-%d')
    heure = date.strftime('%H:%M:%S')
    return jour, heure
