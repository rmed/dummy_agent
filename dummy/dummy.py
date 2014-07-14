#!/usr/bin/env python3

import zoe
from zoe.deco import *

@Agent(name = "dummy")
class DummyAgent:

    #
    # echo -n "dst=dummy&tag=test&key_a=value_a1&key_a=value_a2&key_b=value_b" | nc localhost 30000 
    #
    @Message(tags = ["test"])
    def receive(self, parser):
        print("Hi, I'm a test agent and I have received the following message:", parser)

