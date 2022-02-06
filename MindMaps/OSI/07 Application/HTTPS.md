# HTTPS
## [URL](https://en.wikipedia.org/wiki/HTTPS) - https://en.wikipedia.org/wiki/HTTPS
## Catagories
### All Wikipedia articles in need of updating
### All articles containing potentially dated statements
### All articles with failed verification
### Articles containing potentially dated statements from April 2018
### Articles containing potentially dated statements from February 2020
### Articles with failed verification from January 2022
### Articles with short description
### CS1 maint: url-status
### Commons category link from Wikidata
### Computer-related introductions in 1994
### Cryptographic protocols
### Hypertext Transfer Protocol
### Network booting
### Secure communication
### Short description matches Wikidata
### Transport Layer Security
### URI schemes
### Use dmy dates from November 2021
### Wikipedia articles in need of updating from February 2015
### Wikipedia pending changes protected pages
### "Hypertext Transfer Protocol Secure (HTTPS) is an extension of the Hypertext Transfer Protocol (HTTP). It is used for secure communication over a computer network, and is widely used on the Internet. In HTTPS, the communication protocol is encrypted using Transport Layer Security (TLS) or, formerly, Secure Sockets Layer (SSL). The protocol is therefore also referred to as HTTP over TLS, or HTTP over SSL. 
### The principal motivations for HTTPS are authentication of the accessed website, and protection of the privacy and integrity of the exchanged data while in transit. It protects against man-in-the-middle attacks, and the bidirectional encryption of communications between a client and server protects the communications against eavesdropping and tampering. The authentication aspect of HTTPS requires a trusted third party to sign server-side digital certificates. This was historically an expensive operation, which meant fully authenticated HTTPS connections were usually found only on secured payment transaction services and other secured corporate information systems on the World Wide Web. In 2016, a campaign by the Electronic Frontier Foundation with the support of web browser developers led to the protocol becoming more prevalent. HTTPS is now used more often by web users than the original non-secure HTTP, primarily to protect page authenticity on all types of websites; secure accounts; and to keep user communications, identity, and web browsing private.
## Overview  

### The Uniform Resource Identifier (URI) scheme HTTPS has identical usage syntax to the HTTP scheme. However, HTTPS signals the browser to use an added encryption layer of SSL/TLS to protect the traffic. SSL/TLS is especially suited for HTTP, since it can provide some protection even if only one side of the communication is authenticated. This is the case with HTTP transactions over the Internet, where typically only the server is authenticated (by the client examining the server's certificate). 
### HTTPS creates a secure channel over an insecure network. This ensures reasonable protection from eavesdroppers and man-in-the-middle attacks, provided that adequate cipher suites are used and that the server certificate is verified and trusted. 
### Because HTTPS piggybacks HTTP entirely on top of TLS, the entirety of the underlying HTTP protocol can be encrypted. This includes the request URL (which particular web page was requested), query parameters, headers, and cookies (which often contain identifying information about the user). However, because website addresses and port numbers are necessarily part of the underlying TCP/IP protocols, HTTPS cannot protect their disclosure. In practice this means that even on a correctly configured web server, eavesdroppers can infer the IP address and port number of the web server, and sometimes even the domain name (e.g. www.example.org, but not the rest of the URL) that a user is communicating with, along with the amount of data transferred and the duration of the communication, though not the content of the communication.Web browsers know how to trust HTTPS websites based on certificate authorities that come pre-installed in their software. Certificate authorities are in this way being trusted by web browser creators to provide valid certificates. Therefore, a user should trust an HTTPS connection to a website if and only if all of the following are true: 

