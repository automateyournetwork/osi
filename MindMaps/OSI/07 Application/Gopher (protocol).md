# Gopher (protocol)
## [URL](https://en.wikipedia.org/wiki/Gopher_(protocol)) - https://en.wikipedia.org/wiki/Gopher_(protocol)
## Catagories
### All articles containing potentially dated statements
### All articles to be expanded
### All articles with failed verification
### All articles with specifically marked weasel-worded phrases
### All articles with unsourced statements
### All articles with vague or ambiguous time
### Articles containing potentially dated statements from 2012
### Articles to be expanded from July 2021
### Articles using small message boxes
### Articles with GND identifiers
### Articles with LCCN identifiers
### Articles with failed verification from January 2022
### Articles with short description
### Articles with specifically marked weasel-worded phrases from January 2014
### Articles with unsourced statements from May 2016
### Articles with unsourced statements from September 2021
### CS1 errors: missing periodical
### Gopher (protocol)
### History of the Internet
### Internet Standards
### Short description matches Wikidata
### URI schemes
### University of Minnesota software
### Use dmy dates from April 2021
### Vague or ambiguous time from May 2021
### Webarchive template wayback links
### "The Gopher protocol  is a communication protocol designed for distributing, searching, and retrieving documents in Internet Protocol networks. The design of the Gopher protocol and user interface is menu-driven, and presented an alternative to the World Wide Web in its early stages, but ultimately fell into disfavor, yielding to HTTP. The Gopher ecosystem is often regarded as the effective predecessor of the World Wide Web.The protocol was invented by a team led by Mark P. McCahill at the University of Minnesota.  It offers some features not natively supported by the Web and imposes a much stronger hierarchy on the documents it stores. Its text menu interface is well-suited to computing environments that rely heavily on remote text-oriented computer terminals, which were still common at the time of its creation in 1991, and the simplicity of its protocol facilitated a wide variety of client implementations. More recent Gopher revisions and graphical clients added support for multimedia.Gopher's hierarchical structure provided a platform for the first large-scale electronic library connections. The Gopher protocol is still in use by enthusiasts, and although it has been almost entirely supplanted by the Web, a small population of actively-maintained servers remains.
## Origins  
### Gopher system was released in mid-1991 by Mark P. McCahill, Farhad Anklesaria, Paul Lindner, Daniel Torrey, and Bob Alberti of the University of Minnesota in the United States. Its central goals were, as stated in RFC 1436: 

### A file-like hierarchical arrangement that would be familiar to users. 
### A simple syntax. 
### A system that can be created quickly and inexpensively. 
### Extensibility of the file system metaphor; allowing addition of searches for example.Gopher combines document hierarchies with collections of services, including WAIS, the Archie and Veronica search engines, and gateways to other information systems such as File Transfer Protocol (FTP) and Usenet. 
### The general interest in campus-wide information systems (CWISs) in higher education at the time, and the ease of setup of Gopher servers to create an instant CWIS with links to other sites' online directories and resources were the factors contributing to Gopher's rapid adoption. 
### The name was coined by Anklesaria as a play on several meanings of the word \"gopher\". The University of Minnesota mascot is the gopher, a gofer is an assistant who \"goes for\" things, and a gopher burrows through the ground to reach a desired location.
## Decline  
### The World Wide Web was in its infancy in 1991, and Gopher services quickly became established. By the late 1990s, Gopher had ceased expanding. Several factors contributed to Gopher's stagnation: 

