# Multipath routing
## [URL](https://en.wikipedia.org/wiki/Multipath_routing) - https://en.wikipedia.org/wiki/Multipath_routing
## Catagories
### All articles lacking in-text citations
### All articles needing additional references
### Articles lacking in-text citations from June 2012
### Articles needing additional references from May 2021
### Articles with short description
### Routing algorithms
### Short description matches Wikidata
### "Multipath routing is a routing technique simultaneously using multiple alternative paths through a network. This can yield a variety of benefits such as fault tolerance, increased bandwidth, and improved security.
## Mobile networks  
### To improve performance or fault tolerance, concurrent multipath routing (CMR) is often taken to mean simultaneous management and utilization of multiple available paths for the transmission of streams of data. The streams may be emanating from a single application or multiple applications. A stream is assigned a separate path, as uniquely possible given the number of paths available. If there are more streams than available paths, some streams will share paths. CMR provides better utilization of bandwidth by creating multiple transmission queues. It provides a degree of fault tolerance in that should a path fail, only the traffic assigned to that path is affected. There is also, ideally, an alternative path immediately available upon which to continue or restart the interrupted stream. 
### CMR provides better transmission performance and fault tolerance by providing simultaneous, parallel transport over multiple carriers with the ability to reassign an interrupted stream, and by load balancing over available assets. However, under CMR, some applications may be slower in offering traffic to the transport layer, thus starving paths assigned to them, causing under-utilization. Also, moving to the alternative path will incur a potentially disruptive period during which the connection is re-established.
## True CMR  
### A more powerful form of CMR (true CMR) goes beyond merely presenting paths to applications to which they can bind. True CMR aggregates all available paths into a single, virtual path. 
### Applications send their packets to this virtual path, which is de-multiplexed at the network Layer.  The packets are distributed to the physical paths via some algorithm e.g. round-robin or weighted fair queuing. Should a link fail, succeeding packets are not directed to that path and the stream continues uninterrupted to the application through the remaining path(s). This method provides significant performance benefits over the application level CMR: 

### By continually offering packets to all paths, the paths are more fully utilized. 
### No matter how many paths fail, so long as at least one path is still available, all sessions remain connected and no streams need to be restarted and no re-connection penalty is incurred.
## Capillary routing  
### In networking and in graph theory, capillary routing, for a given network, is a multi-path solution between a pair of source and destination nodes. Unlike shortest-path routing or max-flow routing,  for any given network topology - only one capillary routing solution exists. 
### Capillary routing can be constructed by an iterative linear programming process, transforming a single-path flow into a capillary route. 

### First minimize the maximal value of the load on all of the network routing node links 
### Do that by minimizing a load upper bound value that is applied to all links. 
### The full mass of the flow will be split equally across the possible parallel routes. 
### Find the bottleneck links of the first layer (see below), then set their loading amount at the found minimum. 
### Additionally, minimize the maximal load of all remaining links, but now without the bottleneck links of the first layer. 
### This second iteration further refines the path diversity. 
### Next, we determine the bottleneck links of the 2nd network layer. 
### Again, minimize the maximal load of all remaining links, but now without the bottlenecks of the 2nd network layer as well. 
### Repeat this algorithm until the entire communication footprint is enclosed in the bottlenecks of the constructed layers.At each functional layer of the network protocol, after minimizing the maximal load of links, the bottlenecks of the layer are discovered in a bottleneck detection process. 

### At each iteration of the detection loop, we minimize the sending of traffic over all links having maximal loading, and being suspected as bottlenecks. 
### Links unable to maintain their traffic load at the maximum are eventually removed from the candidate path list. 
### The bottleneck detection process stops when there are no more links to remove, because this best path is now known.
## See also  
### Equal-cost multi-path routing 
### IEEE 802.1aq 
### Multipath TCP 
### TRILL (TRansparent Interconnection of Lots of Links)
## References  

### To improve network security:
## External links  
### Dijiang Huang. \"Multipath routing bibliography\". Archived from the original on 2008-10-13."
## Links
### Bandwidth (computing)
### Computer networking
### Equal-cost multi-path routing
### Fault tolerance
### Graph theory
### IEEE 802.1aq
### Linear programming
### Max-flow routing
### Multipath TCP
### Network security
### Routing
### Shortest-path routing
### TRILL (computing)
### Upper bound
## References
### [Reference](http://mediatum.ub.tum.de/doc/635601/635601.pdf) - http://mediatum.ub.tum.de/doc/635601/635601.pdf
### [Reference](http://snac.eas.asu.edu/snac/multipath/multipath.html) - http://snac.eas.asu.edu/snac/multipath/multipath.html
### [Reference](https://web.archive.org/web/20081013092512/http://snac.eas.asu.edu/snac/multipath/multipath.html) - https://web.archive.org/web/20081013092512/http://snac.eas.asu.edu/snac/multipath/multipath.html
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/a4/Text_document_with_red_question_mark.svg) - https://upload.wikimedia.org/wikipedia/commons/a/a4/Text_document_with_red_question_mark.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg