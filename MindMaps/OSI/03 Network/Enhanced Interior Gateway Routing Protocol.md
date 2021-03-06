# Enhanced Interior Gateway Routing Protocol
## [URL](https://en.wikipedia.org/wiki/Enhanced_Interior_Gateway_Routing_Protocol) - https://en.wikipedia.org/wiki/Enhanced_Interior_Gateway_Routing_Protocol
## Catagories
### Articles with LCCN identifiers
### Articles with short description
### Cisco protocols
### Routing protocols
### Short description matches Wikidata
### Webarchive template wayback links
### "Enhanced Interior Gateway Routing Protocol (EIGRP) is an advanced distance-vector routing protocol that is used on a computer network for automating routing decisions and configuration. The protocol was designed by Cisco Systems as a proprietary protocol, available only on Cisco routers. Functionality of EIGRP was converted to an open standard in 2013 and was published with informational status as RFC 7868 in 2016. 
### EIGRP is used on a router to share routes with other routers within the same autonomous system. Unlike other well known routing protocols, such as RIP, EIGRP only sends incremental updates, reducing the workload on the router and the amount of data that needs to be transmitted. 
### EIGRP replaced the Interior Gateway Routing Protocol (IGRP) in 1993. One of the major reasons for this was the change to classless IPv4 addresses in the Internet Protocol, which IGRP could not support.
## Overview  
### Almost all routers contain a routing table that contains rules by which traffic is forwarded in a network. If the router does not contain a valid path to the destination, the traffic is discarded. EIGRP is a dynamic routing protocol by which routers automatically share route information. This eases the workload on a network administrator who does not have to configure changes to the routing table manually. 
### In addition to the routing table, EIGRP uses the following tables to store information: 

### Neighbor Table: The neighbor table keeps a record of the IP addresses of routers that have a direct physical connection with this router. Routers that are connected to this router indirectly, through another router, are not recorded in this table as they are not considered neighbors. 
### Topology Table: The topology table stores routes that it has learned from neighbor routing tables. Unlike a routing table, the topology table does not store all routes, but only routes that have been determined by EIGRP. The topology table also records the metrics for each of the listed EIGRP routes, the feasible successor and the successors. Routes in the topology table are marked as \"passive\" or \"active\". Passive indicates that EIGRP has determined the path for the specific route and has finished processing. Active indicates that EIGRP is still trying to calculate the best path for the specific route. Routes in the topology table are not usable by the router until they are inserted into the routing table. The topology table is never used by the router to forward traffic. Routes in the topology table will not be inserted into the routing table if they are active, are a feasible successor, or have a higher administrative distance than an equivalent path.Information in the topology table may be inserted into the router's routing table and can then be used to forward traffic. If the network changes (for example, a physical link fails or is disconnected), the path will become unavailable.  EIGRP is designed to detect these changes and will attempt to find a new path to the destination. The old path that is no longer available is removed from the routing table. Unlike most distance vector routing protocols, EIGRP does not transmit all the data in the router's routing table when a change is made, but will only transmit the changes that have been made since the routing table was last updated. EIGRP does not send its routing table periodically, but will only send routing table data when an actual change has occurred.  This behavior is more inline with link-state routing protocols, thus EIGRP is mostly considered a hybrid protocol. 
### When a router running EIGRP is connected to another router also running EIGRP, information is exchanged between the two routers. They form a relationship, known as an adjacency. The entire routing table is exchanged between both routers at this time. After the exchange has completed, only differential changes are sent. 
### EIGRP is often considered a hybrid protocol because it also sends link state updates when link states change.
## Features  
### EIGRP supports the following features: 
### Support for Classless Inter-Domain Routing (CIDR) and variable length subnet masking. Routes are not summarized at the classful network boundary unless auto summary is enabled. 
### Support for load balancing on parallel links between sites. 
### The ability to use different authentication passwords at different times. 
### MD5 and SHA-2 authentication between two routers. 
### Sends topology changes, rather than sending the entire routing table when a route is changed. 
### Periodically checks if a route is available, and propagates routing changes to neighboring routers if any changes have occurred. 
### Runs separate routing processes for Internet Protocol (IP), IPv6, IPX and AppleTalk, through the use of protocol-dependent modules (PDMs). 
### Backwards compatibility with the IGRP routing protocols.
## Configuration 
## Cisco IOS example  
### Example of setting up EIGRP on a Cisco IOS router for a private network.  The 0.0.15.255 wildcard in this example indicates a subnetwork with a maximum of 4094 hosts\u2014it is the bitwise complement of the subnet mask 255.255.240.0.  The no auto-summary command prevents automatic route summarization on classful boundaries, which would otherwise result in routing loops in discontiguous networks. 