### In February 1993, the University of Minnesota announced that it would charge licensing fees for the use of its implementation of the Gopher server. Users became concerned that fees might also be charged for independent implementations. Gopher expansion stagnated, to the advantage of the World Wide Web, to which CERN disclaimed ownership. In September 2000, the University of Minnesota re-licensed its Gopher software under the GNU General Public License. 
### Gopher client functionality was quickly duplicated by the early Mosaic web browser, which subsumed its protocol. 
### Gopher has a more rigid structure than the free-form HTML of the Web. Every Gopher document has a defined format and type, and the typical user navigates through a single server-defined menu system to get to a particular document. This can be quite different from the way a user finds documents on the Web.Gopher remains in active use by its enthusiasts, and there have been attempts to revive Gopher on modern platforms and mobile devices. One attempt is The Overbite Project, which hosts various browser extensions and modern clients.
## Server census  
### As of 2012, there remained about 160 gopher servers indexed by Veronica-2, reflecting a slow growth from 2007 when there were fewer than 100. They are typically infrequently updated. On these servers Veronica indexed approximately 2.5 million unique selectors. A handful of new servers were being set up every year by hobbyists with over 50 having been set up and added to Floodgap's list since 1999. A snapshot of Gopherspace in 2007 circulated on BitTorrent and was still available in 2010. Due to the simplicity of the Gopher protocol, setting up new servers or adding Gopher support to browsers is often done in a tongue-in-cheek manner, principally on April Fools' Day. 
### In November 2014 Veronica indexed 144 gopher servers, reflecting a small drop from 2012, but within these servers Veronica indexed approximately 3 million unique selectors. 
### In March 2016 Veronica indexed 135 gopher servers, within which it indexed approximately 4 million unique selectors. 
### In March 2017 Veronica indexed 133 gopher servers, within which it indexed approximately 4.9 million unique selectors. 
### In May 2018 Veronica indexed 260 gopher servers, within which it indexed approximately 3.7 million unique selectors. 
### In May 2019 Veronica indexed 320 gopher servers, within which it indexed approximately 4.2 million unique selectors. 
### In January 2020 Veronica indexed 395 gopher servers, within which it indexed approximately 4.5 million unique selectors. 
### In February 2021 Veronica indexed 361 gopher servers, within which it indexed approximately 6 million unique selectors. 
### In February 2022 Veronica indexed 325 gopher servers, within which it indexed approximately 5 million unique selectors.
## Technical details  
### The conceptualization of knowledge in \"Gopher space\" or a \"cloud\" as specific information in a particular file, and the prominence of the FTP, influenced the technology and the resulting functionality of Gopher.
## Gopher characteristics  
### Gopher is designed to function and to appear much like a mountable read-only global network file system (and software, such as gopherfs, is available that can actually mount a Gopher server as a FUSE resource). At a minimum, whatever can be done with data files on a CD-ROM, can be done on Gopher. 
### A Gopher system consists of a series of hierarchical hyperlinkable menus. The choice of menu items and titles is controlled by the administrator of the server. 

### Similar to a file on a Web server, a file on a Gopher server can be linked to as a menu item from any other Gopher server. Many servers take advantage of this inter-server linking to provide a directory of other servers that the user can access.
## Protocol  
### The Gopher protocol was first described in RFC 1436. IANA has assigned TCP port 70 to the Gopher protocol. The protocol is simple to negotiate, making it possible to browse without using a client.
## User request  
### First, the client establishes a TCP connection with the server on port 70, the standard gopher port. The client then sends a string followed by a carriage return followed by a line feed (a \"CR + LF\" sequence). This is the selector, which identifies the document to be retrieved. If the item selector were an empty line, the default directory would be selected.
## Server response  
### The server then replies with the requested item and closes the connection. According to the protocol, before the connection is closed, the server should send a full-stop (i.e., a period character) on a line by itself. However, not all servers conform to this part of the protocol and the server may close the connection without returning the final full-stop. 
### The main type of reply from the server is a text or binary resource. Alternatively, the resource can be a menu, a form of structured text resource providing references to other resources. 
### Because of the simplicity of the Gopher protocol, tools such as netcat make it possible to download Gopher content easily from the command line: 

### echo jacks/jack.exe | nc gopher.example.org 70 > jack.exe 

### The protocol is also supported by cURL as of 7.21.2-DEV.
## Search request  
### The selector string in the request can optionally be followed by a tab character and a search string. This is used by item type 7.
## Source code of a menu  
### Gopher menu items are defined by lines of tab-separated values in a text file. This file is sometimes called a gophermap. As the source code to a gopher menu, a gophermap is roughly analogous to an HTML file for a web page. Each tab-separated line (called a selector line) gives the client software a description of the menu item: what it is, what it's called, and where it leads. The client displays the menu items in the order that they appear in the gophermap. 
### The first character in a selector line indicates the item type, which tells the client what kind of file or protocol the menu item points to. This helps the client decide what to do with it. Gopher's item types are a more basic precursor to the media type system used by the Web and email attachments. 
### The item type is followed by the user display string (a description or label that represents the item in the menu); the selector (a path or other string for the resource on the server); the hostname (the domain name or IP address of the server), and the network port. 
### All lines in a gopher menu are terminated by \"CR + LF\". 
### For example: The following selector line generates a link to the \"/home\" directory at the subdomain gopher.floodgap.com, on port 70. The item type of 1 indicates that the resource is a Gopher menu. The string \"Floodgap Home\" is what the user sees in the menu. 