### The user trusts that the browser software correctly implements HTTPS with correctly pre-installed certificate authorities. 
### The user trusts the certificate authority to vouch only for legitimate websites. 
### The website provides a valid certificate, which means it was signed by a trusted authority. 
### The certificate correctly identifies the website (e.g., when the browser visits \"https://example.com\", the received certificate is properly for \"example.com\" and not some other entity). 
### The user trusts that the protocol's encryption layer (SSL/TLS) is sufficiently secure against eavesdroppers.HTTPS is especially important over insecure networks and networks that may be subject to tampering.  Insecure networks, such as public Wi-Fi access points, allow anyone on the same local network to packet-sniff and discover sensitive information not protected by HTTPS. Additionally, some free-to-use and paid WLAN networks have been observed tampering with webpages by engaging in packet injection in order to serve their own ads on other websites. This practice can be exploited maliciously in many ways, such as by injecting malware onto webpages and stealing users' private information.HTTPS is also important for connections over the Tor network, as malicious Tor nodes could otherwise damage or alter the contents passing through them in an insecure fashion and inject malware into the connection. This is one reason why the Electronic Frontier Foundation and the Tor Project started the development of HTTPS Everywhere, which is included in Tor Browser.As more information is revealed about global mass surveillance and criminals stealing personal information, the use of HTTPS security on all websites is becoming increasingly important regardless of the type of Internet connection being used. Even though metadata about individual pages that a user visits might not be considered sensitive, when aggregated it can reveal a lot about the user and compromise the user's privacy.Deploying HTTPS also allows the use of HTTP/2 (or its predecessor, the now-deprecated protocol SPDY), which is a new generation of HTTP designed to reduce page load times, size, and latency. 
### It is recommended to use HTTP Strict Transport Security (HSTS) with HTTPS to protect users from man-in-the-middle attacks, especially SSL stripping.HTTPS should not be confused with the seldom-used Secure HTTP (S-HTTP) specified in RFC 2660.
## Usage in websites  
### As of April 2018, 33.2% of Alexa top 1,000,000 websites use HTTPS as default, 57.1% of the Internet's 137,971 most popular websites have a secure implementation of HTTPS, and 70% of page loads (measured by Firefox Telemetry) use HTTPS.
## Browser integration  
### Most browsers display a warning if they receive an invalid certificate. Older browsers, when connecting to a site with an invalid certificate, would present the user with a dialog box asking whether they wanted to continue. Newer browsers display a warning across the entire window. Newer browsers also prominently display the site's security information in the address bar. Extended validation certificates show the legal entity on the certificate information. Most browsers also display a warning to the user when visiting a site that contains a mixture of encrypted and unencrypted content. Additionally, many web filters return a security warning when visiting prohibited websites. 

### The Electronic Frontier Foundation, opining that \"In an ideal world, every web request could be defaulted to HTTPS\", has provided an add-on called HTTPS Everywhere for Mozilla Firefox, Google Chrome, Chromium, and Android, that enables HTTPS by default for hundreds of frequently used websites.Forcing a web browser to load HTTPS content only has been supported in Firefox starting in version 83.
## Security  