Router# configure terminal 
Router(config)# router eigrp 1 
Router (config-router)# network 10.201.96.0 0.0.15.255 
Router (config-router)# no auto-summary 
Router (config-router)# exit
## Technical details  
### EIGRP is a distance vector & Link State routing protocol that uses the diffusing update algorithm (DUAL) (based on work from SRI International) to improve the efficiency of the protocol and to help prevent calculation errors when attempting to determine the best path to a remote network. EIGRP determines the value of the path using five metrics: bandwidth, load, delay, reliability and MTU. EIGRP uses Five different messages to communicate with its neighbor routers. EIGRP messages are Hello, Update, Query, Reply, and Acknowledgement.EIGRP routing information exchanged to a router from another router within the same autonomous system has a default administrative distance of 90. EIGRP routing information that has come from an EIGRP-enabled router outside the autonomous system has a default administrative distance of 170.EIGRP does not operate using the Transmission Control Protocol (TCP) or the User Datagram Protocol (UDP). This means that EIGRP does not use a port number to identify traffic. Rather, EIGRP is designed to work on top of layer 3  (i.e. the IP protocol). Since EIGRP does not use TCP for communication, it implements Cisco's Reliable Transport Protocol (RTP) to ensure that EIGRP router updates are delivered to all neighbors completely. The reliable transport protocol also contains other mechanisms to maximize efficiency and support multicasting. EIGRP uses 224.0.0.10 as its multicast address and protocol number 88.
## Distance vector routing protocol  
### Cisco Systems now classifies EIGRP as a distance vector routing protocol, but it is normally said to be a hybrid routing protocol. While EIGRP is an advanced routing protocol that combines many of the features of both link-state and distance-vector routing protocols, EIGRP's DUAL algorithm contains many features which make it more of a distance vector routing protocol than a link-state routing protocol. Despite this, EIGRP contains many differences from most other distance-vector routing protocols, including: 
### the use of explicit hello packets to discover and maintain adjacencies between routers. 
### the use of a reliable protocol to transport routing updates. 
### the use of a feasibility condition to select a loop-free path. 
### the use of diffusing computations to involve the affected part of the network into computing a new shortest path.
## EIGRP composite and vector metrics  
### EIGRP associates six different vector metrics with each route and considers only four of the vector metrics in computing the Composite metric: 

Router1# show ip eigrp topology 10.0.0.1 255.255.255.255 
IP-EIGRP topology entry for 10.0.0.1/32 
  State is Passive, Query origin flag is 1, 1 Successor(s), FD is 40640000 
  Routing Descriptor Blocks: 
  10.0.0.1 (Serial0/0/0), from 10.0.0.1, Send flag is 0x0 
      Composite metric is (40640000/128256), Route is Internal 
      Vector metric: 
        Minimum bandwidth is 64 Kbit 
        Total delay is 25000 microseconds 
        Reliability is 255/255 
        Load is 197/255 
        Minimum MTU is 576 
        Hop count is 2 

