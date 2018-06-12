#!/usr/bin/python
# -*- coding: utf-8 -*-
from mininet.topo import Topo
import math

def get_switch_amount(switch_level):
    sum = math.pow(2, switch_level-1)
    while (0 < switch_level-1):
        sum = sum + math.pow(2, switch_level-1)
        switch_level -= 1
    return int(sum)

class Topo1(Topo):
    """Topología 1 - TP3 Introducción a Sistemas Distribuidos"""

    def __init__(self, switchLvl, hostCount):
        Topo.__init__(self)
        hosts = []
        switches = []

        switchCount = get_switch_amount(switchLvl)

        print switchCount

        # create hosts
        for hostNum in range(hostCount):
            hosts.append(self.addHost('h'+ str(hostNum+1)))

        # create switches
        for switchNum in range(switchCount):
            switches.append(self.addSwitch('s' + str(switchNum+1)))

        # link border hosts
        splitHostIndex = int(hostCount / 2)
        print splitHostIndex
        for hostNum in range(hostCount):
            if (hostNum < splitHostIndex):
                self.addLink(hosts[hostNum], switches[0])
            else:
                self.addLink(hosts[hostNum], switches[-1])

        # link switches, left tree
        for i in range(2**(switchLvl-1) - 1):   # 0 a 2^(N-1)-2
            self.addLink(switches[i], switches[2*i + 1])
            self.addLink(switches[i], switches[2*i + 2])

        # link switches, right tree
        for i in range(1, 2**(switchLvl-1)):    # -1 a -2^(N-1)-1
            self.addLink(switches[-(2*i)],     switches[-i])
            self.addLink(switches[-(2*i + 1)], switches[-i])


topos = { 'topo1': lambda s, h: Topo1(s, h) }