### The security of HTTPS is that of the underlying TLS, which typically uses long-term public and private keys to generate a short-term session key, which is then used to encrypt the data flow between the client and the server. X.509 certificates are used to authenticate the server (and sometimes the client as well). As a consequence, certificate authorities and public key certificates are necessary to verify the relation between the certificate and its owner, as well as to generate, sign, and administer the validity of certificates. While this can be more beneficial than verifying the identities via a web of trust, the 2013 mass surveillance disclosures drew attention to certificate authorities as a potential weak point allowing man-in-the-middle attacks. An important property in this context is forward secrecy, which ensures that encrypted communications recorded in the past cannot be retrieved and decrypted should long-term secret keys or passwords be compromised in the future. Not all web servers provide forward secrecy.For HTTPS to be effective, a site must be completely hosted over HTTPS.  If some of the site's contents are loaded over HTTP (scripts or images, for example), or if only a certain page that contains sensitive information, such as a log-in page, is loaded over HTTPS while the rest of the site is loaded over plain HTTP, the user will be vulnerable to attacks and surveillance. Additionally, cookies on a site served through HTTPS must have the secure attribute enabled.  On a site that has sensitive information on it, the user and the session will get exposed every time that site is accessed with HTTP instead of HTTPS.
## Technical 
## Difference from HTTP  
### HTTPS URLs begin with \"https://\" and use port 443 by default, whereas, HTTP URLs begin with \"http://\" and use port 80 by default. 
### HTTP is not encrypted and thus is vulnerable to man-in-the-middle and eavesdropping attacks, which can let attackers gain access to website accounts and sensitive information, and modify webpages to inject malware or advertisements. HTTPS is designed to withstand such attacks and is considered secure against them (with the exception of HTTPS implementations that use deprecated versions of SSL).
## Network layers  
### HTTP operates at the highest layer of the TCP/IP model\u2014the application layer; as does the TLS security protocol (operating as a lower sublayer of the same layer), which encrypts an HTTP message prior to transmission and decrypts a message upon arrival. Strictly speaking, HTTPS is not a separate protocol, but refers to the use of ordinary HTTP over an encrypted SSL/TLS connection. 
### HTTPS encrypts all message contents, including the HTTP headers and the request/response data. With the exception of the possible CCA cryptographic attack described in the limitations section below, an attacker should at most be able to discover that a connection is taking place between two parties, along with their domain names and IP addresses.
## Server setup  
### To prepare a web server to accept HTTPS connections, the administrator must create a public key certificate for the web server. This certificate must be signed by a trusted certificate authority for the web browser to accept it without warning. The authority certifies that the certificate holder is the operator of the web server that presents it. Web browsers are generally distributed with a list of signing certificates of major certificate authorities so that they can verify certificates signed by them.
## Acquiring certificates  
### A number of commercial certificate authorities exist, offering paid-for SSL/TLS certificates of a number of types, including Extended Validation Certificates. 
### Let's Encrypt, launched in April 2016, provides free and automated service that delivers basic SSL/TLS certificates to websites. According to the Electronic Frontier Foundation, Let's Encrypt will make switching from HTTP to HTTPS \"as easy as issuing one command, or clicking one button.\" The majority of web hosts and cloud providers now leverage Let's Encrypt, providing free certificates to their customers.
## Use as access control  
### The system can also be used for client authentication in order to limit access to a web server to authorized users. To do this, the site administrator typically creates a certificate for each user, which the user loads into their browser. Normally, the certificate contains the name and e-mail address of the authorized user and is automatically checked by the server on each connection to verify the user's identity, potentially without even requiring a password.
## In case of compromised secret (private) key  
### An important property in this context is perfect forward secrecy (PFS). Possessing one of the long-term asymmetric secret keys used to establish an HTTPS session should not make it easier to derive the short-term session key to then decrypt the conversation, even at a later time. Diffie\u2013Hellman key exchange (DHE) and Elliptic curve Diffie\u2013Hellman key exchange (ECDHE) are in 2013 the only schemes known to have that property. In 2013, only 30% of Firefox, Opera, and Chromium Browser sessions used it, and nearly 0% of Apple's Safari and Microsoft Internet Explorer sessions. TLS 1.3, published in August 2018, dropped support for ciphers without forward secrecy. As of February 2020, 96.6% of web servers surveyed support some form of forward secrecy, and 52.1% will use forward secrecy with most browsers.
## Certificate revocation  
### A certificate may be revoked before it expires, for example because the secrecy of the private key has been compromised. Newer versions of popular browsers such as Firefox, Opera, and Internet Explorer on Windows Vista implement the Online Certificate Status Protocol (OCSP) to verify that this is not the case. The browser sends the certificate's serial number to the certificate authority or its delegate via OCSP (Online Certificate Status Protocol) and the authority responds, telling the browser whether the certificate is still valid or not. The CA may also issue a  CRL to tell people that these certificates are revoked. CRLs are no longer required by the CA/Browser forum, nevertheless, they are still widely used by the CAs. Most revocation statuses on the Internet disappear soon after the expiration of the certificates.
## Limitations  
### SSL (Secure Sockets Layer) and TLS (Transport Layer Security) encryption can be configured in two modes: simple and mutual. In simple mode, authentication is only performed by the server. The mutual version requires the user to install a personal client certificate in the web browser for user authentication. In either case, the level of protection depends on the correctness of the implementation of the software and the cryptographic algorithms in use. 
### SSL/TLS does not prevent the indexing of the site by a web crawler, and in some cases the URI of the encrypted resource can be inferred by knowing only the intercepted request/response size. This allows an attacker to have access to the plaintext (the publicly available static content), and the encrypted text (the encrypted version of the static content), permitting a cryptographic attack. 
### Because TLS operates at a protocol level below that of HTTP and has no knowledge of the higher-level protocols, TLS servers can only strictly present one certificate for a particular address and port combination. In the past, this meant that it was not feasible to use name-based virtual hosting with HTTPS. A solution called Server Name Indication (SNI) exists, which sends the hostname to the server before encrypting the connection, although many old browsers do not support this extension. Support for SNI is available since Firefox 2, Opera 8, Apple Safari 2.1, Google Chrome 6, and Internet Explorer 7 on Windows Vista.From an architectural point of view: 

