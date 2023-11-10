import requests
def get_crypto_data():
    response =  requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code==200:
        return response.json()

crypt_response=get_crypto_data()
user_input=input("enter your crypto currency:")
for crypto in crypt_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break
        print()

