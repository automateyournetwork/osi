# Internet Relay Chat
## [URL](https://en.wikipedia.org/wiki/Internet_Relay_Chat) - https://en.wikipedia.org/wiki/Internet_Relay_Chat
## Catagories
### 1988 software
### All articles containing potentially dated statements
### All articles covered by WikiProject Wikify
### All articles with failed verification
### All articles with unsourced statements
### All pages needing cleanup
### Application layer protocols
### Articles containing potentially dated statements from 2016
### Articles containing potentially dated statements from 2019
### Articles containing potentially dated statements from January 2022
### Articles containing potentially dated statements from June 2021
### Articles covered by WikiProject Wikify from October 2021
### Articles with Curlie links
### Articles with failed verification from January 2022
### Articles with short description
### Articles with unsourced statements from April 2011
### Articles with unsourced statements from August 2009
### Articles with unsourced statements from January 2010
### Articles with unsourced statements from January 2015
### Articles with unsourced statements from July 2007
### Articles with unsourced statements from May 2009
### Articles with unsourced statements from October 2008
### CS1 German-language sources (de)
### CS1 errors: missing periodical
### CS1 maint: url-status
### Commons category link is on Wikidata
### Computer-related introductions in 1988
### Finnish inventions
### Internet Relay Chat
### Internet terminology
### Short description matches Wikidata
### Virtual communities
### Wikipedia articles needing clarification from July 2009
### Wikipedia introduction cleanup from October 2021
### "Internet Relay Chat (IRC) is a text-based chat (instant messaging) system.  IRC is designed for group communication in discussion forums, called channels, but also allows one-on-one communication via private messages as well as chat and data transfer, including file sharing.Internet Relay Chat is implemented as an application layer protocol to facilitate communication in the form of text. The chat process works on a client\u2013server networking model. Users connect to an IRC server, which may be part of a larger IRC network. Users connect using a client, which may be a web app, a standalone desktop program, or embedded into part of a larger program. Examples of programs used to connect include Mibbit, IRCCloud, KiwiIRC, and MIRC. 
### IRC usage has been declining steadily since 2003, losing 60 percent of its users.  In April 2011, the top 100 IRC networks served more than half a million users at a time.   As of June 2021, there are 481 different IRC networks known to be operating, of which the open source Libera Chat, founded in May 2021, has the most users, with 20,374 channels on 26 servers; between them, the top 100 IRC networks share over 100 thousand channels operating on about one thousand servers.
## History  

### IRC was created by Jarkko Oikarinen in August 1988 to replace a program called MUT (MultiUser Talk) on a BBS called OuluBox at the University of Oulu in Finland, where he was working at the Department of Information Processing Science. Jarkko intended to extend the BBS software he administered, to allow news in the Usenet style, real time discussions and similar BBS features. The first part he implemented was the chat part, which he did with borrowed parts written by his friends Jyrki Kuoppala and Jukka Pihl. The first IRC network was running on a single server named tolsun.oulu.fi. Oikarinen found inspiration in a chat system known as Bitnet Relay, which operated on the BITNET.Jyrki Kuoppala pushed Oikarinen to ask Oulu University to free the IRC code so that it also could be run outside of Oulu, and after they finally got it released, Jyrki Kuoppala immediately installed another server. This was the first \"IRC network\".  Oikarinen got some friends at the Helsinki University and Tampere University to start running IRC servers when his number of users increased and other universities soon followed. At this time Oikarinen realized that the rest of the BBS features probably wouldn't fit in his program.Oikarinen got in touch with people at the University of Denver and Oregon State University. They had their own IRC network running and wanted to connect to the Finnish network. They had obtained the program from one of Oikarinen's friends, Vijay Subramaniam\u2014the first non-Finnish person to use IRC. IRC then grew larger and got used on the entire Finnish national network\u2014FUNET\u2014and then connected to Nordunet, the Scandinavian branch of the Internet. In November 1988, IRC had spread across the Internet and in the middle of 1989, there were some 40 servers worldwide.
## EFnet  
### In August 1990, the first major disagreement took place in the IRC world. The \"A-net\" (Anarchy net) included a server named eris.berkeley.edu. It was all open, required no passwords and had no limit on the number of connects. As Greg \"wumpus\" Lindahl explains: \"it had a wildcard server line, so people were hooking up servers and nick-colliding everyone\". The \"Eris Free Network\", EFnet, made the eris machine the first to be Q-lined (Q for quarantine) from IRC. In wumpus' words again: \"Eris refused to remove that line, so I formed EFnet. It wasn't much of a fight; I got all the hubs to join, and almost everyone else got carried along.\" A-net was formed with the eris servers, while EFnet was formed with the non-eris servers. History showed most servers and users went with EFnet. Once A-net disbanded, the name EFnet became meaningless, and once again it was the one and only IRC network.Around that time IRC was used to report on the 1991 Soviet coup d'\u00e9tat attempt throughout a media blackout. It was previously used in a similar fashion during the Gulf War. Chat logs of these and other events are kept in the ibiblio archive.
## Undernet fork  
### Another fork effort, the first that made a lasting difference, was initiated by \"Wildthang\" in the United States in October 1992. (It forked off the EFnet ircd version 2.8.10). It was meant to be just a test network to develop bots on but it quickly grew to a network \"for friends and their friends\". In Europe and Canada a separate new network was being worked on and in December the French servers connected to the Canadian ones, and by the end of the month, the French and Canadian network was connected to the US one, forming the network that later came to be called \"The Undernet\".The \"undernetters\" wanted to take ircd further in an attempt to make it less bandwidth consumptive and to try to sort out the channel chaos (netsplits and takeovers) that EFnet started to suffer from. For the latter purpose, the Undernet implemented timestamps, new routing and offered the CService\u2014a program that allowed users to register channels and then attempted to protect them from troublemakers. The first server list presented, from 15 February 1993, includes servers from the U.S., Canada, France, Croatia and Japan. On 15 August, the new user count record was set to 57 users.In May 1993, RFC 1459 was published and details a simple protocol for client/server operation, channels, one-to-one and one-to-many conversations.  It is notable that a significant number of extensions like CTCP, colors and formats are not included in the protocol specifications, nor is character encoding, which led various implementations of servers and clients to diverge. Software implementation varied significantly from one network to the other, each network implementing their own policies and standards in their own code bases.
## DALnet fork  
### During the summer of 1994, the Undernet was itself forked. The new network was called DALnet (named after its founder: dalvenjah), formed for better user service and more user and channel protections. One of the more significant changes in DALnet was use of longer nicknames (the original ircd limit being 9 letters). DALnet ircd modifications were made by Alexei \"Lefler\" Kosut. DALnet was thus based on the Undernet ircd server, although the DALnet pioneers were EFnet abandoners. According to James Ng, the initial DALnet people were \"ops in #StarTrek sick from the constant splits/lags/takeovers/etc\".DALnet quickly offered global WallOps (IRCop messages that can be seen by users who are +w (/mode NickName +w)), longer nicknames, Q:Lined nicknames (nicknames that cannot be used i.e. ChanServ, IRCop, NickServ, etc.), global K:Lines (ban of one person or an entire domain from a server or the entire network), IRCop only communications: GlobOps, +H mode showing that an IRCop is a \"helpop\" etc. Much of DALnet's new functions were written in early 1995 by Brian \"Morpher\" Smith and allow users to own nicknames, control channels, send memos, and more.
## IRCnet fork  
### In July 1996, after months of flame wars and discussions on the mailing list, there was yet another split due to disagreement in how the development of the ircd should evolve. Most notably, the \"European\" (most of those servers were in Europe) side that later named itself IRCnet argued for nick and channel delays whereas the EFnet side argued for timestamps. There were also disagreements about policies: the European side had started to establish a set of rules directing what IRCops could and could not do, a point of view opposed by the US side.Most (not all) of the IRCnet servers were in Europe, while most of the EFnet servers were in the US. This event is also known as \"The Great Split\" in many IRC societies. EFnet has since (as of August 1998) grown and passed the number of users it had then. In the (northern) autumn of the year 2000, EFnet had some 50,000 users and IRCnet 70,000.
## Modern IRC  
### IRC has changed much over its life on the Internet. New server software has added a multitude of new features. 