### An SSL/TLS connection is managed by the first front machine that initiates the TLS connection. If, for any reasons (routing, traffic optimization, etc.), this front machine is not the application server and it has to decipher data, solutions have to be found to propagate user authentication information or certificate to the application server, which needs to know who is going to be connected. 
### For SSL/TLS with mutual authentication, the SSL/TLS session is managed by the first server that initiates the connection. In situations where encryption has to be propagated along chained servers, session timeOut management becomes extremely tricky to implement. 
### Security is maximal with mutual SSL/TLS, but on the client-side there is no way to properly end the SSL/TLS connection and disconnect the user except by waiting for the server session to expire or by closing all related client applications.A sophisticated type of man-in-the-middle attack called SSL stripping was presented at the 2009 Blackhat Conference. This type of attack defeats the security provided by HTTPS by changing the https: link into an http: link, taking advantage of the fact that few Internet users actually type \"https\" into their browser interface: they get to a secure site by clicking on a link, and thus are fooled into thinking that they are using HTTPS when in fact they are using HTTP. The attacker then communicates in clear with the client. This prompted the development of a countermeasure in HTTP called HTTP Strict Transport Security. 
### HTTPS has been shown to be vulnerable to a range of traffic analysis attacks. Traffic analysis attacks are a type of side-channel attack that relies on variations in the timing and size of traffic in order to infer properties about the encrypted traffic itself. Traffic analysis is possible because SSL/TLS encryption changes the contents of traffic, but has minimal impact on the size and timing of traffic. In May 2010, a research paper by researchers from Microsoft Research and Indiana University discovered that detailed sensitive user data can be inferred from side channels such as packet sizes. The researchers found that, despite HTTPS protection in several high-profile, top-of-the-line web applications in healthcare, taxation, investment, and web search, an eavesdropper could infer the illnesses/medications/surgeries of the user, his/her family income, and investment secrets. Although this work demonstrated the vulnerability of HTTPS to traffic analysis, the approach presented by the authors required manual analysis and focused specifically on web applications protected by HTTPS. 
### The fact that most modern websites, including Google, Yahoo!, and Amazon, use HTTPS causes problems for many users trying to access public Wi-Fi hot spots, because a Wi-Fi hot spot login page fails to load if the user tries to open an HTTPS resource. Several websites, such as neverssl.com and nonhttps.com, guarantee that they will always remain accessible by HTTP.
## History  
### Netscape Communications created HTTPS in 1994 for its Netscape Navigator web browser. Originally, HTTPS was used with the SSL protocol. As SSL evolved into Transport Layer Security (TLS), HTTPS was formally specified by RFC 2818 in May 2000. Google announced in February 2018 that its Chrome browser would mark HTTP sites as \"Not Secure\" after July 2018. This move was to encourage website owners to implement HTTPS, as an effort to make the World Wide Web more secure.
## See also  
### Bullrun (decryption program) \u2013  a secret anti-encryption program run by the US National Security Agency 
### Computer security 
### HSTS 
### Opportunistic encryption 
### Stunnel
## References 
## External links  
### RFC 2818: HTTP Over TLS 
### RFC 5246: The Transport Layer Security Protocol 1.2 
### RFC 6101: The Secure Sockets Layer (SSL) Protocol Version 3.0 
### How HTTPS works ...in a comic! 
### Is TLS fast yet?"
## References
### [Reference](http://www.eweek.com/security/let-s-encrypt-effort-aims-to-improve-internet-security) - http://www.eweek.com/security/let-s-encrypt-effort-aims-to-improve-internet-security
### [Reference](http://neverssl.com/) - http://neverssl.com/
### [Reference](http://www.nonhttps.com) - http://www.nonhttps.com
### [Reference](http://arxiv.org/abs/2102.04288) - http://arxiv.org/abs/2102.04288
### [Reference](https://example.com) - https://example.com
### [Reference](https://www.exploit-db.com/docs/english/13026-the-pirate-bay-un-ssl.pdf) - https://www.exploit-db.com/docs/english/13026-the-pirate-bay-un-ssl.pdf
### [Reference](https://books.google.com/books?id=FLvsis4_QhEC&pg=PA344) - https://books.google.com/books?id=FLvsis4_QhEC&pg=PA344
### [Reference](https://support.google.com/chrome/a/answer/6080885?hl=en) - https://support.google.com/chrome/a/answer/6080885?hl=en
### [Reference](https://support.google.com/webmasters/answer/6073543?hl=en) - https://support.google.com/webmasters/answer/6073543?hl=en
### [Reference](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html) - https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html
### [Reference](https://www.instantssl.com/ssl-certificate-products/https.html) - https://www.instantssl.com/ssl-certificate-products/https.html
### [Reference](https://istlsfastyet.com/) - https://istlsfastyet.com/
### [Reference](https://docs.microsoft.com/en-us/previous-versions/aa980989(v=msdn.10)) - https://docs.microsoft.com/en-us/previous-versions/aa980989(v=msdn.10)
### [Reference](https://blogs.msdn.microsoft.com/ie/2005/10/22/upcoming-https-improvements-in-internet-explorer-7-beta-2/) - https://blogs.msdn.microsoft.com/ie/2005/10/22/upcoming-https-improvements-in-internet-explorer-7-beta-2/
### [Reference](https://www.microsoft.com/en-us/research/publication/side-channel-leaks-in-web-applications-a-reality-today-a-challenge-tomorrow/) - https://www.microsoft.com/en-us/research/publication/side-channel-leaks-in-web-applications-a-reality-today-a-challenge-tomorrow/
### [Reference](https://news.netcraft.com/archives/2013/06/25/ssl-intercepted-today-decrypted-tomorrow.html) - https://news.netcraft.com/archives/2013/06/25/ssl-intercepted-today-decrypted-tomorrow.html
### [Reference](https://open.blogs.nytimes.com/2014/11/13/embracing-https/) - https://open.blogs.nytimes.com/2014/11/13/embracing-https/
### [Reference](https://news.softpedia.com/news/Opera-8-launched-on-FTP-1330.shtml) - https://news.softpedia.com/news/Opera-8-launched-on-FTP-1330.shtml
### [Reference](https://news.softpedia.com/news/let-s-encrypt-launched-today-currently-protects-3-8-million-domains-502857.shtml) - https://news.softpedia.com/news/let-s-encrypt-launched-today-currently-protects-3-8-million-domains-502857.shtml
### [Reference](https://www.ssllabs.com/ssl-pulse/) - https://www.ssllabs.com/ssl-pulse/
### [Reference](https://statoperator.com/research/https-usage-statistics-on-top-websites/) - https://statoperator.com/research/https-usage-statistics-on-top-websites/
### [Reference](https://w3techs.com/technologies/details/ce-httpsdefault/all/all) - https://w3techs.com/technologies/details/ce-httpsdefault/all/all
### [Reference](https://www.wired.com/2010/03/packet-forensics/) - https://www.wired.com/2010/03/packet-forensics/
### [Reference](https://www.youtube.com/watch?v=cBhZ6S0PFCY) - https://www.youtube.com/watch?v=cBhZ6S0PFCY
### [Reference](https://zapier.com/blog/open-wifi-login-page/) - https://zapier.com/blog/open-wifi-login-page/
### [Reference](https://httpd.apache.org/docs/2.0/ssl/ssl_faq.html#vhosts) - https://httpd.apache.org/docs/2.0/ssl/ssl_faq.html#vhosts
### [Reference](https://web.archive.org/web/20110605022218/https://www.eff.org/https-everywhere) - https://web.archive.org/web/20110605022218/https://www.eff.org/https-everywhere
### [Reference](https://web.archive.org/web/20110825095059/http://tools.ietf.org/html/rfc2560) - https://web.archive.org/web/20110825095059/http://tools.ietf.org/html/rfc2560
### [Reference](https://web.archive.org/web/20150212105201/https://www.instantssl.com/ssl-certificate-products/https.html) - https://web.archive.org/web/20150212105201/https://www.instantssl.com/ssl-certificate-products/https.html
### [Reference](https://web.archive.org/web/20150301023624/https://support.google.com/webmasters/answer/6073543?hl=en) - https://web.archive.org/web/20150301023624/https://support.google.com/webmasters/answer/6073543?hl=en
### [Reference](https://web.archive.org/web/20160104234608/https://www.eff.org/deeplinks/2010/03/researchers-reveal-likelihood-governments-fake-ssl) - https://web.archive.org/web/20160104234608/https://www.eff.org/deeplinks/2010/03/researchers-reveal-likelihood-governments-fake-ssl
### [Reference](https://web.archive.org/web/20171202155646/https://www.ssllabs.com/ssl-pulse/) - https://web.archive.org/web/20171202155646/https://www.ssllabs.com/ssl-pulse/
### [Reference](https://web.archive.org/web/20180620001518/https://www.exploit-db.com/docs/english/13026-the-pirate-bay-un-ssl.pdf) - https://web.archive.org/web/20180620001518/https://www.exploit-db.com/docs/english/13026-the-pirate-bay-un-ssl.pdf
### [Reference](https://web.archive.org/web/20180620042059/https://moxie.org/software/sslstrip/index.html) - https://web.archive.org/web/20180620042059/https://moxie.org/software/sslstrip/index.html
### [Reference](https://web.archive.org/web/20180722120329/https://www.microsoft.com/en-us/research/publication/side-channel-leaks-in-web-applications-a-reality-today-a-challenge-tomorrow/) - https://web.archive.org/web/20180722120329/https://www.microsoft.com/en-us/research/publication/side-channel-leaks-in-web-applications-a-reality-today-a-challenge-tomorrow/
### [Reference](https://web.archive.org/web/20180810143254/https://zapier.com/blog/open-wifi-login-page/) - https://web.archive.org/web/20180810143254/https://zapier.com/blog/open-wifi-login-page/
### [Reference](https://web.archive.org/web/20180810173628/https://blog.ebrahim.org/2006/02/21/server-name-indication-sni/) - https://web.archive.org/web/20180810173628/https://blog.ebrahim.org/2006/02/21/server-name-indication-sni/
### [Reference](https://web.archive.org/web/20180810204919/https://freedom.press/news-advocacy/fifteen-months-after-the-nsa-revelations-why-arenat-more-news-organizations-using-https/) - https://web.archive.org/web/20180810204919/https://freedom.press/news-advocacy/fifteen-months-after-the-nsa-revelations-why-arenat-more-news-organizations-using-https/
### [Reference](https://web.archive.org/web/20180901224536/http://neverssl.com/) - https://web.archive.org/web/20180901224536/http://neverssl.com/
### [Reference](https://web.archive.org/web/20180920113838/https://blogs.msdn.microsoft.com/ie/2005/10/22/upcoming-https-improvements-in-internet-explorer-7-beta-2/) - https://web.archive.org/web/20180920113838/https://blogs.msdn.microsoft.com/ie/2005/10/22/upcoming-https-improvements-in-internet-explorer-7-beta-2/
### [Reference](https://web.archive.org/web/20181006021916/https://news.netcraft.com/archives/2013/06/25/ssl-intercepted-today-decrypted-tomorrow.html) - https://web.archive.org/web/20181006021916/https://news.netcraft.com/archives/2013/06/25/ssl-intercepted-today-decrypted-tomorrow.html
### [Reference](https://web.archive.org/web/20181008070112/https://bugzilla.mozilla.org/show_bug.cgi?id=116169) - https://web.archive.org/web/20181008070112/https://bugzilla.mozilla.org/show_bug.cgi?id=116169
### [Reference](https://web.archive.org/web/20181010233702/https://www.eff.org/https-everywhere/deploying-https) - https://web.archive.org/web/20181010233702/https://www.eff.org/https-everywhere/deploying-https
### [Reference](https://web.archive.org/web/20181017052428/http://www.nonhttps.com/) - https://web.archive.org/web/20181017052428/http://www.nonhttps.com/
### [Reference](https://web.archive.org/web/20181017052432/https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html) - https://web.archive.org/web/20181017052432/https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html
### [Reference](https://web.archive.org/web/20181018063732/https://www.mozilla.org/en-US/privacy/) - https://web.archive.org/web/20181018063732/https://www.mozilla.org/en-US/privacy/
### [Reference](https://web.archive.org/web/20181019105423/http://httpd.apache.org/docs/2.0/ssl/ssl_faq.html#vhosts) - https://web.archive.org/web/20181019105423/http://httpd.apache.org/docs/2.0/ssl/ssl_faq.html#vhosts
### [Reference](https://web.archive.org/web/20181019171534/https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) - https://web.archive.org/web/20181019171534/https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
### [Reference](https://web.archive.org/web/20181019221028/https://letsencrypt.org/stats/) - https://web.archive.org/web/20181019221028/https://letsencrypt.org/stats/
### [Reference](https://web.archive.org/web/20181031095731/https://tools.ietf.org/html/rfc2818) - https://web.archive.org/web/20181031095731/https://tools.ietf.org/html/rfc2818
### [Reference](https://web.archive.org/web/20181114011956/https://www.eff.org/https-everywhere/faq/) - https://web.archive.org/web/20181114011956/https://www.eff.org/https-everywhere/faq/
### [Reference](https://web.archive.org/web/20181118154608/https://justinsomnia.org/2012/04/hotel-wifi-javascript-injection/) - https://web.archive.org/web/20181118154608/https://justinsomnia.org/2012/04/hotel-wifi-javascript-injection/
### [Reference](https://web.archive.org/web/20181118160126/https://www.eff.org/deeplinks/2014/11/certificate-authority-encrypt-entire-web) - https://web.archive.org/web/20181118160126/https://www.eff.org/deeplinks/2014/11/certificate-authority-encrypt-entire-web
### [Reference](https://web.archive.org/web/20181120144918/https://www.youtube.com/watch?v=cBhZ6S0PFCY) - https://web.archive.org/web/20181120144918/https://www.youtube.com/watch?v=cBhZ6S0PFCY
### [Reference](https://web.archive.org/web/20181125102636/https://www.eff.org/deeplinks/2010/06/encrypt-web-https-everywhere-firefox-extension) - https://web.archive.org/web/20181125102636/https://www.eff.org/deeplinks/2010/06/encrypt-web-https-everywhere-firefox-extension
### [Reference](https://web.archive.org/web/20190108190000/https://open.blogs.nytimes.com/2014/11/13/embracing-https/) - https://web.archive.org/web/20190108190000/https://open.blogs.nytimes.com/2014/11/13/embracing-https/
### [Reference](https://web.archive.org/web/20190117142906/https://www.wired.com/2010/03/packet-forensics/) - https://web.archive.org/web/20190117142906/https://www.wired.com/2010/03/packet-forensics/
### [Reference](https://web.archive.org/web/20190209055124/https://books.google.com/books?id=FLvsis4_QhEC&pg=PA344) - https://web.archive.org/web/20190209055124/https://books.google.com/books?id=FLvsis4_QhEC&pg=PA344
### [Reference](https://web.archive.org/web/20190209055127/https://support.google.com/chrome/a/answer/6080885?hl=en) - https://web.archive.org/web/20190209055127/https://support.google.com/chrome/a/answer/6080885?hl=en
### [Reference](https://web.archive.org/web/20190209055128/https://news.softpedia.com/news/Opera-8-launched-on-FTP-1330.shtml) - https://web.archive.org/web/20190209055128/https://news.softpedia.com/news/Opera-8-launched-on-FTP-1330.shtml
### [Reference](https://web.archive.org/web/20190209055129/https://news.softpedia.com/news/let-s-encrypt-launched-today-currently-protects-3-8-million-domains-502857.shtml) - https://web.archive.org/web/20190209055129/https://news.softpedia.com/news/let-s-encrypt-launched-today-currently-protects-3-8-million-domains-502857.shtml
### [Reference](https://web.archive.org/web/20190209055130/https://statoperator.com/research/https-usage-statistics-on-top-websites/) - https://web.archive.org/web/20190209055130/https://statoperator.com/research/https-usage-statistics-on-top-websites/
### [Reference](https://web.archive.org/web/20190215213454/https://www.ssllabs.com/ssl-pulse/) - https://web.archive.org/web/20190215213454/https://www.ssllabs.com/ssl-pulse/
### [Reference](https://web.archive.org/web/20190424215132/https://blog.chromium.org/2018/02/a-secure-web-is-here-to-stay.html) - https://web.archive.org/web/20190424215132/https://blog.chromium.org/2018/02/a-secure-web-is-here-to-stay.html
### [Reference](https://web.archive.org/web/20190801134536/https://w3techs.com/technologies/details/ce-httpsdefault/all/all) - https://web.archive.org/web/20190801134536/https://w3techs.com/technologies/details/ce-httpsdefault/all/all
### [Reference](https://web.archive.org/web/20191118094200/https://www.eff.org/encrypt-the-web) - https://web.archive.org/web/20191118094200/https://www.eff.org/encrypt-the-web
### [Reference](https://arxiv.org/abs/2102.04288) - https://arxiv.org/abs/2102.04288
### [Reference](https://cabforum.org/baseline-requirements-documents/) - https://cabforum.org/baseline-requirements-documents/
### [Reference](https://blog.chromium.org/2018/02/a-secure-web-is-here-to-stay.html) - https://blog.chromium.org/2018/02/a-secure-web-is-here-to-stay.html
### [Reference](https://blog.ebrahim.org/2006/02/21/server-name-indication-sni/) - https://blog.ebrahim.org/2006/02/21/server-name-indication-sni/
### [Reference](https://www.eff.org/deeplinks/2010/03/researchers-reveal-likelihood-governments-fake-ssl) - https://www.eff.org/deeplinks/2010/03/researchers-reveal-likelihood-governments-fake-ssl
### [Reference](https://www.eff.org/deeplinks/2010/06/encrypt-web-https-everywhere-firefox-extension) - https://www.eff.org/deeplinks/2010/06/encrypt-web-https-everywhere-firefox-extension
### [Reference](https://www.eff.org/deeplinks/2014/11/certificate-authority-encrypt-entire-web) - https://www.eff.org/deeplinks/2014/11/certificate-authority-encrypt-entire-web
### [Reference](https://www.eff.org/encrypt-the-web) - https://www.eff.org/encrypt-the-web
### [Reference](https://www.eff.org/https-everywhere) - https://www.eff.org/https-everywhere
### [Reference](https://www.eff.org/https-everywhere/deploying-https) - https://www.eff.org/https-everywhere/deploying-https
### [Reference](https://www.eff.org/https-everywhere/faq) - https://www.eff.org/https-everywhere/faq
### [Reference](https://tools.ietf.org/html/rfc2560) - https://tools.ietf.org/html/rfc2560
### [Reference](https://tools.ietf.org/html/rfc2818) - https://tools.ietf.org/html/rfc2818
### [Reference](https://tools.ietf.org/html/rfc5246) - https://tools.ietf.org/html/rfc5246
### [Reference](https://tools.ietf.org/html/rfc6101) - https://tools.ietf.org/html/rfc6101
### [Reference](https://justinsomnia.org/2012/04/hotel-wifi-javascript-injection/) - https://justinsomnia.org/2012/04/hotel-wifi-javascript-injection/
### [Reference](https://letsencrypt.org/stats/) - https://letsencrypt.org/stats/
### [Reference](https://moxie.org/software/sslstrip/index.html) - https://moxie.org/software/sslstrip/index.html
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=116169) - https://bugzilla.mozilla.org/show_bug.cgi?id=116169
### [Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
### [Reference](https://support.mozilla.org/en-US/kb/https-only-prefs) - https://support.mozilla.org/en-US/kb/https-only-prefs
### [Reference](https://www.mozilla.org/en-US/privacy/) - https://www.mozilla.org/en-US/privacy/
### [Reference](https://www.torproject.org/projects/torbrowser.html.en) - https://www.torproject.org/projects/torbrowser.html.en
### [Reference](https://freedom.press/news-advocacy/fifteen-months-after-the-nsa-revelations-why-arenat-more-news-organizations-using-https/) - https://freedom.press/news-advocacy/fifteen-months-after-the-nsa-revelations-why-arenat-more-news-organizations-using-https/
### [Reference](https://archive.today/20130717222709/https://www.torproject.org/projects/torbrowser.html.en) - https://archive.today/20130717222709/https://www.torproject.org/projects/torbrowser.html.en
### [Reference](https://howhttps.works:) - https://howhttps.works:
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/7c/Extended_Validation_on_Firefox_89_screenshot.png) - https://upload.wikimedia.org/wikipedia/commons/7/7c/Extended_Validation_on_Firefox_89_screenshot.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/b/b1/HTTPS_on_Firefox_89_screenshot.png) - https://upload.wikimedia.org/wikipedia/commons/b/b1/HTTPS_on_Firefox_89_screenshot.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/5/5b/HTTP_logo.svg) - https://upload.wikimedia.org/wikipedia/commons/5/5b/HTTP_logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/da/Internet2.jpg) - https://upload.wikimedia.org/wikipedia/commons/d/da/Internet2.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/4/4e/Self-signed_certificate_warning_on_Firefox_89_screenshot.png) - https://upload.wikimedia.org/wikipedia/commons/4/4e/Self-signed_certificate_warning_on_Firefox_89_screenshot.png
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/b/b7/Pending-protection-shackle.svg) - https://upload.wikimedia.org/wikipedia/en/b/b7/Pending-protection-shackle.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg) - https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg