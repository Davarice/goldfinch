"""
The Market is made up of Nodes, each of which may be connected to a number of Sinks. Nodes connect to each other by way of Ports.

A Node represents a local market, the availability and demand of goods and currency for a given region. It contains certain amounts of various goods, and a value in money.

A Sink represents a private entity or individual, and interacts with the Market via a Node. A Sink may sell goods to the Node, receiving money from it, or purchase goods from the Node, contributing money to it.
"""
import collections


class Resource:
    idx = [] # List of all Resources

    def __init__(self, name, unit="crate", priceBase=10):
        self.name = name
        self.unit = unit
        self.priceBase = priceBase

        self.idx.append(self)

    def __str__(self):
        return self.name + f" (${self.priceBase})"

Resource("Food","crate",10)
Resource("Water","tank",6)
Resource("Spices","box",15)


class Node:
    idx = [] # List of all Nodes

    def __init__(self, name, value=0, ports=[]):
        self.name = name

        self.value = value
        self.ports = ports

        # The supply is the amount of each good that can be found in this Node; It may be stored in warehouses, marketplaces...Basically, this is what is available to be purchased in this region.
        self.supply = {x:0 for x in Resource.idx}
        self.demand = {x:1.0 for x in Resource.idx}
        #self.prices = {x:x.priceBase for x in Resource.idx}

        self.idx.append(self)

    def BuyFrom(self, dest, resource, amount):
        pass

    def SellTo(self, dest, resource, amount):
        pass

    @property
    def Economy(self):
        return [f"Price of {x.name}: ${x.priceBase*self.demand[x]} per {x.unit} (Base price ${x.priceBase})" for x in Resource.idx]



class Sink:
    pass
