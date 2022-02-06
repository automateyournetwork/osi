# Network Time Protocol
## [URL](https://en.wikipedia.org/wiki/Network_Time_Protocol) - https://en.wikipedia.org/wiki/Network_Time_Protocol
## Catagories
### All Wikipedia articles in need of updating
### All accuracy disputes
### All articles containing potentially dated statements
### All articles with failed verification
### Application layer protocols
### Articles containing potentially dated statements from 2014
### Articles needing more detailed references
### Articles with disputed statements from February 2022
### Articles with failed verification from January 2022
### Articles with short description
### CS1 maint: url-status
### Internet Standards
### Network time-related software
### Short description matches Wikidata
### Webarchive template wayback links
### Wikipedia articles in need of updating from January 2020
### "The Network Time Protocol (NTP) is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks. In operation since before 1985, NTP is one of the oldest Internet protocols in current use. NTP was designed by David L. Mills of the University of Delaware. 
### NTP is intended to synchronize all participating computers to within a few milliseconds of Coordinated Universal Time (UTC).:\u200a3\u200a It uses the intersection algorithm, a modified version of Marzullo's algorithm, to select accurate time servers and is designed to mitigate the effects of variable network latency. NTP can usually maintain time to within tens of milliseconds over the public Internet, and can achieve better than one millisecond accuracy in local area networks under ideal conditions. Asymmetric routes and network congestion can cause errors of 100 ms or more.The protocol is usually described in terms of a client\u2013server model, but can as easily be used in peer-to-peer relationships where both peers consider the other to be a potential time source.:\u200a20\u200a Implementations send and receive timestamps using the User Datagram Protocol (UDP) on port number 123. They can also use broadcasting or multicasting, where clients passively listen to time updates after an initial round-trip calibrating exchange. NTP supplies a warning of any impending leap second adjustment, but no information about local time zones or daylight saving time is transmitted.The current protocol is version 4 (NTPv4), which is a proposed standard as documented in RFC 5905. It is backward compatible with version 3, specified in RFC 1305. 
### Network Time Security (NTS), a secure version of NTP with TLS and AEAD is a proposed standard and documented in RFC 8915.
## History  

### In 1979, network time synchronization technology was used in what was possibly the first public demonstration of Internet services running over a trans-Atlantic satellite network, at the National Computer Conference in New York. The technology was later described in the 1981 Internet Engineering Note (IEN) 173 and a public protocol was developed from it that was documented in RFC 778. The technology was first deployed in a local area network as part of the Hello routing protocol and implemented in the Fuzzball router, an experimental operating system used in network prototyping, where it ran for many years. 
### Other related network tools were available both then and now. They include the Daytime and Time protocols for recording the time of events, as well as the ICMP Timestamp messages and IP Timestamp option (RFC 781). More complete synchronization systems, although lacking NTP's data analysis and clock disciplining algorithms, include the Unix daemon timed, which uses an election algorithm to appoint a server for all the clients; and the Digital Time Synchronization Service (DTSS), which uses a hierarchy of servers similar to the NTP stratum model. 
### In 1985, NTP version 0 (NTPv0) was implemented in both Fuzzball and Unix, and the NTP packet header and round-trip delay and offset calculations, which have persisted into NTPv4, were documented in RFC 958. Despite the relatively slow computers and networks available at the time, accuracy of better than 100 milliseconds was usually obtained on Atlantic spanning links, with accuracy of tens of milliseconds on Ethernet networks. 
### In 1988, a much more complete specification of the NTPv1 protocol, with associated algorithms, was published in RFC 1059. It drew on the experimental results and clock filter algorithm documented in RFC 956 and was the first version to describe the client\u2013server and peer-to-peer modes. In 1991, the NTPv1 architecture, protocol and algorithms were brought to the attention of a wider engineering community with the publication of an article by David L. Mills in the IEEE Transactions on Communications.In 1989, RFC 1119 was published defining NTPv2 by means of a state machine, with pseudocode to describe its operation. It introduced a management protocol and cryptographic authentication scheme which have both survived into NTPv4, along with the bulk of the algorithm. However the design of NTPv2 was criticized for lacking formal correctness by the DTSS community, and the clock selection procedure was modified to incorporate Marzullo's algorithm for NTPv3 onwards.In 1992, RFC 1305 defined NTPv3. The RFC included an analysis of all sources of error, from the reference clock down to the final client, which enabled the calculation of a metric that helps choose the best server where several candidates appear to disagree. Broadcast mode was introduced. 
### In subsequent years, as new features were added and algorithm improvements were made, it became apparent that a new protocol version was required. In 2010, RFC 5905 was published containing a proposed specification for NTPv4. The protocol has significantly progressed since then, and As of 2014, an updated RFC has yet to be published. Following the retirement of Mills from the University of Delaware, the reference implementation is currently maintained as an open source project led by Harlan Stenn.
## Clock strata  

### NTP uses a hierarchical, semi-layered system of time sources. Each level of this hierarchy is termed a stratum and is assigned a number starting with zero for the reference clock at the top. A server synchronized to a stratum n server runs at stratum n + 1. The number represents the distance from the reference clock and is used to prevent cyclical dependencies in the hierarchy. Stratum is not always an indication of quality or reliability; it is common to find stratum 3 time sources that are higher quality than other stratum 2 time sources. A brief description of strata 0, 1, 2 and 3 is provided below. 

### Stratum 0 
### These are high-precision timekeeping devices such as atomic clocks, GNSS (including GPS) or other radio clocks. They generate a very accurate pulse per second signal that triggers an interrupt and timestamp on a connected computer. Stratum 0 devices are also known as reference clocks. NTP servers cannot advertise themselves as stratum 0. A stratum field set to 0 in NTP packet indicates an unspecified stratum. 
### Stratum 1 
### These are computers whose system time is synchronized to within a few microseconds of their attached stratum 0 devices. Stratum 1 servers may peer with other stratum 1 servers for sanity check and backup. They are also referred to as primary time servers. 
### Stratum 2 
### These are computers that are synchronized over a network to stratum 1 servers. Often a stratum 2 computer queries several stratum 1 servers. Stratum 2 computers may also peer with other stratum 2 computers to provide more stable and robust time for all devices in the peer group. 
### Stratum 3 
### These are computers that are synchronized to stratum 2 servers. They employ the same algorithms for peering and data sampling as stratum 2, and can themselves act as servers for stratum 4 computers, and so on.The upper limit for stratum is 15; stratum 16 is used to indicate that a device is unsynchronized. The NTP algorithms on each computer interact to construct a Bellman-Ford shortest-path spanning tree, to minimize the accumulated round-trip delay to the stratum 1 servers for all the clients.:\u200a20\u200aIn addition to stratum, the protocol is able to identify the synchronization source for each server in terms of a reference identifier (refid).
## Timestamps  
### The 64-bit timestamps used by NTP consist of a 32-bit part for seconds and a 32-bit part for fractional second, giving a time scale that rolls over every 232 seconds (136 years) and a theoretical resolution of 2\u221232 seconds (233 picoseconds). NTP uses an epoch of January 1, 1900. Therefore, the first rollover occurs on February 7, 2036.NTPv4 introduces a 128-bit date format: 64 bits for the second and 64 bits for the fractional-second. The most-significant 32-bits of this format is the Era Number which resolves rollover ambiguity in most cases. According to Mills, \"The 64-bit value for the fraction is enough to resolve the amount of time it takes a photon to pass an electron at the speed of light. The 64-bit second value is enough to provide unambiguous time representation until the universe goes dim.\"
## Clock synchronization algorithm  

### A typical NTP client regularly polls one or more NTP servers. The client must compute its time offset and round-trip delay. Time offset \u03b8 is positive or negative (client time > server time) difference in absolute time between the two clocks. It is defined by 

### and the round-trip delay \u03b4 by 

### where 

### t0 is the client's timestamp of the request packet transmission, 
### t1 is the server's timestamp of the request packet reception, 
### t2 is the server's timestamp of the response packet transmission and 
### t3 is the client's timestamp of the response packet reception.:\u200a19\u200aTo derive the expression for the offset, note that for the request packet, 

### and for the response packet, 

### Solving for \u03b8 yields the definition of the time offset. 
### The values for \u03b8 and \u03b4 are passed through filters and subjected to statistical analysis. Outliers are discarded and an estimate of time offset is derived from the best three remaining candidates. The clock frequency is then adjusted to reduce the offset gradually, creating a feedback loop.:\u200a20\u200aAccurate synchronization is achieved when both the incoming and outgoing routes between the client and the server have symmetrical nominal delay. If the routes do not have a common nominal delay, a systematic bias exists of half the difference between the forward and backward travel times.
## Software implementations 
## Reference implementation  
### The NTP reference implementation, along with the protocol, has been continuously developed for over 20 years. Backwards compatibility has been maintained as new features have been added. It contains several sensitive algorithms, especially to discipline the clock, that can misbehave when synchronized to servers that use different algorithms. The software has been ported to almost every computing platform, including personal computers. It runs as a daemon called ntpd under Unix or as a service under Windows. Reference clocks are supported and their offsets are filtered and analysed in the same way as remote servers, although they are usually polled more frequently.:\u200a15\u201319\u200a This implementation was audited in 2017, finding numerous potential security issues.
## SNTP  
### Simple Network Time Protocol (SNTP) is a less complex implementation of NTP, using the same protocol but without requiring the storage of state over extended periods of time. It is used in some embedded systems and in applications where full NTP capability is not required.
## Windows Time  
### All Microsoft Windows versions since Windows 2000 include the Windows Time service (W32Time), which has the ability to synchronize the computer clock to an NTP server. 
### W32Time was originally implemented for the purpose of the Kerberos version 5 authentication protocol, which required time to be within 5 minutes of the correct value to prevent replay attacks. The version in Windows 2000 and Windows XP only implements SNTP, and violates several aspects of the NTP version 3 standard.Beginning with Windows Server 2003 and Windows Vista, W32Time became compatible with a significant subset of NTPv3. Microsoft states that W32Time cannot reliably maintain time synchronization with one second accuracy. If higher accuracy is desired, Microsoft recommends using a newer version of Windows or different NTP implementation.Beginning with Windows 10 version 1607 and Windows Server 2016, W32Time can be configured to reach time accuracy of 1 s, 50 ms or 1 ms under certain specified operating conditions.
## OpenNTPD  
### In 2004, Henning Brauer presented OpenNTPD, an NTP implementation with a focus on security and encompassing a privilege separated design. Whilst it is aimed more closely at the simpler generic needs of OpenBSD users, it also includes some protocol security improvements while still being compatible with existing NTP servers. A portable version is available in Linux package repositories.
## Ntimed  
### A new NTP client, ntimed, was started by Poul-Henning Kamp in 2014 and abandoned in 2015. The new implementation was sponsored by the Linux Foundation as a replacement for the reference implementation, as it was determined to be easier to write a new implementation from scratch than to reduce the size of the reference implementation. Although it has not been officially released, ntimed can synchronize clocks reliably.
## NTPsec  
### NTPsec is a fork of the reference implementation that has been systematically security-hardened. The fork point was in June 2015 and was in response to a series of compromises in 2014. The first production release shipped in October 2017. Between removal of unsafe features, removal of support for obsolete hardware, and removal of support for obsolete Unix variants, NTPsec has been able to pare away 75% of the original codebase, making the remainder easier to audit.  A 2017 audit of the code showed eight security issues, including two that were not present in the original reference implementation, but NTPsec did not suffer from eight other issues that remained in the reference implementation.
## chrony  

