#!/usr/bin/python
from mininet.topo import Topo

import math

def get_switch_amount(switch_level):
  sum = math.pow(2, switch_level-1)
  while (0 < switch_level-1):
    sum = sum + math.pow(2, switch_level-1)
    switch_level -= 1
  return int(sum)

class Topo1(Topo):
  """Topologia 1 - TP3 Introduccion a Sistemas Distribuidos"""

  def __init__(self, switchLvl, hostCount):
    Topo.__init__(self)
    hosts = []
    switches = []

    switchAmount = get_switch_amount(switchLvl)

    print switchAmount

    # create hosts
    for hostNum in range(hostCount):
      h = self.addHost('h'+ str(hostNum+1))
      hosts.append(h)
    
    # create switches
    for switchNum in range(switchAmount):
      s = self.addSwitch('s' + str(switchNum+1))
      switches.append(s)
      
    # link border hosts
    splitHostIndex = int(len(hosts) / 2)
    print splitHostIndex
    for hostNum in range(len(hosts)):
      if (hostNum < splitHostIndex):
        self.addLink(hosts[hostNum], switches[0])
      else:
        self.addLink(hosts[hostNum], switches[len(switches)-1])

    # handle switch levels
    # TODO: improve, hardcoded
    if (switchLvl == 2):
      self.addLink(switches[0], switches[1])
      self.addLink(switches[0], switches[2])
      self.addLink(switches[1], switches[len(switches)-1])
      self.addLink(switches[2], switches[len(switches)-1])

    if (switchLvl == 3):
      self.addLink(switches[0], switches[1])
      self.addLink(switches[0], switches[2])
      self.addLink(switches[len(switches)-2], switches[len(switches)-1])
      self.addLink(switches[len(switches)-3], switches[len(switches)-1])
      self.addLink(switches[1], switches[3])
      self.addLink(switches[1], switches[4])
      self.addLink(switches[3], switches[len(switches)-2])
      self.addLink(switches[4], switches[len(switches)-2])
      self.addLink(switches[2], switches[5])
      self.addLink(switches[2], switches[6])
      self.addLink(switches[5], switches[len(switches)-3])
      self.addLink(switches[6], switches[len(switches)-3])

topos = { 'topo1': lambda s, h: Topo1(s, h) }
