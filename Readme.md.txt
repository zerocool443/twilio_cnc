Setup a VPS on cloud.

Take an example - ubuntu server

Push the files to home directory.

http_channel.py  - setup your flask microservice on you mentioned port and read http get and post message on your domain/ip for that port. Also logs it to data.txt

push_sms.py <message> <from number > <to number>  # Must have twilio account and verified number

push_whatsapp <message> <from number> <to number> #Must have twilio and joined whatsapp beta programme

Configure your http_channel.py as service on your ubuntu machine.
Refer to directory - linux_systemd_service_conf for instructions.