### chrony comes by default in Red Hat distributions and is available in the Ubuntu repositories. chrony is aimed at ordinary computers, which are unstable, go into sleep mode or have intermittent connection to the Internet. chrony is also designed for virtual machines, a much more unstable environment. It is characterized by low resource consumption (cost) and supports Precision Time Protocol hardware for greater timestamp precision. It has two main components: chronyd, a daemon that is executed when the computer starts, and chronyc, a command line interface to the user for its configuration. It has been evaluated as very safe and with just a few incidents, its advantage is the versatility of its code, written from scratch to avoid unnecessary complexity. Support for Network Time Security (NTS) was added on version 4.0. chrony is available under GNU General Public License version 2, was created by Richard Curnow in 1997 and is currently maintained by Miroslav Lichvar.
## Leap seconds  
### On the day of a leap second event, ntpd receives notification from either a configuration file, an attached reference clock, or a remote server. Although the NTP clock is actually halted during the event, because of the requirement that time must appear to be strictly increasing, any processes that query the system time cause it to increase by a tiny amount, preserving the order of events. If a negative leap second should ever become necessary, it would be deleted with the sequence 23:59:58, 00:00:00, skipping 23:59:59.An alternative implementation, called leap smearing, consists in introducing the leap second incrementally during a period of 24 hours, from noon to noon in UTC time. This implementation is used by Google (both internally and on their public NTP servers) and by Amazon AWS.
## Security concerns  

