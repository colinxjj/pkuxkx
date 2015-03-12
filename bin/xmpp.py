#!/usr/bin/env python
import sys
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout

class Bot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
	    body = msg['body'].decode("GBK").encode("UTF-8")
	    print ("xmpp message: %s:%s\n" % (msg['from'],body))

if __name__ == '__main__':
    xmpp = Bot(sys.argv[1]+'@localhost/xkx', '123456')
    xmpp.connect(("45.62.101.109",5222))
    xmpp.process(block=False)
    while (True):
	line = sys.stdin.readline().decode("GBK").encode("UTF-8")
	xmpp.send_message(mto="messenger@localhost/xkx", mbody=line, mtype='chat')
	
