import datetime 

def get_current_time() :

    date = datetime.datetime.now()
    jour = date.strftime('%Y-%m-%d')
    heure = date.strftime('%H:%M:%S')
    return jour, heure
