import requests
import json

#https://api.nasa.gov/
#https://tle.ivanstanojevic.me/#/tle/43786

#Le chatbot nous pose une question (utilisateur) afin d'obtenir le nom du satellite pour lequel on veut des informations
#Le chatbot utilise une API pour récupérer les TLE (Two-Line Elements) des différents satellites. 
#Si le nom du satellite est trouvé, le chatbot renvoie les informations



# Configuration de l'API
# url = "http://tle.ivanstanojevic.me/api/tle"
# headers = {
#     "Authorization": "h26chCeQiNLKVlawhgdAD8QQNZDGpysGlFqFNwMD", #"Bearer your_token",
#     "Content-Type": "application/json"
# }

# Fonction pour extraire des données de l'API
# def extract_data():
#     response = requests.get(url, headers=headers)
#     data = json.loads(response.text)
#     return data

# Fonction pour gérer les demandes de l'utilisateur
# def handle_message(message):
#     if message == "get_data":
#         data = extract_data()
#         response = f"Voici les données que j'ai obtenues : {data}"
#     else:
#         response = "Je ne comprends pas votre demande. Veuillez réessayer."
#     return response

#import requests
#import json
def send_message(message):
    # code pour envoyer le message
    print(message)


def handle_message(message):
    if "informations satellite" in message.lower():
        # on demande à l'utilisateur de donner le nom du satellite
        send_message("Quel est le nom du satellite pour lequel vous voulez des informations?")
    elif "tle" in message.lower():
        # on récupère les TLE à partir de l'API
        #on effectue une requête HTTP get  à l'url de l'API 
        response = requests.get("https://tle.ivanstanojevic.me/api/tle/")
        data = response.json() 

# on recherche le satellite spécifié par l'utilisateur
        satellite_name = message[message.lower().find("tle")+3:].strip()
        satellite = None
        for member in data['member']:
            if member['name'] == satellite_name:
                satellite = member
                break

# si le satellite est trouvé, on renvoie ses informations
        if satellite:
            response = f"Nom : {satellite['name']}\nDate : {satellite['date']}\nLigne 1 : {satellite['line1']}\nLigne 2 : {satellite['line2']}"
            send_message(response) 
        else:
            send_message("Désolé, je n'ai pas trouvé d'informations pour ce satellite.")
    else:
        send_message("Je ne comprends pas ce que vous voulez dire. Veuillez reformuler votre demande.")


# Boucle principale du chatbot
while True:
    message = input("Entrez votre demande : ")
    response = handle_message(message) #traitement du message 
    print(response)


handle_message("informations satellite")
handle_message("tle NOAA 15")
#tle MORELOS 3
#tle ITASAT 1


#Comment se présente une info sur un satellite ? :
#{"@context":"https:\/\/www.w3.org\/ns\/hydra\/context.jsonld","@id":"https:\/\/tle.ivanstanojevic.me\/api\/tle\/40946","@type":"Tle","satelliteId":40946,"name":"MORELOS 3","date":"2022-12-09T02:40:55+00:00","line1":"1 40946U 15056A   22343.11175101 -.00000028  00000+0  00000+0 0  9990","line2":"2 40946   3.5000 337.9170 0000993 333.3900  53.6613  1.00271932 26383"}