### Bandwidth 
### Minimum Bandwidth (in kilobits per second) along the path from router to destination network.Load 
### Number in range 1 to 255; 255 being saturatedTotal Delay 
### Delay, in 10s of microseconds, along the path from router to destination networkReliability 
### Number in range 1 to 255; 255 being the most reliableMTU 
### Minimum path Maximum Transmission Unit (MTU) (never used in the metric calculation)Hop Count 
### Number of routers a packet passes through when routing to a remote network, used to limit the EIGRP AS. EIGRP maintains a hop count for every route, however, the hop count is not used in metric calculation. It is only verified against a predefined maximum on an EIGRP router (by default it is set to 100 and can be changed to any value between 1 and 255). Routes having a hop count higher than the maximum will be advertised as unreachable by an EIGRP router.
## Routing metric  
### The composite routing metric calculation uses five parameters, so-called K values, K1 through K5. These act as multipliers or modifiers in the composite metric calculation. K1 is not equal to Bandwidth, etc. 
### By default, only total delay and minimum bandwidth are considered when EIGRP is started on a router, but an administrator can enable or disable all the K values as needed to consider the other Vector metrics. 
### For the purposes of comparing routes, these are combined together in a weighted formula to produce a single overall metric: 

  
    
      
        
          
           [ 
          
        
        
          
           ( 
          
        
        
         K 
          
           1 
          
        
       \u22c5 
        
          
           Bandwidth 
          
          
           E 
          
        
       + 
        
          
            
              
               K 
                
                 2 
                
              
             \u22c5 
              
                
                 Bandwidth 
                
                
                 E 
                
              
            
            
             256 
             \u2212 
              
               Load 
              
            
          
        
       + 
        
         K 
          
           3 
          
        
       \u22c5 
        
          
           Delay 
          
          
           E 
          
        
        
          
           ) 
          
        
       \u22c5 
        
          
            
             K 
              
               5 
              
            
            
              
               K 
                
                 4 
                
              
             + 
              
               Reliability 
              
            
          
        
        
          
           ] 
          
        
       \u22c5 
       256 
      
    
   {\\displaystyle {\\bigg [}{\\bigg (}K_{1}\\cdot {\\text{Bandwidth}}_{E}+{\\frac {K_{2}\\cdot {\\text{Bandwidth}}_{E}}{256-{\\text{Load}}}}+K_{3}\\cdot {\\text{Delay}}_{E}{\\bigg )}\\cdot {\\frac {K_{5}}{K_{4}+{\\text{Reliability}}}}{\\bigg ]}\\cdot 256} 
 where the various constants ( 
  
    
      
        
         K 
          
           1 
          
        
      
    
   {\\displaystyle K_{1}} 
  through  
  
    
      
        
         K 
          
           5 
          
        
      
    
   {\\displaystyle K_{5}} 
 ) can be set by the user to produce varying behaviors. An important and unintuitive fact is that if  
  
    
      
        
         K 
          
           5 
          
        
      
    
   {\\displaystyle K_{5}} 
  is set to zero, the term  
  
    
      
        
          
            
              
               K 
                
                 5 
                
              
              
                
                 K 
                  
                   4 
                  
                
               + 
                
                 Reliability 
                
              
            
          
        
      
    
   {\\displaystyle {\\tfrac {K_{5}}{K_{4}+{\\text{Reliability}}}}} 
  is not used (i.e. taken as 1). 
### The default is for  
  
    
      
        
         K 
          
           1 
          
        
      
    
   {\\displaystyle K_{1}} 
  and  
  
    
      
        
         K 
          
           3 
          
        
      
    
   {\\displaystyle K_{3}} 
  to be set to 1, and the rest to zero, effectively reducing the above formula to  
  
    
      
       ( 
        
          
           Bandwidth 
          
          
           E 
          
        
       + 
        
          
           Delay 
          
          
           E 
          
        
       ) 
       \u22c5 
       256 
      
    
   {\\displaystyle ({\\text{Bandwidth}}_{E}+{\\text{Delay}}_{E})\\cdot 256} 
 . 
### Obviously, these constants must be set to the same value on all routers in an EIGRP system, or permanent routing loops may result. Cisco routers running EIGRP will not form an EIGRP adjacency and will complain about K-values mismatch until these values are identical on these routers. 
### EIGRP scales the interface Bandwidth and Delay configuration values with following calculations: 

  
    
      
        
          
           Bandwidth 
          
          
           E 
          
        
      
    
   {\\displaystyle {\\text{Bandwidth}}_{E}} 
   107 / Value of the bandwidth interface command 

  
    
      
        
          
           Delay 
          
          
           E 
          
        
      
    
   {\\displaystyle {\\text{Delay}}_{E}} 
   Value of the delay interface commandOn Cisco routers, the interface bandwidth is a configurable static parameter expressed in kilobits per second (setting this only affects metric calculation and not actual line bandwidth). Dividing a value of 107 kbit/s (i.e. 10 Gbit/s) by the interface bandwidth statement value yields a result that is used in the weighted formula. The interface delay is a configurable static parameter expressed in tens of microseconds. EIGRP takes this value directly without scaling into the weighted formula. However, various show commands display the interface delay in microseconds. Therefore, if given a delay value in microseconds, it must first be divided by 10 before using it in the weighted formula. 
### IGRP uses the same basic formula for computing the overall metric, the only difference is that in IGRP, the formula does not contain the scaling factor of 256. In fact, this scaling factor was introduced as a simple means to facilitate backward compatility between EIGRP and IGRP: In IGRP, the overall metric is a 24-bit value while EIGRP uses a 32-bit value to express this metric. By multiplying a 24-bit value with the factor of 256 (effectively bit-shifting it 8 bits to the left), the value is extended into 32 bits, and vice versa. This way, redistributing information between EIGRP and IGRP involves simply dividing or multiplying the metric value by a factor of 256, which is done automatically.
## Feasible successor  
### A feasible successor for a particular destination is a next hop router that is guaranteed not to be a part of a routing loop. This condition is verified by testing the feasibility condition. 
### Thus, every successor is also a feasible successor. However, in most references about EIGRP the term feasible successor is used to denote only those routes which provide a loop-free path but which are not successors (i.e. they do not provide the least distance). From this point of view, for a reachable destination, there is always at least one successor, however, there might not be any feasible successors. 
### A feasible successor provides a working route to the same destination, although with a higher distance. At any time, a router can send a packet to a destination marked \"Passive\" through any of its successors or feasible successors without alerting them in the first place, and this packet will be delivered properly. Feasible successors are also recorded in the topology table. 
### The feasible successor effectively provides a backup route in the case that existing successors become unavailable. Also, when performing unequal-cost load-balancing (balancing the network traffic in inverse proportion to the cost of the routes), the feasible successors are used as next hops in the routing table for the load-balanced destination. 
### By default, the total count of successors and feasible successors for a destination stored in the routing table is limited to four. This limit can be changed in the range from 1 to 6. In more recent versions of Cisco IOS (e.g. 12.4), this range is between 1 and 16.
## Active and passive state  
### A destination in the topology table can be marked either as passive or active. A passive state is a state when the router has identified the successor(s) for the destination. The destination changes to active state when the current successor no longer satisfies the feasibility condition and there are no feasible successors identified for that destination (i.e. no backup routes are available). The destination changes back from active to passive when the router received replies to all queries it has sent to its neighbors. Notice that if a successor stops satisfying the feasibility condition but there is at least one feasible successor available, the router will promote a feasible successor with the lowest total distance (the distance as reported by the feasible successor plus the cost of the link to this neighbor) to a new successor and the destination will remain in the passive state.
## Feasibility condition  
### The feasibility condition is a sufficient condition for loop freedom in EIGRP-routed network. It is used to select the successors and feasible successors that are guaranteed to be on a loop-free route to a destination. Its simplified formulation is strikingly simple: 

### If, for a destination, a neighbor router advertises a distance that is strictly lower than our feasible distance, then this neighbor lies on a loop-free route to this destination.or in other words, 

### If, for a destination, a neighbor router tells us that it is closer to the destination than we have ever been, then this neighbor lies on a loop-free route to this destination.It is important to realize that this condition is a sufficient, not a necessary, condition. That means that neighbors which satisfy this condition are guaranteed to be on a loop-free path to some destination, however, there may be also other neighbors on a loop-free path which do not satisfy this condition. However, such neighbors do not provide the shortest path to a destination, therefore, not using them does not present any significant impairment of the network functionality. These neighbors will be re-evaluated for possible usage if the router transitions to Active state for that destination.
## Unequal Path Cost Load Balancing  
### EIGRP features load balancing on paths with different costs. A multiplier, called variance, is used to determine which paths to include into load balancing. The variance is set to 1 by default, which means load balancing on equal cost paths. The maximum variance is 128. The minimum metric of a route is multiplied by the variance value. Each path with a metric that is smaller than the result is used in load balancing.With the functionality of the Unequal Path Cost Load Balancing on EIGRP, OSPF protocol is unable to design the network by Unequal Path Cost Load Balancing. Regarding the Unequal Path Cost Load Balancing function on industry usage, the network design can be flexible with the traffic management.
## EIGRP and compatibility to other vendors  
### Cisco released details of the proprietary EIGRP routing protocol in an RFC in an effort to assist companies whose networks operate in a multi-vendor environment. The protocol is described in RFC 7868. EIGRP was developed 20 years ago, yet it is still one of the primary Cisco routing protocols due to its purported usability and scalability in comparison to other protocols.Cisco has stated that EIGRP is an open standard but they leave out several core details in the RFC definition which makes interoperability hard to setup between different vendors' routers when the protocol is used.
## References  