### Services: Network-operated bots to facilitate registration of nicknames and channels, sending messages for offline users and network operator functions. 
### Extra modes: While the original IRC system used a set of standard user and channel modes, new servers add many new modes for features such as removing color codes from text, or obscuring a user's hostmask (\"cloaking\") to protect from denial-of-service attacks. 
### Proxy detection: Most modern servers support detection of users attempting to connect through an insecure (misconfigured or exploited) proxy server, which can then be denied a connection. This proxy detection software is used by several networks, although that real time list of proxies is defunct since early 2006. 
### Additional commands: New commands can be such things as shorthand commands to issue commands to Services, to network-operator-only commands to manipulate a user's hostmask. 
### Encryption: For the client-to-server leg of the connection TLS might be used (messages cease to be secure once they are relayed to other users on standard connections, but it makes eavesdropping on or wiretapping an individual's IRC sessions difficult). For client-to-client communication, SDCC (Secure DCC) can be used. 
### Connection protocol: IRC can be connected to via IPv4, the old version of the Internet Protocol, or by IPv6, the current standard of the protocol.As of 2016, a new standardization effort is under way under a working group called IRCv3, which focuses on more advanced client features like instant notifications, better history support and improved security. As of 2019, no major IRC networks have fully adopted the proposed standard.After its golden era during the 1990s and early 2000s (240,000 users on QuakeNet in 2004), IRC has seen a significant decline, losing around 60% of users between 2003 and 2012, with users moving to newer social media platforms like Facebook or Twitter, but also to open platforms like XMPP which was developed in 1999. Certain networks like Freenode have not followed the overall trend and have more than quadrupled in size during the same period. However, Freenode, which in 2016 had around 90,000 users, has since declined to about 9,300 users.The largest IRC networks have traditionally been grouped as the \"Big Four\"\u2014a designation for networks that top the statistics. The Big Four networks change periodically, but due to the community nature of IRC there are a large number of other networks for users to choose from. 
### Historically the \"Big Four\" were: 
### EFnet 
### IRCnet 
### Undernet 
### DALnetIRC reached 6 million simultaneous users in 2001 and 10 million users in 2003, dropping to 371k in 2018.As of January 2022, the largest IRC networks are: 

### Libera Chat \u2013 around 48.7k users at peak hours 
### OFTC \u2013 around 19.4k users at peak hours 
### IRCnet \u2013 around 17.9k users at peak hours 
### Undernet \u2013 around 13.4k users at peak hours 
### Rizon \u2013 around 10.5k users at peak hours 
### EFnet \u2013 around 10.4k users at peak hours 
### Freenode \u2013 around 9.3k users at peak hours 
### QuakeNet \u2013 around 8.4k users at peak hours 
### DALnet \u2013 around 7.9k users at peak hoursThe top 100 IRC networks have around 228k users connected at peak hours.
## Timeline  
### Timeline of major servers: 

### EFnet, 1990 to present 
### Undernet, 1992 to present 
### DALnet, 1994 to present 
### freenode, 1995 to 2021 
### IRCnet, 1996 to present 
### QuakeNet, 1997 to present 
### Open and Free Technology Community, 2001 to present 
### Rizon, 2002 to present 
### Libera Chat, 2021 to present
## Technical information  

### IRC is an open protocol that uses TCP and, optionally, TLS. An IRC server can connect to other IRC servers to expand the IRC network. Users access IRC networks by connecting a client to a server. There are many client implementations, such as mIRC, HexChat and irssi, and server implementations, e.g. the original IRCd. Most IRC servers do not require users to register an account but a nick is required before being connected.IRC was originally a plain text protocol (although later extended), which on request was assigned port 194/TCP by IANA. However, the de facto standard has always been to run IRC on 6667/TCP and nearby port numbers (for example TCP ports 6660\u20136669, 7000) to avoid having to run the IRCd software with root privileges. 
### The protocol specified that characters were 8-bit but did not specify the character encoding the text was supposed to use. This can cause problems when users using different clients and/or different platforms want to converse. 
### All client-to-server IRC protocols in use today are descended from the protocol implemented in the irc2.4.0 version of the IRC2 server, and documented in RFC 1459. Since RFC 1459 was published, the new features in the irc2.10 implementation led to the publication of several revised protocol documents (RFC 2810, RFC 2811, RFC 2812 and RFC 2813); however, these protocol changes have not been widely adopted among other implementations.Although many specifications on the IRC protocol have been published, there is no official specification, as the protocol remains dynamic. Virtually no clients and very few servers rely strictly on the above RFCs as a reference.Microsoft made an extension for IRC in 1998 via the proprietary IRCX. They later stopped distributing software supporting IRCX, instead developing the proprietary MSNP. 
### The standard structure of a network of IRC servers is a tree. Messages are routed along only necessary branches of the tree but network state is sent to every server and there is generally a high degree of implicit trust between servers. However, this architecture has a number of problems. A misbehaving or malicious server can cause major damage to the network and any changes in structure, whether intentional or a result of conditions on the underlying network, require a net-split and net-join. This results in a lot of network traffic and spurious quit/join messages to users and temporary loss of communication to users on the splitting servers. Adding a server to a large network means a large background bandwidth load on the network and a large memory load on the server. Once established, however, each message to multiple recipients is delivered in a fashion similar to multicast, meaning each message travels a network link exactly once. This is a strength in comparison to non-multicasting protocols such as Simple Mail Transfer Protocol (SMTP) or Extensible Messaging and Presence Protocol (XMPP). 
### An IRC daemon can also be used on a local area network (LAN). IRC can thus be used to facilitate communication between people within the local area network (internal communication).
## Commands and replies  

### IRC has a line-based structure. Clients send single-line messages to the server, receive replies to those messages and receive copies of some messages sent by other clients. In most clients, users can enter commands by prefixing them with a '/'. Depending on the command, these may either be handled entirely by the client, or (generally for commands the client does not recognize) passed directly to the server, possibly with some modification.Due to the nature of the protocol, automated systems cannot always correctly pair a sent command with its reply with full reliability and are subject to guessing.
## Channels  
### The basic means of communicating to a group of users in an established IRC session is through a channel. Channels on a network can be displayed using the IRC command LIST, which lists all currently available channels that do not have the modes +s or +p set, on that particular network. 
### Users can join a channel using the JOIN command, in most clients available as /join #channelname. Messages sent to the joined channels are then relayed to all other users.Channels that are available across an entire IRC network are prefixed with a '#', while those local to a server use '&'. Other less common channel types include '+' channels\u2014'modeless' channels without operators\u2014and '!' channels, a form of timestamped channel on normally non-timestamped networks.
## Modes  
### Users and channels may have modes that are represented by single case-sensitive letters and are set using the MODE command. User modes and channel modes are separate and can use the same letter to mean different things (e.g. user mode \"i\" is invisible mode while channel mode \"i\" is invite only.) Modes are usually set and unset using the mode command that takes a target (user or channel), a set of modes to set (+) or unset (-) and any parameters the modes need. 
### Some channel modes take parameters and other channel modes apply to a user on a channel or add or remove a mask (e.g. a ban mask) from a list associated with the channel rather than applying to the channel as a whole. Modes that apply to users on a channel have an associated symbol that is used to represent the mode in names replies (sent to clients on first joining a channel and use of the names command) and in many clients also used to represent it in the client's displayed list of users in a channel or to display an own indicator for a user's modes. 
### In order to correctly parse incoming mode messages and track channel state the client must know which mode is of which type and for the modes that apply to a user on a channel which symbol goes with which letter. In early implementations of IRC this had to be hard-coded in the client but there is now a de facto standard extension to the protocol called ISUPPORT that sends this information to the client at connect time using numeric 005.There is a small design fault in IRC regarding modes that apply to users on channels: the names message used to establish initial channel state can only send one such mode per user on the channel, but multiple such modes can be set on a single user. For example, if a user holds both operator status (+o) and voice status (+v) on a channel, a new client will be unable to see the mode with less priority (i.e. voice). Workarounds for this are possible on both the client and server side but none are widely implemented.
## Standard (RFC 1459) modes  
### Many daemons and networks have added extra modes or modified the behavior of modes in the above list.
## Channel operators  
### A channel operator is a client on an IRC channel that manages the channel. 
### IRC channel operators can be easily seen by the a symbol or icon next to their name (varies by client implementation, commonly a \"@\" symbol prefix, a green circle, or a Latin letter \"+o\"/\"o\"). 
### On most networks, an operator can: 

### Kick a user. 
### Ban a user. 
### Give another user IRC Channel Operator Status or IRC Channel Voice Status. 
### Change the IRC Channel topic while channel mode +t is set. 
### Change the IRC Channel Mode locks.
## IRC operators  

### There are also users who maintain elevated rights on their local server, or the entire network; these are called IRC operators, sometimes shortened to IRCops or Opers (not to be confused with channel operators). As the implementation of the IRCd varies, so do the privileges of the IRC operator on the given IRCd. RFC 1459 claims that IRC operators are \"a necessary evil\" to keep a clean state of the network, and as such they need to be able to disconnect and reconnect servers. Additionally, to prevent malicious users or even harmful automated programs from entering IRC, IRC operators are usually allowed to disconnect clients and completely ban IP addresses or complete subnets. Networks that carry services (NickServ et al.) usually allow their IRC operators also to handle basic \"ownership\" matters. Further privileged rights may include overriding channel bans (being able to join channels they would not be allowed to join, if they were not opered), being able to op themselves on channels where they would not be able without being opered, being auto-opped on channels always and so forth.
## Hostmasks  
### A hostmask is a unique identifier of an IRC client connected to an IRC server. IRC servers, services, and other clients, including bots, can use it to identify a specific IRC session. 
### The format of a hostmask is nick!user@host.  The hostmask looks similar to, but should not be confused with an e-mail address. 
### The nick part is the nickname chosen by the user and may be changed while connected. 
### The user part is the username reported by ident on the client. If ident is not available on the client, the username specified when the client connected is used after being prefixed with a tilde.The host part is the hostname the client is connecting from. If the IP address of the client cannot be resolved to a valid hostname by the server, it is used instead of the hostname. 
### Because of the privacy implications of exposing the IP address or hostname of a client, some IRC daemons also provide privacy features, such as InspIRCd or UnrealIRCd's \"+x\" mode. This hashes a client IP address or masks part of a client's hostname, making it unreadable to users other than IRCops. Users may also have the option of requesting a \"virtual host\" (or \"vhost\"), to be displayed in the hostmask to allow further anonymity. Some IRC networks, such as Libera Chat or Freenode, use these as \"cloaks\" to indicate that a user is affiliated with a group or project.
## URI scheme  
### There are three recognized uniform resource identifier (URI) schemes for Internet Relay Chat: irc, ircs, and irc6. When supported, they allow hyperlinks of various forms, including 

### irc://<host>[:<port>]/[<channel>[?<channel_keyword>]] 
### ircs://<host>[:<port>]/[<channel>[?<channel_keyword>]] 
### irc6://<host>[:<port>]/[<channel>[?<channel_keyword>]] 

### (where items enclosed within brackets ([,]) are optional) to be used to (if necessary) connect to the specified host (or network, if known to the IRC client) and join the specified channel. (This can be used within the client itself, or from another application such as a Web browser).  irc is the default URI, irc6 specifies a connection to be made using IPv6, and ircs specifies a secure connection. 
### Per the specification, the usual hash symbol (#) will be prepended to channel names that begin with an alphanumeric character\u2014allowing it to be omitted. Some implementations (for example, mIRC) will do so unconditionally resulting in a (usually unintended) extra (for example, ##channel), if included in the URL. 
### Some implementations allow multiple channels to be specified, separated by commas.
## Challenges  
### Issues in the original design of IRC were the amount of shared state data being a limitation on its scalability, the absence of unique user identifications leading to the nickname collision problem, lack of protection from netsplits by means of cyclic routing, the trade-off in scalability for the sake of real-time user presence information, protocol weaknesses providing a platform for abuse, no transparent and optimizable message passing, and no encryption. Some of these issues have been addressed in Modern IRC.
## Attacks  
### Because IRC connections may be unencrypted and typically span long time periods, they are an attractive target for DoS/DDoS attackers and hackers. Because of this, careful security policy is necessary to ensure that an IRC network is not susceptible to an attack such as a takeover war. IRC networks may also K-line or G-line users or servers that have a harming effect. 
### Some IRC servers support SSL/TLS connections for security purposes. This helps stop the use of packet sniffer programs to obtain the passwords of IRC users, but has little use beyond this scope due to the public nature of IRC channels. SSL connections require both client and server support (that may require the user to install SSL binaries and IRC client specific patches or modules on their computers). Some networks also use SSL for server-to-server connections, and provide a special channel flag (such as +S) to only allow SSL-connected users on the channel, while disallowing operator identification in clear text, to better utilize the advantages that SSL provides.IRC served as an early laboratory for many kinds of Internet attacks, such as using fake ICMP unreachable messages to break TCP-based IRC connections (nuking) to annoy users or facilitate takeovers.
## Abuse prevention  
### One of the most contentious technical issues surrounding IRC implementations, which survives to this day, is the merit of \"Nick/Channel Delay\" vs. \"Timestamp\" protocols. Both methods exist to solve the problem of denial-of-service attacks, but take very different approaches. 
### The problem with the original IRC protocol as implemented was that when two servers split and rejoined, the two sides of the network would simply merge their channels. If a user could join on a \"split\" server, where a channel that existed on the other side of the network was empty, and gain operator status, they would become a channel operator of the \"combined\" channel after the netsplit ended; if a user took a nickname that existed on the other side of the network, the server would kill both users when rejoining (a \"nick collision\"). This was often abused to \"mass-kill\" all users on a channel, thus creating \"opless\" channels where no operators were present to deal with abuse. Apart from causing problems within IRC, this encouraged people to conduct denial-of-service attacks against IRC servers in order to cause netsplits, which they would then abuse. 

### The nick delay (ND) and channel delay (CD) strategies aim to prevent abuse by delaying reconnections and renames. After a user signs off and the nickname becomes available, or a channel ceases to exist because all its users parted (as often happens during a netsplit), the server will not allow any user to use that nickname or join that channel, until a certain period of time (the delay) has passed. The idea behind this is that even if a netsplit occurs, it is useless to an abuser because they cannot take the nickname or gain operator status on a channel, and thus no collision of a nickname or \"merging\" of a channel can occur. To some extent, this inconveniences legitimate users, who might be forced to briefly use a different name after rejoining (appending an underscore is popular). 
### The timestamp protocol is an alternative to nick/channel delays which resolves collisions using timestamped priority. Every nickname and channel on the network is assigned a timestamp \u2013 the date and time when it was created. When a netsplit occurs, two users on each side are free to use the same nickname or channel, but when the two sides are joined, only one can survive. In the case of nicknames, the newer user, according to their TS, is killed; when a channel collides, the members (users on the channel) are merged, but the channel operators on the \"losing\" side of the split lose their channel operator status. 
### TS is a much more complicated protocol than ND/CD, both in design and implementation, and despite having gone through several revisions, some implementations still have problems with \"desyncs\" (where two servers on the same network disagree about the current state of the network), and allowing too much leniency in what was allowed by the \"losing\" side. Under the original TS protocols, for example, there was no protection against users setting bans or other modes in the losing channel that would then be merged when the split rejoined, even though the users who had set those modes lost their channel operator status. Some modern TS-based IRC servers have also incorporated some form of ND and/or CD in addition to timestamping in an attempt to further curb abuse. 
### Most networks today use the timestamping approach. The timestamp versus ND/CD disagreements caused several servers to split away from EFnet and form the newer IRCnet. After the split, EFnet moved to a TS protocol, while IRCnet used ND/CD. 
### In recent versions of the IRCnet ircd, as well as ircds using the TS6 protocol (including Charybdis), ND has been extended/replaced by a mechanism called SAVE. This mechanism assigns every client a UID upon connecting to an IRC server. This ID starts with a number, which is forbidden in nicks (although some ircds, namely IRCnet and InspIRCd, allow clients to switch to their own UID as the nickname). 
### If two clients with the same nickname join from different sides of a netsplit (\"nick collision\"), the first server to see this collision will force both clients to change their nick to their UID, thus saving both clients from being disconnected. On IRCnet, the nickname will also be locked for some time (ND) to prevent both clients from changing back to the original nickname, thus colliding again.
## Clients 
## Client software  

### Client software exists for various operating systems or software packages, as well as web-based or inside games. Many different clients are available for the various operating systems, including Windows, Unix and Linux, macOS and mobile operating systems (such as iOS and Android). On Windows, mIRC is one of the most popular clients.Some programs which are extensible through plug-ins also serve as platforms for IRC clients. For instance, a client called ERC, written entirely in Emacs Lisp, is included in v.22.3 of Emacs. Therefore, any platform that can run Emacs can run ERC. 
### A number of web browsers have built-in IRC clients, such as Opera (version 12.18 and earlier) and the ChatZilla add-on for Mozilla Firefox (for Firefox 56 and earlier; included as a built-in component of SeaMonkey). Web-based clients, such as Mibbit and open source KiwiIRC, can run in most browsers. 
### Games such as War\u00a7ow, Unreal Tournament (up to Unreal Tournament 2004), Uplink, Spring Engine-based games, 0 A.D. and ZDaemon have included IRC.Ustream's chat interface is IRC with custom authentication as well as Twitch's (formerly Justin.tv).
## Bots  

### A typical use of bots in IRC is to provide IRC services or specific functionality within a channel such as to host a chat-based game or provide notifications of external events. However, some IRC bots are used to launch malicious attacks such as denial of service, spamming, or exploitation.
## Bouncer  

### A program that runs as a daemon on a server and functions as a persistent proxy is known as a BNC or bouncer. The purpose is to maintain a connection to an IRC server, acting as a relay between the server and client, or simply to act as a proxy. Should the client lose network connectivity, the BNC may stay connected and archive all traffic for later delivery, allowing the user to resume their IRC session without disrupting their connection to the server.Furthermore, as a way of obtaining a bouncer-like effect, an IRC client (typically text-based, for example Irssi) may be run on an always-on server to which the user connects via ssh. This also allows devices that only have ssh functionality, but no actual IRC client installed themselves, to connect to the IRC, and it allows sharing of IRC sessions.To keep the IRC client from quitting when the ssh connection closes, the client can be run inside a terminal multiplexer such as GNU Screen or tmux, thus staying connected to the IRC network(s) constantly and able to log conversation in channels that the user is interested in, or to maintain a channel's presence on the network. Modelled after this setup, in 2004 an IRC client following the client\u2013server, called Smuxi, was launched.
## Search engines  
### There are numerous search engines available to aid the user in finding what they are looking for on IRC. Generally the search engine consists of two parts, a \"back-end\" (or \"spider/crawler\") and a front-end \"search engine\". 
### The back-end (spider/webcrawler) is the work horse of the search engine. It is responsible for crawling IRC servers to index the information being sent across them. The information that is indexed usually consists solely of channel text (text that is publicly displayed in public channels). The storage method is usually some sort of relational database, like MySQL or Oracle.The front-end \"search engine\" is the user interface to the database. It supplies users with a way to search the database of indexed information to retrieve the data they are looking for. These front-end search engines can also be coded in numerous programming languages. 
### Most search engines have their own spider that is a single application responsible for crawling IRC and indexing data itself; however, others are \"user based\" indexers. The latter rely on users to install their \"add-on\" to their IRC client; the add-on is what sends the database the channel information of whatever channels the user happens to be on.Many users have implemented their own ad hoc search engines using the logging features built into many IRC clients. These search engines are usually implemented as bots and dedicated to a particular channel or group of associated channels.
## Character encoding  
### IRC still lacks a single globally accepted standard convention for how to transmit characters outside the 7-bit ASCII repertoire. 
### IRC servers normally transfer messages from a client to another client just as byte sequences, without any interpretation or recoding of characters. The IRC protocol (unlike e.g. MIME or HTTP) lacks mechanisms for announcing and negotiating character encoding options. This has put the responsibility for choosing the appropriate character codec on the client. In practice, IRC channels have largely used the same character encodings that were also used by operating systems (in particular Unix derivatives) in the respective language communities: 

### 7-bit era: In the early days of IRC, especially among Scandinavian and Finnish language users, national variants of ISO 646 were the dominant character encodings. These encode non-ASCII characters like \u00c4 \u00d6 \u00c5 \u00e4 \u00f6 \u00e5 at code positions 0x5B 0x5C 0x5D 0x7B 0x7C 0x7D (US-ASCII: [ \\ ] { | }). That is why these codes are always allowed in nicknames. According to RFC 1459, { | } in nicknames should be treated as lowercase equivalents of [ \\ ] respectively. By the late 1990s, the use of 7-bit encodings had disappeared in favour of ISO 8859-1, and such equivalence mappings were dropped from some IRC daemons. 
### 8-bit era: Since the early 1990s, 8-bit encodings such as ISO 8859-1 have become commonly used for European languages. Russian users had a choice of KOI8-R, ISO 8859-5 and CP1251, and since about 2000, modern Russian IRC networks convert between these different commonly used encodings of the Cyrillic script. 
### Multi-byte era: For a long time, East Asian IRC channels with logographic scripts in China, Japan, and Korea have been using multi-byte encodings such as EUC or ISO-2022-JP. With the common migration from ISO 8859 to UTF-8 on Linux and Unix platforms since about 2002, UTF-8 has become an increasingly popular substitute for many of the previously used 8-bit encodings in European channels. Some IRC clients are now capable of reading messages both in ISO 8859-1 or UTF-8 in the same channel, heuristically autodetecting which encoding is used. The shift to UTF-8 began in particular on Finnish-speaking IRC (Merkist\u00f6 (Finnish)).Today, the UTF-8 encoding of Unicode/ISO 10646 would be the most likely contender for a single future standard character encoding for all IRC communication, if such standard ever relaxed the 510-byte message size restriction. UTF-8 is ASCII compatible and covers the superset of all other commonly used coded character set standards.
## File sharing  
### Much like conventional P2P file sharing, users can create file servers that allow them to share files with each other by using customised IRC bots or scripts for their IRC client. Often users will group together to distribute warez via a network of IRC bots.Technically, IRC provides no file transfer mechanisms itself; file sharing is implemented by IRC clients, typically using the Direct Client-to-Client (DCC) protocol, in which file transfers are negotiated through the exchange of private messages between clients. The vast majority of IRC clients feature support for DCC file transfers, hence the view that file sharing is an integral feature of IRC. The commonplace usage of this protocol, however, sometimes also causes DCC spam. DCC commands have also been used to exploit vulnerable clients into performing an action such as disconnecting from the server or exiting the client.
## See also  
### Chat room 
### Client-to-client protocol 
### Comparison of instant messaging protocols 
### Comparison of IRC clients 
### Comparison of mobile IRC clients 
### The Hamnet Players 
### Internet slang 
### List of IRC commands 
### Serving channel 
### Matrix (protocol) and XMPP, similar chat protocols
## Citations 
## General bibliography  
### Reed, Darren (May 1992). A Discussion on Computer Network Conferencing. IETF. doi:10.17487/RFC1324. RFC 1324. Retrieved 30 October 2009. 
### Oikarinen, Jarkko; Reed, Darren (May 1993). Internet Relay Chat Protocol. IETF. doi:10.17487/RFC1459. RFC 1459. Retrieved 30 October 2009. 
### Kalt, Christophe (April 2000). Internet Relay Chat: Architecture. IETF. doi:10.17487/RFC2810. RFC 2810. Retrieved 30 October 2009. 
### Kalt, Christophe (April 2000). Internet Relay Chat: Channel Management. IETF. doi:10.17487/RFC2811. RFC 2811. Retrieved 30 October 2009. 
### Loesch, Carl (17 July 2003). \"Functionality Provided by Systems for Synchronous Conferencing\". psyc.eu. Retrieved 10 April 2011. {{cite journal}}: Cite journal requires |journal (help)
## Further reading  
### Kalt, Christophe (April 2000). Internet Relay Chat: Client Protocol. IETF. doi:10.17487/RFC2812. RFC 2812. Retrieved 30 October 2009. 
### Kalt, Christophe (April 2000). Internet Relay Chat: Server Protocol. IETF. doi:10.17487/RFC2813. RFC 2813. Retrieved 30 October 2009. 
### \"Logs of major events in the online community\". Chapel Hill, North Carolina: ibiblio. Retrieved 8 April 2011. 
### Butcher, Simon. \"IRC technical information\". alien.net.au. Retrieved 10 April 2011.
## External links  
### IRC at Curlie 
### IRC Numerics List 
### History of IRC 
### IRC.org \u2013 Technical and Historical IRC6 information; Articles on the history of IRC 
### IRChelp.org \u2013 Internet Relay Chat (IRC) help archive; Large archive of IRC-related documents 
### IRCv3 \u2013 Working group of developers, who add new features to the protocol and write specs for them 
### IRC-Source \u2013 Internet Relay Chat (IRC) network and channel search engine with historical data 
### irc.netsplit.de \u2013 Internet Relay Chat (IRC) network listing with historical data"
## References
### [Reference](http://www.psybnc.at/readme.txt) - http://www.psybnc.at/readme.txt
### [Reference](http://www.alien.net.au/irc/) - http://www.alien.net.au/irc/
### [Reference](http://www.alien.net.au/irc/chanmodes.html) - http://www.alien.net.au/irc/chanmodes.html
### [Reference](http://www.alien.net.au/irc/servermodes.html) - http://www.alien.net.au/irc/servermodes.html
### [Reference](http://www.alien.net.au/irc/usermodes.html) - http://www.alien.net.au/irc/usermodes.html
### [Reference](http://www.bcchardware.com/index.php?option=com_content&task=view&id=35&Itemid=40) - http://www.bcchardware.com/index.php?option=com_content&task=view&id=35&Itemid=40
### [Reference](http://chriscarey.com/wordpress/2009/07/18/irc-with-irssi-proxy-screen/) - http://chriscarey.com/wordpress/2009/07/18/irc-with-irssi-proxy-screen/
### [Reference](http://computerquestionhelp.com/content/how-guide-setup-your-own-irc-server-using-personal-or-dedicated-system-or-server-top-freewar) - http://computerquestionhelp.com/content/how-guide-setup-your-own-irc-server-using-personal-or-dedicated-system-or-server-top-freewar
### [Reference](http://www.macobserver.com/tip/2002/04/04.1.shtml) - http://www.macobserver.com/tip/2002/04/04.1.shtml
### [Reference](http://www.mirc.com/jarkko.html) - http://www.mirc.com/jarkko.html
### [Reference](http://royal.pingdom.com/2012/04/24/irc-is-dead-long-live-irc/) - http://royal.pingdom.com/2012/04/24/irc-is-dead-long-live-irc/
### [Reference](http://www.symantec.com/avcenter/reference/the.evolution.of.malicious.irc.bots.pdf) - http://www.symantec.com/avcenter/reference/the.evolution.of.malicious.irc.bots.pdf
### [Reference](http://ustream-helpers.com/how-to/ircclient) - http://ustream-helpers.com/how-to/ircclient
### [Reference](http://webtoman.com/opera/panel/ircdmodes.html) - http://webtoman.com/opera/panel/ircdmodes.html
### [Reference](http://www.zdnet.com/news/pirated-movies-now-playing-on-a-server-near-you/122663) - http://www.zdnet.com/news/pirated-movies-now-playing-on-a-server-near-you/122663
### [Reference](http://irc.netsplit.de/networks/top10.php) - http://irc.netsplit.de/networks/top10.php
### [Reference](http://irc.netsplit.de/networks/top100.php) - http://irc.netsplit.de/networks/top100.php
### [Reference](http://www.psyc.eu/synconf) - http://www.psyc.eu/synconf
### [Reference](http://operawiki.info/OperaIRC) - http://operawiki.info/OperaIRC
### [Reference](http://www.dal.net/news/shownews.php?id=67) - http://www.dal.net/news/shownews.php?id=67
### [Reference](http://esper.net/help.php) - http://esper.net/help.php
### [Reference](http://freenode.net/faq.shtml) - http://freenode.net/faq.shtml
### [Reference](http://ircv3.net/) - http://ircv3.net/
### [Reference](http://guide.modlink.net/section11.php) - http://guide.modlink.net/section11.php
### [Reference](http://www.warsow.net/wiki/index.php?title=IRC_Module) - http://www.warsow.net/wiki/index.php?title=IRC_Module
### [Reference](http://doi.org/10.17487%2FRFC1324) - http://doi.org/10.17487%2FRFC1324
### [Reference](http://doi.org/10.17487%2FRFC1459) - http://doi.org/10.17487%2FRFC1459
### [Reference](http://doi.org/10.17487%2FRFC2810) - http://doi.org/10.17487%2FRFC2810
### [Reference](http://doi.org/10.17487%2FRFC2811) - http://doi.org/10.17487%2FRFC2811
### [Reference](http://doi.org/10.17487%2FRFC2812) - http://doi.org/10.17487%2FRFC2812
### [Reference](http://doi.org/10.17487%2FRFC2813) - http://doi.org/10.17487%2FRFC2813
### [Reference](http://www.ibiblio.org/pub/academic/communications/logs/) - http://www.ibiblio.org/pub/academic/communications/logs/
### [Reference](http://www.ibiblio.org/pub/academic/communications/logs/Gulf-War/) - http://www.ibiblio.org/pub/academic/communications/logs/Gulf-War/
### [Reference](http://www.ibiblio.org/pub/academic/communications/logs/report-ussr-gorbatchev) - http://www.ibiblio.org/pub/academic/communications/logs/report-ussr-gorbatchev
### [Reference](http://www.irc-junkie.org/2006-05-07/blitzed-open-proxy-monitor-shuts-down/) - http://www.irc-junkie.org/2006-05-07/blitzed-open-proxy-monitor-shuts-down/
### [Reference](http://www.irc-wiki.org/IRC_server) - http://www.irc-wiki.org/IRC_server
### [Reference](http://www.irc.org/) - http://www.irc.org/
### [Reference](http://www.irc.org/history.html) - http://www.irc.org/history.html
### [Reference](http://www.irc.org/history_docs/TheGreatSplit.html) - http://www.irc.org/history_docs/TheGreatSplit.html
### [Reference](http://www.irc.org/tech_docs/005.html) - http://www.irc.org/tech_docs/005.html
### [Reference](http://www.irchelp.org/) - http://www.irchelp.org/
### [Reference](http://www.irchelp.org/irchelp/rfc/dccspec.html) - http://www.irchelp.org/irchelp/rfc/dccspec.html
### [Reference](http://www.liquidsilver.org/2010/06/ustream-v-justin/) - http://www.liquidsilver.org/2010/06/ustream-v-justin/
### [Reference](http://www.smuxi.org/blog/show/Detachable_Frontend_Core_Rewrite__UML__Windows_Port_kicking_Glade) - http://www.smuxi.org/blog/show/Detachable_Frontend_Core_Rewrite__UML__Windows_Port_kicking_Glade
### [Reference](http://www.smuxi.org/page/About) - http://www.smuxi.org/page/About
### [Reference](http://meta.wikimedia.org/wiki/IRC/Cloaks) - http://meta.wikimedia.org/wiki/IRC/Cloaks
### [Reference](http://www.shanemcc.co.uk/irc/#listmode) - http://www.shanemcc.co.uk/irc/#listmode
### [Reference](https://books.google.com/books?id=OuPtI5fHhBoC) - https://books.google.com/books?id=OuPtI5fHhBoC
### [Reference](https://books.google.com/books?id=aQ74THYRyYsC&q=hostmask&pg=PA315) - https://books.google.com/books?id=aQ74THYRyYsC&q=hostmask&pg=PA315
### [Reference](https://books.google.com/books?id=b2mMzS0hCkAC&q=Hostmask&pg=PA500) - https://books.google.com/books?id=b2mMzS0hCkAC&q=Hostmask&pg=PA500
### [Reference](https://books.google.com/books?id=e3ggsGgTzUgC&q=Hostmask+IRC&pg=PA10) - https://books.google.com/books?id=e3ggsGgTzUgC&q=Hostmask+IRC&pg=PA10
### [Reference](https://irc-source.com/) - https://irc-source.com/
### [Reference](https://www.npmjs.com/package/node-irc) - https://www.npmjs.com/package/node-irc
### [Reference](https://netsplit.de/networks/index.php.php) - https://netsplit.de/networks/index.php.php
### [Reference](https://netsplit.de/networks/top100.php.php) - https://netsplit.de/networks/top100.php.php
### [Reference](https://defs.ircdocs.horse/defs/numerics.html) - https://defs.ircdocs.horse/defs/numerics.html
### [Reference](https://www.devever.net/~hl/freenode_suicide.xhtml) - https://www.devever.net/~hl/freenode_suicide.xhtml
### [Reference](https://ircv3.net/support/networks.html) - https://ircv3.net/support/networks.html
### [Reference](https://archive.org/details/bookofirc00char) - https://archive.org/details/bookofirc00char
### [Reference](https://archive.org/details/bookofirc00char/page/61) - https://archive.org/details/bookofirc00char/page/61
### [Reference](https://archive.org/details/encyclopediaofne00jone) - https://archive.org/details/encyclopediaofne00jone
### [Reference](https://archive.org/details/encyclopediaofne00jone/page/257) - https://archive.org/details/encyclopediaofne00jone/page/257
### [Reference](https://archive.org/details/isbn_9780789722836/page/289) - https://archive.org/details/isbn_9780789722836/page/289
### [Reference](https://archive.org/details/stealthisfilesha00wang/page/61) - https://archive.org/details/stealthisfilesha00wang/page/61
### [Reference](https://archive.org/details/stealthisfilesha00wang/page/65) - https://archive.org/details/stealthisfilesha00wang/page/65
### [Reference](https://web.archive.org/web/20090628013626/http://www.ibiblio.org/pub/academic/communications/logs/report-ussr-gorbatchev) - https://web.archive.org/web/20090628013626/http://www.ibiblio.org/pub/academic/communications/logs/report-ussr-gorbatchev
### [Reference](https://web.archive.org/web/20100326082146/http://freenode.net/faq.shtml) - https://web.archive.org/web/20100326082146/http://freenode.net/faq.shtml
### [Reference](https://web.archive.org/web/20110317014824/http://operawiki.info/OperaIRC) - https://web.archive.org/web/20110317014824/http://operawiki.info/OperaIRC
### [Reference](https://web.archive.org/web/20110425010535/http://www.warsow.net/wiki/index.php?title=IRC_Module) - https://web.archive.org/web/20110425010535/http://www.warsow.net/wiki/index.php?title=IRC_Module
### [Reference](https://web.archive.org/web/20111015190740/http://webtoman.com/opera/panel/ircdmodes.html) - https://web.archive.org/web/20111015190740/http://webtoman.com/opera/panel/ircdmodes.html
### [Reference](https://web.archive.org/web/20190113165832/http://irc.netsplit.de/) - https://web.archive.org/web/20190113165832/http://irc.netsplit.de/
### [Reference](https://curlie.org/Computers/Internet/Chat/IRC) - https://curlie.org/Computers/Internet/Chat/IRC
### [Reference](https://doomwiki.org/wiki/ZDaemon#Other_utilities) - https://doomwiki.org/wiki/ZDaemon#Other_utilities
### [Reference](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=5) - https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=5
### [Reference](https://www.iana.org/assignments/uri-schemes.html) - https://www.iana.org/assignments/uri-schemes.html
### [Reference](https://datatracker.ietf.org/doc/html/draft-brocklesby-irc-isupport-03) - https://datatracker.ietf.org/doc/html/draft-brocklesby-irc-isupport-03
### [Reference](https://datatracker.ietf.org/doc/html/draft-butcher-irc-url-04) - https://datatracker.ietf.org/doc/html/draft-butcher-irc-url-04
### [Reference](https://datatracker.ietf.org/doc/html/draft-pfenning-irc-extensions-04) - https://datatracker.ietf.org/doc/html/draft-pfenning-irc-extensions-04
### [Reference](https://datatracker.ietf.org/doc/html/rfc1324) - https://datatracker.ietf.org/doc/html/rfc1324
### [Reference](https://datatracker.ietf.org/doc/html/rfc1324#section-2.1) - https://datatracker.ietf.org/doc/html/rfc1324#section-2.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1324#section-2.5.1) - https://datatracker.ietf.org/doc/html/rfc1324#section-2.5.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1324#section-5.2.1) - https://datatracker.ietf.org/doc/html/rfc1324#section-5.2.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1324#section-5.2.4) - https://datatracker.ietf.org/doc/html/rfc1324#section-5.2.4
### [Reference](https://datatracker.ietf.org/doc/html/rfc1324#section-5.4.1) - https://datatracker.ietf.org/doc/html/rfc1324#section-5.4.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1324#section-5.4.2) - https://datatracker.ietf.org/doc/html/rfc1324#section-5.4.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459) - https://datatracker.ietf.org/doc/html/rfc1459
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#page-51) - https://datatracker.ietf.org/doc/html/rfc1459#page-51
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-1) - https://datatracker.ietf.org/doc/html/rfc1459#section-1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-1.1) - https://datatracker.ietf.org/doc/html/rfc1459#section-1.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-1.2) - https://datatracker.ietf.org/doc/html/rfc1459#section-1.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-1.2.1) - https://datatracker.ietf.org/doc/html/rfc1459#section-1.2.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-2.2) - https://datatracker.ietf.org/doc/html/rfc1459#section-2.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-2.3.1) - https://datatracker.ietf.org/doc/html/rfc1459#section-2.3.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-2.4) - https://datatracker.ietf.org/doc/html/rfc1459#section-2.4
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-3.2) - https://datatracker.ietf.org/doc/html/rfc1459#section-3.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-3.2.2) - https://datatracker.ietf.org/doc/html/rfc1459#section-3.2.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-4.2.1) - https://datatracker.ietf.org/doc/html/rfc1459#section-4.2.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-4.2.3) - https://datatracker.ietf.org/doc/html/rfc1459#section-4.2.3
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-4.2.3.1) - https://datatracker.ietf.org/doc/html/rfc1459#section-4.2.3.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-4.2.6) - https://datatracker.ietf.org/doc/html/rfc1459#section-4.2.6
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-4.3.5) - https://datatracker.ietf.org/doc/html/rfc1459#section-4.3.5
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-5.6) - https://datatracker.ietf.org/doc/html/rfc1459#section-5.6
### [Reference](https://datatracker.ietf.org/doc/html/rfc1459#section-9.3) - https://datatracker.ietf.org/doc/html/rfc1459#section-9.3
### [Reference](https://datatracker.ietf.org/doc/html/rfc2810) - https://datatracker.ietf.org/doc/html/rfc2810
### [Reference](https://datatracker.ietf.org/doc/html/rfc2810#section-1) - https://datatracker.ietf.org/doc/html/rfc2810#section-1
### [Reference](https://datatracker.ietf.org/doc/html/rfc2810#section-2.2) - https://datatracker.ietf.org/doc/html/rfc2810#section-2.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc2810#section-3) - https://datatracker.ietf.org/doc/html/rfc2810#section-3
### [Reference](https://datatracker.ietf.org/doc/html/rfc2810#section-5.1) - https://datatracker.ietf.org/doc/html/rfc2810#section-5.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc2810#section-5.2.1) - https://datatracker.ietf.org/doc/html/rfc2810#section-5.2.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc2810#section-6.1) - https://datatracker.ietf.org/doc/html/rfc2810#section-6.1
### [Reference](https://datatracker.ietf.org/doc/html/rfc2810#section-6.3) - https://datatracker.ietf.org/doc/html/rfc2810#section-6.3
### [Reference](https://datatracker.ietf.org/doc/html/rfc2811) - https://datatracker.ietf.org/doc/html/rfc2811
### [Reference](https://datatracker.ietf.org/doc/html/rfc2811#section-2.2) - https://datatracker.ietf.org/doc/html/rfc2811#section-2.2
### [Reference](https://datatracker.ietf.org/doc/html/rfc2811#section-2.3) - https://datatracker.ietf.org/doc/html/rfc2811#section-2.3
### [Reference](https://datatracker.ietf.org/doc/html/rfc2811#section-3) - https://datatracker.ietf.org/doc/html/rfc2811#section-3
### [Reference](https://datatracker.ietf.org/doc/html/rfc2811#section-4) - https://datatracker.ietf.org/doc/html/rfc2811#section-4
### [Reference](https://datatracker.ietf.org/doc/html/rfc2811#section-4.3) - https://datatracker.ietf.org/doc/html/rfc2811#section-4.3
### [Reference](https://datatracker.ietf.org/doc/html/rfc2812) - https://datatracker.ietf.org/doc/html/rfc2812
### [Reference](https://datatracker.ietf.org/doc/html/rfc2813) - https://datatracker.ietf.org/doc/html/rfc2813
### [Reference](https://www.unrealircd.org/docs/Channel_modes) - https://www.unrealircd.org/docs/Channel_modes
### [Reference](https://www.unrealircd.org/docs/Cloaking) - https://www.unrealircd.org/docs/Cloaking
### [Reference](https://daniel.haxx.se/irchistory.html) - https://daniel.haxx.se/irchistory.html
### [Reference](https://help.twitch.tv/customer/portal/articles/1302780-twitch-irc) - https://help.twitch.tv/customer/portal/articles/1302780-twitch-irc
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/1/14/Hexchat_2.16.0_screenshot.png) - https://upload.wikimedia.org/wikipedia/commons/1/14/Hexchat_2.16.0_screenshot.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/ab/Ircnetz-Schema.svg) - https://upload.wikimedia.org/wikipedia/commons/a/ab/Ircnetz-Schema.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/e/e3/Tolsun_2.jpg) - https://upload.wikimedia.org/wikipedia/commons/e/e3/Tolsun_2.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/df/Wikibooks-logo-en-noslogan.svg) - https://upload.wikimedia.org/wikipedia/commons/d/df/Wikibooks-logo-en-noslogan.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/6/65/Xaric_screen_shot.jpg) - https://upload.wikimedia.org/wikipedia/commons/6/65/Xaric_screen_shot.jpg
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg) - https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg