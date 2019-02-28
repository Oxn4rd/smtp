import smtpd
import asyncore
import argparse


peerperr = ('127.0.0.1', 2025)


class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peerperr, mailfrom, rcpttos, data,
                        mail_options=None, rcpt_options=None):
        print('Message Received from:', peer)
        print('From:', mailfrom)
        print('To :', rcpttos)
        print('Message :', data)
        return


parser = argparse.ArgumentParser(description='Mail Server Example')
parser.add_argument('--host', action="store",
                    dest="host", type=str, required=True)
parser.add_argument('--port', action="store",
                    dest="port", type=int, required=True)
given_args = parser.parse_args()
server = CustomSMTPServer((given_args.host, given_args.port), None)
asyncore.loop()
