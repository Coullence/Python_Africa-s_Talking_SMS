# sendsms.py

# Import request from python library to make the RPC request to the API
import requests
# Enter the URL from the Africa's Talking
url = "https://api.sandbox.africastalking.com/version1/messaging"
# Set the header data
headers = {'ApiKey': 'ad2dc98223bf70af56bcba2f7b04120039e3b73c2a8c810af37fd41eec214f3f', 
           'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json'}
# Here you create a data dictionary of what to be sent....now you see its a JSON dictionary composing of username, from, message and phone
data = {'username': 'sandbox',
        'from': '26009',
        'message': "Hello world !",
        'to': '+254726634786'}

# Create a function that will be called t make request and return respond if request was succesfull. 
def postData():  
    response = requests.post( url = url, headers = headers, data = data )
    return response


print( postData().json() )

