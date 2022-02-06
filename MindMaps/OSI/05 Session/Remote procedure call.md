# Remote procedure call
## [URL](https://en.wikipedia.org/wiki/Remote_procedure_call) - https://en.wikipedia.org/wiki/Remote_procedure_call
## Catagories
### All articles needing additional references
### Articles needing additional references from December 2013
### Articles with short description
### Distributed computing
### Inter-process communication
### Middleware
### Remote procedure call
### Short description matches Wikidata
### Webarchive template wayback links
### "In distributed computing, a remote procedure call (RPC) is when a computer program causes a procedure (subroutine) to execute in a different address space (commonly on another computer on a shared network), which is coded as if it were a normal (local) procedure call, without the programmer explicitly coding the details for the remote interaction. That is, the programmer writes essentially the same code whether the subroutine is local to the executing program, or remote. This is a form of client\u2013server interaction (caller is client, executor is server), typically implemented via a request\u2013response message-passing system. In the object-oriented programming paradigm, RPCs are represented by remote method invocation (RMI). The RPC model implies a level of location transparency, namely that calling procedures are largely the same whether they are local or remote, but usually they are not identical, so local calls can be distinguished from remote calls. Remote calls are usually orders of magnitude slower and less reliable than local calls, so distinguishing them is important. 
### RPCs are a form of inter-process communication (IPC), in that different processes have different address spaces: if on the same host machine, they have distinct virtual address spaces, even though the physical address space is the same; while if they are on different hosts, the physical address space is different. Many different (often incompatible) technologies have been used to implement the concept.
## History and origins  
### Request\u2013response protocols date to early distributed computing in the late 1960s, theoretical proposals of remote procedure calls as the model of network operations date to the 1970s, and practical implementations date to the early 1980s. Bruce Jay Nelson is generally credited with coining the term \"remote procedure call\" in 1981.Remote procedure calls used in modern operating systems trace their roots back to the RC 4000 multiprogramming system, which used a request-response communication protocol for process synchronization. The idea of treating network operations as remote procedure calls goes back at least to the 1970s in early ARPANET documents. In 1978, Per Brinch Hansen proposed Distributed Processes, a language for distributed computing based on \"external requests\" consisting of procedure calls between processes.One of the earliest practical implementations was in 1982 by Brian Randell and colleagues for their Newcastle Connection between UNIX machines.  This was soon followed by \"Lupine\" by Andrew Birrell and Bruce Nelson in the Cedar environment at Xerox PARC. Lupine automatically generated stubs, providing type-safe bindings, and used an efficient protocol for communication. One of the first business uses of RPC was by Xerox under the name \"Courier\" in 1981. The first popular implementation of RPC on Unix was Sun's RPC (now called ONC RPC), used as the basis for Network File System (NFS). 
### In the 1990s, with the popularity of object-oriented programming, an alternative model of remote method invocation (RMI) was widely implemented, such as in Common Object Request Broker Architecture (CORBA, 1991) and Java remote method invocation. RMIs in turn fell in popularity with the rise of the internet, particularly in the 2000s.
## Message passing  
### RPC is a request\u2013response protocol. An RPC is initiated by the client, which sends a request message to a known remote server to execute a specified procedure with supplied parameters. The remote server sends a response to the client, and the application continues its process. While the server is processing the call, the client is blocked (it waits until the server has finished processing before resuming execution), unless the client sends an asynchronous request to the server, such as an XMLHttpRequest. There are many variations and subtleties in various implementations, resulting in a variety of different (incompatible) RPC protocols. 
### An important difference between remote procedure calls and local calls is that remote calls can fail because of unpredictable network problems. Also, callers generally must deal with such failures without knowing whether the remote procedure was actually invoked. Idempotent procedures (those that have no additional effects if called more than once) are easily handled, but enough difficulties remain that code to call remote procedures is often confined to carefully written low-level subsystems.
## Sequence of events  
### The client calls the client stub. The call is a local procedure call, with parameters pushed on to the stack in the normal way. 
### The client stub packs the parameters into a message and makes a system call to send the message. Packing the parameters is called marshalling. 
### The client's local operating system sends the message from the client machine to the server machine. 
### The local operating system on the server machine passes the incoming packets to the server stub. 
### The server stub unpacks the parameters from the message. Unpacking the parameters is called unmarshalling. 
### Finally, the server stub calls the server procedure. The reply traces the same steps in the reverse direction.
## Standard contact mechanisms  
### To let different clients access servers, a number of standardized RPC systems have been created. Most of these use an interface description language (IDL) to let various platforms call the RPC. The IDL files can then be used to generate code to interface between the client and servers.
## Analogues  
### Notable RPC implementations and analogues include:
## Language-specific  
### Java's Java Remote Method Invocation (Java RMI) API provides similar functionality to standard Unix RPC methods. 
### Go provides package rpc for implementing RPC, with support for asynchronous calls. 
### Modula-3's network objects, which were the basis for Java's RMI 
### RPyC implements RPC mechanisms in Python, with support for asynchronous calls. 
### Distributed Ruby (DRb) allows Ruby programs to communicate with each other on the same machine or over a network. DRb uses remote method invocation (RMI) to pass commands and data between processes. 
### Erlang is process oriented and natively supports distribution and RPCs via message passing between nodes and local processes alike. 
### Elixir builds on top of the Erlang VM and allows process communication (Elixir/Erlang processes, not OS processes) of the same network out-of-the-box via Agents and message passing.
## Application-specific  
### Action Message Format (AMF) allows Adobe Flex applications to communicate with back-ends or other applications that support AMF. 
### Remote Function Call is the standard SAP interface for communication between SAP systems. RFC calls a function to be executed in a remote system.
## General  
### NFS (Network File System) is one of the most prominent users of RPC 
### Open Network Computing Remote Procedure Call, by Sun Microsystems 
### D-Bus open source IPC program provides similar function to CORBA. 
### SORCER provides the API and exertion-oriented language (EOL) for a federated method invocation 
### XML-RPC is an RPC protocol that uses XML to encode its calls and HTTP as a transport mechanism. 
### JSON-RPC is an RPC protocol that uses JSON-encoded messages 
### JSON-WSP is an RPC protocol that uses JSON-encoded messages 
### SOAP is a successor of XML-RPC and also uses XML to encode its HTTP-based calls. 
### ZeroC's Internet Communications Engine (Ice) distributed computing platform. 
### Etch framework for building network services. 
### Apache Thrift protocol and framework. 
### CORBA provides remote procedure invocation through an intermediate layer called the object request broker. 
### Libevent provides a framework for creating RPC servers and clients. 
### Windows Communication Foundation is an application programming interface in the .NET framework for building connected, service-oriented applications. 
### Microsoft .NET Remoting offers RPC facilities for distributed systems implemented on the Windows platform. It has been superseded by WCF. 
### The Microsoft DCOM uses MSRPC which is based on DCE/RPC 
### The Open Software Foundation DCE/RPC Distributed Computing Environment (also implemented by Microsoft). 
### Google Protocol Buffers (protobufs) package includes an interface definition language used for its RPC protocols open sourced in 2015 as gRPC. 
### WAMP combines RPC and Publish-Subscribe into a single, transport-agnostic protocol. 
### Google Web Toolkit uses an asynchronous RPC to communicate to the server service. 
### Apache Avro provides RPC where client and server exchange schemas in the connection handshake and code generation is not required. 
### Embedded RPC is lightweight RPC implementation developed by NXP, targeting primary CortexM cores 
### KF Trusted Execution Environment uses proxy and objects marshaling to communicate objects across sandboxes 
### msgpack-rpc is a lightweight RPC implementation using MessagePack to serialize data. It is used in the text editor Neovim.
## See also  
### 9P 
### Microsoft RPC 
### Local Procedure Call 
### HTTP 
### ODBC 
### Remote evaluation 
### External Data Representation (serialization format used by e.g. NFS) 
### Network Data Representation (serialization format used by e.g. Microsoft RPC) 
### Resource-oriented architecture 
### Distributed object middleware 
### Fragmented object 
### gRPC
## References 
## External links  
### RFC 1057 - Specifies version 1 of ONC RPC 
### RFC 5531 - Specifies version 2 of ONC RPC 
### Remote Procedure Calls (RPC) \u2014 A tutorial on ONC RPC by Dr Dave Marshall of Cardiff University 
### Introduction to RPC Programming \u2014 A developer's introduction to RPC and XDR, from SGI IRIX documentation."
## References
### [Reference](http://www.computerworld.com.au/index.php/id;1422447371;pp;3;fp;4194304;fpid;1) - http://www.computerworld.com.au/index.php/id;1422447371;pp;3;fp;4194304;fpid;1
### [Reference](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.107.3108) - http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.107.3108
### [Reference](http://www.grpc.io/) - http://www.grpc.io/
### [Reference](http://brinch-hansen.net/papers/1969c.pdf) - http://brinch-hansen.net/papers/1969c.pdf
### [Reference](http://brinch-hansen.net/papers/1978a.pdf) - http://brinch-hansen.net/papers/1978a.pdf
### [Reference](http://www.e-s-r.net/specifications/index.html) - http://www.e-s-r.net/specifications/index.html
### [Reference](http://awards.acm.org/citation.cfm?id=5125494&srt=all&aw=149&ao=SOFTWSYS&yr=1994) - http://awards.acm.org/citation.cfm?id=5125494&srt=all&aw=149&ao=SOFTWSYS&yr=1994
### [Reference](http://www.computer.org/web/awards/pioneer-per-hansen) - http://www.computer.org/web/awards/pioneer-per-hansen
### [Reference](http://doi.org/10.1002%2Fspe.4380121206) - http://doi.org/10.1002%2Fspe.4380121206
### [Reference](http://doi.org/10.1145%2F2080.357392) - http://doi.org/10.1145%2F2080.357392
### [Reference](http://doi.org/10.1145%2F359642.359651) - http://doi.org/10.1145%2F359642.359651
### [Reference](http://tools.ietf.org/html/rfc707) - http://tools.ietf.org/html/rfc707
### [Reference](http://www.monkey.org/~provos/libevent/doxygen-1.4.10/) - http://www.monkey.org/~provos/libevent/doxygen-1.4.10/
### [Reference](http://www.sigops.org/award-hof.html) - http://www.sigops.org/award-hof.html
### [Reference](http://www.cs.cf.ac.uk/Dave/C/node33.html) - http://www.cs.cf.ac.uk/Dave/C/node33.html
### [Reference](http://www.cs.ncl.ac.uk/publications/articles/papers/399.pdf) - http://www.cs.ncl.ac.uk/publications/articles/papers/399.pdf
### [Reference](https://github.com/EmbeddedRPC/erpc) - https://github.com/EmbeddedRPC/erpc
### [Reference](https://github.com/msgpack-rpc/msgpack-rpc) - https://github.com/msgpack-rpc/msgpack-rpc
### [Reference](https://code.google.com/p/protobuf/) - https://code.google.com/p/protobuf/
### [Reference](https://code.google.com/webtoolkit/) - https://code.google.com/webtoolkit/
### [Reference](https://www.cs.cmu.edu/~dga/15-712/F07/papers/birrell842.pdf) - https://www.cs.cmu.edu/~dga/15-712/F07/papers/birrell842.pdf
### [Reference](https://web.archive.org/web/20030404113118/http://techpubs.sgi.com/library/tpl/cgi-bin/getdoc.cgi?coll=0650&db=bks&srch=&fname=/SGI_Developer/IRIX_NetPG/sgi_html/ch04.html) - https://web.archive.org/web/20030404113118/http://techpubs.sgi.com/library/tpl/cgi-bin/getdoc.cgi?coll=0650&db=bks&srch=&fname=/SGI_Developer/IRIX_NetPG/sgi_html/ch04.html
### [Reference](https://web.archive.org/web/20090105145818/http://www.computerworld.com.au/index.php/id;1422447371;pp;3;fp;4194304;fpid;1) - https://web.archive.org/web/20090105145818/http://www.computerworld.com.au/index.php/id;1422447371;pp;3;fp;4194304;fpid;1
### [Reference](https://web.archive.org/web/20120402204704/http://awards.acm.org/citation.cfm?id=5125494&srt=all&aw=149&ao=SOFTWSYS&yr=1994) - https://web.archive.org/web/20120402204704/http://awards.acm.org/citation.cfm?id=5125494&srt=all&aw=149&ao=SOFTWSYS&yr=1994
### [Reference](https://web.archive.org/web/20160816184205/http://www.cs.ncl.ac.uk/research/pubs/articles/papers/399.pdf) - https://web.archive.org/web/20160816184205/http://www.cs.ncl.ac.uk/research/pubs/articles/papers/399.pdf
### [Reference](https://golang.org/) - https://golang.org/
### [Reference](https://golang.org/pkg/net/rpc/) - https://golang.org/pkg/net/rpc/
### [Reference](https://datatracker.ietf.org/doc/html/rfc1057) - https://datatracker.ietf.org/doc/html/rfc1057
### [Reference](https://datatracker.ietf.org/doc/html/rfc5531) - https://datatracker.ietf.org/doc/html/rfc5531
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20210726203439%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20210726203439%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20201004174738%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20201004174738%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171208221057%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171208221057%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171207131032%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20171207131032%21Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/archive/9/99/20160612140736%21Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/archive/9/99/20160612140736%21Question_book-new.svg