### Cisco Systems (2005-09-09), Enhanced Interior Gateway Routing Protocol, Document ID 16406, retrieved 2008-04-27. 
### Cisco Systems (n.d.), Internetworking Technology Handbook: Enhanced Interior Gateway Routing Protocol (EIGRP), retrieved 2008-04-27. 
### Cisco Systems (2005-08-10), Introduction to EIGRP, Document ID 13669, retrieved 2008-04-27. 
### Lammle, Todd (2007), CCNA Cisco Certified Network Associate Study Guide (Sixth ed.), Indianapolis, Indiana: Wiley Publishing, ISBN 978-0-470-11008-9. 
### Cisco Systems (2013-02-18), EIGRP Information Draft, rfc number not yet assigned, retrieved 2013-02-18.
## External links  
### \"Introduction to EIGRP\". Cisco Systems. 2005-08-10."
## References
### [Reference](http://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/enhanced-interior-gateway-routing-protocol-eigrp/whitepaper_C11-720525.html) - http://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/enhanced-interior-gateway-routing-protocol-eigrp/whitepaper_C11-720525.html
### [Reference](http://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/13677-19.html) - http://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/13677-19.html
### [Reference](http://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/13669-1.html) - http://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/13669-1.html
### [Reference](http://www.cisco.com/en/US/docs/internetworking/technology/handbook/Enhanced_IGRP.html) - http://www.cisco.com/en/US/docs/internetworking/technology/handbook/Enhanced_IGRP.html
### [Reference](http://www.cisco.com/en/US/prod/collateral/iosswrel/ps6537/ps6554/ps6599/ps6630/qa_C67-726299.html) - http://www.cisco.com/en/US/prod/collateral/iosswrel/ps6537/ps6554/ps6599/ps6630/qa_C67-726299.html
### [Reference](http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a0080093f07.shtml) - http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a0080093f07.shtml
### [Reference](http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a0080094195.shtml) - http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a0080094195.shtml
### [Reference](http://www.cisco.com/en/US/tech/tk365/technologies_white_paper09186a0080094cb7.shtml) - http://www.cisco.com/en/US/tech/tk365/technologies_white_paper09186a0080094cb7.shtml
### [Reference](http://www.globalknowledge.com/training/whitepaperdetail.asp?pageid=502&wpid=663) - http://www.globalknowledge.com/training/whitepaperdetail.asp?pageid=502&wpid=663
### [Reference](http://www.informit.com/library/content.aspx?b=CCIE_Practical_Studies_I&seqNum=116) - http://www.informit.com/library/content.aspx?b=CCIE_Practical_Studies_I&seqNum=116
### [Reference](http://packetlife.net/blog/2009/jan/17/rtp-eigrp/) - http://packetlife.net/blog/2009/jan/17/rtp-eigrp/
### [Reference](http://www.ietf.org/staging/draft-savage-eigrp-00.txt) - http://www.ietf.org/staging/draft-savage-eigrp-00.txt
### [Reference](http://www.ijcsmr.org/vol2issue4/paper346.pdf) - http://www.ijcsmr.org/vol2issue4/paper346.pdf
### [Reference](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html) - https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html
### [Reference](https://www.gns3network.com/eigrp-messages-types-and-neighborship-parameters/) - https://www.gns3network.com/eigrp-messages-types-and-neighborship-parameters/
### [Reference](https://books.google.com/books?id=fzBOZDGBDDgC&lpg=PA214&ots=eyWtKIr1dc&dq=reliable%20transport%20protocol%20eigrp&pg=PA214#v=onepage&q=reliable%20transport%20protocol%20eigrp&f=true) - https://books.google.com/books?id=fzBOZDGBDDgC&lpg=PA214&ots=eyWtKIr1dc&dq=reliable%20transport%20protocol%20eigrp&pg=PA214#v=onepage&q=reliable%20transport%20protocol%20eigrp&f=true
### [Reference](https://id.loc.gov/authorities/subjects/sh00001881) - https://id.loc.gov/authorities/subjects/sh00001881
### [Reference](https://10-0-0-0-1.org/10-0-0-1/) - https://10-0-0-0-1.org/10-0-0-1/
### [Reference](https://web.archive.org/web/20131015204027/http://www.globalknowledge.com/training/whitepaperdetail.asp?pageid=502&wpid=663) - https://web.archive.org/web/20131015204027/http://www.globalknowledge.com/training/whitepaperdetail.asp?pageid=502&wpid=663
### [Reference](https://web.archive.org/web/20131109014953/http://www.ijcsmr.org/vol2issue4/paper346.pdf) - https://web.archive.org/web/20131109014953/http://www.ijcsmr.org/vol2issue4/paper346.pdf
### [Reference](https://web.archive.org/web/20140426202321/http://www.informit.com/library/content.aspx?b=CCIE_Practical_Studies_I&seqNum=116) - https://web.archive.org/web/20140426202321/http://www.informit.com/library/content.aspx?b=CCIE_Practical_Studies_I&seqNum=116
### [Reference](https://web.archive.org/web/20180303041447/https://10-0-0-0-1.org/) - https://web.archive.org/web/20180303041447/https://10-0-0-0-1.org/
### [Reference](https://datatracker.ietf.org/doc/html/rfc7868) - https://datatracker.ietf.org/doc/html/rfc7868
### [Reference](https://www.wikidata.org/wiki/Q1091139#identifiers) - https://www.wikidata.org/wiki/Q1091139#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/8/8a/20190821112659%21OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/archive/8/8a/20190821112659%21OOjs_UI_icon_edit-ltr-progressive.svg