### 1Floodgap Home\t/home\tgopher.floodgap.com\t70
## Item types  
### In a Gopher menu's source code, a one-character code indicates what kind of content the client should expect. This code may either be a digit or a letter of the alphabet; letters are case-sensitive. 
### The technical specification for Gopher, RFC 1436, defines 14 item types. The later gopher+ specification defined an additional 3 types. A one-character code indicates what kind of content the client should expect. Item type 3 is an error code for exception handling. Gopher client authors improvised item types h (HTML), i (informational message), and s (sound file) after the publication of RFC 1436. Browsers like Netscape Navigator and early versions of Microsoft Internet Explorer would prepend the item type code to the selector as described in RFC 4266, so that the type of the gopher item could be determined by the url itself. Most gopher browsers still available, use these prefixes in their urls. 

### Here is an example gopher session where the user requires a gopher menu (/Reference on the first line): 

### /Reference 
### 1CIA World Factbook     /Archives/mirrors/textfiles.com/politics/CIA    gopher.quux.org 70 
### 0Jargon 4.2.0   /Reference/Jargon 4.2.0 gopher.quux.org 70      + 
### 1Online Libraries       /Reference/Online Libraries     gopher.quux.org 70     + 
### 1RFCs: Internet Standards       /Computers/Standards and Specs/RFC      gopher.quux.org 70 
### 1U.S. Gazetteer /Reference/U.S. Gazetteer       gopher.quux.org 70      + 
### iThis file contains information on United States        fake    (NULL)  0 
### icities, counties, and geographical areas.  It has      fake    (NULL)  0 
### ilatitude/longitude, population, land and water area,   fake    (NULL)  0 
### iand ZIP codes. fake    (NULL)  0 
### i       fake    (NULL)  0 
### iTo search for a city, enter the city's name.  To search        fake    (NULL) 0 
### ifor a county, use the name plus County -- for instance,        fake    (NULL) 0 
### iDallas County. fake    (NULL)  0 

### The gopher menu sent back from the server, is a sequence of lines each of which describes an item that can be retrieved. Most clients will display these as hypertext links, and so allow the user to navigate through gopherspace by following the links. 
### This menu includes a text resource (itemtype 0 on the third line), multiple links to submenus (itemtype 1, on the second line as well as lines 4-6) and a non-standard information message (from line 7 on), broken down to multiple lines by providing dummy values for selector, host and port.
## Web links  
### Historically, to create a link to a Web server, \"GET /\" was used as a pseudo-selector to emulate an HTTP GET request. John Goerzen created an addition to the Gopher protocol, commonly referred to as \"URL links\", that allows links to any protocol that supports URLs. For example, to create a link to http://gopher.quux.org/, the item type is h, the display string is the title of the link, the item selector is \"URL:http://gopher.quux.org/\", and the domain and port are that of the originating Gopher server (so that clients that do not support URL links will query the server and receive an HTML redirection page).
## Related technology 
## Gopher+  
### Gopher+ is a forward compatible enhancement to the Gopher protocol. Gopher+ works by sending metadata between the client and the server. The enhancement was never widely adopted by Gopher servers.
## How it works  
### The client sends a tab followed by a +. A Gopher+ server will respond with a status line followed by the content the client requested. An item is marked as supporting Gopher+ in the Gopher directory listing by a tab + after the port (this is the case of some of the items in the example above).
## Other features  
### Other features of Gopher+ include: 

### Item attributes, which can include the items 
### Administrator 
### Last date of modification 
### Different views of the file, like PostScript or plain text, or different languages 
### Abstract, or description of the item 
### Interactive queries
## Search Engines 
## Veronica  

### The master Gopherspace search engine is Veronica. Veronica offers a keyword search of all the public Internet Gopher server menu titles. A Veronica search produces a menu of Gopher items, each of which is a direct pointer to a Gopher data source. Individual Gopher servers may also use localized search engines specific to their content such as Jughead and Jugtail.
## Jugtail  
### Jugtail (formerly Jughead) is a search engine system for the Gopher protocol. It is distinct from Veronica in that it searches a single server at a time.
## GopherVR  

### GopherVR is a 3D virtual reality variant of the original Gopher system.
## Client software 
## Gopher clients  
### These are clients, libraries, and utilities primarily designed to access gopher resources.
## Web clients  
### Web clients are browsers, libraries, and utilities primarily designed to access world wide web resources, but which maintain gopher support. 

