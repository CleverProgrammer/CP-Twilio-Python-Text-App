account_sid = "Your Account Sid"
auth_token = "Your Auth Token"
my_cell = "+Your Cell Number"
my_twilio = "+Your Twilio Number"
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC37b5699c2f2c158171b0d7b06881732b"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", 
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
