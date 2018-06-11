#!/usr/bin/env python
from mininet.topo import Topo


class DiamondTopo(Topo):

    def build(self, hosts, levels, *args, **kwargs):
        """
        Builds a diamond topology.

        :hosts: Total amount of hosts to add.
        :levels: Amount of levels the topology would have.
        """
        host_list = [self.addHost('h%d' % i) for i in xrange(1, hosts + 1)]
        # Total number of switches
        n = 3 * 2 ** (levels - 1) - 2
        switches = [self.addSwitch('s%d' % i) for i in xrange(1, n + 1)]
        # Links hosts against border switches
        for host in host_list[:hosts - hosts / 2]:
            self.addLink(switches[0], host)
        for host in host_list[hosts - hosts / 2:]:
            self.addLink(switches[-1], host)
        # Links switches 
        next_switch = 1
        for i in xrange(2 ** (levels - 1) - 1):
            for _ in range(2):
                self.addLink(switches[i], switches[next_switch])
                self.addLink(switches[-1 - i], switches[-1 - next_switch])
                next_switch += 1


class SimpleTopo(Topo):

    def build(self, n, *args, **kwargs):
        """
        Builds a simple linear topology with 2 host connected on each
        border switch.

        :n: Amount of switches to create.
        """
        switches = [self.addSwitch('s%d' % i) for i in xrange(1, n + 1)]
        for s in xrange(1, len(switches)):
            self.addLink(switches[s - 1], switches[s])
        for (s, i) in zip((0, 0, -1, -1), range(1, 5)):
            self.addLink(switches[s], self.addHost('h%d' % i))


topos = {'diamond': DiamondTopo, 'simple': SimpleTopo}
