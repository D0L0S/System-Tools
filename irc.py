#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

class IRCClient:
    socket = None
    connected = False
    nickname = 'Nick'
    channels = ['#python']

    def __init__(self):
        self.socket = socket.socket()
        self.socket.connect(('irc.freenode.org', 6667))
        self.send("NICK {Nick}".format(Nick=self.nickname))
        self.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s" % {'nick':self.nickname})

        while True:
            buf = self.socket.recv(4096)
            lines = buf.split("\n")
            for data in lines:
                data = str(data).strip()

                if data == '':
                    continue
                print "I<", data

                # server ping/pong?
                if data.find('PING') != -1:
                    n = data.split(':')[1]
                    self.send('PONG :' + n)
                    if self.connected == False:
                        self.perform()
                        self.connected = True

                args = data.split(None, 3)
                if len(args) != 4:
                    continue
                ctx = {}
                ctx['sender'] = args[0][1:]
                ctx['type']   = args[1]
                ctx['target'] = args[2]
                ctx['msg']    = args[3][1:]

                # whom to reply?
                target = ctx['target']
                if ctx['target'] == self.nickname:
                    target = ctx['sender'].split("!")[0]

                # some basic commands
                if ctx['msg'] == '!help':
                    self.say('available commands: !help', target)

                # directed to the bot?
                if ctx['type'] == 'PRIVMSG' and (ctx['msg'].lower()[0:len(self.nickname)] == self.nickname.lower() or ctx['target'] == self.nickname):
                    # something is speaking to the bot
                    query = ctx['msg']
                    if ctx['target'] != self.nickname:
                        query = query[len(self.nickname):]
                        query = query.lstrip(':,;. ')
                    # do something intelligent here, like query a chatterbot
                    print 'someone spoke to us: ', query
                    self.say('alright :|', target)

    def send(self, msg):
        print "I>",msg
        self.socket.send(msg+"\r\n")

    def say(self, msg, to):
        self.send("PRIVMSG {TO} :{Message}".format(TO=to, Message=msg))

    def perform(self):
        #self.send("PRIVMSG R : Register <>")
        self.send("PRIVMSG R : Login <>")
        self.send("MODE {Nick} +x".format(Nick=self.nickname))
        for c in self.channels:
            self.send("JOIN {C}".format(C=c))
            # say hello to every channel
            self.say('hello world!', c)

if __name__=="__main__":
	IRCClient()
