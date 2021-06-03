# Python_Africa-s_Talking_SMS
This is a simple file on how to create a sms simulation with Africa' Talking API in python. 
For this case, folllow this steps to get along on how you can easly invoke the Africa's Talking API from your end point python files.

The sms end point requires these parameters

  - Url = this is the main url to Africa's Talking 
  - Headers = THis is JSON dictionary that hold the authentiocation credetials.
 		it will have the following
			- API key
			- Conte-type
			- Accept
   data  = this refers to the data that are sent to the sms API. It requires the following
		Username: Your app username
		from : The shortcode
		message : the actual message to be sent
		to: the phone number you are sending message to

Now you will sent a POST request through terminal, to the url above and the respond that you get will be
in a json format

