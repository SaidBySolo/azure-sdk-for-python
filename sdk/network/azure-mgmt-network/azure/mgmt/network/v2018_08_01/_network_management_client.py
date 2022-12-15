# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from .._serialization import Deserializer, Serializer
from ._configuration import NetworkManagementClientConfiguration
from .operations import (
    ApplicationGatewaysOperations,
    ApplicationSecurityGroupsOperations,
    AvailableDelegationsOperations,
    AvailableEndpointServicesOperations,
    AvailableResourceGroupDelegationsOperations,
    AzureFirewallFqdnTagsOperations,
    AzureFirewallsOperations,
    BgpServiceCommunitiesOperations,
    ConnectionMonitorsOperations,
    DdosProtectionPlansOperations,
    DefaultSecurityRulesOperations,
    ExpressRouteCircuitAuthorizationsOperations,
    ExpressRouteCircuitConnectionsOperations,
    ExpressRouteCircuitPeeringsOperations,
    ExpressRouteCircuitsOperations,
    ExpressRouteConnectionsOperations,
    ExpressRouteCrossConnectionPeeringsOperations,
    ExpressRouteCrossConnectionsOperations,
    ExpressRouteGatewaysOperations,
    ExpressRouteLinksOperations,
    ExpressRoutePortsLocationsOperations,
    ExpressRoutePortsOperations,
    ExpressRouteServiceProvidersOperations,
    HubVirtualNetworkConnectionsOperations,
    InboundNatRulesOperations,
    InterfaceEndpointsOperations,
    LoadBalancerBackendAddressPoolsOperations,
    LoadBalancerFrontendIPConfigurationsOperations,
    LoadBalancerLoadBalancingRulesOperations,
    LoadBalancerNetworkInterfacesOperations,
    LoadBalancerOutboundRulesOperations,
    LoadBalancerProbesOperations,
    LoadBalancersOperations,
    LocalNetworkGatewaysOperations,
    NetworkInterfaceIPConfigurationsOperations,
    NetworkInterfaceLoadBalancersOperations,
    NetworkInterfaceTapConfigurationsOperations,
    NetworkInterfacesOperations,
    NetworkManagementClientOperationsMixin,
    NetworkProfilesOperations,
    NetworkSecurityGroupsOperations,
    NetworkWatchersOperations,
    Operations,
    P2SVpnGatewaysOperations,
    P2SVpnServerConfigurationsOperations,
    PacketCapturesOperations,
    PublicIPAddressesOperations,
    PublicIPPrefixesOperations,
    RouteFilterRulesOperations,
    RouteFiltersOperations,
    RouteTablesOperations,
    RoutesOperations,
    SecurityRulesOperations,
    ServiceEndpointPoliciesOperations,
    ServiceEndpointPolicyDefinitionsOperations,
    SubnetsOperations,
    UsagesOperations,
    VirtualHubsOperations,
    VirtualNetworkGatewayConnectionsOperations,
    VirtualNetworkGatewaysOperations,
    VirtualNetworkPeeringsOperations,
    VirtualNetworkTapsOperations,
    VirtualNetworksOperations,
    VirtualWansOperations,
    VpnConnectionsOperations,
    VpnGatewaysOperations,
    VpnSitesConfigurationOperations,
    VpnSitesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class NetworkManagementClient(
    NetworkManagementClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Network Client.

    :ivar application_gateways: ApplicationGatewaysOperations operations
    :vartype application_gateways:
     azure.mgmt.network.v2018_08_01.operations.ApplicationGatewaysOperations
    :ivar application_security_groups: ApplicationSecurityGroupsOperations operations
    :vartype application_security_groups:
     azure.mgmt.network.v2018_08_01.operations.ApplicationSecurityGroupsOperations
    :ivar available_delegations: AvailableDelegationsOperations operations
    :vartype available_delegations:
     azure.mgmt.network.v2018_08_01.operations.AvailableDelegationsOperations
    :ivar available_resource_group_delegations: AvailableResourceGroupDelegationsOperations
     operations
    :vartype available_resource_group_delegations:
     azure.mgmt.network.v2018_08_01.operations.AvailableResourceGroupDelegationsOperations
    :ivar azure_firewalls: AzureFirewallsOperations operations
    :vartype azure_firewalls: azure.mgmt.network.v2018_08_01.operations.AzureFirewallsOperations
    :ivar azure_firewall_fqdn_tags: AzureFirewallFqdnTagsOperations operations
    :vartype azure_firewall_fqdn_tags:
     azure.mgmt.network.v2018_08_01.operations.AzureFirewallFqdnTagsOperations
    :ivar ddos_protection_plans: DdosProtectionPlansOperations operations
    :vartype ddos_protection_plans:
     azure.mgmt.network.v2018_08_01.operations.DdosProtectionPlansOperations
    :ivar available_endpoint_services: AvailableEndpointServicesOperations operations
    :vartype available_endpoint_services:
     azure.mgmt.network.v2018_08_01.operations.AvailableEndpointServicesOperations
    :ivar express_route_circuit_authorizations: ExpressRouteCircuitAuthorizationsOperations
     operations
    :vartype express_route_circuit_authorizations:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteCircuitAuthorizationsOperations
    :ivar express_route_circuit_peerings: ExpressRouteCircuitPeeringsOperations operations
    :vartype express_route_circuit_peerings:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteCircuitPeeringsOperations
    :ivar express_route_circuit_connections: ExpressRouteCircuitConnectionsOperations operations
    :vartype express_route_circuit_connections:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteCircuitConnectionsOperations
    :ivar express_route_circuits: ExpressRouteCircuitsOperations operations
    :vartype express_route_circuits:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteCircuitsOperations
    :ivar express_route_service_providers: ExpressRouteServiceProvidersOperations operations
    :vartype express_route_service_providers:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteServiceProvidersOperations
    :ivar express_route_cross_connections: ExpressRouteCrossConnectionsOperations operations
    :vartype express_route_cross_connections:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteCrossConnectionsOperations
    :ivar express_route_cross_connection_peerings: ExpressRouteCrossConnectionPeeringsOperations
     operations
    :vartype express_route_cross_connection_peerings:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteCrossConnectionPeeringsOperations
    :ivar express_route_gateways: ExpressRouteGatewaysOperations operations
    :vartype express_route_gateways:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteGatewaysOperations
    :ivar express_route_connections: ExpressRouteConnectionsOperations operations
    :vartype express_route_connections:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteConnectionsOperations
    :ivar express_route_ports_locations: ExpressRoutePortsLocationsOperations operations
    :vartype express_route_ports_locations:
     azure.mgmt.network.v2018_08_01.operations.ExpressRoutePortsLocationsOperations
    :ivar express_route_ports: ExpressRoutePortsOperations operations
    :vartype express_route_ports:
     azure.mgmt.network.v2018_08_01.operations.ExpressRoutePortsOperations
    :ivar express_route_links: ExpressRouteLinksOperations operations
    :vartype express_route_links:
     azure.mgmt.network.v2018_08_01.operations.ExpressRouteLinksOperations
    :ivar interface_endpoints: InterfaceEndpointsOperations operations
    :vartype interface_endpoints:
     azure.mgmt.network.v2018_08_01.operations.InterfaceEndpointsOperations
    :ivar load_balancers: LoadBalancersOperations operations
    :vartype load_balancers: azure.mgmt.network.v2018_08_01.operations.LoadBalancersOperations
    :ivar load_balancer_backend_address_pools: LoadBalancerBackendAddressPoolsOperations operations
    :vartype load_balancer_backend_address_pools:
     azure.mgmt.network.v2018_08_01.operations.LoadBalancerBackendAddressPoolsOperations
    :ivar load_balancer_frontend_ip_configurations: LoadBalancerFrontendIPConfigurationsOperations
     operations
    :vartype load_balancer_frontend_ip_configurations:
     azure.mgmt.network.v2018_08_01.operations.LoadBalancerFrontendIPConfigurationsOperations
    :ivar inbound_nat_rules: InboundNatRulesOperations operations
    :vartype inbound_nat_rules: azure.mgmt.network.v2018_08_01.operations.InboundNatRulesOperations
    :ivar load_balancer_load_balancing_rules: LoadBalancerLoadBalancingRulesOperations operations
    :vartype load_balancer_load_balancing_rules:
     azure.mgmt.network.v2018_08_01.operations.LoadBalancerLoadBalancingRulesOperations
    :ivar load_balancer_outbound_rules: LoadBalancerOutboundRulesOperations operations
    :vartype load_balancer_outbound_rules:
     azure.mgmt.network.v2018_08_01.operations.LoadBalancerOutboundRulesOperations
    :ivar load_balancer_network_interfaces: LoadBalancerNetworkInterfacesOperations operations
    :vartype load_balancer_network_interfaces:
     azure.mgmt.network.v2018_08_01.operations.LoadBalancerNetworkInterfacesOperations
    :ivar load_balancer_probes: LoadBalancerProbesOperations operations
    :vartype load_balancer_probes:
     azure.mgmt.network.v2018_08_01.operations.LoadBalancerProbesOperations
    :ivar network_interfaces: NetworkInterfacesOperations operations
    :vartype network_interfaces:
     azure.mgmt.network.v2018_08_01.operations.NetworkInterfacesOperations
    :ivar network_interface_ip_configurations: NetworkInterfaceIPConfigurationsOperations
     operations
    :vartype network_interface_ip_configurations:
     azure.mgmt.network.v2018_08_01.operations.NetworkInterfaceIPConfigurationsOperations
    :ivar network_interface_load_balancers: NetworkInterfaceLoadBalancersOperations operations
    :vartype network_interface_load_balancers:
     azure.mgmt.network.v2018_08_01.operations.NetworkInterfaceLoadBalancersOperations
    :ivar network_interface_tap_configurations: NetworkInterfaceTapConfigurationsOperations
     operations
    :vartype network_interface_tap_configurations:
     azure.mgmt.network.v2018_08_01.operations.NetworkInterfaceTapConfigurationsOperations
    :ivar network_profiles: NetworkProfilesOperations operations
    :vartype network_profiles: azure.mgmt.network.v2018_08_01.operations.NetworkProfilesOperations
    :ivar network_security_groups: NetworkSecurityGroupsOperations operations
    :vartype network_security_groups:
     azure.mgmt.network.v2018_08_01.operations.NetworkSecurityGroupsOperations
    :ivar security_rules: SecurityRulesOperations operations
    :vartype security_rules: azure.mgmt.network.v2018_08_01.operations.SecurityRulesOperations
    :ivar default_security_rules: DefaultSecurityRulesOperations operations
    :vartype default_security_rules:
     azure.mgmt.network.v2018_08_01.operations.DefaultSecurityRulesOperations
    :ivar network_watchers: NetworkWatchersOperations operations
    :vartype network_watchers: azure.mgmt.network.v2018_08_01.operations.NetworkWatchersOperations
    :ivar packet_captures: PacketCapturesOperations operations
    :vartype packet_captures: azure.mgmt.network.v2018_08_01.operations.PacketCapturesOperations
    :ivar connection_monitors: ConnectionMonitorsOperations operations
    :vartype connection_monitors:
     azure.mgmt.network.v2018_08_01.operations.ConnectionMonitorsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.network.v2018_08_01.operations.Operations
    :ivar public_ip_addresses: PublicIPAddressesOperations operations
    :vartype public_ip_addresses:
     azure.mgmt.network.v2018_08_01.operations.PublicIPAddressesOperations
    :ivar public_ip_prefixes: PublicIPPrefixesOperations operations
    :vartype public_ip_prefixes:
     azure.mgmt.network.v2018_08_01.operations.PublicIPPrefixesOperations
    :ivar route_filters: RouteFiltersOperations operations
    :vartype route_filters: azure.mgmt.network.v2018_08_01.operations.RouteFiltersOperations
    :ivar route_filter_rules: RouteFilterRulesOperations operations
    :vartype route_filter_rules:
     azure.mgmt.network.v2018_08_01.operations.RouteFilterRulesOperations
    :ivar route_tables: RouteTablesOperations operations
    :vartype route_tables: azure.mgmt.network.v2018_08_01.operations.RouteTablesOperations
    :ivar routes: RoutesOperations operations
    :vartype routes: azure.mgmt.network.v2018_08_01.operations.RoutesOperations
    :ivar bgp_service_communities: BgpServiceCommunitiesOperations operations
    :vartype bgp_service_communities:
     azure.mgmt.network.v2018_08_01.operations.BgpServiceCommunitiesOperations
    :ivar service_endpoint_policies: ServiceEndpointPoliciesOperations operations
    :vartype service_endpoint_policies:
     azure.mgmt.network.v2018_08_01.operations.ServiceEndpointPoliciesOperations
    :ivar service_endpoint_policy_definitions: ServiceEndpointPolicyDefinitionsOperations
     operations
    :vartype service_endpoint_policy_definitions:
     azure.mgmt.network.v2018_08_01.operations.ServiceEndpointPolicyDefinitionsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.network.v2018_08_01.operations.UsagesOperations
    :ivar virtual_networks: VirtualNetworksOperations operations
    :vartype virtual_networks: azure.mgmt.network.v2018_08_01.operations.VirtualNetworksOperations
    :ivar subnets: SubnetsOperations operations
    :vartype subnets: azure.mgmt.network.v2018_08_01.operations.SubnetsOperations
    :ivar virtual_network_peerings: VirtualNetworkPeeringsOperations operations
    :vartype virtual_network_peerings:
     azure.mgmt.network.v2018_08_01.operations.VirtualNetworkPeeringsOperations
    :ivar virtual_network_taps: VirtualNetworkTapsOperations operations
    :vartype virtual_network_taps:
     azure.mgmt.network.v2018_08_01.operations.VirtualNetworkTapsOperations
    :ivar virtual_network_gateways: VirtualNetworkGatewaysOperations operations
    :vartype virtual_network_gateways:
     azure.mgmt.network.v2018_08_01.operations.VirtualNetworkGatewaysOperations
    :ivar virtual_network_gateway_connections: VirtualNetworkGatewayConnectionsOperations
     operations
    :vartype virtual_network_gateway_connections:
     azure.mgmt.network.v2018_08_01.operations.VirtualNetworkGatewayConnectionsOperations
    :ivar local_network_gateways: LocalNetworkGatewaysOperations operations
    :vartype local_network_gateways:
     azure.mgmt.network.v2018_08_01.operations.LocalNetworkGatewaysOperations
    :ivar virtual_wans: VirtualWansOperations operations
    :vartype virtual_wans: azure.mgmt.network.v2018_08_01.operations.VirtualWansOperations
    :ivar vpn_sites: VpnSitesOperations operations
    :vartype vpn_sites: azure.mgmt.network.v2018_08_01.operations.VpnSitesOperations
    :ivar vpn_sites_configuration: VpnSitesConfigurationOperations operations
    :vartype vpn_sites_configuration:
     azure.mgmt.network.v2018_08_01.operations.VpnSitesConfigurationOperations
    :ivar virtual_hubs: VirtualHubsOperations operations
    :vartype virtual_hubs: azure.mgmt.network.v2018_08_01.operations.VirtualHubsOperations
    :ivar hub_virtual_network_connections: HubVirtualNetworkConnectionsOperations operations
    :vartype hub_virtual_network_connections:
     azure.mgmt.network.v2018_08_01.operations.HubVirtualNetworkConnectionsOperations
    :ivar vpn_gateways: VpnGatewaysOperations operations
    :vartype vpn_gateways: azure.mgmt.network.v2018_08_01.operations.VpnGatewaysOperations
    :ivar vpn_connections: VpnConnectionsOperations operations
    :vartype vpn_connections: azure.mgmt.network.v2018_08_01.operations.VpnConnectionsOperations
    :ivar p2_svpn_server_configurations: P2SVpnServerConfigurationsOperations operations
    :vartype p2_svpn_server_configurations:
     azure.mgmt.network.v2018_08_01.operations.P2SVpnServerConfigurationsOperations
    :ivar p2_svpn_gateways: P2SVpnGatewaysOperations operations
    :vartype p2_svpn_gateways: azure.mgmt.network.v2018_08_01.operations.P2SVpnGatewaysOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft
     Azure subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = NetworkManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.application_gateways = ApplicationGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.application_security_groups = ApplicationSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.available_delegations = AvailableDelegationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.available_resource_group_delegations = AvailableResourceGroupDelegationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.azure_firewalls = AzureFirewallsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.azure_firewall_fqdn_tags = AzureFirewallFqdnTagsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.ddos_protection_plans = DdosProtectionPlansOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.available_endpoint_services = AvailableEndpointServicesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_circuit_authorizations = ExpressRouteCircuitAuthorizationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_circuit_peerings = ExpressRouteCircuitPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_circuit_connections = ExpressRouteCircuitConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_circuits = ExpressRouteCircuitsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_service_providers = ExpressRouteServiceProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_cross_connections = ExpressRouteCrossConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_cross_connection_peerings = ExpressRouteCrossConnectionPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_gateways = ExpressRouteGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_connections = ExpressRouteConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_ports_locations = ExpressRoutePortsLocationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_ports = ExpressRoutePortsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_links = ExpressRouteLinksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.interface_endpoints = InterfaceEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.load_balancers = LoadBalancersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.load_balancer_backend_address_pools = LoadBalancerBackendAddressPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.load_balancer_frontend_ip_configurations = LoadBalancerFrontendIPConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.inbound_nat_rules = InboundNatRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.load_balancer_load_balancing_rules = LoadBalancerLoadBalancingRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.load_balancer_outbound_rules = LoadBalancerOutboundRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.load_balancer_network_interfaces = LoadBalancerNetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.load_balancer_probes = LoadBalancerProbesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_interfaces = NetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_interface_ip_configurations = NetworkInterfaceIPConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_interface_load_balancers = NetworkInterfaceLoadBalancersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_interface_tap_configurations = NetworkInterfaceTapConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_profiles = NetworkProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_security_groups = NetworkSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.security_rules = SecurityRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.default_security_rules = DefaultSecurityRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_watchers = NetworkWatchersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.packet_captures = PacketCapturesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection_monitors = ConnectionMonitorsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.public_ip_addresses = PublicIPAddressesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.public_ip_prefixes = PublicIPPrefixesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.route_filters = RouteFiltersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.route_filter_rules = RouteFilterRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.route_tables = RouteTablesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.routes = RoutesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.bgp_service_communities = BgpServiceCommunitiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.service_endpoint_policies = ServiceEndpointPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.service_endpoint_policy_definitions = ServiceEndpointPolicyDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_networks = VirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.subnets = SubnetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_peerings = VirtualNetworkPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_network_taps = VirtualNetworkTapsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_network_gateways = VirtualNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_network_gateway_connections = VirtualNetworkGatewayConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.local_network_gateways = LocalNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_wans = VirtualWansOperations(self._client, self._config, self._serialize, self._deserialize)
        self.vpn_sites = VpnSitesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.vpn_sites_configuration = VpnSitesConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_hubs = VirtualHubsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.hub_virtual_network_connections = HubVirtualNetworkConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.vpn_gateways = VpnGatewaysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.vpn_connections = VpnConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.p2_svpn_server_configurations = P2SVpnServerConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.p2_svpn_gateways = P2SVpnGatewaysOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> NetworkManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