### Only a few other security problems have been identified in the reference implementation of the NTP codebase, but those that appeared in 2009 were cause for significant concern. The protocol has been undergoing revision and review throughout its history. The codebase for the reference implementation has undergone security audits from several sources for several years.A stack buffer overflow exploit was discovered and patched in 2014. Apple was concerned enough about this vulnerability that it used its auto-update capability for the first time. Some implementation errors are basic, such as a missing return statement in a routine, that can lead to unlimited access to systems that are running some versions of NTP in the root daemon. Systems that do not use the root daemon, such as those derived from Berkeley Software Distribution (BSD), are not subject to this flaw.A 2017 security audit of three NTP implementations, conducted on behalf of the Linux Foundation's Core Infrastructure Initiative, suggested that both NTP and NTPsec were more problematic than Chrony from a security standpoint.NTP servers can be susceptible to man-in-the-middle attacks unless packets are cryptographically signed for authentication. The computational overhead involved can make this impractical on busy servers, particularly during denial of service attacks. NTP message spoofing from a man-in-the-middle attack can be used to alter clocks on client computers and allow a number of attacks based on bypassing of cryptographic key expiration. Some of the services affected by fake NTP messages identified are TLS, DNSSEC, various caching schemes (such as DNS cache), Border Gateway Protocol (BGP), Bitcoin and a number of persistent login schemes.NTP has been used in distributed denial of service attacks. A small query is sent to an NTP server with the return IP address spoofed to be the target address. Similar to the DNS amplification attack, the server responds with a much larger reply that allows an attacker to substantially increase the amount of data being sent to the target. To avoid participating in an attack, NTP server software can be upgraded or servers can be configured to ignore external queries.To improve NTP security, a secure version called Network Time Security (NTS) was developed and currently supported by several time servers.
## See also  
### Allan variance 
### Clock network 
### International Atomic Time 
### IRIG timecode 
### NITZ 
### NTP pool 
### Ntpdate
## Notes 
## References 
## Further reading  
### Definitions of Managed Objects for Network Time Protocol Version 4 (NTPv4). doi:10.17487/RFC5907. RFC 5907. 
### Network Time Protocol (NTP) Server Option for DHCPv6. doi:10.17487/RFC5908. RFC 5908.
## External links  
### Official website  
### Official Stratum One Time Servers list 
### IETF NTP working group 
### Microsft Windows accurate time guide and more 
### Time and NTP paper 
### NTP Survey 2005 
### Current NIST leap seconds file compatible with ntpd 
### David L. Mills, A Brief History of NTP Time: Confessions of an Internet Timekeeper (PDF), retrieved 2021-02-07"
## References
### [Reference](http://www.cisco.com/en/US/tech/tk869/tk769/technologies_white_paper09186a0080117070.shtml) - http://www.cisco.com/en/US/tech/tk869/tk769/technologies_white_paper09186a0080117070.shtml
### [Reference](http://www.informationweek.com/cloud/infrastructure-as-a-service/ntp-needs-money-is-a-foundation-the-answer/d/d-id/1319557) - http://www.informationweek.com/cloud/infrastructure-as-a-service/ntp-needs-money-is-a-foundation-the-answer/d/d-id/1319557
### [Reference](http://www.informationweek.com/it-life/ntps-fate-hinges-on-father-time/d/d-id/1319432?cmp=em-prog-na-na-newsltr_20150313_control&imm_mid=0ce65e&page_number=2) - http://www.informationweek.com/it-life/ntps-fate-hinges-on-father-time/d/d-id/1319432?cmp=em-prog-na-na-newsltr_20150313_control&imm_mid=0ce65e&page_number=2
### [Reference](http://support.microsoft.com/kb/939322) - http://support.microsoft.com/kb/939322
### [Reference](http://rhelblog.redhat.com/2016/07/20/combining-ptp-with-ntp-to-get-the-best-of-both-worlds/) - http://rhelblog.redhat.com/2016/07/20/combining-ptp-with-ntp-to-get-the-best-of-both-worlds/
### [Reference](http://www.skrenta.com/rt/man/timed.8.html) - http://www.skrenta.com/rt/man/timed.8.html
### [Reference](http://what-when-how.com/computer-network-time-synchronization/how-ntp-represents-the-time-computer-network-time-synchronization/) - http://what-when-how.com/computer-network-time-synchronization/how-ntp-represents-the-time-computer-network-time-synchronization/
### [Reference](http://www.lieberbiber.de/2017/03/14/a-look-at-the-year-20362038-problems-and-time-proofness-in-various-systems/) - http://www.lieberbiber.de/2017/03/14/a-look-at-the-year-20362038-problems-and-time-proofness-in-various-systems/
### [Reference](http://phk.freebsd.dk/time/20140926) - http://phk.freebsd.dk/time/20140926
### [Reference](http://www.cs.bu.edu/~goldbe/NTPattack.html) - http://www.cs.bu.edu/~goldbe/NTPattack.html
### [Reference](http://www.cs.bu.edu/~goldbe/papers/NTPattack.pdf) - http://www.cs.bu.edu/~goldbe/papers/NTPattack.pdf
### [Reference](http://www.cis.ohio-state.edu/htbin/ien/ien173.html) - http://www.cis.ohio-state.edu/htbin/ien/ien173.html
### [Reference](http://www3.cs.stonybrook.edu/~jgao/CSE590-spring11/91-ntp.pdf) - http://www3.cs.stonybrook.edu/~jgao/CSE590-spring11/91-ntp.pdf
### [Reference](http://www.eecis.udel.edu/~mills/exec.html) - http://www.eecis.udel.edu/~mills/exec.html
### [Reference](http://www.eecis.udel.edu/~mills/leap.html) - http://www.eecis.udel.edu/~mills/leap.html
### [Reference](http://www.eecis.udel.edu/~mills/security.html) - http://www.eecis.udel.edu/~mills/security.html
### [Reference](http://www.i-programmer.info/news/149-security/8120-ntp-the-latest-open-source-security-problem.html) - http://www.i-programmer.info/news/149-security/8120-ntp-the-latest-open-source-security-problem.html
### [Reference](http://doi.org/10.1109%2F26.103043) - http://doi.org/10.1109%2F26.103043
### [Reference](http://doi.org/10.1109%2FCPEM.2002.1034915) - http://doi.org/10.1109%2FCPEM.2002.1034915
### [Reference](http://doi.org/10.17487%2FRFC4330) - http://doi.org/10.17487%2FRFC4330
### [Reference](http://doi.org/10.17487%2FRFC5906) - http://doi.org/10.17487%2FRFC5906
### [Reference](http://doi.org/10.17487%2FRFC5907) - http://doi.org/10.17487%2FRFC5907
### [Reference](http://doi.org/10.17487%2FRFC5908) - http://doi.org/10.17487%2FRFC5908
### [Reference](http://tools.ietf.org/html/rfc5905) - http://tools.ietf.org/html/rfc5905
### [Reference](http://support.ntp.org/Main/CodeAudit) - http://support.ntp.org/Main/CodeAudit
### [Reference](http://support.ntp.org/bin/view/Main/SecurityNotice) - http://support.ntp.org/bin/view/Main/SecurityNotice
### [Reference](http://support.ntp.org/bin/view/Main/SecurityNotice#April_2010_DRDoS_Amplification_A) - http://support.ntp.org/bin/view/Main/SecurityNotice#April_2010_DRDoS_Amplification_A
### [Reference](http://support.ntp.org/bin/view/Servers/StratumOneTimeServers) - http://support.ntp.org/bin/view/Servers/StratumOneTimeServers
### [Reference](http://support.ntp.org/security) - http://support.ntp.org/security
### [Reference](http://www.ntp.org/ntpfaq/NTP-s-algo.htm#Q-ACCURATE-CLOCK) - http://www.ntp.org/ntpfaq/NTP-s-algo.htm#Q-ACCURATE-CLOCK
### [Reference](https://arstechnica.com/apple/2014/12/apple-automatically-patches-macs-to-fix-severe-ntp-security-flaw/) - https://arstechnica.com/apple/2014/12/apple-automatically-patches-macs-to-fix-severe-ntp-security-flaw/
### [Reference](https://arstechnica.com/security/2014/01/new-dos-attacks-taking-down-game-sites-deliver-crippling-100-gbps-floods/) - https://arstechnica.com/security/2014/01/new-dos-attacks-taking-down-game-sites-deliver-crippling-100-gbps-floods/
### [Reference](https://www.blackhat.com/docs/eu-14/materials/eu-14-Selvi-Bypassing-HTTP-Strict-Transport-Security-wp.pdf) - https://www.blackhat.com/docs/eu-14/materials/eu-14-Selvi-Bypassing-HTTP-Strict-Transport-Security-wp.pdf
### [Reference](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20090923-ntp) - https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20090923-ntp
### [Reference](https://github.com/bsdphk/Ntimed) - https://github.com/bsdphk/Ntimed
### [Reference](https://books.google.com/books?id=AB-1DQAAQBAJ&pg=PA80) - https://books.google.com/books?id=AB-1DQAAQBAJ&pg=PA80
### [Reference](https://books.google.com/books?id=BxTOBQAAQBAJ&pg=PA377) - https://books.google.com/books?id=BxTOBQAAQBAJ&pg=PA377
### [Reference](https://books.google.com/books?id=pdTcJBfnbq8C&pg=PA12) - https://books.google.com/books?id=pdTcJBfnbq8C&pg=PA12
### [Reference](https://books.google.com/books?id=ptSC4LpwGA0C&pg=PA582) - https://books.google.com/books?id=ptSC4LpwGA0C&pg=PA582
### [Reference](https://developers.google.com/time/smear) - https://developers.google.com/time/smear
### [Reference](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/accurate-time) - https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/accurate-time
### [Reference](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/configuring-systems-for-high-accuracy?tabs=MinPollInterval) - https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/configuring-systems-for-high-accuracy?tabs=MinPollInterval
### [Reference](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/support-boundary) - https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/support-boundary
### [Reference](https://technet.microsoft.com/en-us/library/cc773013(WS.10).aspx) - https://technet.microsoft.com/en-us/library/cc773013(WS.10).aspx
### [Reference](https://technet.microsoft.com/en-us/library/cc773061(WS.10).aspx) - https://technet.microsoft.com/en-us/library/cc773061(WS.10).aspx
### [Reference](https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/get-started/windows-time-service/windows-2016-accurate-time) - https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/get-started/windows-time-service/windows-2016-accurate-time
### [Reference](https://opensource.com/article/18/12/manage-ntp-chrony) - https://opensource.com/article/18/12/manage-ntp-chrony
### [Reference](https://blogs.technet.com/b/askds/archive/2007/10/23/high-accuracy-w32time-requirements.aspx) - https://blogs.technet.com/b/askds/archive/2007/10/23/high-accuracy-w32time-requirements.aspx
### [Reference](https://packages.ubuntu.com/xenial/chrony) - https://packages.ubuntu.com/xenial/chrony
### [Reference](https://www.eecis.udel.edu/~mills/database/papers/history.pdf) - https://www.eecis.udel.edu/~mills/database/papers/history.pdf
### [Reference](https://www.eecis.udel.edu/~mills/ntp.html) - https://www.eecis.udel.edu/~mills/ntp.html
### [Reference](https://www.eecis.udel.edu/~mills/y2k.html) - https://www.eecis.udel.edu/~mills/y2k.html
### [Reference](https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:ntp&cpe_product=cpe:/::ntp) - https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:ntp&cpe_product=cpe:/::ntp
### [Reference](https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:ntpsec&cpe_product=cpe:/::ntpsec) - https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:ntpsec&cpe_product=cpe:/::ntpsec
### [Reference](https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:tuxfamily&cpe_product=cpe:/::chrony) - https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:tuxfamily&cpe_product=cpe:/::chrony
### [Reference](https://ics-cert.us-cert.gov/advisories/ICSA-14-353-01) - https://ics-cert.us-cert.gov/advisories/ICSA-14-353-01
### [Reference](https://weberblog.net/setting-up-nts-secured-ntp-with-ntpsec/) - https://weberblog.net/setting-up-nts-secured-ntp-with-ntpsec/
### [Reference](https://nts.time.nl/) - https://nts.time.nl/
### [Reference](https://web.archive.org/web/19961230073104/http://www.cis.ohio-state.edu/htbin/ien/ien173.html) - https://web.archive.org/web/19961230073104/http://www.cis.ohio-state.edu/htbin/ien/ien173.html
### [Reference](https://web.archive.org/web/20010604223215/https://www.iana.org/assignments/port-numbers) - https://web.archive.org/web/20010604223215/https://www.iana.org/assignments/port-numbers
### [Reference](https://web.archive.org/web/20090112213922/http://support.microsoft.com/kb/939322) - https://web.archive.org/web/20090112213922/http://support.microsoft.com/kb/939322
### [Reference](https://web.archive.org/web/20091209115945/https://chrony.tuxfamily.org/) - https://web.archive.org/web/20091209115945/https://chrony.tuxfamily.org/
### [Reference](https://web.archive.org/web/20110722012159/http://www.skrenta.com/rt/man/timed.8.html) - https://web.archive.org/web/20110722012159/http://www.skrenta.com/rt/man/timed.8.html
### [Reference](https://web.archive.org/web/20110906014530/http://www.ntp.org/ntpfaq/NTP-s-algo.htm#Q-ACCURATE-CLOCK) - https://web.archive.org/web/20110906014530/http://www.ntp.org/ntpfaq/NTP-s-algo.htm#Q-ACCURATE-CLOCK
### [Reference](https://web.archive.org/web/20110906143547/http://technet.microsoft.com/en-us/library/cc773061(WS.10).aspx) - https://web.archive.org/web/20110906143547/http://technet.microsoft.com/en-us/library/cc773061(WS.10).aspx
### [Reference](https://web.archive.org/web/20110924184432/http://technet.microsoft.com/en-us/library/cc773013(WS.10).aspx) - https://web.archive.org/web/20110924184432/http://technet.microsoft.com/en-us/library/cc773013(WS.10).aspx
### [Reference](https://web.archive.org/web/20111102204926/http://www.eecis.udel.edu/~mills/exec.html) - https://web.archive.org/web/20111102204926/http://www.eecis.udel.edu/~mills/exec.html
### [Reference](https://web.archive.org/web/20120910031733/http://tools.ietf.org/html/rfc5905#section-14) - https://web.archive.org/web/20120910031733/http://tools.ietf.org/html/rfc5905#section-14
### [Reference](https://web.archive.org/web/20121017165107/http://blogs.technet.com/b/askds/archive/2007/10/23/high-accuracy-w32time-requirements.aspx) - https://web.archive.org/web/20121017165107/http://blogs.technet.com/b/askds/archive/2007/10/23/high-accuracy-w32time-requirements.aspx
### [Reference](https://web.archive.org/web/20130907021050/http://www.eecis.udel.edu/~mills/leap.html) - https://web.archive.org/web/20130907021050/http://www.eecis.udel.edu/~mills/leap.html
### [Reference](https://web.archive.org/web/20130907040625/http://www.eecis.udel.edu/~mills/security.html) - https://web.archive.org/web/20130907040625/http://www.eecis.udel.edu/~mills/security.html
### [Reference](https://web.archive.org/web/20131001041853/http://www.cisco.com/en/US/tech/tk869/tk769/technologies_white_paper09186a0080117070.shtml) - https://web.archive.org/web/20131001041853/http://www.cisco.com/en/US/tech/tk869/tk769/technologies_white_paper09186a0080117070.shtml
### [Reference](https://web.archive.org/web/20140124074451/http://arstechnica.com/security/2014/01/new-dos-attacks-taking-down-game-sites-deliver-crippling-100-gbps-floods/) - https://web.archive.org/web/20140124074451/http://arstechnica.com/security/2014/01/new-dos-attacks-taking-down-game-sites-deliver-crippling-100-gbps-floods/
### [Reference](https://web.archive.org/web/20140211175533/http://www.bbc.co.uk/news/technology-26136774) - https://web.archive.org/web/20140211175533/http://www.bbc.co.uk/news/technology-26136774
### [Reference](https://web.archive.org/web/20140219093152/http://support.ntp.org/bin/view/Main/SecurityNotice) - https://web.archive.org/web/20140219093152/http://support.ntp.org/bin/view/Main/SecurityNotice
### [Reference](https://web.archive.org/web/20140330131447/http://support.ntp.org/bin/view/Main/SecurityNotice#April_2010_DRDoS_Amplification_A) - https://web.archive.org/web/20140330131447/http://support.ntp.org/bin/view/Main/SecurityNotice#April_2010_DRDoS_Amplification_A
### [Reference](https://web.archive.org/web/20140718092324/http://books.google.com/books?id=pdTcJBfnbq8C&pg=PA12) - https://web.archive.org/web/20140718092324/http://books.google.com/books?id=pdTcJBfnbq8C&pg=PA12
### [Reference](https://web.archive.org/web/20141018053055/https://www.blackhat.com/docs/eu-14/materials/eu-14-Selvi-Bypassing-HTTP-Strict-Transport-Security-wp.pdf) - https://web.archive.org/web/20141018053055/https://www.blackhat.com/docs/eu-14/materials/eu-14-Selvi-Bypassing-HTTP-Strict-Transport-Security-wp.pdf
### [Reference](https://web.archive.org/web/20141220002022/https://ics-cert.us-cert.gov/advisories/ICSA-14-353-01) - https://web.archive.org/web/20141220002022/https://ics-cert.us-cert.gov/advisories/ICSA-14-353-01
### [Reference](https://web.archive.org/web/20141223013515/http://www.eecis.udel.edu/~mills/ntp.html) - https://web.archive.org/web/20141223013515/http://www.eecis.udel.edu/~mills/ntp.html
### [Reference](https://web.archive.org/web/20141224071634/http://www.i-programmer.info/news/149-security/8120-ntp-the-latest-open-source-security-problem.html) - https://web.archive.org/web/20141224071634/http://www.i-programmer.info/news/149-security/8120-ntp-the-latest-open-source-security-problem.html
### [Reference](https://web.archive.org/web/20150410021745/http://www.informationweek.com/it-life/ntps-fate-hinges-on-father-time/d/d-id/1319432?cmp=em-prog-na-na-newsltr_20150313_control&imm_mid=0ce65e&page_number=2) - https://web.archive.org/web/20150410021745/http://www.informationweek.com/it-life/ntps-fate-hinges-on-father-time/d/d-id/1319432?cmp=em-prog-na-na-newsltr_20150313_control&imm_mid=0ce65e&page_number=2
### [Reference](https://web.archive.org/web/20150410033108/http://www.informationweek.com/cloud/infrastructure-as-a-service/ntp-needs-money-is-a-foundation-the-answer/d/d-id/1319557) - https://web.archive.org/web/20150410033108/http://www.informationweek.com/cloud/infrastructure-as-a-service/ntp-needs-money-is-a-foundation-the-answer/d/d-id/1319557
### [Reference](https://web.archive.org/web/20150415002211/http://arstechnica.com/apple/2014/12/apple-automatically-patches-macs-to-fix-severe-ntp-security-flaw/) - https://web.archive.org/web/20150415002211/http://arstechnica.com/apple/2014/12/apple-automatically-patches-macs-to-fix-severe-ntp-security-flaw/
### [Reference](https://web.archive.org/web/20150802090927/https://github.com/bsdphk/Ntimed/) - https://web.archive.org/web/20150802090927/https://github.com/bsdphk/Ntimed/
### [Reference](https://web.archive.org/web/20151022140151/http://www.cs.bu.edu/~goldbe/papers/NTPattack.pdf) - https://web.archive.org/web/20151022140151/http://www.cs.bu.edu/~goldbe/papers/NTPattack.pdf
### [Reference](https://web.archive.org/web/20151024172618/http://www.cs.bu.edu/~goldbe/NTPattack.html) - https://web.archive.org/web/20151024172618/http://www.cs.bu.edu/~goldbe/NTPattack.html
### [Reference](https://web.archive.org/web/20160610113047/http://www3.cs.stonybrook.edu/~jgao/CSE590-spring11/91-ntp.pdf) - https://web.archive.org/web/20160610113047/http://www3.cs.stonybrook.edu/~jgao/CSE590-spring11/91-ntp.pdf
### [Reference](https://web.archive.org/web/20160730091110/http://rhelblog.redhat.com/2016/07/20/combining-ptp-with-ntp-to-get-the-best-of-both-worlds/) - https://web.archive.org/web/20160730091110/http://rhelblog.redhat.com/2016/07/20/combining-ptp-with-ntp-to-get-the-best-of-both-worlds/
### [Reference](https://web.archive.org/web/20161026011515/https://www.eecis.udel.edu/~mills/y2k.html) - https://web.archive.org/web/20161026011515/https://www.eecis.udel.edu/~mills/y2k.html
### [Reference](https://web.archive.org/web/20161202233231/https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/get-started/windows-time-service/windows-2016-accurate-time) - https://web.archive.org/web/20161202233231/https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/get-started/windows-time-service/windows-2016-accurate-time
### [Reference](https://web.archive.org/web/20170514214217/http://support.ntp.org/bin/view/Support/WindowsTimeService) - https://web.archive.org/web/20170514214217/http://support.ntp.org/bin/view/Support/WindowsTimeService
### [Reference](https://web.archive.org/web/20170615091357/http://what-when-how.com/computer-network-time-synchronization/how-ntp-represents-the-time-computer-network-time-synchronization/) - https://web.archive.org/web/20170615091357/http://what-when-how.com/computer-network-time-synchronization/how-ntp-represents-the-time-computer-network-time-synchronization/
### [Reference](https://web.archive.org/web/20171005123643/https://wiki.mozilla.org/images/e/e4/Chrony-report.pdf) - https://web.archive.org/web/20171005123643/https://wiki.mozilla.org/images/e/e4/Chrony-report.pdf
### [Reference](https://web.archive.org/web/20171028123642/https://www.coreinfrastructure.org/news/blogs/2017/09/securing-network-time) - https://web.archive.org/web/20171028123642/https://www.coreinfrastructure.org/news/blogs/2017/09/securing-network-time
### [Reference](https://web.archive.org/web/20171119213641/https://packages.ubuntu.com/xenial/chrony) - https://web.archive.org/web/20171119213641/https://packages.ubuntu.com/xenial/chrony
### [Reference](https://web.archive.org/web/20180101075712/https://tools.ietf.org/html/rfc5905) - https://web.archive.org/web/20180101075712/https://tools.ietf.org/html/rfc5905
### [Reference](https://web.archive.org/web/20180203195701/https://www.linuxfoundation.org/blog/cii-audit-identifies-secure-ntp-implementation/) - https://web.archive.org/web/20180203195701/https://www.linuxfoundation.org/blog/cii-audit-identifies-secure-ntp-implementation/
### [Reference](https://web.archive.org/web/20180721014309/http://www.lieberbiber.de/2017/03/14/a-look-at-the-year-20362038-problems-and-time-proofness-in-various-systems/) - https://web.archive.org/web/20180721014309/http://www.lieberbiber.de/2017/03/14/a-look-at-the-year-20362038-problems-and-time-proofness-in-various-systems/
### [Reference](https://web.archive.org/web/20181112141516/https://nlug.ml1.co.uk/2012/01/ntpq-p-output/831) - https://web.archive.org/web/20181112141516/https://nlug.ml1.co.uk/2012/01/ntpq-p-output/831
### [Reference](https://web.archive.org/web/20181201232241/https://wiki.mozilla.org/images/e/ea/Ntp-report.pdf) - https://web.archive.org/web/20181201232241/https://wiki.mozilla.org/images/e/ea/Ntp-report.pdf
### [Reference](https://web.archive.org/web/20190113232124/https://ntpsec.org/) - https://web.archive.org/web/20190113232124/https://ntpsec.org/
### [Reference](https://web.archive.org/web/20190330170620/https://books.google.com/books?id=ptSC4LpwGA0C&pg=PA582) - https://web.archive.org/web/20190330170620/https://books.google.com/books?id=ptSC4LpwGA0C&pg=PA582
### [Reference](https://web.archive.org/web/20190404122431/https://developers.google.com/time/smear) - https://web.archive.org/web/20190404122431/https://developers.google.com/time/smear
### [Reference](https://web.archive.org/web/20190504164134/http://ntpsurvey.arauc.br/) - https://web.archive.org/web/20190504164134/http://ntpsurvey.arauc.br/
### [Reference](https://web.archive.org/web/20190629174030/https://opensource.com/article/18/12/manage-ntp-chrony) - https://web.archive.org/web/20190629174030/https://opensource.com/article/18/12/manage-ntp-chrony
### [Reference](https://web.archive.org/web/20190704001204/https://wiki.mozilla.org/images/1/10/Ntpsec-report.pdf) - https://web.archive.org/web/20190704001204/https://wiki.mozilla.org/images/1/10/Ntpsec-report.pdf
### [Reference](https://web.archive.org/web/20191211062440/https://tools.ietf.org/html/rfc1305) - https://web.archive.org/web/20191211062440/https://tools.ietf.org/html/rfc1305
### [Reference](https://web.archive.org/web/20191220015844/http://phk.freebsd.dk/time/20140926/) - https://web.archive.org/web/20191220015844/http://phk.freebsd.dk/time/20140926/
### [Reference](https://web.archive.org/web/20200611155551/https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20090923-ntp) - https://web.archive.org/web/20200611155551/https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20090923-ntp
### [Reference](https://web.archive.org/web/20200626160445/https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:ntpsec&cpe_product=cpe:/::ntpsec) - https://web.archive.org/web/20200626160445/https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:ntpsec&cpe_product=cpe:/::ntpsec
### [Reference](https://web.archive.org/web/20200626200844/https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:tuxfamily&cpe_product=cpe:/::chrony) - https://web.archive.org/web/20200626200844/https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cpe_vendor=cpe:/:tuxfamily&cpe_product=cpe:/::chrony
### [Reference](https://www.coreinfrastructure.org/news/blogs/2017/09/securing-network-time) - https://www.coreinfrastructure.org/news/blogs/2017/09/securing-network-time
### [Reference](https://www.iana.org/assignments/port-numbers) - https://www.iana.org/assignments/port-numbers
### [Reference](https://datatracker.ietf.org/doc/html/rfc1059) - https://datatracker.ietf.org/doc/html/rfc1059
### [Reference](https://datatracker.ietf.org/doc/html/rfc1119) - https://datatracker.ietf.org/doc/html/rfc1119
### [Reference](https://datatracker.ietf.org/doc/html/rfc1305) - https://datatracker.ietf.org/doc/html/rfc1305
### [Reference](https://datatracker.ietf.org/doc/html/rfc4330) - https://datatracker.ietf.org/doc/html/rfc4330
### [Reference](https://datatracker.ietf.org/doc/html/rfc5905) - https://datatracker.ietf.org/doc/html/rfc5905
### [Reference](https://datatracker.ietf.org/doc/html/rfc5906) - https://datatracker.ietf.org/doc/html/rfc5906
### [Reference](https://datatracker.ietf.org/doc/html/rfc5907) - https://datatracker.ietf.org/doc/html/rfc5907
### [Reference](https://datatracker.ietf.org/doc/html/rfc5908) - https://datatracker.ietf.org/doc/html/rfc5908
### [Reference](https://datatracker.ietf.org/doc/html/rfc778) - https://datatracker.ietf.org/doc/html/rfc778
### [Reference](https://datatracker.ietf.org/doc/html/rfc781) - https://datatracker.ietf.org/doc/html/rfc781
### [Reference](https://datatracker.ietf.org/doc/html/rfc8915) - https://datatracker.ietf.org/doc/html/rfc8915
### [Reference](https://datatracker.ietf.org/doc/html/rfc956) - https://datatracker.ietf.org/doc/html/rfc956
### [Reference](https://datatracker.ietf.org/doc/html/rfc958) - https://datatracker.ietf.org/doc/html/rfc958
### [Reference](https://datatracker.ietf.org/wg/ntp/charter/) - https://datatracker.ietf.org/wg/ntp/charter/
### [Reference](https://tools.ietf.org/html/rfc1305) - https://tools.ietf.org/html/rfc1305
### [Reference](https://tools.ietf.org/html/rfc5905#section-14) - https://tools.ietf.org/html/rfc5905#section-14
### [Reference](https://www.ietf.org/timezones/data/leap-seconds.list) - https://www.ietf.org/timezones/data/leap-seconds.list
### [Reference](https://www.linuxfoundation.org/blog/cii-audit-identifies-secure-ntp-implementation/) - https://www.linuxfoundation.org/blog/cii-audit-identifies-secure-ntp-implementation/
### [Reference](https://wiki.mozilla.org/images/1/10/Ntpsec-report.pdf) - https://wiki.mozilla.org/images/1/10/Ntpsec-report.pdf
### [Reference](https://wiki.mozilla.org/images/e/e4/Chrony-report.pdf) - https://wiki.mozilla.org/images/e/e4/Chrony-report.pdf
### [Reference](https://wiki.mozilla.org/images/e/ea/Ntp-report.pdf) - https://wiki.mozilla.org/images/e/ea/Ntp-report.pdf
### [Reference](https://support.ntp.org/bin/view/Support/WindowsTimeService) - https://support.ntp.org/bin/view/Support/WindowsTimeService
### [Reference](https://www.ntp.org/) - https://www.ntp.org/
### [Reference](https://ntpsec.org) - https://ntpsec.org
### [Reference](https://chrony.tuxfamily.org/) - https://chrony.tuxfamily.org/
### [Reference](https://chrony.tuxfamily.org/doc/3.4/chrony.conf.html#hwtimestamp) - https://chrony.tuxfamily.org/doc/3.4/chrony.conf.html#hwtimestamp
### [Reference](https://git.tuxfamily.org/chrony/chrony.git/tree/NEWS?id=4.0#n6) - https://git.tuxfamily.org/chrony/chrony.git/tree/NEWS?id=4.0#n6
### [Reference](https://www.wikidata.org/wiki/Q217491#P856) - https://www.wikidata.org/wiki/Q217491#P856
### [Reference](https://www.netnod.se/time-and-frequency/how-to-use-nts) - https://www.netnod.se/time-and-frequency/how-to-use-nts
### [Reference](https://www.ijs.si/time/) - https://www.ijs.si/time/
### [Reference](https://www.bbc.co.uk/news/technology-26136774) - https://www.bbc.co.uk/news/technology-26136774
### [Reference](https://nlug.ml1.co.uk/2012/01/ntpq-p-output/831) - https://nlug.ml1.co.uk/2012/01/ntpq-p-output/831
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/a4/Chrony_4.1_screenshot.png) - https://upload.wikimedia.org/wikipedia/commons/a/a4/Chrony_4.1_screenshot.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/3f/DL_Mills-2.jpg) - https://upload.wikimedia.org/wikipedia/commons/3/3f/DL_Mills-2.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/8d/NTP-Algorithm.svg) - https://upload.wikimedia.org/wikipedia/commons/8/8d/NTP-Algorithm.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/c/c9/Network_Time_Protocol_servers_and_clients.svg) - https://upload.wikimedia.org/wikipedia/commons/c/c9/Network_Time_Protocol_servers_and_clients.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/dc/Ntpq_-p_query.png) - https://upload.wikimedia.org/wikipedia/commons/d/dc/Ntpq_-p_query.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/4/45/Usno-amc.jpg) - https://upload.wikimedia.org/wikipedia/commons/4/45/Usno-amc.jpg
### [Image](https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg) - https://upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg