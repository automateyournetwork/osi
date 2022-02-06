# Domain Name System
## [URL](https://en.wikipedia.org/wiki/Domain_Name_System) - https://en.wikipedia.org/wiki/Domain_Name_System
## Catagories
### All Wikipedia articles written in American English
### All articles needing additional references
### All articles with failed verification
### Application layer protocols
### Articles needing additional references from September 2014
### Articles with GND identifiers
### Articles with PLWABN identifiers
### Articles with failed verification from January 2022
### Articles with short description
### Computer-related introductions in 1983
### Domain Name System
### Internet Standards
### Short description is different from Wikidata
### Use American English from February 2019
### Webarchive template wayback links
### Wikipedia articles needing clarification from November 2017
### Wikipedia semi-protected pages
### "The Domain Name System (DNS) is the hierarchical and decentralized naming system used to identify computers, services, and other resources reachable through the Internet or other Internet Protocol (IP) networks. The resource records contained in the DNS associate domain names with other forms of information. These are most commonly used to map human-friendly domain names to the numerical IP addresses computers need to locate services and devices using the underlying network protocols, but have been extended over time to perform many other functions as well. The Domain Name System has been an essential component of the functionality of the Internet since 1985.
## Function  
### An often-used analogy to explain the Domain Name System is that it serves as the phone book for the Internet by translating human-friendly computer hostnames into IP addresses. For example, the domain name www.example.com translates to the addresses 93.184.216.34 (IPv4) and 2606:2800:220:1:248:1893:25c8:1946 (IPv6). The DNS can be quickly and transparently updated, allowing a service's location on the network to change without affecting the end users, who continue to use the same hostname. Users take advantage of this when they use meaningful Uniform Resource Locators (URLs) and e-mail addresses without having to know how the computer actually locates the services. 
### An important and ubiquitous function of the DNS is its central role in distributed Internet services such as cloud services and  content delivery networks. When a user accesses a distributed Internet service using a URL, the domain name of the URL is translated to the IP address of a server that is proximal to the user.  The key functionality of the DNS exploited here is that different users can simultaneously receive different translations for the same domain name, a key point of divergence from a traditional phone-book view of the DNS. This process of using the DNS to assign proximal servers to users is key to providing faster and more reliable responses on the Internet and is widely used by most major Internet services.The DNS reflects the structure of administrative responsibility in the Internet. Each subdomain is a zone of administrative autonomy delegated to a manager. For zones operated by a registry, administrative information is often complemented by the registry's RDAP and WHOIS services.  That data can be used to gain insight on, and track responsibility for, a given host on the Internet.
## History  
### Using a simpler, more memorable name in place of a host's numerical address dates back to the ARPANET era. The Stanford Research Institute (now SRI International) maintained a text file named HOSTS.TXT that mapped host names to the numerical addresses of computers on the ARPANET. Elizabeth Feinler developed and maintained the first ARPANET directory. Maintenance of numerical addresses, called the Assigned Numbers List, was handled by Jon Postel at the University of Southern California's Information Sciences Institute (ISI), whose team worked closely with SRI.Addresses were assigned manually. Computers, including their hostnames and addresses, were added to the primary file by contacting the SRI Network Information Center (NIC), directed by Feinler, telephone during business hours. Later, Feinler set up a WHOIS directory on a server in the NIC for  retrieval of information about resources, contacts, and entities. She and her team developed the concept of domains. Feinler suggested that domains should be based on the location of the physical address of the computer. Computers at educational institutions would have the domain edu, for example. She and her team managed the Host Naming Registry from 1972 to 1989.By the early 1980s, maintaining a single, centralized host table had become slow and unwieldy and the emerging network required an automated naming system to address technical and personnel issues.  Postel directed the task of forging a compromise between five competing proposals of solutions to Paul Mockapetris. Mockapetris instead created the Domain Name System in 1983.The Internet Engineering Task Force published the original specifications in RFC 882 and RFC 883 in November 1983.In 1984, four UC Berkeley students, Douglas Terry, Mark Painter, David Riggle, and Songnian Zhou, wrote the first Unix name server implementation for the Berkeley Internet Name Domain, commonly referred to as BIND. In 1985, Kevin Dunlap of DEC substantially revised the DNS implementation. Mike Karels, Phil Almquist, and Paul Vixie have maintained BIND since then. In the early 1990s, BIND was ported to the Windows NT platform. 
### In November 1987, RFC 1034 and RFC 1035 superseded the 1983 DNS specifications. Several additional Request for Comments have proposed extensions to the core DNS protocols.
## Structure 
## Domain name space  
### The domain name space consists of a tree data structure. Each node or leaf in the tree has a label and zero or more resource records (RR), which hold information associated with the domain name.  The domain name itself consists of the label, concatenated with the name of its parent node on the right, separated by a dot.The tree sub-divides into zones beginning at the root zone.  A DNS zone may consist of only one domain, or may consist of many domains and sub-domains, depending on the administrative choices of the zone manager.  DNS can also be partitioned according to class where the separate classes can be thought of as an array of parallel namespace trees. 

### Administrative responsibility for any zone may be divided by creating additional zones. Authority over the new zone is said to be delegated to a designated name server. The parent zone ceases to be authoritative for the new zone.
## Domain name syntax, internationalization  
### The definitive descriptions of the rules for forming domain names appear in RFC 1035, RFC 1123, RFC 2181, and RFC 5892.  A domain name consists of one or more parts, technically called labels, that are conventionally concatenated, and delimited by dots, such as example.com. 
### The right-most label conveys the top-level domain; for example, the domain name www.example.com belongs to the top-level domain com. 
### The hierarchy of domains descends from right to left; each label to the left specifies a subdivision, or subdomain of the domain to the right. For example, the label example specifies a subdomain of the com domain, and www is a subdomain of example.com. This tree of subdivisions may have up to 127 levels.A label may contain zero to 63 characters. The null label, of length zero, is reserved for the root zone. The full domain name may not exceed the length of 253 characters in its textual representation. In the internal binary representation of the DNS the maximum length requires 255 octets of storage, as it also stores the length of the name.Although no technical limitation exists to prevent domain name labels using any character which is representable by an octet, hostnames use a preferred format and character set. The characters allowed in labels are a subset of the ASCII character set, consisting of characters a through z, A through Z, digits 0 through 9, and hyphen. This rule is known as the LDH rule (letters, digits, hyphen). Domain names are interpreted in case-independent manner. Labels may not start or end with a hyphen. An additional rule requires that top-level domain names should not be all-numeric.The limited set of ASCII characters permitted in the DNS prevented the representation of names and words of many languages in their native alphabets or scripts. To make this possible, ICANN approved the Internationalizing Domain Names in Applications (IDNA) system, by which user applications, such as web browsers, map Unicode strings into the valid DNS character set using Punycode. In 2009 ICANN approved the installation of internationalized domain name country code top-level domains (ccTLDs). In addition, many registries of the existing top-level domain names (TLDs) have adopted the IDNA system, guided by RFC 5890, RFC 5891, RFC 5892, RFC 5893.
## Name servers  
### The Domain Name System is maintained by a distributed database system, which uses the client\u2013server model. The nodes of this database are the name servers. Each domain has at least one authoritative DNS server that publishes information about that domain and the name servers of any domains subordinate to it. The top of the hierarchy is served by the root name servers, the servers to query when looking up (resolving) a TLD.
## Authoritative name server  
### An authoritative name server is a name server that only gives answers to DNS queries from data that has been configured by an original source, for example, the domain administrator or by dynamic DNS methods, in contrast to answers obtained via a query to another name server that only maintains a cache of data. 
### An authoritative name server can either be a primary server or a secondary server. Historically the terms master/slave and primary/secondary were sometimes used interchangeably but the current practice is to use the latter form. A primary server is a server that stores the original copies of all zone records. A secondary server uses a special automatic updating mechanism in the DNS protocol in communication with its primary to maintain an identical copy of the primary records. 
### Every DNS zone must be assigned a set of authoritative name servers. This set of servers is stored in the parent domain zone with name server (NS) records. 
### An authoritative server indicates its status of supplying definitive answers, deemed authoritative, by setting a protocol flag, called the \"Authoritative Answer\" (AA) bit in its responses. This flag is usually reproduced prominently in the output of DNS administration query tools, such as dig, to indicate that the responding name server is an authority for the domain name in question.When a name server is designated as the authoritative server for a domain name for which it does not have authoritative data, it presents a type of error called a \"lame delegation\" or \"lame response\".
## Operation 
## Address resolution mechanism  
### Domain name resolvers determine the domain name servers responsible for the domain name in question by a sequence of queries starting with the right-most (top-level) domain label. 

### For proper operation of its domain name resolver, a network host is configured with an initial cache (hints) of the known addresses of the root name servers. The hints are updated periodically by an administrator by retrieving a dataset from a reliable source. 
### Assuming the resolver has no cached records to accelerate the process, the resolution process starts with a query to one of the root servers.  In typical operation, the root servers do not answer directly, but respond with a referral to more authoritative servers, e.g., a query for \"www.wikipedia.org\" is referred to the org servers.   The resolver now queries the servers referred to, and iteratively repeats this process until it receives an authoritative answer. The diagram illustrates this process for the host that is named by the fully qualified domain name \"www.wikipedia.org\". 
### This mechanism would place a large traffic burden on the root servers, if every resolution on the Internet required starting at the root. In practice caching is used in DNS servers to off-load the root servers, and as a result, root name servers actually are involved in only a relatively small fraction of all requests.
## Recursive and caching name server  
### In theory, authoritative name servers are sufficient for the operation of the Internet. However, with only authoritative name servers operating, every DNS query must start with recursive queries at the root zone of the Domain Name System and each user system would have to implement resolver software capable of recursive operation. 
### To improve efficiency, reduce DNS traffic across the Internet, and increase performance in end-user applications, the Domain Name System supports DNS cache servers which store DNS query results for a period of time determined in the configuration (time-to-live) of the domain name record in question. 
### Typically, such caching DNS servers also implement the recursive algorithm necessary to resolve a given name starting with the DNS root through to the authoritative name servers of the queried domain. With this function implemented in the name server, user applications gain efficiency in design and operation. 
### The combination of DNS caching and recursive functions in a name server is not mandatory; the functions can be implemented independently in servers for special purposes. 
### Internet service providers  typically provide recursive and caching name servers for their customers. In addition, many home networking routers implement DNS caches and recursion to improve efficiency in the local network.
## DNS resolvers  
### The client side of the DNS is called a DNS resolver. A resolver is responsible for initiating and sequencing the queries that ultimately lead to a full resolution (translation) of the resource sought, e.g., translation of a domain name into an IP address. DNS resolvers are classified by a variety of query methods, such as recursive, non-recursive, and iterative. A resolution process may use a combination of these methods.In a non-recursive query, a DNS resolver queries a DNS server that provides a record either for which the server is authoritative, or it provides a partial result without querying other servers. In case of a caching DNS resolver, the non-recursive query of its local DNS cache delivers a result and reduces the load on upstream DNS servers by caching DNS resource records for a period of time after an initial response from upstream DNS servers. 
### In a recursive query, a DNS resolver queries a single DNS server, which may in turn query other DNS servers on behalf of the requester. For example, a simple stub resolver running on a home router typically makes a recursive query to the DNS server run by the user's ISP. A recursive query is one for which the DNS server answers the query completely by querying other name servers as needed. In typical operation, a client issues a recursive query to a caching recursive DNS server, which subsequently issues non-recursive queries to determine the answer and send a single answer back to the client. The resolver, or another DNS server acting recursively on behalf of the resolver, negotiates use of recursive service using bits in the query headers. DNS servers are not required to support recursive queries. 
### The iterative query procedure is a process in which a DNS resolver queries a chain of one or more DNS servers. Each server refers the client to the next server in the chain, until the current server can fully resolve the request. For example, a possible resolution of www.example.com would query a global root server, then a \"com\" server, and finally an \"example.com\" server.
## Circular dependencies and glue records  
### Name servers in delegations are identified by name, rather than by IP address. This means that a resolving name server must issue another DNS request to find out the IP address of the server to which it has been referred. If the name given in the delegation is a subdomain of the domain for which the delegation is being provided, there is a circular dependency. 
### In this case, the name server providing the delegation must also provide one or more IP addresses for the authoritative name server mentioned in the delegation. This information is called glue.   The delegating name server provides this glue in the form of records in the additional section of the DNS response, and provides the delegation in the authority section of the response. A glue record is a combination of the name server and IP address. 
### For example, if the authoritative name server for example.org is ns1.example.org, a computer trying to resolve www.example.org first resolves ns1.example.org. As ns1 is contained in example.org, this requires resolving example.org first, which presents a circular dependency. To break the dependency, the name server for the top level domain org includes glue along with the delegation for example.org.  The glue records are address records that provide IP addresses for ns1.example.org. The resolver uses one or more of these IP addresses to query one of the domain's authoritative servers, which allows it to complete the DNS query.
## Record caching  
### A standard practice in implementing name resolution in applications is to reduce the load on the Domain Name System servers by caching results locally, or in intermediate resolver hosts. Results obtained from a DNS request are always associated with the time to live (TTL), an expiration time after which the results must be discarded or refreshed. The TTL is set by the administrator of the authoritative DNS server. The period of validity may vary from a few seconds to days or even weeks. 
### As a result of this distributed caching architecture, changes to DNS records do not propagate throughout the network immediately, but require all caches to expire and to be refreshed after the TTL. RFC 1912 conveys basic rules for determining appropriate TTL values. 
### Some resolvers may override TTL values, as the protocol supports caching for up to sixty-eight years or no caching at all. Negative caching, i.e. the caching of the fact of non-existence of a record, is determined by name servers authoritative for a zone which must include the Start of Authority (SOA) record when reporting no data of the requested type exists. The value of the minimum field of the SOA record and the TTL of the SOA itself is used to establish the TTL for the negative answer.
## Reverse lookup  
### A reverse DNS lookup is a query of the DNS for domain names when the IP address is known. Multiple domain names may be associated with an IP address. The DNS stores IP addresses in the form of domain names as specially formatted names in pointer (PTR) records within the infrastructure top-level domain arpa. For IPv4, the domain is in-addr.arpa.  For IPv6, the reverse lookup domain is ip6.arpa. The IP address is represented as a name in reverse-ordered octet representation for IPv4, and reverse-ordered nibble representation for IPv6. 
### When performing a reverse lookup, the DNS client converts the address into these formats before querying the name for a PTR record following the delegation chain as for any DNS query. For example, assuming the IPv4 address 208.80.152.2 is assigned to Wikimedia, it is represented as a DNS name in reverse order: 2.152.80.208.in-addr.arpa. When the DNS resolver gets a pointer (PTR) request, it begins by querying the root servers, which point to the servers of American Registry for Internet Numbers (ARIN) for the 208.in-addr.arpa zone. ARIN's servers delegate 152.80.208.in-addr.arpa to Wikimedia to which the resolver sends another query for 2.152.80.208.in-addr.arpa, which results in an authoritative response.
## Client lookup  

### Users generally do not communicate directly with a DNS resolver. Instead DNS resolution takes place transparently in applications such as web browsers, e-mail clients, and other Internet applications. When an application makes a request that requires a domain name lookup, such programs send a resolution request to the DNS resolver in the local operating system, which in turn handles the communications required. 
### The DNS resolver will almost invariably have a cache (see above) containing recent lookups. If the cache can provide the answer to the request, the resolver will return the value in the cache to the program that made the request. If the cache does not contain the answer, the resolver will send the request to one or more designated DNS servers. In the case of most home users, the Internet service provider to which the machine connects will usually supply this DNS server: such a user will either have configured that server's address manually or allowed DHCP to set it; however, where systems administrators have configured systems to use their own DNS servers, their DNS resolvers point to separately maintained name servers of the organization. In any event, the name server thus queried will follow the process outlined above, until it either successfully finds a result or does not. It then returns its results to the DNS resolver; assuming it has found a result, the resolver duly caches that result for future use, and hands the result back to the software which initiated the request.
## Broken resolvers  
### Some large ISPs have configured their DNS servers to violate rules, such as by disobeying TTLs, or by indicating that a domain name does not exist just because one of its name servers does not respond.Some applications such as web browsers maintain an internal DNS cache to avoid repeated lookups via the network. This practice can add extra difficulty when debugging DNS issues as it obscures the history of such data. These caches typically use very short caching times on the order of one minute.Internet Explorer represents a notable exception: versions up to IE 3.x cache DNS records for 24 hours by default. Internet Explorer 4.x and later versions (up to IE 8) decrease the default timeout value to half an hour, which may be changed by modifying the default configuration.When Google Chrome detects issues with the DNS server it displays a specific error message.
## Other applications  
### The Domain Name System includes several other functions and features. 
### Hostnames and IP addresses are not required to match in a one-to-one relationship. Multiple hostnames may correspond to a single IP address, which is useful in virtual hosting, in which many web sites are served from a single host. Alternatively, a single hostname may resolve to many IP addresses to facilitate fault tolerance and load distribution to multiple server instances across an enterprise or the global Internet. 
### DNS serves other purposes in addition to translating names to IP addresses. For instance, mail transfer agents use DNS to find the best mail server to deliver e-mail: An MX record provides a mapping between a domain and a mail exchanger; this can provide an additional layer of fault tolerance and load distribution. 
### The DNS is used for efficient storage and distribution of IP addresses of blacklisted email hosts. A common method is to place the IP address of the subject host into the sub-domain of a higher level domain name, and to resolve that name to a record that indicates a positive or a negative indication. 
### For example: 

### The address 102.3.4.5 is blacklisted. It points to 5.4.3.102.blacklist.example, which resolves to 127.0.0.1. 
### The address 102.3.4.6 is not blacklisted and points to 6.4.3.102.blacklist.example. This hostname is either not configured, or resolves to 127.0.0.2.E-mail servers can query blacklist.example to find out if a specific host connecting to them is in the blacklist. Many of such blacklists, either subscription-based or free of cost, are available for use by email administrators and anti-spam software. 
### To provide resilience in the event of computer or network failure, multiple DNS servers are usually provided for coverage of each domain. At the top level of global DNS, thirteen groups of root name servers exist, with additional \"copies\" of them distributed worldwide via anycast addressing. 
### Dynamic DNS (DDNS) updates a DNS server with a client IP address on-the-fly, for example, when moving between ISPs or mobile hot spots, or when the IP address changes administratively.
## DNS message format  
### The DNS protocol uses two types of DNS messages, queries and replies; both have the same format. Each message consists of a header and four sections: question, answer, authority, and an additional space. A header field (flags) controls the content of these four sections.The header section consists of the following fields: Identification, Flags, Number of questions, Number of answers, Number of authority resource records (RRs), and Number of additional RRs. Each field is 16 bits long, and appears in the order given. The identification field is used to match responses with queries. The flag field consists of sub-fields as follows: 

### After the flag, the header ends with four 16-bit integers which contain the number of records in each of the sections that follow, in the same order.
## Question section  
### The question section has a simpler format than the resource record format used in the other sections.  Each question record (there is usually just one in the section) contains the following fields: 

### The domain name is broken into discrete labels which are concatenated; each label is prefixed by the length of that label.
## DNS transport protocols 
## DNS-over-UDP/53 (\"Do53\")  
### From the time of its origin in 1983 until quite recently, DNS has primarily answered queries on User Datagram Protocol (UDP) port number 53. Such queries consist of a clear-text request sent in a single UDP packet from the client, responded to with a clear-text reply sent in a single UDP packet from the server. When the length of the answer exceeds 512 bytes and both client and server support Extension Mechanisms for DNS (EDNS), larger UDP packets may be used. Use of DNS-over-UDP is limited by, among other things, its lack of transport-layer encryption, authentication, reliable delivery, and message length.
## DNS-over-TCP/53 (\"Do53/TCP\")  
### In 1989, RFC 1123 specified optional Transmission Control Protocol (TCP) transport for DNS queries, replies and, particularly, zone transfers. Via fragmentation of long replies, TCP allows longer responses, reliable delivery, and re-use of long-lived connections between clients and servers.
## DNSCrypt  

### The DNSCrypt protocol, which was developed in 2011 outside the IETF standards framework, introduced DNS encryption on the downstream side of recursive resolvers, wherein clients encrypt query payloads using servers' public keys, which are published in the DNS (rather than relying upon third-party certificate authorities) and which may in turn be protected by DNSSEC signatures. DNSCrypt uses either TCP or UDP port 443, the same port as HTTPS encrypted web traffic. This introduced not only privacy regarding the content of the query, but also a significant measure of firewall-traversal capability. In 2019, DNSCrypt was further extended to support an \"anonymized\" mode, similar to the proposed \"Oblivious DNS,\" in which an ingress node receives a query which has been encrypted with the public key of a different server, and relays it to that server, which acts as an egress node, performing the recursive resolution. Privacy of user/query pairs is created, since the ingress node does not know the content of the query, while the egress nodes does not know the identity of the client. DNSCrypt was first implemented in production by OpenDNS in December of 2011.
## DNS-over-TLS (\"DoT\")  

### An IETF standard for encrypted DNS emerged in 2016, utilizing standard Transport Layer Security (TLS) to protect the entire connection, rather than just the DNS payload. DoT servers listen on TCP port 853. RFC7858 specifies that opportunistic encryption and authenticated encryption may be supported, but did not make either server or client authentication mandatory.
## DNS-over-HTTPS (\"DoH\")  

### A competing standard for DNS query transport was introduced in 2018, tunneling DNS query data over HTTPS (which in turn transports HTTP over TLS). DoH was promoted as a more web-friendly alternative to DNS since, like DNSCrypt, it travels on TCP port 443, and thus looks similar to web traffic, though they are easily differentiable in practice. DoH has been widely criticized for decreasing user anonymity relative to DoT.
## DNS-over-TOR  
### Like other Internet protocols, DNS may be run over VPNs and tunnels. One use which has become common enough since 2019 to warrant its own frequently used acronym is DNS-over-Tor. The privacy gains of Oblivious DNS can be garnered through the use of the preexisting Tor network of ingress and egress nodes, paired with the transport-layer encryption provided by TLS.
## Oblivious DNS-over-HTTPS (\"ODoH\")  
### In 2021, an \"oblivious\" implementation of DoH was proposed and has been implemented in draft form, combining ingress/egress separation with HTTPS tunneling and TLS transport-layer encryption in a single defined protocol.
## Resource records  

### The Domain Name System specifies a database of information elements for network resources. The types of information elements are categorized and organized with a list of DNS record types, the resource records (RRs). Each record has a type (name and number), an expiration time (time to live), a class, and type-specific data. Resource records of the same type are described as a resource record set (RRset), having no special ordering. DNS resolvers return the entire set upon query, but servers may implement round-robin ordering to achieve load balancing. In contrast, the Domain Name System Security Extensions (DNSSEC) work on the complete set of resource record in canonical order. 
### When sent over an Internet Protocol network, all records use the common format specified in RFC 1035: 
### NAME is the fully qualified domain name of the node in the tree. On the wire, the name may be shortened using label compression where ends of domain names mentioned earlier in the packet can be substituted for the end of the current domain name. 
### TYPE is the record type. It indicates the format of the data and it gives a hint of its intended use. For example, the A record is used to translate from a domain name to an IPv4 address, the NS record lists which name servers can answer lookups on a DNS zone, and the MX record specifies the mail server used to handle mail for  a domain specified in an e-mail address. 
### RDATA is data of type-specific relevance, such as the IP address for address records, or the priority and hostname for MX records. Well known record types may use label compression in the RDATA field, but \"unknown\" record types must not (RFC 3597). 
### The CLASS of a record is set to IN (for Internet) for common DNS records involving Internet hostnames, servers, or IP addresses. In addition, the classes Chaos (CH) and Hesiod (HS) exist.  Each class is an independent name space with potentially different delegations of DNS zones. 
### In addition to resource records defined in a zone file, the domain name system also defines several request types that are used only in communication with other DNS nodes (on the wire), such as when performing zone transfers (AXFR/IXFR) or for EDNS (OPT).
## Wildcard DNS records  
### The domain name system supports wildcard DNS records which specify names that start with the asterisk label, '*', e.g., *.example. DNS records belonging to wildcard domain names specify rules for generating resource records within a single DNS zone by substituting whole labels with matching components of the query name, including any specified descendants. For example, in the following configuration, the DNS zone x.example specifies that all subdomains, including subdomains of subdomains, of x.example use the mail exchanger (MX) a.x.example. The A record for a.x.example is needed to specify the mail exchanger IP address. As this has the result of excluding this domain name and its subdomains from the wildcard matches, an additional MX record for the subdomain a.x.example, as well as a wildcarded MX record for all of its subdomains, must also be defined in the DNS zone. 

### The role of wildcard records was refined in RFC 4592, because the original definition in RFC 1034 was incomplete and resulted in misinterpretations by implementers.
## Protocol extensions  
### The original DNS protocol had limited provisions for extension with new features. In 1999, Paul Vixie published in RFC 2671 (superseded by RFC 6891) an extension mechanism, called Extension Mechanisms for DNS (EDNS) that introduced optional protocol elements without increasing overhead when not in use. This was accomplished through the OPT pseudo-resource record that only exists in wire transmissions of the protocol, but not in any zone files. Initial extensions were also suggested (EDNS0), such as increasing the DNS message size in UDP datagrams.
## Dynamic zone updates  
### Dynamic DNS updates use the UPDATE DNS opcode to add or remove resource records dynamically from a zone database maintained on an authoritative DNS server. The feature is described in RFC 2136. This facility is useful to register network clients into the DNS when they boot or become otherwise available on the network. As a booting client may be assigned a different IP address each time from a DHCP server, it is not possible to provide static DNS assignments for such clients.
## Security issues  
### Originally, security concerns were not major design considerations for DNS software or any software for deployment on the early Internet, as the network was not open for participation by the general public. However, the expansion of the Internet into the commercial sector in the 1990s changed the requirements for security measures to protect data integrity and user authentication. 
### Several vulnerability issues were discovered and exploited by malicious users. One such issue is DNS cache poisoning, in which data is distributed to caching resolvers under the pretense of being an authoritative origin server, thereby polluting the data store with potentially false information and long expiration times (time-to-live). Subsequently, legitimate application requests may be redirected to network hosts operated with malicious intent. 
### DNS responses traditionally do not have a cryptographic signature, leading to many attack possibilities; the Domain Name System Security Extensions (DNSSEC) modify DNS to add support for cryptographically signed responses. DNSCurve has been proposed as an alternative to DNSSEC. Other extensions, such as TSIG, add support for cryptographic authentication between trusted peers and are commonly used to authorize zone transfer or dynamic update operations. 
### Some domain names may be used to achieve spoofing effects. For example, paypal.com and paypa1.com are different names, yet users may be unable to distinguish them in a graphical user interface depending on the user's chosen typeface. In many fonts the letter l and the numeral 1 look very similar or even identical. This problem is acute in systems that support internationalized domain names, as many character codes in ISO 10646 may appear identical on typical computer screens. This vulnerability is occasionally exploited in phishing.Techniques such as forward-confirmed reverse DNS can also be used to help validate DNS results. 
### DNS can also \"leak\" from otherwise secure or private connections, if attention is not paid to their configuration, and at times DNS has been used to bypass firewalls by malicious persons, and exfiltrate data, since it is often seen as innocuous.
## Privacy and tracking issues  
### Originally designed as a public, hierarchical, distributed and heavily cached database, DNS protocol has no confidentiality controls. User queries and nameserver responses are being sent unencrypted which enables network packet sniffing, DNS hijacking, DNS cache poisoning and man-in-the-middle attacks. This deficiency is commonly used by cybercriminals and network operators for marketing purposes, user authentication on captive portals and censorship.User privacy is further exposed by proposals for increasing the level of client IP information in DNS queries (RFC 7871) for the benefit of Content Delivery Networks. 
### The main approaches that are in use to counter privacy issues with DNS: 

### VPNs, which move DNS resolution to the VPN operator and hide user traffic from local ISP, 
### Tor, which replaces traditional DNS resolution with anonymous .onion domains, hiding both name resolution and user traffic behind onion routing counter-surveillance, 
### Proxies and public DNS servers, which move the actual DNS resolution to a third-party provider, who usually promises little or no request logging and optional added features, such as DNS-level advertisement or pornography blocking. 
### Public DNS servers can be queried using traditional DNS protocol, in which case they provide no protection from local surveillance, or DNS-over-HTTPS, DNS-over-TLS and DNSCrypt, which do provide such protectionSolutions preventing DNS inspection  by local network operator are criticized for thwarting corporate network security policies and Internet censorship. They are also criticized from a privacy point of view, as giving away the DNS resolution to the hands of a small number of companies known for monetizing user traffic and for centralizing DNS name resolution, which is generally perceived as harmful for the Internet. 
### Google is the dominant provider of the platform in Android, the browser in Chrome, and the DNS resolver in the 8.8.8.8 service. Would this scenario be a case of a single corporate entity being in a position of overarching control of  the  entire  namespace  of  the  Internet?  Netflix  already  fielded  an  app that used its own DNS resolution mechanism independent of the platform upon which the app was running. What if the Facebook app included DoH? What if Apple\u2019s iOS used a DoH-resolution mechanism to bypass local DNS resolution and steer all DNS queries from Apple\u2019s platforms to a set of Apple-operated name resolvers?
## Domain name registration  
### The right to use a domain name is delegated by domain name registrars which are accredited by the Internet Corporation for Assigned Names and Numbers (ICANN) or other organizations such as OpenNIC, that are charged with overseeing the name and number systems of the Internet. In addition to ICANN, each top-level domain (TLD) is maintained and serviced technically by an administrative organization, operating a registry. A registry is responsible for operating the database of names within its authoritative zone, although the term is most often used for TLDs.  A registrant is a person or organization who asked for domain registration.  The registry receives registration information from each domain name registrar, which is authorized (accredited) to assign names in the corresponding zone and publishes the information using the WHOIS protocol.  As of 2015, usage of RDAP is being considered.ICANN publishes the complete list of TLDs, TLD registries, and domain name registrars. Registrant information associated with domain names is maintained in an online database accessible with the WHOIS service. For most of the more than 290 country code top-level domains (ccTLDs), the domain registries maintain the WHOIS (Registrant, name servers, expiration dates, etc.) information. For instance, DENIC, Germany NIC, holds the DE domain data. From about 2001, most Generic top-level domain (gTLD) registries have adopted this so-called thick registry approach, i.e. keeping the WHOIS data in central registries instead of registrar databases. 
### For top-level domains on COM and NET, a thin registry model is used. The domain registry (e.g., GoDaddy, BigRock and PDR, VeriSign, etc., etc.) holds basic WHOIS data (i.e., registrar and name servers, etc.). Organizations, or registrants using ORG on the other hand, are on the Public Interest Registry exclusively. 
### Some domain name registries, often called network information centers (NIC), also function as registrars to end-users, in addition to providing access to the WHOIS datasets. The top-level domain registries, such as for the domains COM, NET, and ORG use a registry-registrar model consisting of many domain name registrars. In this method of management, the registry only manages the domain name database and the relationship with the registrars. The registrants (users of a domain name) are customers of the registrar, in some cases through additional subcontracting of resellers.
## RFC documents 
## Standards  
### The Domain Name System is defined by Request for Comments (RFC) documents published by the Internet Engineering Task Force (Internet standards). The following is a list of RFCs that define the DNS protocol. 

### RFC 1034, Domain Names - Concepts and Facilities 
### RFC 1035, Domain Names - Implementation and Specification 
### RFC 1123, Requirements for Internet Hosts\u2014Application and Support 
### RFC 1995, Incremental Zone Transfer in DNS 
### RFC 1996, A Mechanism for Prompt Notification of Zone Changes (DNS NOTIFY) 
### RFC 2136, Dynamic Updates in the domain name system (DNS UPDATE) 
### RFC 2181, Clarifications to the DNS Specification 
### RFC 2308, Negative Caching of DNS Queries (DNS NCACHE) 
### RFC 2672, Non-Terminal DNS Name Redirection 
### RFC 2845, Secret Key Transaction Authentication for DNS (TSIG) 
### RFC 3225, Indicating Resolver Support of DNSSEC 
### RFC 3226, DNSSEC and IPv6 A6 aware server/resolver message size requirements 
### RFC 3596, DNS Extensions to Support IP Version 6 
### RFC 3597, Handling of Unknown DNS Resource Record (RR) Types 
### RFC 4343, Domain Name System (DNS) Case Insensitivity Clarification 
### RFC 4592, The Role of Wildcards in the Domain Name System 
### RFC 4635, HMAC SHA TSIG Algorithm Identifiers 
### RFC 5001, DNS Name Server Identifier (NSID) Option 
### RFC 5011, Automated Updates of DNS Security (DNSSEC) Trust Anchors 
### RFC 5452, Measures for Making DNS More Resilient against Forged Answers 
### RFC 5890, Internationalized Domain Names for Applications (IDNA):Definitions and Document Framework 
### RFC 5891, Internationalized Domain Names in Applications (IDNA): Protocol 
### RFC 5892, The Unicode Code Points and Internationalized Domain Names for Applications (IDNA) 
### RFC 5893, Right-to-Left Scripts for Internationalized Domain Names for Applications (IDNA) 
### RFC 6891, Extension Mechanisms for DNS (EDNS0) 
### RFC 7766, DNS Transport over TCP - Implementation Requirements
## Proposed security standards  
### RFC 4033, DNS Security Introduction and Requirements 
### RFC 4034, Resource Records for the DNS Security Extensions 
### RFC 4035, Protocol Modifications for the DNS Security Extensions 
### RFC 4509, Use of SHA-256 in DNSSEC Delegation Signer (DS) Resource Records 
### RFC 4470, Minimally Covering NSEC Records and DNSSEC On-line Signing 
### RFC 5155, DNS Security (DNSSEC) Hashed Authenticated Denial of Existence 
### RFC 5702, Use of SHA-2 Algorithms with RSA in DNSKEY and RRSIG Resource Records for DNSSEC 
### RFC 5910, Domain Name System (DNS) Security Extensions Mapping for the Extensible Provisioning Protocol (EPP) 
### RFC 5933, Use of GOST Signature Algorithms in DNSKEY and RRSIG Resource Records for DNSSEC 
### RFC 7830, The EDNS(0) Padding Option 
### RFC 7858, Specification for DNS over Transport Layer Security (TLS) 
### RFC 8310, Usage Profiles for DNS over TLS and DNS over DTLS 
### RFC 8484, DNS Queries over HTTPS (DoH)
## Experimental RFCs  
### RFC 1183, New DNS RR Definitions
## Best Current Practices  
### RFC 2182, Selection and Operation of Secondary DNS Servers (BCP 16) 
### RFC 2317, Classless IN-ADDR.ARPA delegation (BCP 20) 
### RFC 5625, DNS Proxy Implementation Guidelines (BCP 152) 
### RFC 6895, Domain Name System (DNS) IANA Considerations (BCP 42) 
### RFC 7720, DNS Root Name Service Protocol and Deployment Requirements (BCP 40)
## Informational RFCs  
### These RFCs are advisory in nature, but may provide useful information despite defining neither a standard or BCP. (RFC 1796) 

### RFC 1178, Choosing a Name for Your Computer (FYI 5) 
### RFC 1591, Domain Name System Structure and Delegation 
### RFC 1912, Common DNS Operational and Configuration Errors 
### RFC 2100, The Naming of Hosts 
### RFC 3696, Application Techniques for Checking and Transformation of Names 
### RFC 3833. Threat Analysis of the Domain Name System (DNS) 
### RFC 4892, Requirements for a Mechanism Identifying a Name Server Instance 
### RFC 5894, Internationalized Domain Names for Applications (IDNA):Background, Explanation, and Rationale 
### RFC 5895, Mapping Characters for Internationalized Domain Names in Applications (IDNA) 2008 
### RFC 7626, DNS Privacy Considerations 
### RFC 7706, Decreasing Access Time to Root Servers by Running One on Loopback 
### RFC 8499, DNS Terminology
## Unknown  
### These RFCs have an official status of Unknown, but due to their age are not clearly labeled as such. 

### RFC 920, Domain Requirements \u2013 Specified original top-level domains 
### RFC 1032, Domain Administrators Guide 
### RFC 1033, Domain Administrators Operations Guide 
### RFC 1101, DNS Encodings of Network Names and Other Types
## See also 
## References 
## Sources  
### Evans, Claire L. (2018). Broad Band: The Untold Story of the Women Who Made the Internet. New York: Portfolio/Penguin. ISBN 9780735211759.
## External links  
### Vixie, Paul (2007-04-01). \"DNS Complexity\". ACM Queue. Archived from the original on 2007-06-10. 
### Zytrax.com, Open Source Guide \u2013 DNS for Rocket Scientists. 
### Internet Governance and the Domain Name System: Issues for Congress Congressional Research Service 
### Ball, James (28 February 2014). \"Meet the seven people who hold the keys to worldwide internet security\". The Guardian. Guardian News & Media Limited. Retrieved 28 February 2014."
## References
### [Reference](http://www.acmqueue.com/modules.php?name=Content&pa=showpage&pid=481) - http://www.acmqueue.com/modules.php?name=Content&pa=showpage&pid=481
### [Reference](http://www.akamai.com/dl/technical_publications/network_overview_osr.pdf) - http://www.akamai.com/dl/technical_publications/network_overview_osr.pdf
### [Reference](http://ipj.dreamhosters.com/wp-content/uploads/2019/07/ipj222.pdf) - http://ipj.dreamhosters.com/wp-content/uploads/2019/07/ipj222.pdf
### [Reference](http://dyn.com/web-browser-dns-caching-bad-thing/) - http://dyn.com/web-browser-dns-caching-bad-thing/
### [Reference](http://support.microsoft.com/default.aspx?scid=KB;en-us;263558) - http://support.microsoft.com/default.aspx?scid=KB;en-us;263558
### [Reference](http://www.verisign.com/en_US/domain-names/domain-registrar/index.xhtml) - http://www.verisign.com/en_US/domain-names/domain-registrar/index.xhtml
### [Reference](http://www.zytrax.com/books/dns/) - http://www.zytrax.com/books/dns/
### [Reference](http://www.eecs.berkeley.edu/Pubs/TechRpts/1984/5957.html) - http://www.eecs.berkeley.edu/Pubs/TechRpts/1984/5957.html
### [Reference](http://www.apwg.org/reports/APWG_GlobalPhishingSurvey_1H2010.pdf) - http://www.apwg.org/reports/APWG_GlobalPhishingSurvey_1H2010.pdf
### [Reference](http://doi.org/10.1145%2F1842733.1842736) - http://doi.org/10.1145%2F1842733.1842736
### [Reference](http://doi.org/10.17487%2FRFC1034) - http://doi.org/10.17487%2FRFC1034
### [Reference](http://doi.org/10.17487%2FRFC1035) - http://doi.org/10.17487%2FRFC1035
### [Reference](http://doi.org/10.17487%2FRFC7719) - http://doi.org/10.17487%2FRFC7719
### [Reference](http://www.fas.org/sgp/crs/misc/R42351.pdf) - http://www.fas.org/sgp/crs/misc/R42351.pdf
### [Reference](http://internethalloffame.org/blog/2012/07/23/why-does-net-still-work-christmas-paul-mockapetris) - http://internethalloffame.org/blog/2012/07/23/why-does-net-still-work-christmas-paul-mockapetris
### [Reference](http://www.internetsociety.org/blog/2013/11/happy-30th-birthday-dns) - http://www.internetsociety.org/blog/2013/11/happy-30th-birthday-dns
### [Reference](http://www.isc.org/downloads/bind/) - http://www.isc.org/downloads/bind/
### [Reference](http://ask.slashdot.org/story/05/04/18/198259/providers-ignoring-dns-ttl) - http://ask.slashdot.org/story/05/04/18/198259/providers-ignoring-dns-ttl
### [Reference](http://mak.bn.org.pl/cgi-bin/KHW/makwww.exe?BM=1&NU=1&IM=4&WI=9810532434805606) - http://mak.bn.org.pl/cgi-bin/KHW/makwww.exe?BM=1&NU=1&IM=4&WI=9810532434805606
### [Reference](https://umbrella.cisco.com/blog/dnscrypt-critical-fundamental-and-about-time) - https://umbrella.cisco.com/blog/dnscrypt-critical-fundamental-and-about-time
### [Reference](https://raw.githubusercontent.com/DNSCrypt/dnscrypt-protocol/master/ANONYMIZED-DNSCRYPT.txt) - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-protocol/master/ANONYMIZED-DNSCRYPT.txt
### [Reference](https://raw.githubusercontent.com/cslev/doh_ml/main/DNS_over_HTTPS_identification.pdf) - https://raw.githubusercontent.com/cslev/doh_ml/main/DNS_over_HTTPS_identification.pdf
### [Reference](https://books.google.com/books?id=C8ouDwAAQBAJ&q=9780735211759&pg=PP1) - https://books.google.com/books?id=C8ouDwAAQBAJ&q=9780735211759&pg=PP1
### [Reference](https://books.google.com/books?id=GB_O89fnz_sC&dq=%22lame+delegation%22&pg=PA475) - https://books.google.com/books?id=GB_O89fnz_sC&dq=%22lame+delegation%22&pg=PA475
### [Reference](https://books.google.com/books?id=YjE5DwAAQBAJ&dq=%22lame+delegation%22&pg=PA235) - https://books.google.com/books?id=YjE5DwAAQBAJ&dq=%22lame+delegation%22&pg=PA235
### [Reference](https://hackaday.com/2019/10/21/dns-over-https-is-the-wrong-partial-solution/) - https://hackaday.com/2019/10/21/dns-over-https-is-the-wrong-partial-solution/
### [Reference](https://www.theguardian.com/technology/2014/feb/28/seven-people-keys-worldwide-internet-security-web) - https://www.theguardian.com/technology/2014/feb/28/seven-people-keys-worldwide-internet-security-web
### [Reference](https://people.cs.umass.edu/~ramesh/Site/PUBLICATIONS_files/DMPPSW02.pdf) - https://people.cs.umass.edu/~ramesh/Site/PUBLICATIONS_files/DMPPSW02.pdf
### [Reference](https://d-nb.info/gnd/4348318-5) - https://d-nb.info/gnd/4348318-5
### [Reference](https://conference.apnic.net/data/39/dns-abuse-handling-final_1425362607.pdf) - https://conference.apnic.net/data/39/dns-abuse-handling-final_1425362607.pdf
### [Reference](https://web.archive.org/web/20070610092333/http://acmqueue.com/modules.php?name=Content&pa=showpage&pid=481) - https://web.archive.org/web/20070610092333/http://acmqueue.com/modules.php?name=Content&pa=showpage&pid=481
### [Reference](https://web.archive.org/web/20121003212327/http://apwg.org/reports/APWG_GlobalPhishingSurvey_1H2010.pdf) - https://web.archive.org/web/20121003212327/http://apwg.org/reports/APWG_GlobalPhishingSurvey_1H2010.pdf
### [Reference](https://web.archive.org/web/20151222144443/https://www.icann.org/news/announcement-2015-12-03-en) - https://web.archive.org/web/20151222144443/https://www.icann.org/news/announcement-2015-12-03-en
### [Reference](https://web.archive.org/web/20180914182353/https://www.internethalloffame.org/inductees/elizabeth-feinler) - https://web.archive.org/web/20180914182353/https://www.internethalloffame.org/inductees/elizabeth-feinler
### [Reference](https://web.archive.org/web/20191025094649/https://raw.githubusercontent.com/DNSCrypt/dnscrypt-protocol/master/ANONYMIZED-DNSCRYPT.txt) - https://web.archive.org/web/20191025094649/https://raw.githubusercontent.com/DNSCrypt/dnscrypt-protocol/master/ANONYMIZED-DNSCRYPT.txt
### [Reference](https://web.archive.org/web/20200701221715/https://umbrella.cisco.com/blog/dnscrypt-critical-fundamental-and-about-time) - https://web.archive.org/web/20200701221715/https://umbrella.cisco.com/blog/dnscrypt-critical-fundamental-and-about-time
### [Reference](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6) - https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6
### [Reference](https://www.icann.org/news/announcement-2015-12-03-en) - https://www.icann.org/news/announcement-2015-12-03-en
### [Reference](https://datatracker.ietf.org/doc/draft-pauly-dprive-oblivious-doh/) - https://datatracker.ietf.org/doc/draft-pauly-dprive-oblivious-doh/
### [Reference](https://datatracker.ietf.org/doc/html/rfc1032) - https://datatracker.ietf.org/doc/html/rfc1032
### [Reference](https://datatracker.ietf.org/doc/html/rfc1033) - https://datatracker.ietf.org/doc/html/rfc1033
### [Reference](https://datatracker.ietf.org/doc/html/rfc1034) - https://datatracker.ietf.org/doc/html/rfc1034
### [Reference](https://datatracker.ietf.org/doc/html/rfc1034#section-3.1) - https://datatracker.ietf.org/doc/html/rfc1034#section-3.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1034#section-4.2) - https://datatracker.ietf.org/doc/html/rfc1034#section-4.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc1035) - https://datatracker.ietf.org/doc/html/rfc1035
### [Reference](https://datatracker.ietf.org/doc/html/rfc1101) - https://datatracker.ietf.org/doc/html/rfc1101
### [Reference](https://datatracker.ietf.org/doc/html/rfc1123) - https://datatracker.ietf.org/doc/html/rfc1123
### [Reference](https://datatracker.ietf.org/doc/html/rfc1178) - https://datatracker.ietf.org/doc/html/rfc1178
### [Reference](https://datatracker.ietf.org/doc/html/rfc1183) - https://datatracker.ietf.org/doc/html/rfc1183
### [Reference](https://datatracker.ietf.org/doc/html/rfc1591) - https://datatracker.ietf.org/doc/html/rfc1591
### [Reference](https://datatracker.ietf.org/doc/html/rfc1912) - https://datatracker.ietf.org/doc/html/rfc1912
### [Reference](https://datatracker.ietf.org/doc/html/rfc1995) - https://datatracker.ietf.org/doc/html/rfc1995
### [Reference](https://datatracker.ietf.org/doc/html/rfc1996) - https://datatracker.ietf.org/doc/html/rfc1996
### [Reference](https://datatracker.ietf.org/doc/html/rfc2100) - https://datatracker.ietf.org/doc/html/rfc2100
### [Reference](https://datatracker.ietf.org/doc/html/rfc2136) - https://datatracker.ietf.org/doc/html/rfc2136
### [Reference](https://datatracker.ietf.org/doc/html/rfc2181) - https://datatracker.ietf.org/doc/html/rfc2181
### [Reference](https://datatracker.ietf.org/doc/html/rfc2182) - https://datatracker.ietf.org/doc/html/rfc2182
### [Reference](https://datatracker.ietf.org/doc/html/rfc2308) - https://datatracker.ietf.org/doc/html/rfc2308
### [Reference](https://datatracker.ietf.org/doc/html/rfc2317) - https://datatracker.ietf.org/doc/html/rfc2317
### [Reference](https://datatracker.ietf.org/doc/html/rfc2671) - https://datatracker.ietf.org/doc/html/rfc2671
### [Reference](https://datatracker.ietf.org/doc/html/rfc2672) - https://datatracker.ietf.org/doc/html/rfc2672
### [Reference](https://datatracker.ietf.org/doc/html/rfc2845) - https://datatracker.ietf.org/doc/html/rfc2845
### [Reference](https://datatracker.ietf.org/doc/html/rfc3225) - https://datatracker.ietf.org/doc/html/rfc3225
### [Reference](https://datatracker.ietf.org/doc/html/rfc3226) - https://datatracker.ietf.org/doc/html/rfc3226
### [Reference](https://datatracker.ietf.org/doc/html/rfc3596) - https://datatracker.ietf.org/doc/html/rfc3596
### [Reference](https://datatracker.ietf.org/doc/html/rfc3597) - https://datatracker.ietf.org/doc/html/rfc3597
### [Reference](https://datatracker.ietf.org/doc/html/rfc3696) - https://datatracker.ietf.org/doc/html/rfc3696
### [Reference](https://datatracker.ietf.org/doc/html/rfc3833) - https://datatracker.ietf.org/doc/html/rfc3833
### [Reference](https://datatracker.ietf.org/doc/html/rfc4033) - https://datatracker.ietf.org/doc/html/rfc4033
### [Reference](https://datatracker.ietf.org/doc/html/rfc4034) - https://datatracker.ietf.org/doc/html/rfc4034
### [Reference](https://datatracker.ietf.org/doc/html/rfc4035) - https://datatracker.ietf.org/doc/html/rfc4035
### [Reference](https://datatracker.ietf.org/doc/html/rfc4343) - https://datatracker.ietf.org/doc/html/rfc4343
### [Reference](https://datatracker.ietf.org/doc/html/rfc4470) - https://datatracker.ietf.org/doc/html/rfc4470
### [Reference](https://datatracker.ietf.org/doc/html/rfc4509) - https://datatracker.ietf.org/doc/html/rfc4509
### [Reference](https://datatracker.ietf.org/doc/html/rfc4592) - https://datatracker.ietf.org/doc/html/rfc4592
### [Reference](https://datatracker.ietf.org/doc/html/rfc4635) - https://datatracker.ietf.org/doc/html/rfc4635
### [Reference](https://datatracker.ietf.org/doc/html/rfc4892) - https://datatracker.ietf.org/doc/html/rfc4892
### [Reference](https://datatracker.ietf.org/doc/html/rfc5001) - https://datatracker.ietf.org/doc/html/rfc5001
### [Reference](https://datatracker.ietf.org/doc/html/rfc5011) - https://datatracker.ietf.org/doc/html/rfc5011
### [Reference](https://datatracker.ietf.org/doc/html/rfc5155) - https://datatracker.ietf.org/doc/html/rfc5155
### [Reference](https://datatracker.ietf.org/doc/html/rfc5452) - https://datatracker.ietf.org/doc/html/rfc5452
### [Reference](https://datatracker.ietf.org/doc/html/rfc5625) - https://datatracker.ietf.org/doc/html/rfc5625
### [Reference](https://datatracker.ietf.org/doc/html/rfc5702) - https://datatracker.ietf.org/doc/html/rfc5702
### [Reference](https://datatracker.ietf.org/doc/html/rfc5890) - https://datatracker.ietf.org/doc/html/rfc5890
### [Reference](https://datatracker.ietf.org/doc/html/rfc5891) - https://datatracker.ietf.org/doc/html/rfc5891
### [Reference](https://datatracker.ietf.org/doc/html/rfc5892) - https://datatracker.ietf.org/doc/html/rfc5892
### [Reference](https://datatracker.ietf.org/doc/html/rfc5893) - https://datatracker.ietf.org/doc/html/rfc5893
### [Reference](https://datatracker.ietf.org/doc/html/rfc5894) - https://datatracker.ietf.org/doc/html/rfc5894
### [Reference](https://datatracker.ietf.org/doc/html/rfc5895) - https://datatracker.ietf.org/doc/html/rfc5895
### [Reference](https://datatracker.ietf.org/doc/html/rfc5910) - https://datatracker.ietf.org/doc/html/rfc5910
### [Reference](https://datatracker.ietf.org/doc/html/rfc5933) - https://datatracker.ietf.org/doc/html/rfc5933
### [Reference](https://datatracker.ietf.org/doc/html/rfc6891) - https://datatracker.ietf.org/doc/html/rfc6891
### [Reference](https://datatracker.ietf.org/doc/html/rfc6895) - https://datatracker.ietf.org/doc/html/rfc6895
### [Reference](https://datatracker.ietf.org/doc/html/rfc7626) - https://datatracker.ietf.org/doc/html/rfc7626
### [Reference](https://datatracker.ietf.org/doc/html/rfc7706) - https://datatracker.ietf.org/doc/html/rfc7706
### [Reference](https://datatracker.ietf.org/doc/html/rfc7719) - https://datatracker.ietf.org/doc/html/rfc7719
### [Reference](https://datatracker.ietf.org/doc/html/rfc7720) - https://datatracker.ietf.org/doc/html/rfc7720
### [Reference](https://datatracker.ietf.org/doc/html/rfc7766) - https://datatracker.ietf.org/doc/html/rfc7766
### [Reference](https://datatracker.ietf.org/doc/html/rfc7830) - https://datatracker.ietf.org/doc/html/rfc7830
### [Reference](https://datatracker.ietf.org/doc/html/rfc7858) - https://datatracker.ietf.org/doc/html/rfc7858
### [Reference](https://datatracker.ietf.org/doc/html/rfc8310) - https://datatracker.ietf.org/doc/html/rfc8310
### [Reference](https://datatracker.ietf.org/doc/html/rfc8484) - https://datatracker.ietf.org/doc/html/rfc8484
### [Reference](https://datatracker.ietf.org/doc/html/rfc8499) - https://datatracker.ietf.org/doc/html/rfc8499
### [Reference](https://datatracker.ietf.org/doc/html/rfc920) - https://datatracker.ietf.org/doc/html/rfc920
### [Reference](https://tools.ietf.org/html/rfc8499#page-19) - https://tools.ietf.org/html/rfc8499#page-19
### [Reference](https://internethalloffame.org/inductees/paul-mockapetris) - https://internethalloffame.org/inductees/paul-mockapetris
### [Reference](https://www.internethalloffame.org/inductees/elizabeth-feinler) - https://www.internethalloffame.org/inductees/elizabeth-feinler
### [Reference](https://www.ndss-symposium.org/wp-content/uploads/dnspriv21-03-paper.pdf) - https://www.ndss-symposium.org/wp-content/uploads/dnspriv21-03-paper.pdf
### [Reference](https://api.semanticscholar.org/CorpusID:207181702) - https://api.semanticscholar.org/CorpusID:207181702
### [Reference](https://www.wikidata.org/wiki/Q8767#identifiers) - https://www.wikidata.org/wiki/Q8767#identifiers
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/f/f9/Crystal_Clear_app_linneighborhood.svg) - https://upload.wikimedia.org/wikipedia/commons/f/f9/Crystal_Clear_app_linneighborhood.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/60/DNS_Architecture.svg) - https://upload.wikimedia.org/wikipedia/commons/6/60/DNS_Architecture.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/b/b1/Domain_name_space.svg) - https://upload.wikimedia.org/wikipedia/commons/b/b1/Domain_name_space.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/a5/Example_of_an_iterative_DNS_resolver.svg) - https://upload.wikimedia.org/wikipedia/commons/a/a5/Example_of_an_iterative_DNS_resolver.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg) - https://upload.wikimedia.org/wikipedia/commons/0/0b/Wikiversity_logo_2017.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/1/1b/Semi-protection-shackle.svg) - https://upload.wikimedia.org/wikipedia/en/1/1b/Semi-protection-shackle.svg