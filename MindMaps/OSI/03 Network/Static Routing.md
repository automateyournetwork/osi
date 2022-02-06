# Static routing
## [URL](https://en.wikipedia.org/wiki/Static_routing) - https://en.wikipedia.org/wiki/Static_routing
## Catagories
### All articles with unsourced statements
### Articles with unsourced statements from December 2017
### Routing
### "Static routing is a form of routing that occurs when a router uses a manually-configured routing entry, rather than information from dynamic routing traffic. In many cases, static routes are manually configured by a network administrator by adding in entries into a routing table, though this may not always be the case. Unlike dynamic routing, static routes are fixed and do not change if the network is changed or reconfigured. Static routing and dynamic routing are not mutually exclusive. Both dynamic routing and static routing are usually used on a router to maximise routing efficiency and to provide backups in case dynamic routing information fails to be exchanged. Static routing can also be used in stub networks, or to provide a gateway of last resort.
## Uses  
### Static routing may have the following uses: 

### Static routing can be used to define an exit point from a router when no other routes are available or necessary. This is called a default route. 
### Static routing can be used for small networks that require only one or two routes. This is often more efficient since a link is not being wasted by exchanging dynamic routing information. 
### Static routing is often used as a complement to dynamic routing to provide a failsafe backup if a dynamic route is unavailable. 
### Static routing is often used to help transfer routing information from one routing protocol to another (routing redistribution).
## Advantages  
### Static routing, if used without dynamic routing, has the following advantages: 
### Static routing causes very little load on the CPU of the router, and produces no traffic to other routers. 
### Static routing leaves the network administrator with full control over the routing behavior of the network. 
### Static Routing Is very easy to configure on small networks.
## Disadvantages  
### Static routing can have some potential disadvantages: 
### Human error: In many cases, static routes are manually configured. This increases the potential for input mistakes. Administrators can make mistakes and mistype in network information, or configure incorrect routing paths by mistake. 
### Fault tolerance: Static routing is not fault tolerant. This means that when there is a change in the network or a failure occurs between two statically defined devices, traffic will not be re-routed. As a result, the network is unusable until the failure is repaired or the static route is manually reconfigured by an administrator. 
### Administrative distance: Static routes typically take precedence over routes configured with a dynamic routing protocol. This means that static routes may prevent routing protocols from working as intended. A solution is to manually modify the administrative distance. 
### Administrative overhead: Static routes must be configured on each router in the network(s). This configuration can take a long time if there are many routers. It also means that reconfiguration can be slow and inefficient. Dynamic routing on the other hand automatically propagates routing changes, reducing the need for manual reconfiguration.
## Example  
### To route IP traffic destined for the network 10.10.20.0/24 via the next-hop router with the IPv4 address of 192.168.100.1, the following configuration commands or steps can be used:
## Linux  
### In most Linux distributions, a static route can be added using the iproute2 command. The following is typed at a terminal:-
## Cisco  
### Enterprise-level Cisco routers are configurable using the Cisco IOS command line, rather than a web management interface.
## Add a static route  
### The commands to add a static route are as follows: 
### Router> enable 
### Router# configure terminal 
### Router(config)# ip route 10.10.20.0 255.255.255.0 192.168.100.1 

### Network configurations are not restricted to a single static route per destination: 
### Router> enable 
### Router# configure terminal 
### Router(config)# ip route 197.164.73.0 255.255.255.0 197.164.72.2 
### Router(config)# ip route 197.164.74.0 255.255.255.0 197.164.72.2
## Configuring administrative distance  
### The administrative distance can be manually (re)configured so that the static route can be configured as a backup route, to be used only if the dynamic route is unavailable.Router(config)# ip route 10.10.20.0 255.255.255.0 exampleRoute 1 254 
### Setting the administrative distance to 254 will result in the route being used only as a backup.
## See also 
## References "
## References
### [Reference](http://www.cisco.com/c/en/us/td/docs/ios/dial/configuration/guide/12_2sr/dia_12_2sr_book/dia_rel_stc_rtg_bckup.html) - http://www.cisco.com/c/en/us/td/docs/ios/dial/configuration/guide/12_2sr/dia_12_2sr_book/dia_rel_stc_rtg_bckup.html
### [Reference](http://www.cisco.com/en/US/docs/ios/12_3t/ip_route/command/reference/ip2_i2gt.html#wp1106404) - http://www.cisco.com/en/US/docs/ios/12_3t/ip_route/command/reference/ip2_i2gt.html#wp1106404
### [Reference](http://www.cisco.com/en/US/docs/switches/datacenter/sw/5_x/nx-os/unicast/configuration/guide/l3_route.html) - http://www.cisco.com/en/US/docs/switches/datacenter/sw/5_x/nx-os/unicast/configuration/guide/l3_route.html
### [Reference](http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a0080094195.shtml) - http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a0080094195.shtml
### [Reference](http://www.dummies.com/how-to/content/pros-and-cons-of-static-routing.html) - http://www.dummies.com/how-to/content/pros-and-cons-of-static-routing.html
### [Reference](http://www.redbooks.ibm.com/redbooks/pdfs/gg243376.pdf) - http://www.redbooks.ibm.com/redbooks/pdfs/gg243376.pdf
### [Reference](https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/5/html/Deployment_Guide/s1-networkscripts-static-routes.html) - https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/5/html/Deployment_Guide/s1-networkscripts-static-routes.html
## Images