### Browsers that do not natively support Gopher can still access servers using one of the available Gopher to HTTP gateways. 
### Gopher support was disabled in Internet Explorer versions 5.x and 6 for Windows in August 2002 by a patch meant to fix a security vulnerability in the browser's Gopher protocol handler to reduce the attack surface which was included in IE6 SP1; however, it can be re-enabled by editing the Windows registry. In Internet Explorer 7, Gopher support was removed on the WinINET level.
## Gopher browser extensions  
### For Mozilla Firefox and SeaMonkey, Overbite extensions extend Gopher browsing and support the current versions of the browsers (Firefox Quantum v \u226557 and equivalent versions of SeaMonkey): 

### OverbiteWX redirects gopher:// URLs to a proxy; 
### OverbiteNX adds native-like support; 
### for Firefox up to 56.*, and equivalent versions of SeaMonkey, OverbiteFF adds native-like support, but it is no longer maintainedOverbiteWX includes support for accessing Gopher servers not on port 70 using a whitelist and for CSO/ph queries. OverbiteFF always uses port 70. 
### For Chromium and Google Chrome, Burrow is available. It redirects gopher:// URLs to a proxy. In the past an Overbite proxy-based extension for these browsers was available but is no longer maintained and does not work with the current (>23) releases.For Konqueror, Kio gopher is available.
## Gopher over HTTP gateways  
### Users of Web browsers that have incomplete or no support for Gopher can access content on Gopher servers via a server gateway or proxy server that converts Gopher menus into HTML; known proxies are the Floodgap Public Gopher proxy and Gopher Proxy. Similarly, certain server packages such as GN and PyGopherd have built-in Gopher to HTTP interfaces. Squid Proxy software gateways any gopher:// URL to HTTP content, enabling any browser or web agent to access gopher content easily.
## Gopher clients for mobile devices  
### Some have suggested that the bandwidth-sparing simple interface of Gopher would be a good match for mobile phones and personal digital assistants (PDAs), but so far, mobile adaptations of HTML and XML and other simplified content have proven more popular. The PyGopherd server provides a built-in WML front-end to Gopher sites served with it. 
### The early 2010s saw a renewed interest in native Gopher clients for popular smartphones: Overbite, an open source client for Android 1.5+ was released in alpha stage in 2010. PocketGopher was also released in 2010, along with its source code, for several Java ME compatible devices. Gopher Client was released in 2016 as a proprietary client for iPhone and iPad devices and is currently maintained.
## Other Gopher clients  
### Gopher popularity was at its height at a time when there were still many equally competing computer architectures and operating systems. As a result, there are several Gopher clients available for Acorn RISC OS, AmigaOS, Atari MiNT, CMS, DOS, classic Mac OS, MVS, NeXT, OS/2 Warp, most UNIX-like operating systems, VMS, Windows 3.x, and Windows 9x. GopherVR was a client designed for 3D visualization, and there is even a Gopher client in MOO. The majority of these clients are hard-coded to work on TCP port 70.
## Server software  
### Because the protocol is trivial to implement in a basic fashion, there are many server packages still available, and some are still maintained.
## See also 
## References 
## External links  
### List of public Gopher servers (Gopher link) (proxied link) 
### An announcement of Gopher on the Usenet 8 October 1991 
### Why is Gopher Still Relevant? \u2014 a position statement on Gopher's survival 
### The Web may have won, but Gopher tunnels on \u2014 an article published by the technology discussion site Ars Technica about the Gopher community of enthusiasts as of 5 November 2009 
### History of Gopher \u2014 Article in MinnPost 
### Gopherpedia \u2014 Gopher interface for Wikipedia (Gopher link) (proxied link, by another proxy) 
### Mark McCahill and Farhad Anklesaria \u2013 gopher inventors \u2013 explain the evolution of gopher: part 1, part 2 
### Proposed Gopher+ Specification (gopher link)"
## References
### [Reference](http:gopher://gopher.floodgap.com/0/gopher/tech/gopherplus.txt) - http:gopher://gopher.floodgap.com/0/gopher/tech/gopherplus.txt
### [Reference](http:gopher://gopher.floodgap.com/1/buck/) - http:gopher://gopher.floodgap.com/1/buck/
### [Reference](http:gopher://gopher.floodgap.com/1/world) - http:gopher://gopher.floodgap.com/1/world
### [Reference](http:gopher://gopherpedia.com/1) - http:gopher://gopherpedia.com/1
### [Reference](http:gopher://gopher.r-36.net/1/scm/geomyidae) - http:gopher://gopher.r-36.net/1/scm/geomyidae
### [Reference](http:gopher://gopher.r-36.net/1/scm/gopherfs) - http:gopher://gopher.r-36.net/1/scm/gopherfs
### [Reference](http://www.chronicle.com/article/How-Gopher-Nearly-Won-the/237682?cid=wc&elqTrackId=efb09ffa986845e1ac578b879a71c12d&elq=79b4d513152c4e8c8f1c4e70634b60c9&elqaid=10545&elqat=1&elqCampaignId=3974) - http://www.chronicle.com/article/How-Gopher-Nearly-Won-the/237682?cid=wc&elqTrackId=efb09ffa986845e1ac578b879a71c12d&elq=79b4d513152c4e8c8f1c4e70634b60c9&elqaid=10545&elqat=1&elqCampaignId=3974
### [Reference](http://gopher.floodgap.com/1/new) - http://gopher.floodgap.com/1/new
### [Reference](http://gopher.floodgap.com/gopher/gw?a=gopher://gopher.floodgap.com/1/world) - http://gopher.floodgap.com/gopher/gw?a=gopher://gopher.floodgap.com/1/world
### [Reference](http://gopher.floodgap.com/gopher/gw?a=gopher://gopher.floodgap.com/1/buck) - http://gopher.floodgap.com/gopher/gw?a=gopher://gopher.floodgap.com/1/buck
### [Reference](http://gopher.floodgap.com/gopher/gw?a=gopher://gopher.r-36.net/1/scm/geomyidae) - http://gopher.floodgap.com/gopher/gw?a=gopher://gopher.r-36.net/1/scm/geomyidae
### [Reference](http://gopher.floodgap.com/gopher/gw?gopher/0/v2/vstat) - http://gopher.floodgap.com/gopher/gw?gopher/0/v2/vstat
### [Reference](http://gopher.floodgap.com/overbite/) - http://gopher.floodgap.com/overbite/
### [Reference](http://gopher.floodgap.com/overbite/relevance.html) - http://gopher.floodgap.com/overbite/relevance.html
### [Reference](http://www.gophersports.com/) - http://www.gophersports.com/
### [Reference](http://www.jaruzel.com/gopher/gopher-client-browser-for-windows) - http://www.jaruzel.com/gopher/gopher-client-browser-for-windows
### [Reference](http://msdn2.microsoft.com/en-us/ie/aa740486.aspx) - http://msdn2.microsoft.com/en-us/ie/aa740486.aspx
### [Reference](http://blog.omnigroup.com/2009/04/01/for-immediate-release-omniweb-592-now-includes-gopher-support/) - http://blog.omnigroup.com/2009/04/01/for-immediate-release-omniweb-592-now-includes-gopher-support/
### [Reference](http://www.omnigroup.com/applications/omniweb/releasenotes/) - http://www.omnigroup.com/applications/omniweb/releasenotes/
### [Reference](http://prentissriddle.com/trips/gophercon1993.html) - http://prentissriddle.com/trips/gophercon1993.html
### [Reference](http://gp.ratthing.com/gopherpedia.com) - http://gp.ratthing.com/gopherpedia.com
### [Reference](http://db.tidbits.com/article/8909) - http://db.tidbits.com/article/8909
### [Reference](http://archive.wikiwix.com/cache/20110723002553/http://changelog.complete.org/archives/1466-download-a-piece-of-internet-history) - http://archive.wikiwix.com/cache/20110723002553/http://changelog.complete.org/archives/1466-download-a-piece-of-internet-history
### [Reference](http://archive.wikiwix.com/cache/20110814030727/http://blog.omnigroup.com/2009/04/01/for-immediate-release-omniweb-592-now-includes-gopher-support/) - http://archive.wikiwix.com/cache/20110814030727/http://blog.omnigroup.com/2009/04/01/for-immediate-release-omniweb-592-now-includes-gopher-support/
### [Reference](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.198.5779) - http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.198.5779
### [Reference](http://mediamill.cla.umn.edu/mediamill/display/69597) - http://mediamill.cla.umn.edu/mediamill/display/69597
### [Reference](http://www.funet.fi/pub/vms/networking/gopher/gopher-software-licensing-policy.ancient) - http://www.funet.fi/pub/vms/networking/gopher/gopher-software-licensing-policy.ancient
### [Reference](http://aftershock.sourceforge.net/) - http://aftershock.sourceforge.net/
### [Reference](http://gofish.sourceforge.net/) - http://gofish.sourceforge.net/
### [Reference](http://gopherus.sourceforge.net/) - http://gopherus.sourceforge.net/
### [Reference](http://motsognir.sourceforge.net/) - http://motsognir.sourceforge.net/
### [Reference](http://changelog.complete.org/archives/1466-download-a-piece-of-internet-history) - http://changelog.complete.org/archives/1466-download-a-piece-of-internet-history
### [Reference](http://permalink.gmane.org/gmane.network.gopher.general/1814) - http://permalink.gmane.org/gmane.network.gopher.general/1814
### [Reference](http://permalink.gmane.org/gmane.network.gopher.general/2571) - http://permalink.gmane.org/gmane.network.gopher.general/2571
### [Reference](http://gophernicus.org/) - http://gophernicus.org/
### [Reference](http://userbase.kde.org/Kio_gopher) - http://userbase.kde.org/Kio_gopher
### [Reference](http://linuxfromscratch.org/pipermail/elinks-users/2004-December/000785.html) - http://linuxfromscratch.org/pipermail/elinks-users/2004-December/000785.html
### [Reference](http://gopher.quux.org/) - http://gopher.quux.org/
### [Reference](http://gopher.quux.org/Archives/Mailing%20Lists/gopher/gopher.2002-02) - http://gopher.quux.org/Archives/Mailing%20Lists/gopher/gopher.2002-02
### [Reference](http://gophrier.tuxfamily.org/) - http://gophrier.tuxfamily.org/
### [Reference](https://itunes.apple.com/us/app/gopher-client/id1235310088) - https://itunes.apple.com/us/app/gopher-client/id1235310088
### [Reference](https://arstechnica.com/open-source/news/2010/07/overbite-project-brings-gopher-protocol-to-android.ars) - https://arstechnica.com/open-source/news/2010/07/overbite-project-brings-gopher-protocol-to-android.ars
### [Reference](https://arstechnica.com/tech-policy/news/2009/11/the-web-may-have-won-but-gopher-tunnels-on.ars) - https://arstechnica.com/tech-policy/news/2009/11/the-web-may-have-won-but-gopher-tunnels-on.ars
### [Reference](https://sunriseprogrammer.blogspot.com/2019/03/directory-entry-says-what-current.html) - https://sunriseprogrammer.blogspot.com/2019/03/directory-entry-says-what-current.html
### [Reference](https://gopher.floodgap.com/gopher/gw?gopher/1/new) - https://gopher.floodgap.com/gopher/gw?gopher/1/new
### [Reference](https://gopher.floodgap.com/gopher/gw?gopher://gopherpedia.com/1) - https://gopher.floodgap.com/gopher/gw?gopher://gopherpedia.com/1
### [Reference](https://github.com/arcfide/goscher) - https://github.com/arcfide/goscher
### [Reference](https://github.com/crcx/atua) - https://github.com/crcx/atua
### [Reference](https://github.com/dotcomboom/Pituophis) - https://github.com/dotcomboom/Pituophis
### [Reference](https://github.com/heddwch/geomyid) - https://github.com/heddwch/geomyid
### [Reference](https://github.com/jgoerzen/pygopherd/blob/master/doc/standards/Gopher+.txt) - https://github.com/jgoerzen/pygopherd/blob/master/doc/standards/Gopher+.txt
### [Reference](https://github.com/michael-lazar/flask-gopher) - https://github.com/michael-lazar/flask-gopher
### [Reference](https://github.com/rkd77/elinks/issues/102) - https://github.com/rkd77/elinks/issues/102
### [Reference](https://github.com/skyjake/lagrange) - https://github.com/skyjake/lagrange
### [Reference](https://github.com/sternenseemann/spacecookie) - https://github.com/sternenseemann/spacecookie
### [Reference](https://gitlab.com/SSS8555/acid/-/blob/master/README.md) - https://gitlab.com/SSS8555/acid/-/blob/master/README.md
### [Reference](https://gitlab.com/SSS8555/save_gopher_server) - https://gitlab.com/SSS8555/save_gopher_server
### [Reference](https://gitlab.com/leveck/xylophar) - https://gitlab.com/leveck/xylophar
### [Reference](https://books.google.com/books?id=A1UoH2vGKE8C&pg=PA69) - https://books.google.com/books?id=A1UoH2vGKE8C&pg=PA69
### [Reference](https://chrome.google.com/webstore/detail/burrow-gopherspace-explor/plhaaggiajlcjclagmjnjmaonhkdhhji) - https://chrome.google.com/webstore/detail/burrow-gopherspace-explor/plhaaggiajlcjclagmjnjmaonhkdhhji
### [Reference](https://code.google.com/p/chromium/issues/detail?id=11345) - https://code.google.com/p/chromium/issues/detail?id=11345
### [Reference](https://groups.google.com/d/msg/comp.infosystems.gopher/4A-LS_A6qtA/nT89yWKzzsIJ) - https://groups.google.com/d/msg/comp.infosystems.gopher/4A-LS_A6qtA/nT89yWKzzsIJ
### [Reference](https://groups.google.com/group/bit.listserv.cwis-l/browse_frm/thread/11db689fbe802834/bc8a60ab89926a4b?lnk=st&q=cwis+gopher&rnum=482&hl=en#bc8a60ab89926a4b) - https://groups.google.com/group/bit.listserv.cwis-l/browse_frm/thread/11db689fbe802834/bc8a60ab89926a4b?lnk=st&q=cwis+gopher&rnum=482&hl=en#bc8a60ab89926a4b
### [Reference](https://groups.google.com/group/comp.sys.mac.announce/msg/24ad9de8dcfd6e4b) - https://groups.google.com/group/comp.sys.mac.announce/msg/24ad9de8dcfd6e4b
### [Reference](https://groups.google.com/groups?selm=1mj6cb$6gm@pith.uoregon.edu) - https://groups.google.com/groups?selm=1mj6cb$6gm@pith.uoregon.edu
### [Reference](https://groups.google.com/groups?selm=36e4c2f1.10244576@nntp.best.ix.netcom.com) - https://groups.google.com/groups?selm=36e4c2f1.10244576@nntp.best.ix.netcom.com
### [Reference](https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2002/ms02-047) - https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2002/ms02-047
### [Reference](https://www.minnpost.com/business/2016/08/rise-and-fall-gopher-protocol) - https://www.minnpost.com/business/2016/08/rise-and-fall-gopher-protocol
### [Reference](https://www.newscientist.com/blogs/shortsharpscience/2009/03/how-moores-law-saved-the-web.html) - https://www.newscientist.com/blogs/shortsharpscience/2009/03/how-moores-law-saved-the-web.html
### [Reference](https://www.wired.com/news/technology/0,1282,62988,00.html) - https://www.wired.com/news/technology/0,1282,62988,00.html
### [Reference](https://www.youtube.com/watch?v=RObkISaq8wc) - https://www.youtube.com/watch?v=RObkISaq8wc
### [Reference](https://www.youtube.com/watch?v=dNY9RscP-lI) - https://www.youtube.com/watch?v=dNY9RscP-lI
### [Reference](https://math.albany.edu/g/Adm/goph-www.html#1.2) - https://math.albany.edu/g/Adm/goph-www.html#1.2
### [Reference](https://kb.iu.edu/d/aawk) - https://kb.iu.edu/d/aawk
### [Reference](https://id.loc.gov/authorities/subjects/sh95000820) - https://id.loc.gov/authorities/subjects/sh95000820
### [Reference](https://d-nb.info/gnd/4372140-0) - https://d-nb.info/gnd/4372140-0
### [Reference](https://redis.io/topics/gopher) - https://redis.io/topics/gopher
### [Reference](https://port70.net/?1mgod) - https://port70.net/?1mgod
### [Reference](https://kristall.random-projects.net/) - https://kristall.random-projects.net/
### [Reference](https://archive.org/details/hackingcapitalis00sder_520) - https://archive.org/details/hackingcapitalis00sder_520
### [Reference](https://archive.org/details/hackingcapitalis00sder_520/page/n33) - https://archive.org/details/hackingcapitalis00sder_520/page/n33
### [Reference](https://archive.org/details/worldwidewebunle00dece/page/20) - https://archive.org/details/worldwidewebunle00dece/page/20
### [Reference](https://web.archive.org/web/20070220130659/http://linuxfromscratch.org/pipermail/elinks-users/2004-December/000785.html) - https://web.archive.org/web/20070220130659/http://linuxfromscratch.org/pipermail/elinks-users/2004-December/000785.html
### [Reference](https://web.archive.org/web/20081012175802/http://wired.com/news/technology/0,1282,62988,00.html) - https://web.archive.org/web/20081012175802/http://wired.com/news/technology/0,1282,62988,00.html
### [Reference](https://web.archive.org/web/20100814175230/http://www.gophersports.com/) - https://web.archive.org/web/20100814175230/http://www.gophersports.com/
### [Reference](https://web.archive.org/web/20110704230831/http://www.microsoft.com/technet/security/Bulletin/MS02-047.mspx) - https://web.archive.org/web/20110704230831/http://www.microsoft.com/technet/security/Bulletin/MS02-047.mspx
### [Reference](https://web.archive.org/web/20110720093228/http://mediamill.cla.umn.edu/mediamill/display/69597) - https://web.archive.org/web/20110720093228/http://mediamill.cla.umn.edu/mediamill/display/69597
### [Reference](https://web.archive.org/web/20110804042206/http://msdn.microsoft.com/en-us/ie/aa740486.aspx) - https://web.archive.org/web/20110804042206/http://msdn.microsoft.com/en-us/ie/aa740486.aspx
### [Reference](https://web.archive.org/web/20110804183515/http://gopher.floodgap.com/1/new) - https://web.archive.org/web/20110804183515/http://gopher.floodgap.com/1/new
### [Reference](https://web.archive.org/web/20110807064232/http://www.omnigroup.com/products/omniweb/download/releasenotes/) - https://web.archive.org/web/20110807064232/http://www.omnigroup.com/products/omniweb/download/releasenotes/
### [Reference](https://web.archive.org/web/20110831183201/http://www.newscientist.com/blogs/shortsharpscience/2009/03/how-moores-law-saved-the-web.html) - https://web.archive.org/web/20110831183201/http://www.newscientist.com/blogs/shortsharpscience/2009/03/how-moores-law-saved-the-web.html
### [Reference](https://web.archive.org/web/20150310110252/http://permalink.gmane.org/gmane.network.gopher.general/1814) - https://web.archive.org/web/20150310110252/http://permalink.gmane.org/gmane.network.gopher.general/1814
### [Reference](https://web.archive.org/web/20150310110257/http://permalink.gmane.org/gmane.network.gopher.general/2571) - https://web.archive.org/web/20150310110257/http://permalink.gmane.org/gmane.network.gopher.general/2571
### [Reference](https://web.archive.org/web/20180501125030/https://userbase.kde.org/Kio_gopher) - https://web.archive.org/web/20180501125030/https://userbase.kde.org/Kio_gopher
### [Reference](https://web.archive.org/web/20190421225505/https://curl.haxx.se/mail/lib-2010-08/0346.html) - https://web.archive.org/web/20190421225505/https://curl.haxx.se/mail/lib-2010-08/0346.html
### [Reference](https://gophie.org/) - https://gophie.org/
### [Reference](https://datatracker.ietf.org/doc/html/rfc1436) - https://datatracker.ietf.org/doc/html/rfc1436
### [Reference](https://datatracker.ietf.org/doc/html/rfc4266) - https://datatracker.ietf.org/doc/html/rfc4266
### [Reference](https://userbase.kde.org/Kio_gopher) - https://userbase.kde.org/Kio_gopher
### [Reference](https://metacpan.org/pod/Apache::GopherHandler) - https://metacpan.org/pod/Apache::GopherHandler
### [Reference](https://metacpan.org/release/Gopher-Server) - https://metacpan.org/release/Gopher-Server
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=388195) - https://bugzilla.mozilla.org/show_bug.cgi?id=388195
### [Reference](https://www.rfc-editor.org/rfc/rfc4266.html) - https://www.rfc-editor.org/rfc/rfc4266.html
### [Reference](https://www.wikidata.org/wiki/Q322654#identifiers) - https://www.wikidata.org/wiki/Q322654#identifiers
### [Reference](https://curl.haxx.se/mail/lib-2010-08/0346.html) - https://curl.haxx.se/mail/lib-2010-08/0346.html
### [Reference](https://twit.tv/shows/triangulation/episodes/264/) - https://twit.tv/shows/triangulation/episodes/264/
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/f/f9/Crystal_Clear_app_linneighborhood.svg) - https://upload.wikimedia.org/wikipedia/commons/f/f9/Crystal_Clear_app_linneighborhood.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/1/15/Gopher_in_Firefox_1.5.png) - https://upload.wikimedia.org/wikipedia/commons/1/15/Gopher_in_Firefox_1.5.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/3e/Kristall.png) - https://upload.wikimedia.org/wikipedia/commons/3/3e/Kristall.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/1/1c/Wiki_letter_w_cropped.svg) - https://upload.wikimedia.org/wikipedia/commons/1/1c/Wiki_letter_w_cropped.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg