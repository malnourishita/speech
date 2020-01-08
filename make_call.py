
from twilio.rest import Client

account_sid = 'AC438cd64fea3ffdd0cba846199b7bd030'
auth_token = 'ae8db1e9182640e5edca376349ea03a9'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        to="+639437057481",
                        from_="+12019493856",
                        url="http://demo.twilio.com/docs/voice.xml"
                    )

print(call.sid)
 
