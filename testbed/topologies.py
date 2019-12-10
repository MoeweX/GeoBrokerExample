from networkx.classes import Graph

from common import node_attrs, edge_attrs, client_config, broker_config


def simple_topology(g: Graph):
    # zones are used to prevent cyclies
    g.add_node('cloud1', **node_attrs(type='zone'))

    # if you do not supply a zone, the node is interpreted as being a machine
    # the role is attached as tag to the AWS instance and can be used to run tasks only on machines with a certain role (see mockfog_application.yml notebook)
    g.add_node('broker1', **node_attrs(role='broker',
                                              app_configs=[
                                                  broker_config(
                                                  )]))
    g.add_node('client1', **node_attrs(role='client',
                                              app_configs=[
                                                  client_config(
                                                      connect_to='broker1'
                                                  )]))
    g.add_node('client2', **node_attrs(role='client',
                                              app_configs=[
                                                  client_config(
                                                      connect_to='broker1'
                                                  )]))


    g.add_edge('broker1', 'cloud1', **edge_attrs(delay=0))
    g.add_edge('client1', 'cloud1', **edge_attrs(delay=5))
    g.add_edge('client2', 'cloud1', **edge_attrs(delay=10))
