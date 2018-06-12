#!/usr/bin/env python2
'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment: Layer-2 Firewall Application
Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
import pox.lib.packet as pkt # POX convention


log = core.getLogger()

''' Add your global variables here ... '''
rules = (
    {'dl_src': EthAddr('00:00:00:00:00:01'),
     'dl_dst': EthAddr('00:00:00:00:00:02')},
    {'dl_src': EthAddr('00:00:00:00:00:02'),
     'dl_dst': EthAddr('00:00:00:00:00:01')},
    {'dl_type': pkt.ethernet.IP_TYPE, 'tp_dst': 80,
     'nw_proto': pkt.ipv4.TCP_PROTOCOL},
    {'dl_type': pkt.ethernet.IP_TYPE, 'tp_dst': 80,
     'nw_proto': pkt.ipv4.UDP_PROTOCOL},
    {'dl_src': EthAddr('00:00:00:00:00:01'), 'dl_type': pkt.ethernet.IP_TYPE,
     'tp_dst': 5001, 'nw_proto': pkt.ipv4.UDP_PROTOCOL},
)

class Firewall (EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp(self, event):
        ''' Add your logic here ... '''
        for rule in rules:
            match = of.ofp_match(**rule)
            msg = of.ofp_flow_mod(priority=1, match=match)
            event.connection.send(msg)


def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
