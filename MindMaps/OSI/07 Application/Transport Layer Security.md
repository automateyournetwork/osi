# Transport Layer Security
## [URL](https://en.wikipedia.org/wiki/Transport_Layer_Security) - https://en.wikipedia.org/wiki/Transport_Layer_Security
## Catagories
### All articles containing potentially dated statements
### All articles with failed verification
### All articles with unsourced statements
### Articles containing potentially dated statements from April 2016
### Articles containing potentially dated statements from August 2019
### Articles containing potentially dated statements from July 2021
### Articles with failed verification from January 2022
### Articles with short description
### Articles with unsourced statements from August 2016
### Articles with unsourced statements from December 2016
### Articles with unsourced statements from February 2015
### Articles with unsourced statements from February 2019
### Articles with unsourced statements from January 2015
### CS1 errors: generic name
### CS1 errors: missing periodical
### CS1 maint: multiple names: authors list
### CS1 maint: uses authors parameter
### Commons category link is on Wikidata
### Computer-related introductions in 1999
### Cryptographic protocols
### Presentation layer protocols
### Short description matches Wikidata
### Transport Layer Security
### Webarchive template wayback links
### "Transport Layer Security (TLS), the successor of the now-deprecated Secure Sockets Layer (SSL), is a cryptographic protocol designed to provide communications security over a computer network. The protocol is widely used in applications such as email, instant messaging, and voice over IP, but its use in securing HTTPS remains the most publicly visible. 
### The TLS protocol aims primarily to provide cryptography, including privacy (confidentiality), integrity, and authenticity through the use of certificates, between two or more communicating computer applications. It runs in the application layer and is itself composed of two layers: the TLS record and the TLS handshake protocols. 
### TLS is a proposed Internet Engineering Task Force (IETF) standard, first defined in 1999, and the current version is TLS 1.3 defined in August 2018. TLS builds on the earlier SSL specifications (1994, 1995, 1996) developed by Netscape Communications for adding the HTTPS protocol to their Navigator web browser.
## Description  
### Client-server applications use the TLS protocol to communicate across a network in a way designed to prevent eavesdropping and tampering. 
### Since applications can communicate either with or without TLS (or SSL), it is necessary for the client to request that the server sets up a TLS connection. One of the main ways of achieving this is to use a different port number for TLS connections. For example, port 80 is typically used for unencrypted HTTP traffic while port 443 is the common port used for encrypted HTTPS traffic. Another mechanism is for the client to make a protocol-specific request to the server to switch the connection to TLS; for example, by making a STARTTLS request when using the mail and news protocols. 
### Once the client and server have agreed to use TLS, they negotiate a stateful connection by using a handshaking procedure. The protocols use a handshake with an asymmetric cipher to establish not only cipher settings but also a session-specific shared key with which further communication is encrypted using a symmetric cipher. During this handshake, the client and server agree on various parameters used to establish the connection's security: 

### The handshake begins when a client connects to a TLS-enabled server requesting a secure connection and the client presents a list of supported cipher suites (ciphers and hash functions). 
### From this list, the server picks a cipher and hash function that it also supports and notifies the client of the decision. 
### The server usually then provides identification in the form of a digital certificate. The certificate contains the server name, the trusted certificate authority (CA) that vouches for the authenticity of the certificate, and the server's public encryption key. 
### The client confirms the validity of the certificate before proceeding. 
### To generate the session keys used for the secure connection, the client either: 
### encrypts a random number (PreMasterSecret) with the server's public key and sends the result to the server (which only the server should be able to decrypt with its private key); both parties then use the random number to generate a unique session key for subsequent encryption and decryption of data during the session 
### uses Diffie\u2013Hellman key exchange to securely generate a random and unique session key for encryption and decryption that has the additional property of forward secrecy: if the server's private key is disclosed in future, it cannot be used to decrypt the current session, even if the session is intercepted and recorded by a third party.This concludes the handshake and begins the secured connection, which is encrypted and decrypted with the session key until the connection closes. If any one of the above steps fails, then the TLS handshake fails and the connection is not created. 
### TLS and SSL do not fit neatly into any single layer of the OSI model or the TCP/IP model. TLS runs \"on top of some reliable transport protocol (e.g., TCP),\" which would imply that it is above the transport layer. It serves encryption to higher layers, which is normally the function of the presentation layer. However, applications generally use TLS as if it were a transport layer, even though applications using TLS must actively control initiating TLS handshakes and handling of exchanged authentication certificates.When secured by TLS, connections between a client (e.g., a web browser) and a server (e.g., wikipedia.org) should have one or more of the following properties: 

### The connection is private (or secure) because a symmetric-key algorithm is used to encrypt the data transmitted. The keys for this symmetric encryption are generated uniquely for each connection and are based on a shared secret that was negotiated at the start of the session. The server and client negotiate the details of which encryption algorithm and cryptographic keys to use before the first byte of data is transmitted (see below). The negotiation of a shared secret is both secure (the negotiated secret is unavailable to eavesdroppers and cannot be obtained, even by an attacker who places themself in the middle of the connection) and reliable (no attacker can modify the communications during the negotiation without being detected). 
### The identity of the communicating parties can be authenticated using public-key cryptography. This authentication is required for the server and optional for the client. 
### The connection is reliable because each message transmitted includes a message integrity check using a message authentication code to prevent undetected loss or alteration of the data during transmission.:\u200a3\u200aIn addition to the above, careful configuration of TLS can provide additional privacy-related properties such as forward secrecy, ensuring that any future disclosure of encryption keys cannot be used to decrypt any TLS communications recorded in the past. 
### TLS supports many different methods for exchanging keys, encrypting data, and authenticating message integrity. As a result, secure configuration of TLS involves many configurable parameters, and not all choices provide all of the privacy-related properties described in the list above (see the tables below \u00a7 Key exchange, \u00a7 Cipher security, and \u00a7 Data integrity). 
### Attempts have been made to subvert aspects of the communications security that TLS seeks to provide, and the protocol has been revised several times to address these security threats. Developers of web browsers have repeatedly revised their products to defend against potential security weaknesses after these were discovered (see TLS/SSL support history of web browsers).
## History and development 
## Secure Data Network System  

### The Transport Layer Security Protocol (TLS), together with several other basic network security platforms, was developed through a joint initiative begun in August 1986, among the National Security Agency, the National Bureau of Standards, the Defense Communications Agency, and twelve communications and computer corporations who initiated a special project called the Secure Data Network System (SDNS). The program was described in September 1987 at the 10th National Computer Security Conference in an extensive set of published papers. The innovative research program focused on designing the next generation of secure computer communications network and product specifications to be implemented for applications on public and private internets. It was intended to complement the rapidly emerging new OSI internet standards moving forward both in the U.S. government's GOSIP Profiles and in the huge ITU-ISO JTC1 internet effort internationally. Originally known as the SP4 protocol, it was renamed TLS and subsequently published in 1995 as international standard ITU-T X.274| ISO/IEC 10736:1995.
## Secure Network Programming  
### Early research efforts towards transport layer security included the Secure Network Programming (SNP) application programming interface (API), which in 1993 explored the approach of having a secure transport layer API closely resembling Berkeley sockets, to facilitate retrofitting pre-existing network applications with security measures.
## SSL 1.0, 2.0, and 3.0  

### Netscape developed the original SSL protocols, and Taher Elgamal, chief scientist at Netscape Communications from 1995 to 1998, has been described as the \"father of SSL\". SSL version 1.0 was never publicly released because of serious security flaws in the protocol. Version 2.0, after being released in February 1995 was quickly discovered to contain a number of security and usability flaws. It used the same cryptographic keys for message authentication and encryption. It had a weak MAC construction that used the MD5 hash function with a secret prefix, making it vulnerable to length extension attacks. And it provided no protection for either the opening handshake or an explicit message close, both of which meant man-in-the-middle attacks could go undetected. Moreover, SSL 2.0 assumed a single service and a fixed domain certificate, conflicting with the widely used feature of virtual hosting in Web servers, so most websites were effectively impaired from using SSL. 
### These flaws necessitated the complete redesign of the protocol to SSL version 3.0. Released in 1996, it was produced by Paul Kocher working with Netscape engineers Phil Karlton and Alan Freier, with a reference implementation by Christopher Allen and Tim Dierks of Consensus Development. Newer versions of SSL/TLS are based on SSL 3.0. The 1996 draft of SSL 3.0 was published by IETF as a historical document in RFC 6101. 
### SSL 2.0 was deprecated in 2011 by RFC 6176. In 2014, SSL 3.0 was found to be vulnerable to the POODLE attack that affects all block ciphers in SSL; RC4, the only non-block cipher supported by SSL 3.0, is also feasibly broken as used in SSL 3.0. SSL 3.0 was deprecated in June 2015 by RFC 7568.
## TLS 1.0  
### TLS 1.0 was first defined in RFC 2246 in January 1999 as an upgrade of SSL Version 3.0, and written by Christopher Allen and Tim Dierks of Consensus Development. As stated in the RFC, \"the differences between this protocol and SSL 3.0 are not dramatic, but they are significant enough to preclude interoperability between TLS 1.0 and SSL 3.0\". Tim Dierks later wrote that these changes, and the renaming from \"SSL\" to \"TLS\", were a face-saving gesture to Microsoft, \"so it wouldn't look [like] the IETF was just rubberstamping Netscape's protocol\".The PCI Council suggested that organizations migrate from TLS 1.0 to TLS 1.1 or higher before June 30, 2018. In October 2018, Apple, Google, Microsoft, and Mozilla jointly announced they would deprecate TLS 1.0 and 1.1 in March 2020.
## TLS 1.1  
### TLS 1.1 was defined in RFC 4346 in April 2006. It is an update from TLS version 1.0. Significant differences in this version include: 

### Added protection against cipher-block chaining (CBC) attacks. 
### The implicit initialization vector (IV) was replaced with an explicit IV. 
### Change in handling of padding errors. 
### Support for IANA registration of parameters.:\u200a2\u200aSupport for TLS versions 1.0 and 1.1 was widely deprecated by web sites around 2020, disabling access to Firefox versions before 24 and Google Chrome before 29.
## TLS 1.2  
### TLS 1.2 was defined in RFC 5246 in August 2008. It is based on the earlier TLS 1.1 specification. Major differences include: 

### The MD5\u2013SHA-1 combination in the pseudorandom function (PRF) was replaced with SHA-256, with an option to use cipher suite specified PRFs. 
### The MD5\u2013SHA-1 combination in the finished message hash was replaced with SHA-256, with an option to use cipher suite specific hash algorithms. However, the size of the hash in the finished message must still be at least 96 bits. 
### The MD5\u2013SHA-1 combination in the digitally signed element was replaced with a single hash negotiated during handshake, which defaults to SHA-1. 
### Enhancement in the client's and server's ability to specify which hashes and signature algorithms they accept. 
### Expansion of support for authenticated encryption ciphers, used mainly for Galois/Counter Mode (GCM) and CCM mode of Advanced Encryption Standard (AES) encryption. 
### TLS Extensions definition and AES cipher suites were added.:\u200a2\u200aAll TLS versions were further refined in RFC 6176 in March 2011, removing their backward compatibility with SSL such that TLS sessions never negotiate the use of Secure Sockets Layer (SSL) version 2.0.
## TLS 1.3  
### TLS 1.3 was defined in RFC 8446 in August 2018. It is based on the earlier TLS 1.2 specification. Major differences from TLS 1.2 include: 
### Separating key agreement and authentication algorithms from the cipher suites 
### Removing support for weak and less-used named elliptic curves 
### Removing support for MD5 and SHA-224 cryptographic hash functions 
### Requiring digital signatures even when a previous configuration is used 
### Integrating HKDF and the semi-ephemeral DH proposal 
### Replacing resumption with PSK and tickets 
### Supporting 1-RTT handshakes and initial support for 0-RTT 
### Mandating perfect forward secrecy, by means of using ephemeral keys during the (EC)DH key agreement 
### Dropping support for many insecure or obsolete features including compression, renegotiation, non-AEAD ciphers, non-PFS key exchange (among which are static RSA and static DH key exchanges), custom DHE groups, EC point format negotiation, Change Cipher Spec protocol, Hello message UNIX time, and the length field AD input to AEAD ciphers 
### Prohibiting SSL or RC4 negotiation for backwards compatibility 
### Integrating use of session hash 
### Deprecating use of the record layer version number and freezing the number for improved backwards compatibility 
### Moving some security-related algorithm details from an appendix to the specification and relegating ClientKeyShare to an appendix 
### Adding the ChaCha20 stream cipher with the Poly1305 message authentication code 
### Adding the Ed25519 and Ed448 digital signature algorithms 
### Adding the x25519 and x448 key exchange protocols 
### Adding support for sending multiple OCSP responses 
### Encrypting all handshake messages after the ServerHelloNetwork Security Services (NSS), the cryptography library developed by Mozilla and used by its web browser Firefox, enabled TLS 1.3 by default in February 2017. TLS 1.3 support was subsequently added \u2014 but due to compatibility issues for a small number of users, not automatically enabled \u2014 to Firefox 52.0, which was released in March 2017. TLS 1.3 was enabled by default in May 2018 with the release of Firefox 60.0.Google Chrome set TLS 1.3 as the default version for a short time in 2017. It then removed it as the default, due to incompatible middleboxes such as Blue Coat web proxies.During the IETF 100 Hackathon which took place in Singapore in 2017, The TLS Group worked on adapting open-source applications to use TLS 1.3. The TLS group was made up of individuals from Japan, United Kingdom, and Mauritius via the cyberstorm.mu team. This work was continued in the IETF 101 Hackathon in London, and the IETF 102 Hackathon in Montreal.wolfSSL enabled the use of TLS 1.3 as of version 3.11.1, released in May 2017. As the first commercial TLS 1.3 implementation, wolfSSL 3.11.1 supported Draft 18 and now supports Draft 28, the final version, as well as many older versions. A series of blogs were published on the performance difference between TLS 1.2 and 1.3.In September 2018, the popular OpenSSL project released version 1.1.1 of its library, in which support for TLS 1.3 was \"the headline new feature\".Support for TLS 1.3 was first added to SChannel with Windows 11 and Windows Server 2022.
## Enterprise Transport Security  
### The Electronic Frontier Foundation praised TLS 1.3 and expressed concern about the variant protocol Enterprise Transport Security (ETS) that intentionally disables important security measures in TLS 1.3. Originally called Enterprise TLS (eTLS), ETS is a published standard known as the 'ETSI TS103523-3', \"Middlebox Security Protocol, Part3: Enterprise Transport Security\". It is intended for use entirely within proprietary networks such as banking systems. ETS does not support forward secrecy so as to allow third-party organizations connected to the proprietary networks to be able to use their private key to monitor network traffic for the detection of malware and to make it easier to conduct audits. Despite the claimed benefits, the EFF warned that the loss of forward secrecy could make it easier for data to be exposed along with saying that there are better ways to analyze traffic.
## Digital certificates  

### A digital certificate certifies the ownership of a public key by the named subject of the certificate, and indicates certain expected usages of that key. This allows others (relying parties) to rely upon signatures or on assertions made by the private key that corresponds to the certified public key. Keystores and trust stores can be in various formats, such as .pem, .crt, .pfx, and .jks.
## Certificate authorities  

### TLS typically relies on a set of trusted third-party certificate authorities to establish the authenticity of certificates. Trust is usually anchored in a list of certificates distributed with user agent software, and can be modified by the relying party. 
### According to Netcraft, who monitors active TLS certificates, the market-leading certificate authority (CA) has been Symantec since the beginning of their survey (or VeriSign before the authentication services business unit was purchased by Symantec). As of 2015, Symantec accounted for just under a third of all certificates and 44% of the valid certificates used by the 1 million busiest websites, as counted by Netcraft. In 2017, Symantec sold its TLS/SSL business to DigiCert. In an updated report, it was shown that IdenTrust, DigiCert, and Sectigo are the top 3 certificate authorities in terms of market share since May 2019.As a consequence of choosing X.509 certificates, certificate authorities and a public key infrastructure are necessary to verify the relation between a certificate and its owner, as well as to generate, sign, and administer the validity of certificates. While this can be more convenient than verifying the identities via a web of trust, the 2013 mass surveillance disclosures made it more widely known that certificate authorities are a weak point from a security standpoint, allowing man-in-the-middle attacks (MITM) if the certificate authority cooperates (or is compromised).
## Algorithms 
## Key exchange or key agreement  
### Before a client and server can begin to exchange information protected by TLS, they must securely exchange or agree upon an encryption key and a cipher to use when encrypting data (see \u00a7 Cipher). Among the methods used for key exchange/agreement are: public and private keys generated with RSA (denoted TLS_RSA in the TLS handshake protocol), Diffie\u2013Hellman (TLS_DH), ephemeral Diffie\u2013Hellman (TLS_DHE), elliptic-curve Diffie\u2013Hellman (TLS_ECDH), ephemeral elliptic-curve Diffie\u2013Hellman (TLS_ECDHE), anonymous Diffie\u2013Hellman (TLS_DH_anon), pre-shared key (TLS_PSK) and Secure Remote Password (TLS_SRP).The TLS_DH_anon and TLS_ECDH_anon key agreement methods do not authenticate the server or the user and hence are rarely used because those are vulnerable to man-in-the-middle attacks. Only TLS_DHE and TLS_ECDHE provide forward secrecy. 
### Public key certificates used during exchange/agreement also vary in the size of the public/private encryption keys used during the exchange and hence the robustness of the security provided. In July 2013, Google announced that it would no longer use 1024-bit public keys and would switch instead to 2048-bit keys to increase the security of the TLS encryption it provides to its users because the encryption strength is directly related to the key size.
## Cipher  

### Notes
## Data integrity  
### A message authentication code (MAC) is used for data integrity. HMAC is used for CBC mode of block ciphers. Authenticated encryption (AEAD) such as GCM mode and CCM mode uses AEAD-integrated MAC and doesn't use HMAC. HMAC-based PRF, or HKDF is used for TLS handshake.
## Applications and adoption  
### In applications design, TLS is usually implemented on top of Transport Layer protocols, encrypting all of the protocol-related data of protocols such as HTTP, FTP, SMTP, NNTP and XMPP. 
### Historically, TLS has been used primarily with reliable transport protocols such as the Transmission Control Protocol (TCP). However, it has also been implemented with datagram-oriented transport protocols, such as the User Datagram Protocol (UDP) and the Datagram Congestion Control Protocol (DCCP), usage of which has been standardized independently using the term Datagram Transport Layer Security (DTLS).
## Websites  
### A primary use of TLS is to secure World Wide Web traffic between a website and a web browser encoded with the HTTP protocol. This use of TLS to secure HTTP traffic constitutes the HTTPS protocol. 
### Notes
## Web browsers  

### As of April 2016, the latest versions of all major web browsers support TLS 1.0, 1.1, and 1.2, and have them enabled by default. However, not all supported Microsoft operating systems support the latest version of IE. Additionally, many Microsoft operating systems currently support multiple versions of IE, but this has changed according to Microsoft's Internet Explorer Support Lifecycle Policy FAQ, \"beginning January 12, 2016, only the most current version of Internet Explorer available for a supported operating system will receive technical support and security updates.\" The page then goes on to list the latest supported version of IE at that date for each operating system. The next critical date would be when an operating system reaches the end of life stage, which is in Microsoft's Windows lifecycle fact sheet. 
### Mitigations against known attacks are not enough yet: 

### Mitigations against POODLE attack: some browsers already prevent fallback to SSL 3.0; however, this mitigation needs to be supported by not only clients but also servers. Disabling SSL 3.0 itself, implementation of \"anti-POODLE record splitting\", or denying CBC ciphers in SSL 3.0 is required. 
### Google Chrome: complete (TLS_FALLBACK_SCSV is implemented since version 33, fallback to SSL 3.0 is disabled since version 39, SSL 3.0 itself is disabled by default since version 40. Support of SSL 3.0 itself was dropped since version 44.) 
### Mozilla Firefox: complete (support of SSL 3.0 itself is dropped since version 39. SSL 3.0 itself is disabled by default and fallback to SSL 3.0 are disabled since version 34, TLS_FALLBACK_SCSV is implemented since version 35. In ESR, SSL 3.0 itself is disabled by default and TLS_FALLBACK_SCSV is implemented since ESR 31.3.) 
### Internet Explorer: partial (only in version 11, SSL 3.0 is disabled by default since April 2015. Version 10 and older are still vulnerable against POODLE.) 
### Opera: complete (TLS_FALLBACK_SCSV is implemented since version 20, \"anti-POODLE record splitting\", which is effective only with client-side implementation, is implemented since version 25, SSL 3.0 itself is disabled by default since version 27. Support of SSL 3.0 itself will be dropped since version 31.) 
### Safari: complete (only on OS X 10.8 and later and iOS 8, CBC ciphers during fallback to SSL 3.0 is denied, but this means it will use RC4, which is not recommended as well. Support of SSL 3.0 itself is dropped on OS X 10.11 and later and iOS 9.) 
### Mitigation against RC4 attacks: 
### Google Chrome disabled RC4 except as a fallback since version 43. RC4 is disabled since Chrome 48. 
### Firefox disabled RC4 except as a fallback since version 36. Firefox 44 disabled RC4 by default. 
### Opera disabled RC4 except as a fallback since version 30. RC4 is disabled since Opera 35. 
### Internet Explorer for Windows 7 / Server 2008 R2 and for Windows 8 / Server 2012 have set the priority of RC4 to lowest and can also disable RC4 except as a fallback through registry settings. Internet Explorer 11 Mobile 11 for Windows Phone 8.1 disable RC4 except as a fallback if no other enabled algorithm works. Edge and IE 11 disable RC4 completely in August 2016. 
### Mitigation against FREAK attack: 
### The Android Browser included with Android 4.0 and older is still vulnerable to the FREAK attack. 
### Internet Explorer 11 Mobile is still vulnerable to the FREAK attack. 
### Google Chrome, Internet Explorer (desktop), Safari (desktop & mobile), and Opera (mobile) have FREAK mitigations in place. 
### Mozilla Firefox on all platforms and Google Chrome on Windows were not affected by FREAK. 
### Notes
## Libraries  

### Most SSL and TLS programming libraries are free and open source software. 

### BoringSSL, a fork of OpenSSL for Chrome/Chromium and Android as well as other Google applications. 
### Botan, a BSD-licensed cryptographic library written in C++. 
### BSAFE Micro Edition Suite: a multi-platform implementation of TLS written in C using a FIPS-validated cryptographic module 
### BSAFE SSL-J: a TLS library providing both a proprietary API and JSSE API, using FIPS-validated cryptographic module 
### cryptlib: a portable open source cryptography library (includes TLS/SSL implementation) 
### Delphi programmers may use a library called Indy which utilizes OpenSSL or alternatively ICS which supports TLS 1.3 now. 
### GnuTLS: a free implementation (LGPL licensed) 
### Java Secure Socket Extension (JSSE): the Java API and provider implementation (named SunJSSE) 
### LibreSSL: a fork of OpenSSL by OpenBSD project. 
### MatrixSSL: a dual licensed implementation 
### mbed TLS (previously PolarSSL): A tiny SSL library implementation for embedded devices that is designed for ease of use 
### Network Security Services: FIPS 140 validated open source library 
### OpenSSL: a free implementation (BSD license with some extensions) 
### SChannel: an implementation of SSL and TLS Microsoft Windows as part of its package. 
### Secure Transport: an implementation of SSL and TLS used in OS X and iOS as part of their packages. 
### wolfSSL (previously CyaSSL): Embedded SSL/TLS Library with a strong focus on speed and size. 
### A paper presented at the 2012 ACM conference on computer and communications security showed that few applications used some of these SSL libraries correctly, leading to vulnerabilities. According to the authors 

### \"the root cause of most of these vulnerabilities is the terrible design of the APIs to the underlying SSL libraries. Instead of expressing high-level security properties of network tunnels such as confidentiality and authentication, these APIs expose low-level details of the SSL protocol to application developers. As a consequence, developers often use SSL APIs incorrectly, misinterpreting and misunderstanding their manifold parameters, options, side effects, and return values.\"
## Other uses  
### The Simple Mail Transfer Protocol (SMTP) can also be protected by TLS. These applications use public key certificates to verify the identity of endpoints. 
### TLS can also be used for tunnelling an entire network stack to create a VPN, which is the case with OpenVPN and OpenConnect. Many vendors have by now married TLS's encryption and authentication capabilities with authorization. There has also been substantial development since the late 1990s in creating client technology outside of Web-browsers, in order to enable support for client/server applications. Compared to traditional IPsec VPN technologies, TLS has some inherent advantages in firewall and NAT traversal that make it easier to administer for large remote-access populations. 
### TLS is also a standard method for protecting Session Initiation Protocol (SIP) application signaling. TLS can be used for providing authentication and encryption of the SIP signalling associated with VoIP and other SIP-based applications.
## Security 
## Attacks against TLS/SSL  
### Significant attacks against TLS/SSL are listed below. 
### In February 2015, IETF issued an informational RFC summarizing the various known attacks against TLS/SSL.
## Renegotiation attack  
### A vulnerability of the renegotiation procedure was discovered in August 2009 that can lead to plaintext injection attacks against SSL 3.0 and all current versions of TLS. For example, it allows an attacker who can hijack an https connection to splice their own requests into the beginning of the conversation the client has with the web server. The attacker can't actually decrypt the client\u2013server communication, so it is different from a typical man-in-the-middle attack. A short-term fix is for web servers to stop allowing renegotiation, which typically will not require other changes unless client certificate authentication is used. To fix the vulnerability, a renegotiation indication extension was proposed for TLS. It will require the client and server to include and verify information about previous handshakes in any renegotiation handshakes. This extension has become a proposed standard and has been assigned the number RFC 5746. The RFC has been implemented by several libraries.
## Downgrade attacks: FREAK attack and Logjam attack  

### A protocol downgrade attack (also called a version rollback attack) tricks a web server into negotiating connections with previous versions of TLS (such as SSLv2) that have long since been abandoned as insecure. 
### Previous modifications to the original protocols, like False Start (adopted and enabled by Google Chrome) or Snap Start, reportedly introduced limited TLS protocol downgrade attacks or allowed modifications to the cipher suite list sent by the client to the server. In doing so, an attacker might succeed in influencing the cipher suite selection in an attempt to downgrade the cipher suite negotiated to use either a weaker symmetric encryption algorithm or a weaker key exchange. A paper presented at an ACM conference on computer and communications security in 2012 demonstrated that the False Start extension was at risk: in certain circumstances it could allow an attacker to recover the encryption keys offline and to access the encrypted data.Encryption downgrade attacks can force servers and clients to negotiate a connection using cryptographically weak keys. In 2014, a man-in-the-middle attack called FREAK was discovered affecting the OpenSSL stack, the default Android web browser, and some Safari browsers. The attack involved tricking servers into negotiating a TLS connection using cryptographically weak 512 bit encryption keys. 
### Logjam is a security exploit discovered in May 2015 that exploits the option of using legacy \"export-grade\" 512-bit Diffie\u2013Hellman groups dating back to the 1990s. It forces susceptible servers to downgrade to cryptographically weak 512-bit Diffie\u2013Hellman groups. An attacker can then deduce the keys the client and server determine using the Diffie\u2013Hellman key exchange.
## Cross-protocol attacks: DROWN  

### The DROWN attack is an exploit that attacks servers supporting contemporary SSL/TLS protocol suites by exploiting their support for the obsolete, insecure, SSLv2 protocol to leverage an attack on connections using up-to-date protocols that would otherwise be secure. DROWN exploits a vulnerability in the protocols used and the configuration of the server, rather than any specific implementation error. Full details of DROWN were announced in March 2016, together with a patch for the exploit. At that time, more than 81,000 of the top 1 million most popular websites were among the TLS protected websites that were vulnerable to the DROWN attack.
## BEAST attack  
### On September 23, 2011 researchers Thai Duong and Juliano Rizzo demonstrated a proof of concept called BEAST (Browser Exploit Against SSL/TLS) using a Java applet to violate same origin policy constraints, for a long-known cipher block chaining (CBC) vulnerability in TLS 1.0: an attacker observing 2 consecutive ciphertext blocks C0, C1 can test if the plaintext block P1 is equal to x by choosing the next plaintext block P2  x  
  
    
      
       \u2295 
      
    
   {\\displaystyle \\oplus } 
  C0  
  
    
      
       \u2295 
      
    
   {\\displaystyle \\oplus } 
  C1; as per CBC operation, C2  E(C1  
  
    
      
       \u2295 
      
    
   {\\displaystyle \\oplus } 
  P2)  E(C1  
  
    
      
       \u2295 
      
    
   {\\displaystyle \\oplus } 
  x  
  
    
      
       \u2295 
      
    
   {\\displaystyle \\oplus } 
  C0  
  
    
      
       \u2295 
      
    
   {\\displaystyle \\oplus } 
  C1)  E(C0  
  
    
      
       \u2295 
      
    
   {\\displaystyle \\oplus } 
  x), which will be equal to C1 if x  P1. Practical exploits had not been previously demonstrated for this vulnerability, which was originally discovered by Phillip Rogaway in 2002. The vulnerability of the attack had been fixed with TLS 1.1 in 2006, but TLS 1.1 had not seen wide adoption prior to this attack demonstration. 
### RC4 as a stream cipher is immune to BEAST attack. Therefore, RC4 was widely used as a way to mitigate BEAST attack on the server side. However, in 2013, researchers found more weaknesses in RC4. Thereafter enabling RC4 on server side was no longer recommended.Chrome and Firefox themselves are not vulnerable to BEAST attack, however, Mozilla updated their NSS libraries to mitigate BEAST-like attacks. NSS is used by Mozilla Firefox and Google Chrome to implement SSL. Some web servers that have a broken implementation of the SSL specification may stop working as a result.Microsoft released Security Bulletin MS12-006 on January 10, 2012, which fixed the BEAST vulnerability by changing the way that the Windows Secure Channel (SChannel) component transmits encrypted network packets from the server end. Users of Internet Explorer (prior to version 11) that run on older versions of Windows (Windows 7, Windows 8 and Windows Server 2008 R2) can restrict use of TLS to 1.1 or higher. 
### Apple fixed BEAST vulnerability by implementing 1/n-1 split and turning it on by default in OS X Mavericks, released on October 22, 2013.
## CRIME and BREACH attacks  

### The authors of the BEAST attack are also the creators of the later CRIME attack, which can allow an attacker to recover the content of web cookies when data compression is used along with TLS. When used to recover the content of secret authentication cookies, it allows an attacker to perform session hijacking on an authenticated web session. 
### While the CRIME attack was presented as a general attack that could work effectively against a large number of protocols, including but not limited to TLS, and application-layer protocols such as SPDY or HTTP, only exploits against TLS and SPDY were demonstrated and largely mitigated in browsers and servers. The CRIME exploit against HTTP compression has not been mitigated at all, even though the authors of CRIME have warned that this vulnerability might be even more widespread than SPDY and TLS compression combined. In 2013 a new instance of the CRIME attack against HTTP compression, dubbed BREACH, was announced. Based on the CRIME attack a BREACH attack can extract login tokens, email addresses or other sensitive information from TLS encrypted web traffic in as little as 30 seconds (depending on the number of bytes to be extracted), provided the attacker tricks the victim into visiting a malicious web link or is able to inject content into valid pages the user is visiting (ex: a wireless network under the control of the attacker). All versions of TLS and SSL are at risk from BREACH regardless of the encryption algorithm or cipher used. Unlike previous instances of CRIME, which can be successfully defended against by turning off TLS compression or SPDY header compression, BREACH exploits HTTP compression which cannot realistically be turned off, as virtually all web servers rely upon it to improve data transmission speeds for users. This is a known limitation of TLS as it is susceptible to chosen-plaintext attack against the application-layer data it was meant to protect.
## Timing attacks on padding  
### Earlier TLS versions were vulnerable against the padding oracle attack discovered in 2002. A novel variant, called the Lucky Thirteen attack, was published in 2013. 
### Some experts also recommended avoiding Triple-DES CBC. Since the last supported ciphers developed to support any program using Windows XP's SSL/TLS library like Internet Explorer on Windows XP are RC4 and Triple-DES, and since RC4 is now deprecated (see discussion of RC4 attacks), this makes it difficult to support any version of SSL for any program using this library on XP. 
### A fix was released as the Encrypt-then-MAC extension to the TLS specification, released as RFC 7366. The Lucky Thirteen attack can be mitigated in TLS 1.2 by using only AES_GCM ciphers; AES_CBC remains vulnerable.
## POODLE attack  

### On October 14, 2014, Google researchers published a vulnerability in the design of SSL 3.0, which makes CBC mode of operation with SSL 3.0 vulnerable to a padding attack (CVE-2014-3566). They named this attack POODLE (Padding Oracle On Downgraded Legacy Encryption). On average, attackers only need to make 256 SSL 3.0 requests to reveal one byte of encrypted messages.Although this vulnerability only exists in SSL 3.0 and most clients and servers support TLS 1.0 and above, all major browsers voluntarily downgrade to SSL 3.0 if the handshakes with newer versions of TLS fail unless they provide the option for a user or administrator to disable SSL 3.0 and the user or administrator does so. Therefore, the man-in-the-middle can first conduct a version rollback attack and then exploit this vulnerability.On December 8, 2014, a variant of POODLE was announced that impacts TLS implementations that do not properly enforce padding byte requirements.
## RC4 attacks  

### Despite the existence of attacks on RC4 that broke its security, cipher suites in SSL and TLS that were based on RC4 were still considered secure prior to 2013 based on the way in which they were used in SSL and TLS. In 2011, the RC4 suite was actually recommended as a work around for the BEAST attack. New forms of attack disclosed in March 2013 conclusively demonstrated the feasibility of breaking RC4 in TLS, suggesting it was not a good workaround for BEAST. An attack scenario was proposed by AlFardan, Bernstein, Paterson, Poettering and Schuldt that used newly discovered statistical biases in the RC4 key table to recover parts of the plaintext with a large number of TLS encryptions. An attack on RC4 in TLS and SSL that requires 13 \u00d7 220 encryptions to break RC4 was unveiled on 8 July 2013 and later described as \"feasible\" in the accompanying presentation at a USENIX Security Symposium in August 2013. In July 2015, subsequent improvements in the attack make it increasingly practical to defeat the security of RC4-encrypted TLS.As many modern browsers have been designed to defeat BEAST attacks (except Safari for Mac OS X 10.7 or earlier, for iOS 6 or earlier, and for Windows; see \u00a7 Web browsers), RC4 is no longer a good choice for TLS 1.0. The CBC ciphers which were affected by the BEAST attack in the past have become a more popular choice for protection. Mozilla and Microsoft recommend disabling RC4 where possible. RFC 7465 prohibits the use of RC4 cipher suites in all versions of TLS. 
### On September 1, 2015, Microsoft, Google and Mozilla announced that RC4 cipher suites would be disabled by default in their browsers (Microsoft Edge, Internet Explorer 11 on Windows 7/8.1/10, Firefox, and Chrome) in early 2016.
## Truncation attack  
### A TLS (logout) truncation attack blocks a victim's account logout requests so that the user unknowingly remains logged into a web service. When the request to sign out is sent, the attacker injects an unencrypted TCP FIN message (no more data from sender) to close the connection. The server therefore doesn't receive the logout request and is unaware of the abnormal termination.Published in July 2013, the attack causes web services such as Gmail and Hotmail to display a page that informs the user that they have successfully signed-out, while ensuring that the user's browser maintains authorization with the service, allowing an attacker with subsequent access to the browser to access and take over control of the user's logged-in account. The attack does not rely on installing malware on the victim's computer; attackers need only place themselves between the victim and the web server (e.g., by setting up a rogue wireless hotspot). This vulnerability also requires access to the victim's computer. 
### Another possibility is when using FTP the data connection can have a false FIN in the data stream, and if the protocol rules for exchanging close_notify alerts is not adhered to a file can be truncated.
## Unholy PAC attack  
### This attack, discovered in mid-2016, exploits weaknesses in the Web Proxy Autodiscovery Protocol (WPAD) to expose the URL that a web user is attempting to reach via a TLS-enabled web link. Disclosure of a URL can violate a user's privacy, not only because of the website accessed, but also because URLs are sometimes used to authenticate users. Document sharing services, such as those offered by Google and Dropbox, also work by sending a user a security token that's included in the URL. An attacker who obtains such URLs may be able to gain full access to a victim's account or data. 
### The exploit works against almost all browsers and operating systems.
## Sweet32 attack  
### The Sweet32 attack breaks all 64-bit block ciphers used in CBC mode as used in TLS by exploiting a birthday attack and either a man-in-the-middle attack or injection of a malicious JavaScript into a web page. The purpose of the man-in-the-middle attack or the JavaScript injection is to allow the attacker to capture enough traffic to mount a birthday attack.
## Implementation errors: Heartbleed bug, BERserk attack, Cloudflare bug  

### The Heartbleed bug is a serious vulnerability specific to the implementation of SSL/TLS in the popular OpenSSL cryptographic software library, affecting versions 1.0.1 to 1.0.1f. This weakness, reported in April 2014, allows attackers to steal private keys from servers that should normally be protected. The Heartbleed bug allows anyone on the Internet to read the memory of the systems protected by the vulnerable versions of the OpenSSL software. This compromises the secret private keys associated with the public certificates used to identify the service providers and to encrypt the traffic, the names and passwords of the users and the actual content. This allows attackers to eavesdrop on communications, steal data directly from the services and users and to impersonate services and users. The vulnerability is caused by a buffer over-read bug in the OpenSSL software, rather than a defect in the SSL or TLS protocol specification. 
### In September 2014, a variant of Daniel Bleichenbacher's PKCS#1 v1.5 RSA Signature Forgery vulnerability was announced by Intel Security Advanced Threat Research. This attack, dubbed BERserk, is a result of incomplete ASN.1 length decoding of public key signatures in some SSL implementations, and allows a man-in-the-middle attack by forging a public key signature.In February 2015, after media reported the hidden pre-installation of Superfish adware on some Lenovo notebooks, a researcher found a trusted root certificate on affected Lenovo machines to be insecure, as the keys could easily be accessed using the company name, Komodia, as a passphrase. The Komodia library was designed to intercept client-side TLS/SSL traffic for parental control and surveillance, but it was also used in numerous adware programs, including Superfish, that were often surreptitiously installed unbeknownst to the computer user. In turn, these potentially unwanted programs installed the corrupt root certificate, allowing attackers to completely control web traffic and confirm false websites as authentic. 
### In May 2016, it was reported that dozens of Danish HTTPS-protected websites belonging to Visa Inc. were vulnerable to attacks allowing hackers to inject malicious code and forged content into the browsers of visitors. The attacks worked because the TLS implementation used on the affected servers incorrectly reused random numbers (nonces) that are intended to be used only once, ensuring that each TLS handshake is unique.In February 2017, an implementation error caused by a single mistyped character in code used to parse HTML created a buffer overflow error on Cloudflare servers. Similar in its effects to the Heartbleed bug discovered in 2014, this overflow error, widely known as Cloudbleed, allowed unauthorized third parties to read data in the memory of programs running on the servers\u2014data that should otherwise have been protected by TLS.
## Survey of websites vulnerable to attacks  
### As of July 2021, the Trustworthy Internet Movement estimated the ratio of websites that are vulnerable to TLS attacks.
## Forward secrecy  

### Forward secrecy is a property of cryptographic systems which ensures that a session key derived from a set of public and private keys will not be compromised if one of the private keys is compromised in the future. Without forward secrecy, if the server's private key is compromised, not only will all future TLS-encrypted sessions using that server certificate be compromised, but also any past sessions that used it as well (provided of course that these past sessions were intercepted and stored at the time of transmission). An implementation of TLS can provide forward secrecy by requiring the use of ephemeral Diffie\u2013Hellman key exchange to establish session keys, and some notable TLS implementations do so exclusively: e.g., Gmail and other Google HTTPS services that use OpenSSL. However, many clients and servers supporting TLS (including browsers and web servers) are not configured to implement such restrictions. In practice, unless a web service uses Diffie\u2013Hellman key exchange to implement forward secrecy, all of the encrypted web traffic to and from that service can be decrypted by a third party if it obtains the server's master (private) key; e.g., by means of a court order.Even where Diffie\u2013Hellman key exchange is implemented, server-side session management mechanisms can impact forward secrecy. The use of TLS session tickets (a TLS extension) causes the session to be protected by AES128-CBC-SHA256 regardless of any other negotiated TLS parameters, including forward secrecy ciphersuites, and the long-lived TLS session ticket keys defeat the attempt to implement forward secrecy. Stanford University research in 2014 also found that of 473,802 TLS servers surveyed, 82.9% of the servers deploying ephemeral Diffie\u2013Hellman (DHE) key exchange to support forward secrecy were using weak Diffie\u2013Hellman parameters. These weak parameter choices could potentially compromise the effectiveness of the forward secrecy that the servers sought to provide.Since late 2011, Google has provided forward secrecy with TLS by default to users of its Gmail service, along with Google Docs and encrypted search, among other services. 
### Since November 2013, Twitter has provided forward secrecy with TLS to users of its service. As of August 2019, about 80% of TLS-enabled websites are configured to use cipher suites that provide forward secrecy to most web browsers.
## TLS interception  

### TLS interception (or HTTPS interception if applied particularly to that protocol) is the practice of intercepting an encrypted data stream in order to decrypt it, read and possibly manipulate it, and then re-encrypt it and send the data on its way again. This is done by way of a \"transparent proxy\": the interception software terminates the incoming TLS connection, inspects the HTTP plaintext, and then creates a new TLS connection to the destination.TLS / HTTPS interception is used as an information security measure by network operators in order to be able to scan for and protect against the intrusion of malicious content into the network, such as computer viruses and other malware. Such content could otherwise not be detected as long as it is protected by encryption, which is increasingly the case as a result of the routine use of HTTPS and other secure protocols. 
### A significant drawback of TLS / HTTPS interception is that it introduces new security risks of its own. One notable limitation is that it provides a point where network traffic is available unencrypted thus giving attackers an incentive to attack this point in particular in order to gain access to otherwise secure content. The interception also allows the network operator, or persons who gain access to its interception system, to perform man-in-the-middle attacks against network users. A 2017 study found that \"HTTPS interception has become startlingly widespread, and that interception products as a class have a dramatically negative impact on connection security\".
## Protocol details  
### The TLS protocol exchanges records, which encapsulate the data to be exchanged in a specific format (see below). Each record can be compressed, padded, appended with a message authentication code (MAC), or encrypted, all depending on the state of the connection. Each record has a content type field that designates the type of data encapsulated, a length field and a TLS version field. The data encapsulated may be control or procedural messages of the TLS itself, or simply the application data needed to be transferred by TLS. The specifications (cipher suite, keys etc.) required to exchange application data by TLS, are agreed upon in the \"TLS handshake\" between the client requesting the data and the server responding to requests. The protocol therefore defines both the structure of payloads transferred in TLS and the procedure to establish and monitor the transfer.
## TLS handshake  

### When the connection starts, the record encapsulates a \"control\" protocol \u2013 the handshake messaging protocol (content type 22). This protocol is used to exchange all the information required by both sides for the exchange of the actual application data by TLS. It defines the format of messages and the order of their exchange. These may vary according to the demands of the client and server \u2013 i.e., there are several possible procedures to set up the connection. This initial exchange results in a successful TLS connection (both parties ready to transfer application data with TLS) or an alert message (as specified below).
## Basic TLS handshake  
### A typical connection example follows, illustrating a handshake where the server (but not the client) is authenticated by its certificate: 

### Negotiation phase: 
### A client sends a ClientHello message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and suggested compression methods. If the client is attempting to perform a resumed handshake, it may send a session ID. If the client can use Application-Layer Protocol Negotiation, it may include a list of supported application protocols, such as HTTP/2. 
### The server responds with a ServerHello message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. To confirm or allow resumed handshakes the server may send a session ID. The chosen protocol version should be the highest that both the client and server support. For example, if the client supports TLS version 1.1 and the server supports version 1.2, version 1.1 should be selected; version 1.2 should not be selected. 
### The server sends its Certificate message (depending on the selected cipher suite, this may be omitted by the server). 
### The server sends its ServerKeyExchange message (depending on the selected cipher suite, this may be omitted by the server). This message is sent for all DHE, ECDHE and DH_anon cipher suites. 
### The server sends a ServerHelloDone message, indicating it is done with handshake negotiation. 
### The client responds with a ClientKeyExchange message, which may contain a PreMasterSecret, public key, or nothing. (Again, this depends on the selected cipher.) This PreMasterSecret is encrypted using the public key of the server certificate. 
### The client and server then use the random numbers and PreMasterSecret to compute a common secret, called the \"master secret\". All other key data (session keys such as IV, symmetric encryption key, MAC key) for this connection is derived from this master secret (and the client- and server-generated random values), which is passed through a carefully designed pseudorandom function. 
### The client now sends a ChangeCipherSpec record, essentially telling the server, \"Everything I tell you from now on will be authenticated (and encrypted if encryption parameters were present in the server certificate).\" The ChangeCipherSpec is itself a record-level protocol with content type of 20. 
### The client sends an authenticated and encrypted Finished message, containing a hash and MAC over the previous handshake messages. 
### The server will attempt to decrypt the client's Finished message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be torn down. 
### Finally, the server sends a ChangeCipherSpec, telling the client, \"Everything I tell you from now on will be authenticated (and encrypted, if encryption was negotiated).\" 
### The server sends its authenticated and encrypted Finished message. 
### The client performs the same decryption and verification procedure as the server did in the previous step. 
### Application phase: at this point, the \"handshake\" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be authenticated and optionally encrypted exactly like in their Finished message. Otherwise, the content type will return 25 and the client will not authenticate.
## Client-authenticated TLS handshake  
### The following full example shows a client being authenticated (in addition to the server as in the example above; see mutual authentication) via TLS using certificates exchanged between both peers. 

### Negotiation Phase: 
### A client sends a ClientHello message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and compression methods. 
### The server responds with a ServerHello message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. The server may also send a session id as part of the message to perform a resumed handshake. 
### The server sends its Certificate message (depending on the selected cipher suite, this may be omitted by the server). 
### The server sends its ServerKeyExchange message (depending on the selected cipher suite, this may be omitted by the server). This message is sent for all DHE, ECDHE and DH_anon ciphersuites. 
### The server sends a CertificateRequest message, to request a certificate from the client. 
### The server sends a ServerHelloDone message, indicating it is done with handshake negotiation. 
### The client responds with a Certificate message, which contains the client's certificate. 
### The client sends a ClientKeyExchange message, which may contain a PreMasterSecret, public key, or nothing. (Again, this depends on the selected cipher.) This PreMasterSecret is encrypted using the public key of the server certificate. 
### The client sends a CertificateVerify message, which is a signature over the previous handshake messages using the client's certificate's private key. This signature can be verified by using the client's certificate's public key. This lets the server know that the client has access to the private key of the certificate and thus owns the certificate. 
### The client and server then use the random numbers and PreMasterSecret to compute a common secret, called the \"master secret\". All other key data (\"session keys\") for this connection is derived from this master secret (and the client- and server-generated random values), which is passed through a carefully designed pseudorandom function. 
### The client now sends a ChangeCipherSpec record, essentially telling the server, \"Everything I tell you from now on will be authenticated (and encrypted if encryption was negotiated). \" The ChangeCipherSpec is itself a record-level protocol and has type 20 and not 22. 
### Finally, the client sends an encrypted Finished message, containing a hash and MAC over the previous handshake messages. 
### The server will attempt to decrypt the client's Finished message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be torn down. 
### Finally, the server sends a ChangeCipherSpec, telling the client, \"Everything I tell you from now on will be authenticated (and encrypted if encryption was negotiated). \" 
### The server sends its own encrypted Finished message. 
### The client performs the same decryption and verification procedure as the server did in the previous step. 
### Application phase: at this point, the \"handshake\" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be encrypted exactly like in their Finished message.
## Resumed TLS handshake  
### Public key operations (e.g., RSA) are relatively expensive in terms of computational power. TLS provides a secure shortcut in the handshake mechanism to avoid these operations: resumed sessions. Resumed sessions are implemented using session IDs or session tickets. 
### Apart from the performance benefit, resumed sessions can also be used for single sign-on, as it guarantees that both the original session and any resumed session originate from the same client. This is of particular importance for the FTP over TLS/SSL protocol, which would otherwise suffer from a man-in-the-middle attack in which an attacker could intercept the contents of the secondary data connections.
## TLS 1.3 handshake  
### The TLS 1.3 handshake was condensed to only one round trip compared to the two round trips required in previous versions of TLS/SSL. 
### First the client sends a clientHello message to the server that contains a list of supported ciphers in order of the client's preference and makes a guess on what key algorithm will be used so that it can send a secret key to share if needed. By making a guess at what key algorithm will be used, the server eliminates a round trip. After receiving the clientHello, the server sends a serverHello with its key, a certificate, the chosen cipher suite and the finished message. 
### After the client receives the server's finished message, it now is coordinated with the server on which cipher suite to use.
## Session IDs  
### In an ordinary full handshake, the server sends a session id as part of the ServerHello message. The client associates this session id with the server's IP address and TCP port, so that when the client connects again to that server, it can use the session id to shortcut the handshake. In the server, the session id maps to the cryptographic parameters previously negotiated, specifically the \"master secret\". Both sides must have the same \"master secret\" or the resumed handshake will fail (this prevents an eavesdropper from using a session id). The random data in the ClientHello and ServerHello messages virtually guarantee that the generated connection keys will be different from in the previous connection. In the RFCs, this type of handshake is called an abbreviated handshake. It is also described in the literature as a restart handshake. 

### Negotiation phase: 
### A client sends a ClientHello message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and compression methods. Included in the message is the session id from the previous TLS connection. 
### The server responds with a ServerHello message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. If the server recognizes the session id sent by the client, it responds with the same session id. The client uses this to recognize that a resumed handshake is being performed. If the server does not recognize the session id sent by the client, it sends a different value for its session id. This tells the client that a resumed handshake will not be performed. At this point, both the client and server have the \"master secret\" and random data to generate the key data to be used for this connection. 
### The server now sends a ChangeCipherSpec record, essentially telling the client, \"Everything I tell you from now on will be encrypted.\" The ChangeCipherSpec is itself a record-level protocol and has type 20 and not 22. 
### Finally, the server sends an encrypted Finished message, containing a hash and MAC over the previous handshake messages. 
### The client will attempt to decrypt the server's Finished message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be torn down. 
### Finally, the client sends a ChangeCipherSpec, telling the server, \"Everything I tell you from now on will be encrypted. \" 
### The client sends its own encrypted Finished message. 
### The server performs the same decryption and verification procedure as the client did in the previous step. 
### Application phase: at this point, the \"handshake\" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be encrypted exactly like in their Finished message.
## Session tickets  
### RFC 5077 extends TLS via use of session tickets, instead of session IDs. It defines a way to resume a TLS session without requiring that session-specific state is stored at the TLS server. 
### When using session tickets, the TLS server stores its session-specific state in a session ticket and sends the session ticket to the TLS client for storing. The client resumes a TLS session by sending the session ticket to the server, and the server resumes the TLS session according to the session-specific state in the ticket. The session ticket is encrypted and authenticated by the server, and the server verifies its validity before using its contents. 
### One particular weakness of this method with OpenSSL is that it always limits encryption and authentication security of the transmitted TLS session ticket to AES128-CBC-SHA256, no matter what other TLS parameters were negotiated for the actual TLS session. This means that the state information (the TLS session ticket) is not as well protected as the TLS session itself. Of particular concern is OpenSSL's storage of the keys in an application-wide context (SSL_CTX), i.e. for the life of the application, and not allowing for re-keying of the AES128-CBC-SHA256 TLS session tickets without resetting the application-wide OpenSSL context (which is uncommon, error-prone and often requires manual administrative intervention).
## TLS record  
### This is the general format of all TLS records. 

### Content type 
### This field identifies the Record Layer Protocol Type contained in this record.Legacy version 
### This field identifies the major and minor version of TLS prior to TLS 1.3 for the contained message. For a ClientHello message, this need not be the highest version supported by the client. For TLS 1.3 and later, this must to be set 0x0303 and application must send supported versions in an extra message extension block.LengthThe length of \"protocol message(s)\", \"MAC\" and \"padding\" fields combined (i.e. q\u22125), not to exceed 214 bytes (16 KiB). 
### Protocol message(s) 
### One or more messages identified by the Protocol field. Note that this field may be encrypted depending on the state of the connection. 
### MAC and padding 
### A message authentication code computed over the \"protocol message(s)\" field, with additional key material included. Note that this field may be encrypted, or not included entirely, depending on the state of the connection. 
### No \"MAC\" or \"padding\" fields can be present at end of TLS records before all cipher algorithms and parameters have been negotiated and handshaked and then confirmed by sending a CipherStateChange record (see below) for signalling that these parameters will take effect in all further records sent by the same peer.
## Handshake protocol  
### Most messages exchanged during the setup of the TLS session are based on this record, unless an error or warning occurs and needs to be signaled by an Alert protocol record (see below), or the encryption mode of the session is modified by another record (see ChangeCipherSpec protocol below). 

### Message type 
### This field identifies the handshake message type.Handshake message data length 
### This is a 3-byte field indicating the length of the handshake data, not including the header.Note that multiple handshake messages may be combined within one record.
## Alert protocol  
### This record should normally not be sent during normal handshaking or application exchanges. However, this message can be sent at any time during the handshake and up to the closure of the session. If this is used to signal a fatal error, the session will be closed immediately after sending this record, so this record is used to give a reason for this closure. If the alert level is flagged as a warning, the remote can decide to close the session if it decides that the session is not reliable enough for its needs (before doing so, the remote may also send its own signal). 

### Level 
### This field identifies the level of alert. If the level is fatal, the sender should close the session immediately. Otherwise, the recipient may decide to terminate the session itself, by sending its own fatal alert and closing the session itself immediately after sending it. The use of Alert records is optional, however if it is missing before the session closure, the session may be resumed automatically (with its handshakes). 
### Normal closure of a session after termination of the transported application should preferably be alerted with at least the Close notify Alert type (with a simple warning level) to prevent such automatic resume of a new session. Signalling explicitly the normal closure of a secure session before effectively closing its transport layer is useful to prevent or detect attacks (like attempts to truncate the securely transported data, if it intrinsically does not have a predetermined length or duration that the recipient of the secured data may expect).Description 
### This field identifies which type of alert is being sent.
## ChangeCipherSpec protocol  
### CCS protocol type 
### Currently only 1.
## Application protocol  
### Length 
### Length of application data (excluding the protocol header and including the MAC and padding trailers) 
### MAC 
### 32 bytes for the SHA-256-based HMAC, 20 bytes for the SHA-1-based HMAC, 16 bytes for the MD5-based HMAC. 
### Padding 
### Variable length; last byte contains the padding length.
## Support for name-based virtual servers  
### From the application protocol point of view, TLS belongs to a lower layer, although the TCP/IP model is too coarse to show it. This means that the TLS handshake is usually (except in the STARTTLS case) performed before the application protocol can start. In the name-based virtual server feature being provided by the application layer, all co-hosted virtual servers share the same certificate because the server has to select and send a certificate immediately after the ClientHello message. This is a big problem in hosting environments because it means either sharing the same certificate among all customers or using a different IP address for each of them. 
### There are two known workarounds provided by X.509: 

### If all virtual servers belong to the same domain, a wildcard certificate can be used. Besides the loose host name selection that might be a problem or not, there is no common agreement about how to match wildcard certificates. Different rules are applied depending on the application protocol or software used. 
### Add every virtual host name in the subjectAltName extension. The major problem being that the certificate needs to be reissued whenever a new virtual server is added.To provide the server name, RFC 4366 Transport Layer Security (TLS) Extensions allow clients to include a Server Name Indication extension (SNI) in the extended ClientHello message. This extension hints to the server immediately which name the client wishes to connect to, so the server 
### can select the appropriate certificate to send to the clients. 
### RFC 2817 also documents a method to implement name-based virtual hosting by upgrading HTTP to TLS via an HTTP/1.1 Upgrade header. Normally this is to securely implement HTTP over TLS within the main \"http\" URI scheme (which avoids forking the URI space and reduces the number of used ports), however, few implementations currently support this.
## Standards 
## Primary standards  
### The current approved version of TLS is version 1.3, which is specified in: 

### RFC 8446: \"The Transport Layer Security (TLS) Protocol Version 1.3\".The current standard replaces these former versions, which are now considered obsolete: 

### RFC 2246: \"The TLS Protocol Version 1.0\". 
### RFC 4346: \"The Transport Layer Security (TLS) Protocol Version 1.1\". 
### RFC 5246: \"The Transport Layer Security (TLS) Protocol Version 1.2\".As well as the never standardized SSL 2.0 and 3.0, which are considered obsolete: 

### Internet Draft (1995), SSL Version 2.0 
### RFC 6101: \"The Secure Sockets Layer (SSL) Protocol Version 3.0\".
## Extensions  
### Other RFCs subsequently extended TLS. 
### Extensions to TLS 1.0 include: 

### RFC 2595: \"Using TLS with IMAP, POP3 and ACAP\". Specifies an extension to the IMAP, POP3 and ACAP services that allow the server and client to use transport-layer security to provide private, authenticated communication over the Internet. 
### RFC 2712: \"Addition of Kerberos Cipher Suites to Transport Layer Security (TLS)\". The 40-bit cipher suites defined in this memo appear only for the purpose of documenting the fact that those cipher suite codes have already been assigned. 
### RFC 2817: \"Upgrading to TLS Within HTTP/1.1\", explains how to use the Upgrade mechanism in HTTP/1.1 to initiate Transport Layer Security (TLS) over an existing TCP connection. This allows unsecured and secured HTTP traffic to share the same well known port (in this case, http: at 80 rather than https: at 443). 
### RFC 2818: \"HTTP Over TLS\", distinguishes secured traffic from insecure traffic by the use of a different 'server port'. 
### RFC 3207: \"SMTP Service Extension for Secure SMTP over Transport Layer Security\". Specifies an extension to the SMTP service that allows an SMTP server and client to use transport-layer security to provide private, authenticated communication over the Internet. 
### RFC 3268: \"AES Ciphersuites for TLS\". Adds Advanced Encryption Standard (AES) cipher suites to the previously existing symmetric ciphers. 
### RFC 3546: \"Transport Layer Security (TLS) Extensions\", adds a mechanism for negotiating protocol extensions during session initialisation and defines some extensions. Made obsolete by RFC 4366. 
### RFC 3749: \"Transport Layer Security Protocol Compression Methods\", specifies the framework for compression methods and the DEFLATE compression method. 
### RFC 3943: \"Transport Layer Security (TLS) Protocol Compression Using Lempel-Ziv-Stac (LZS)\". 
### RFC 4132: \"Addition of Camellia Cipher Suites to Transport Layer Security (TLS)\". 
### RFC 4162: \"Addition of SEED Cipher Suites to Transport Layer Security (TLS)\". 
### RFC 4217: \"Securing FTP with TLS\". 
### RFC 4279: \"Pre-Shared Key Ciphersuites for Transport Layer Security (TLS)\", adds three sets of new cipher suites for the TLS protocol to support authentication based on pre-shared keys.Extensions to TLS 1.1 include: 

### RFC 4347: \"Datagram Transport Layer Security\" specifies a TLS variant that works over datagram protocols (such as UDP). 
### RFC 4366: \"Transport Layer Security (TLS) Extensions\" describes both a set of specific extensions and a generic extension mechanism. 
### RFC 4492: \"Elliptic Curve Cryptography (ECC) Cipher Suites for Transport Layer Security (TLS)\". 
### RFC 4680: \"TLS Handshake Message for Supplemental Data\". 
### RFC 4681: \"TLS User Mapping Extension\". 
### RFC 4785: \"Pre-Shared Key (PSK) Ciphersuites with NULL Encryption for Transport Layer Security (TLS)\". 
### RFC 5054: \"Using the Secure Remote Password (SRP) Protocol for TLS Authentication\". Defines the TLS-SRP ciphersuites. 
### RFC 5077: \"Transport Layer Security (TLS) Session Resumption without Server-Side State\". 
### RFC 5081: \"Using OpenPGP Keys for Transport Layer Security (TLS) Authentication\", obsoleted by RFC 6091.Extensions to TLS 1.2 include: 

### RFC 5288: \"AES Galois Counter Mode (GCM) Cipher Suites for TLS\". 
### RFC 5289: \"TLS Elliptic Curve Cipher Suites with SHA-256/384 and AES Galois Counter Mode (GCM)\". 
### RFC 5746: \"Transport Layer Security (TLS) Renegotiation Indication Extension\". 
### RFC 5878: \"Transport Layer Security (TLS) Authorization Extensions\". 
### RFC 5932: \"Camellia Cipher Suites for TLS\" 
### RFC 6066: \"Transport Layer Security (TLS) Extensions: Extension Definitions\", includes Server Name Indication and OCSP stapling. 
### RFC 6091: \"Using OpenPGP Keys for Transport Layer Security (TLS) Authentication\". 
### RFC 6176: \"Prohibiting Secure Sockets Layer (SSL) Version 2.0\". 
### RFC 6209: \"Addition of the ARIA Cipher Suites to Transport Layer Security (TLS)\". 
### RFC 6347: \"Datagram Transport Layer Security Version 1.2\". 
### RFC 6367: \"Addition of the Camellia Cipher Suites to Transport Layer Security (TLS)\". 
### RFC 6460: \"Suite B Profile for Transport Layer Security (TLS)\". 
### RFC 6655: \"AES-CCM Cipher Suites for Transport Layer Security (TLS)\". 
### RFC 7027: \"Elliptic Curve Cryptography (ECC) Brainpool Curves for Transport Layer Security (TLS)\". 
### RFC 7251: \"AES-CCM Elliptic Curve Cryptography (ECC) Cipher Suites for TLS\". 
### RFC 7301: \"Transport Layer Security (TLS) Application-Layer Protocol Negotiation Extension\". 
### RFC 7366: \"Encrypt-then-MAC for Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)\". 
### RFC 7465: \"Prohibiting RC4 Cipher Suites\". 
### RFC 7507: \"TLS Fallback Signaling Cipher Suite Value (SCSV) for Preventing Protocol Downgrade Attacks\". 
### RFC 7568: \"Deprecating Secure Sockets Layer Version 3.0\". 
### RFC 7627: \"Transport Layer Security (TLS) Session Hash and Extended Master Secret Extension\". 
### RFC 7685: \"A Transport Layer Security (TLS) ClientHello Padding Extension\".Encapsulations of TLS include: 

### RFC 5216: \"The EAP-TLS Authentication Protocol\"
## Informational RFCs  
### RFC 7457: \"Summarizing Known Attacks on Transport Layer Security (TLS) and Datagram TLS (DTLS)\" 
### RFC 7525: \"Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)\"
## See also  
### Application-Layer Protocol Negotiation \u2013 a TLS extension used for SPDY and TLS False Start 
### Bullrun (decryption program) \u2013 a secret anti-encryption program run by the U.S. National Security Agency 
### Certificate authority 
### Certificate Transparency 
### HTTP Strict Transport Security \u2013 HSTS 
### Key ring file 
### Private Communications Technology (PCT) \u2013 a historic Microsoft competitor to SSL 2.0 
### QUIC (Quick UDP Internet Connections) \u2013 \"...was designed to provide security protection equivalent to TLS/SSL\"; QUIC's main goal is to improve perceived performance of connection-oriented web applications that are currently using TCP 
### Server-Gated Cryptography 
### tcpcrypt 
### DTLS 
### TLS acceleration
## References 
## Further reading  
### Wagner, David; Schneier, Bruce (November 1996). \"Analysis of the SSL 3.0 Protocol\" (PDF). The Second USENIX Workshop on Electronic Commerce Proceedings. USENIX Press. pp. 29\u201340. 
### Eric Rescorla (2001). SSL and TLS: Designing and Building Secure Systems. United States: Addison-Wesley Pub Co. ISBN 978-0-201-61598-2. 
### Stephen A. Thomas (2000). SSL and TLS essentials securing the Web. New York: Wiley. ISBN 978-0-471-38354-3. 
### Bard, Gregory (2006). \"A Challenging But Feasible Blockwise-Adaptive Chosen-Plaintext Attack on SSL\". International Association for Cryptologic Research (136). Retrieved 2011-09-23. 
### Canvel, Brice. \"Password Interception in a SSL/TLS Channel\". Retrieved 2007-04-20. 
### IETF Multiple Authors. \"RFC of change for TLS Renegotiation\". Retrieved 2009-12-11. 
### Creating VPNs with IPsec and SSL/TLS Linux Journal article by Rami Rosen 
### Joshua Davies (2010). Implementing SSL/TLS. Wiley. ISBN 978-0470920411. 
### Polk, Tim; McKay, Kerry; Chokhani, Santosh (April 2014). \"Guidelines for the Selection, Configuration, and Use of Transport Layer Security (TLS) Implementations\" (PDF). National Institute of Standards and Technology. Archived from the original (PDF) on 2014-05-08. Retrieved 2014-05-07. 
### Abdou, AbdelRahman; van Oorschot, Paul (August 2017). \"Server Location Verification (SLV) and Server Location Pinning: Augmenting TLS Authentication\". Transactions on Privacy and Security. ACM. 21 (1): 1:1\u20131:26. doi:10.1145/3139294. S2CID 5869541.
## External links  
### IETF (Internet Engineering Task Force) TLS Workgroup"
## References
### [Reference](http://googleonlinesecurity.blogspot.com.au/2011/11/protecting-data-for-long-term-with.html) - http://googleonlinesecurity.blogspot.com.au/2011/11/protecting-data-for-long-term-with.html
### [Reference](http://lasecwww.epfl.ch/memo/memo_ssl.shtml) - http://lasecwww.epfl.ch/memo/memo_ssl.shtml
### [Reference](http://developer.android.com/about/versions/android-5.0-changes.html#ssl) - http://developer.android.com/about/versions/android-5.0-changes.html#ssl
### [Reference](http://developer.android.com/reference/javax/net/ssl/SSLSocket.html) - http://developer.android.com/reference/javax/net/ssl/SSLSocket.html
### [Reference](http://support.apple.com/kb/HT6011) - http://support.apple.com/kb/HT6011
### [Reference](http://support.apple.com/kb/HT6531) - http://support.apple.com/kb/HT6531
### [Reference](http://support.apple.com/kb/HT6541) - http://support.apple.com/kb/HT6541
### [Reference](http://googlechromereleases.blogspot.com/2014/02/stable-channel-update_20.html) - http://googlechromereleases.blogspot.com/2014/02/stable-channel-update_20.html
### [Reference](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-exploiting-ssl-30.html) - http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-exploiting-ssl-30.html
### [Reference](http://scarybeastsecurity.blogspot.com/2009/02/vsftpd-210-released.html) - http://scarybeastsecurity.blogspot.com/2009/02/vsftpd-210-released.html
### [Reference](http://www.conceivablytech.com/3299/products/false-start-google-proposes-faster-web-chrome-supports-it-already) - http://www.conceivablytech.com/3299/products/false-start-google-proposes-faster-web-chrome-supports-it-already
### [Reference](http://blog.cryptographyengineering.com/2013/03/attack-of-week-rc4-is-kind-of-broken-in.html) - http://blog.cryptographyengineering.com/2013/03/attack-of-week-rc4-is-kind-of-broken-in.html
### [Reference](http://www.esecurityplanet.com/mac-os-security/apple-secures-mac-os-x-with-mavericks-release.html) - http://www.esecurityplanet.com/mac-os-security/apple-secures-mac-os-x-with-mavericks-release.html
### [Reference](http://bluecoat.force.com/knowledgebase/articles/Technical_Alert/000032878) - http://bluecoat.force.com/knowledgebase/articles/Technical_Alert/000032878
### [Reference](http://code.google.com/p/chromium/issues/detail?id=278370) - http://code.google.com/p/chromium/issues/detail?id=278370
### [Reference](http://www.intelsecurity.com/advanced-threat-research/) - http://www.intelsecurity.com/advanced-threat-research/
### [Reference](http://blog.ivanristic.com/2013/10/apple-enabled-beast-mitigations-in-mavericks.html) - http://blog.ivanristic.com/2013/10/apple-enabled-beast-mitigations-in-mavericks.html
### [Reference](http://www.linuxjournal.com/article/9916) - http://www.linuxjournal.com/article/9916
### [Reference](http://labs.mwrinfosecurity.com/blog/2012/04/16/adventures-with-ios-uiwebviews/) - http://labs.mwrinfosecurity.com/blog/2012/04/16/adventures-with-ios-uiwebviews/
### [Reference](http://news.netcraft.com/archives/2015/05/13/counting-ssl-certificates.html) - http://news.netcraft.com/archives/2015/05/13/counting-ssl-certificates.html
### [Reference](http://home.netscape.com/newsref/std/SSL.html) - http://home.netscape.com/newsref/std/SSL.html
### [Reference](http://www.networkworld.com/news/2011/101111-elgamal-251806.html) - http://www.networkworld.com/news/2011/101111-elgamal-251806.html
### [Reference](http://www.networkworld.com/news/2012/120412-elgamal-264739.html) - http://www.networkworld.com/news/2012/120412-elgamal-264739.html
### [Reference](http://www.oracle.com/technetwork/java/javase/8u31-relnotes-2389094.html) - http://www.oracle.com/technetwork/java/javase/8u31-relnotes-2389094.html
### [Reference](http://www.schneier.com/paper-ssl.pdf) - http://www.schneier.com/paper-ssl.pdf
### [Reference](http://serverfault.com/questions/315042/) - http://serverfault.com/questions/315042/
### [Reference](http://blogs.technet.com/b/srd/archive/2013/11/12/security-advisory-2868725-recommendation-to-disable-rc4.aspx) - http://blogs.technet.com/b/srd/archive/2013/11/12/security-advisory-2868725-recommendation-to-disable-rc4.aspx
### [Reference](http://searchsecurity.techtarget.com/answer/From-1024-to-2048-bit-The-security-effect-of-encryption-key-length) - http://searchsecurity.techtarget.com/answer/From-1024-to-2048-bit-The-security-effect-of-encryption-key-length
### [Reference](http://www.theiphoneblog.com/2009/03/31/iphone-30-mobile-safari-enhanced-security-certificate-visualization/) - http://www.theiphoneblog.com/2009/03/31/iphone-30-mobile-safari-enhanced-security-certificate-visualization/
### [Reference](http://threatpost.com/en_us/blogs/crime-attack-uses-compression-ratio-tls-requests-side-channel-hijack-secure-sessions-091312) - http://threatpost.com/en_us/blogs/crime-attack-uses-compression-ratio-tls-requests-side-channel-hijack-secure-sessions-091312
### [Reference](http://wolfssl.com/wolfSSL/Blog/Entries/2015/8/24_wolfSSL_3.6.6_is_Now_Available.html) - http://wolfssl.com/wolfSSL/Blog/Entries/2015/8/24_wolfSSL_3.6.6_is_Now_Available.html
### [Reference](http://forum.xda-developers.com/windows-phone-8/development/poodle-ssl-vulnerability-secure-windows-t2906203) - http://forum.xda-developers.com/windows-phone-8/development/poodle-ssl-vulnerability-secure-windows-t2906203
### [Reference](http://news.ycombinator.com/item?id=3015498) - http://news.ycombinator.com/item?id=3015498
### [Reference](http://citeseer.ist.psu.edu/diffie92authentication.html) - http://citeseer.ist.psu.edu/diffie92authentication.html
### [Reference](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.59.6682) - http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.59.6682
### [Reference](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.663.4653) - http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.663.4653
### [Reference](http://crypto.stanford.edu/~dabo/pubs/abstracts/websec_ecc.html) - http://crypto.stanford.edu/~dabo/pubs/abstracts/websec_ecc.html
### [Reference](http://www.cs.utexas.edu/users/lam/Vita/Cpapers/WBSL94.pdf) - http://www.cs.utexas.edu/users/lam/Vita/Cpapers/WBSL94.pdf
### [Reference](http://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf) - http://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf
### [Reference](http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf) - http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf
### [Reference](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r1.pdf) - http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r1.pdf
### [Reference](http://vincent.bernat.im/en/blog/2011-ssl-perfect-forward-secrecy.html) - http://vincent.bernat.im/en/blog/2011-ssl-perfect-forward-secrecy.html
### [Reference](http://googlechromereleases.blogspot.jp/2011/10/chrome-stable-release.html) - http://googlechromereleases.blogspot.jp/2011/10/chrome-stable-release.html
### [Reference](http://www.carbonwind.net/TLS_Cipher_Suites_Project/tls_ssl_cipher_suites_annex_a1_main.docx) - http://www.carbonwind.net/TLS_Cipher_Suites_Project/tls_ssl_cipher_suites_annex_a1_main.docx
### [Reference](http://www.carbonwind.net/blog/post/Random-SSLTLS-101-False-Start.aspx) - http://www.carbonwind.net/blog/post/Random-SSLTLS-101-False-Start.aspx
### [Reference](http://botan.randombit.net/relnotes/1_11_13.html) - http://botan.randombit.net/relnotes/1_11_13.html
### [Reference](http://seed7.sourceforge.net/libraries/tls.htm) - http://seed7.sourceforge.net/libraries/tls.htm
### [Reference](http://googlechromereleases.blogspot.nl/2012/05/dev-channel-update_29.html) - http://googlechromereleases.blogspot.nl/2012/05/dev-channel-update_29.html
### [Reference](http://tim.dierks.org/2014/05/security-standards-and-name-changes-in.html) - http://tim.dierks.org/2014/05/security-standards-and-name-changes-in.html
### [Reference](http://doi.org/10.1007%2F978-3-642-19574-7_5) - http://doi.org/10.1007%2F978-3-642-19574-7_5
### [Reference](http://doi.org/10.1007%2FBF00124891) - http://doi.org/10.1007%2FBF00124891
### [Reference](http://doi.org/10.1109%2FMIC.2014.86) - http://doi.org/10.1109%2FMIC.2014.86
### [Reference](http://doi.org/10.1145%2F3139294) - http://doi.org/10.1145%2F3139294
### [Reference](http://doi.org/10.14722%2Fndss.2017.23456) - http://doi.org/10.14722%2Fndss.2017.23456
### [Reference](http://doi.org/10.17487%2FRFC5246) - http://doi.org/10.17487%2FRFC5246
### [Reference](http://www.educatedguesswork.org/2009/11/understanding_the_tls_renegoti.html) - http://www.educatedguesswork.org/2009/11/understanding_the_tls_renegoti.html
### [Reference](http://article.gmane.org/gmane.network.gnutls.general/2046) - http://article.gmane.org/gmane.network.gnutls.general/2046
### [Reference](http://lists.gnutls.org/pipermail/gnutls-devel/2015-April/007535.html) - http://lists.gnutls.org/pipermail/gnutls-devel/2015-April/007535.html
### [Reference](http://eprint.iacr.org/2006/136) - http://eprint.iacr.org/2006/136
### [Reference](http://tools.ietf.org/html/draft-bmoeller-tls-falsestart-00) - http://tools.ietf.org/html/draft-bmoeller-tls-falsestart-00
### [Reference](http://tools.ietf.org/html/draft-chudov-cryptopro-cptls-04) - http://tools.ietf.org/html/draft-chudov-cryptopro-cptls-04
### [Reference](http://tools.ietf.org/html/draft-hickman-netscape-ssl-00) - http://tools.ietf.org/html/draft-hickman-netscape-ssl-00
### [Reference](http://tools.ietf.org/html/rfc4279) - http://tools.ietf.org/html/rfc4279
### [Reference](http://tools.ietf.org/html/rfc4346) - http://tools.ietf.org/html/rfc4346
### [Reference](http://tools.ietf.org/html/rfc5054) - http://tools.ietf.org/html/rfc5054
### [Reference](http://tools.ietf.org/html/rfc5246) - http://tools.ietf.org/html/rfc5246
### [Reference](http://tools.ietf.org/html/rfc5246#ref-TLS1.1) - http://tools.ietf.org/html/rfc5246#ref-TLS1.1
### [Reference](http://tools.ietf.org/html/rfc5630) - http://tools.ietf.org/html/rfc5630
### [Reference](http://tools.ietf.org/html/rfc5746) - http://tools.ietf.org/html/rfc5746
### [Reference](http://tools.ietf.org/html/rfc7366) - http://tools.ietf.org/html/rfc7366
### [Reference](http://tools.ietf.org/html/rfc7457) - http://tools.ietf.org/html/rfc7457
### [Reference](http://www.ietf.org/mail-archive/web/tls/current/msg06933.html) - http://www.ietf.org/mail-archive/web/tls/current/msg06933.html
### [Reference](http://www1.ietf.org/mail-archive/web/tls/current/msg02134.html) - http://www1.ietf.org/mail-archive/web/tls/current/msg02134.html
### [Reference](http://www.imc.org/ietf-openpgp/mail-archive/msg06063.html) - http://www.imc.org/ietf-openpgp/mail-archive/msg06063.html
### [Reference](http://www.matrixssl.org/news.html) - http://www.matrixssl.org/news.html
### [Reference](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3555) - http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3555
### [Reference](http://www.openssl.org/~bodo/tls-cbc.txt) - http://www.openssl.org/~bodo/tls-cbc.txt
### [Reference](http://arquivo.pt/wayback/20110122130054/https://groups.google.com/forum/#!topic/mozilla.dev.platform/JIEFcrGhqSM/discussion) - http://arquivo.pt/wayback/20110122130054/https://groups.google.com/forum/#!topic/mozilla.dev.platform/JIEFcrGhqSM/discussion
### [Reference](http://arquivo.pt/wayback/20110122130054/https://groups.google.com/forum/#!searchin/mozilla.dev.platform/rc4/mozilla.dev.platform/JIEFcrGhqSM/CIjtpwxoLQAJ) - http://arquivo.pt/wayback/20110122130054/https://groups.google.com/forum/#!searchin/mozilla.dev.platform/rc4/mozilla.dev.platform/JIEFcrGhqSM/CIjtpwxoLQAJ
### [Reference](http://curl.haxx.se/mail/lib-2012-08/0120.html) - http://curl.haxx.se/mail/lib-2012-08/0120.html
### [Reference](http://www.isg.rhul.ac.uk/tls/) - http://www.isg.rhul.ac.uk/tls/
### [Reference](http://www.isg.rhul.ac.uk/tls/RC4biases.pdf) - http://www.isg.rhul.ac.uk/tls/RC4biases.pdf
### [Reference](http://www.computing.co.uk/ctg/news/2285984/google-updates-ssl-certificates-to-2048bit-encryption) - http://www.computing.co.uk/ctg/news/2285984/google-updates-ssl-certificates-to-2048bit-encryption
### [Reference](https://www.cosic.esat.kuleuven.be/publications/article-2216.pdf) - https://www.cosic.esat.kuleuven.be/publications/article-2216.pdf
### [Reference](https://www.switch.ch/pki/meetings/2007-01/namebased_ssl_virtualhosts.pdf) - https://www.switch.ch/pki/meetings/2007-01/namebased_ssl_virtualhosts.pdf
### [Reference](https://developer.android.com/about/versions/oreo/android-8.0-changes.html) - https://developer.android.com/about/versions/oreo/android-8.0-changes.html
### [Reference](https://developer.android.com/reference/javax/net/ssl/SSLSocket.html) - https://developer.android.com/reference/javax/net/ssl/SSLSocket.html
### [Reference](https://developer.apple.com/library/ios/#technotes/tn2287/_index.html) - https://developer.apple.com/library/ios/#technotes/tn2287/_index.html
### [Reference](https://developer.apple.com/library/ios/technotes/tn2287/) - https://developer.apple.com/library/ios/technotes/tn2287/
### [Reference](https://developer.apple.com/library/mac/documentation/security/Reference/secureTransportRef/Reference/reference.html#//apple_ref/c/tdef/SSLProtocol) - https://developer.apple.com/library/mac/documentation/security/Reference/secureTransportRef/Reference/reference.html#//apple_ref/c/tdef/SSLProtocol
### [Reference](https://support.apple.com/en-us/HT204413) - https://support.apple.com/en-us/HT204413
### [Reference](https://support.apple.com/en-us/HT204423) - https://support.apple.com/en-us/HT204423
### [Reference](https://support.apple.com/en-us/HT204941) - https://support.apple.com/en-us/HT204941
### [Reference](https://support.apple.com/en-us/HT204942) - https://support.apple.com/en-us/HT204942
### [Reference](https://www.apple.com/safari/features.html) - https://www.apple.com/safari/features.html
### [Reference](https://arstechnica.com/gadgets/2018/10/browser-vendors-unite-to-end-support-for-20-year-old-tls-1-0/) - https://arstechnica.com/gadgets/2018/10/browser-vendors-unite-to-end-support-for-20-year-old-tls-1-0/
### [Reference](https://arstechnica.com/information-technology/2015/02/lenovo-pcs-ship-with-man-in-the-middle-adware-that-breaks-https-connections/) - https://arstechnica.com/information-technology/2015/02/lenovo-pcs-ship-with-man-in-the-middle-adware-that-breaks-https-connections/
### [Reference](https://arstechnica.com/security/2012/09/crime-hijacks-https-sessions/) - https://arstechnica.com/security/2012/09/crime-hijacks-https-sessions/
### [Reference](https://arstechnica.com/security/2013/08/gone-in-30-seconds-new-attack-plucks-secrets-from-https-protected-pages/) - https://arstechnica.com/security/2013/08/gone-in-30-seconds-new-attack-plucks-secrets-from-https-protected-pages/
### [Reference](https://arstechnica.com/security/2015/05/https-crippling-attack-threatens-tens-of-thousands-of-web-and-mail-servers/) - https://arstechnica.com/security/2015/05/https-crippling-attack-threatens-tens-of-thousands-of-web-and-mail-servers/
### [Reference](https://arstechnica.com/security/2015/07/once-theoretical-crypto-attack-against-https-now-verges-on-practicality/) - https://arstechnica.com/security/2015/07/once-theoretical-crypto-attack-against-https-now-verges-on-practicality/
### [Reference](https://arstechnica.com/security/2016/03/more-than-13-million-https-websites-imperiled-by-new-decryption-attack/) - https://arstechnica.com/security/2016/03/more-than-13-million-https-websites-imperiled-by-new-decryption-attack/
### [Reference](https://arstechnica.com/security/2016/05/faulty-https-settings-leave-dozens-of-visa-sites-vulnerable-to-forgery-attacks/) - https://arstechnica.com/security/2016/05/faulty-https-settings-leave-dozens-of-visa-sites-vulnerable-to-forgery-attacks/
### [Reference](https://arstechnica.com/security/2016/07/new-attack-that-cripples-https-crypto-works-on-macs-windows-and-linux/) - https://arstechnica.com/security/2016/07/new-attack-that-cripples-https-crypto-works-on-macs-windows-and-linux/
### [Reference](https://arstechnica.com/security/2016/08/new-attack-can-pluck-secrets-from-1-of-https-traffic-affects-top-sites/) - https://arstechnica.com/security/2016/08/new-attack-can-pluck-secrets-from-1-of-https-traffic-affects-top-sites/
### [Reference](https://media.blackhat.com/us-13/US-13-Daigniere-TLS-Secrets-WP.pdf) - https://media.blackhat.com/us-13/US-13-Daigniere-TLS-Secrets-WP.pdf
### [Reference](https://media.blackhat.com/us-13/US-13-Daigniere-TLS-Secrets-Slides.pdf) - https://media.blackhat.com/us-13/US-13-Daigniere-TLS-Secrets-Slides.pdf
### [Reference](https://www.blackhat.com/us-13/briefings.html#Smyth) - https://www.blackhat.com/us-13/briefings.html#Smyth
### [Reference](https://googleonlinesecurity.blogspot.com/2015/12/an-update-on-sha-1-certificates-in.html) - https://googleonlinesecurity.blogspot.com/2015/12/an-update-on-sha-1-certificates-in.html
### [Reference](https://chromestatus.com/feature/5759116003770368) - https://chromestatus.com/feature/5759116003770368
### [Reference](https://www.circleid.com/posts/20190124_creating_tls_the_pioneering_role_of_ruth_nelson/) - https://www.circleid.com/posts/20190124_creating_tls_the_pioneering_role_of_ruth_nelson/
### [Reference](https://blog.cloudflare.com/tls-1-3-overview-and-q-and-a/) - https://blog.cloudflare.com/tls-1-3-overview-and-q-and-a/
### [Reference](https://support.cloudflare.com/hc/en-us/articles/203041594-What-browsers-work-with-Universal-SSL) - https://support.cloudflare.com/hc/en-us/articles/203041594-What-browsers-work-with-Universal-SSL
### [Reference](https://blogs.comodo.com/e-commerce/heartbleed-bug-comodo-urges-openssl-users-to-apply-patch/) - https://blogs.comodo.com/e-commerce/heartbleed-bug-comodo-urges-openssl-users-to-apply-patch/
### [Reference](https://ssl.comodo.com/wildcard-ssl-certificates.php) - https://ssl.comodo.com/wildcard-ssl-certificates.php
### [Reference](https://www.deseretnews.com/article/865686081/Lehis-DigiCert-swallows-web-security-competitor-in-1-billion-deal.html) - https://www.deseretnews.com/article/865686081/Lehis-DigiCert-swallows-web-security-competitor-in-1-billion-deal.html
### [Reference](https://www.forbes.com/sites/thesba/2018/05/30/changes-to-pci-compliance-are-coming-june-30-is-your-ecommerce-business-ready/) - https://www.forbes.com/sites/thesba/2018/05/30/changes-to-pci-compliance-are-coming-june-30-is-your-ecommerce-business-ready/
### [Reference](https://freakattack.com/) - https://freakattack.com/
### [Reference](https://www.fxsitecompat.com/en-US/docs/2015/rc4-is-now-allowed-only-on-whitelisted-sites/) - https://www.fxsitecompat.com/en-US/docs/2015/rc4-is-now-allowed-only-on-whitelisted-sites/
### [Reference](https://github.com/libressl-portable/portable/issues/228) - https://github.com/libressl-portable/portable/issues/228
### [Reference](https://gizmodo.com/everything-you-need-to-know-about-cloudbleed-the-lates-1792710616) - https://gizmodo.com/everything-you-need-to-know-about-cloudbleed-the-lates-1792710616
### [Reference](https://support.globalsign.com/customer/portal/articles/1499561-sha-256-compatibility) - https://support.globalsign.com/customer/portal/articles/1499561-sha-256-compatibility
### [Reference](https://support.globalsign.com/customer/portal/articles/1995283-ecc-compatibility) - https://support.globalsign.com/customer/portal/articles/1995283-ecc-compatibility
### [Reference](https://books.google.com/books?id=5PJisOKJ0k8C&pg=PA22) - https://books.google.com/books?id=5PJisOKJ0k8C&pg=PA22
### [Reference](https://books.google.com/books?id=jm6uDgAAQBAJ&pg=PA15) - https://books.google.com/books?id=jm6uDgAAQBAJ&pg=PA15
### [Reference](https://code.google.com/p/chromium/issues/detail?id=318442) - https://code.google.com/p/chromium/issues/detail?id=318442
### [Reference](https://code.google.com/p/chromium/issues/detail?id=375342) - https://code.google.com/p/chromium/issues/detail?id=375342
### [Reference](https://code.google.com/p/chromium/issues/detail?id=436391) - https://code.google.com/p/chromium/issues/detail?id=436391
### [Reference](https://code.google.com/p/chromium/issues/detail?id=490240) - https://code.google.com/p/chromium/issues/detail?id=490240
### [Reference](https://code.google.com/p/chromium/issues/detail?id=90392) - https://code.google.com/p/chromium/issues/detail?id=90392
### [Reference](https://groups.google.com/a/chromium.org/forum/#!msg/security-dev/kVfCywocUO8/vgi_rQuhKgAJ) - https://groups.google.com/a/chromium.org/forum/#!msg/security-dev/kVfCywocUO8/vgi_rQuhKgAJ
### [Reference](https://groups.google.com/a/chromium.org/forum/#!msg/security-dev/kVfCywocUO8/2BW3INFdDwAJ) - https://groups.google.com/a/chromium.org/forum/#!msg/security-dev/kVfCywocUO8/2BW3INFdDwAJ
### [Reference](https://groups.google.com/a/chromium.org/forum/#!topic/security-dev/Vnhy9aKM_l4) - https://groups.google.com/a/chromium.org/forum/#!topic/security-dev/Vnhy9aKM_l4
### [Reference](https://groups.google.com/forum/#!searchin/mozilla.dev.platform/rc4/mozilla.dev.platform/JIEFcrGhqSM/CIjtpwxoLQAJ) - https://groups.google.com/forum/#!searchin/mozilla.dev.platform/rc4/mozilla.dev.platform/JIEFcrGhqSM/CIjtpwxoLQAJ
### [Reference](https://groups.google.com/forum/#!topic/mozilla.dev.platform/JIEFcrGhqSM/discussion) - https://groups.google.com/forum/#!topic/mozilla.dev.platform/JIEFcrGhqSM/discussion
### [Reference](https://sites.google.com/site/tlsssloverview/ssl-v-tls/tls-versions-and-browser-compatability) - https://sites.google.com/site/tlsssloverview/ssl-v-tls/tls-versions-and-browser-compatability
### [Reference](https://support.google.com/chrome/a/answer/7679408?hl=en) - https://support.google.com/chrome/a/answer/7679408?hl=en
### [Reference](https://www.instantssl.com/ssl-certificate-products/https.html) - https://www.instantssl.com/ssl-certificate-products/https.html
### [Reference](https://mcpmag.com/articles/2020/04/02/microsoft-tls-1-0-and-1-1.aspx) - https://mcpmag.com/articles/2020/04/02/microsoft-tls-1-0-and-1-1.aspx
### [Reference](https://blogs.microsoft.com/cybertrust/2014/11/11/hundreds-of-millions-of-microsoft-customers-now-benefit-from-best-in-class-encryption/) - https://blogs.microsoft.com/cybertrust/2014/11/11/hundreds-of-millions-of-microsoft-customers-now-benefit-from-best-in-class-encryption/
### [Reference](https://devblogs.microsoft.com/premier-developer/microsoft-tls-1-3-support-reference/) - https://devblogs.microsoft.com/premier-developer/microsoft-tls-1-3-support-reference/
### [Reference](https://docs.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#sslversionmin) - https://docs.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#sslversionmin
### [Reference](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785811(v=ws.10)) - https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785811(v=ws.10)
### [Reference](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-phone/dn756283(v=technet.10)) - https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-phone/dn756283(v=technet.10)
### [Reference](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-8.1-and-8/dn303404(v=ws.11)) - https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-8.1-and-8/dn303404(v=ws.11)
### [Reference](https://docs.microsoft.com/en-us/security-updates/SecurityAdvisories/2015/3009008) - https://docs.microsoft.com/en-us/security-updates/SecurityAdvisories/2015/3009008
### [Reference](https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2015/ms15-031) - https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2015/ms15-031
### [Reference](https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2015/ms15-055) - https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2015/ms15-055
### [Reference](https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2012/ms12-006) - https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2012/ms12-006
### [Reference](https://docs.microsoft.com/en-us/windows-server/security/tls/tls-schannel-ssp-changes-in-windows-10-and-windows-server) - https://docs.microsoft.com/en-us/windows-server/security/tls/tls-schannel-ssp-changes-in-windows-10-and-windows-server
### [Reference](https://docs.microsoft.com/en-us/windows/whats-new/whats-new-windows-10-version-1909) - https://docs.microsoft.com/en-us/windows/whats-new/whats-new-windows-10-version-1909
### [Reference](https://docs.microsoft.com/en-us/windows/win32/secauthn/protocols-in-tls-ssl--schannel-ssp-) - https://docs.microsoft.com/en-us/windows/win32/secauthn/protocols-in-tls-ssl--schannel-ssp-
### [Reference](https://msdn.microsoft.com/en-us/library/aa380123.aspx) - https://msdn.microsoft.com/en-us/library/aa380123.aspx
### [Reference](https://msdn.microsoft.com/en-us/library/bb250503.aspx) - https://msdn.microsoft.com/en-us/library/bb250503.aspx
### [Reference](https://msdn.microsoft.com/en-us/library/dd208005.aspx) - https://msdn.microsoft.com/en-us/library/dd208005.aspx
### [Reference](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380512.aspx) - https://msdn.microsoft.com/en-us/library/windows/desktop/aa380512.aspx
### [Reference](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380512(v=vs.85).aspx) - https://msdn.microsoft.com/en-us/library/windows/desktop/aa380512(v=vs.85).aspx
### [Reference](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374757(v=vs.85).aspx) - https://msdn.microsoft.com/en-us/library/windows/desktop/aa374757(v=vs.85).aspx
### [Reference](https://msdn.microsoft.com/en-us/library/windows/desktop/ff468651(v=vs.85).aspx) - https://msdn.microsoft.com/en-us/library/windows/desktop/ff468651(v=vs.85).aspx
### [Reference](https://social.msdn.microsoft.com/Forums/windowsapps/en-US/2ddee177-5086-4453-987b-d02b6a7ec62d/what-tls-version-is-used-in-windows-phone-8-for-secure-http-connections?forum=wpdevelop) - https://social.msdn.microsoft.com/Forums/windowsapps/en-US/2ddee177-5086-4453-987b-d02b6a7ec62d/what-tls-version-is-used-in-windows-phone-8-for-secure-http-connections?forum=wpdevelop
### [Reference](https://support.microsoft.com/en-us/gp/microsoft-internet-explorer) - https://support.microsoft.com/en-us/gp/microsoft-internet-explorer
### [Reference](https://support.microsoft.com/en-us/help/4492872/update-for-internet-explorer-april-16-2019) - https://support.microsoft.com/en-us/help/4492872/update-for-internet-explorer-april-16-2019
### [Reference](https://support.microsoft.com/kb/2868725/) - https://support.microsoft.com/kb/2868725/
### [Reference](https://support.microsoft.com/kb/3038778) - https://support.microsoft.com/kb/3038778
### [Reference](https://support.microsoft.com/kb/4019276) - https://support.microsoft.com/kb/4019276
### [Reference](https://support.microsoft.com/kb/948963) - https://support.microsoft.com/kb/948963
### [Reference](https://windows.microsoft.com/en-us/windows/lifecycle) - https://windows.microsoft.com/en-us/windows/lifecycle
### [Reference](https://blogs.msdn.com/b/ie/archive/2015/02/10/february-2015-security-updates-for-internet-explorer.aspx) - https://blogs.msdn.com/b/ie/archive/2015/02/10/february-2015-security-updates-for-internet-explorer.aspx
### [Reference](https://blogs.msdn.com/b/ieinternals/archive/2009/06/19/windows-7-support-for-tls-and-ciphers.aspx) - https://blogs.msdn.com/b/ieinternals/archive/2009/06/19/windows-7-support-for-tls-and-ciphers.aspx
### [Reference](https://blogs.msdn.com/b/ieinternals/archive/2013/09/24/internet-explorer-11-changelist-change-log.aspx) - https://blogs.msdn.com/b/ieinternals/archive/2013/09/24/internet-explorer-11-changelist-change-log.aspx
### [Reference](https://www.nbcnews.com/id/44896639) - https://www.nbcnews.com/id/44896639
### [Reference](https://docs.oracle.com/en/java/javase/17/security/java-secure-socket-extension-jsse-reference-guide.html) - https://docs.oracle.com/en/java/javase/17/security/java-secure-socket-extension-jsse-reference-guide.html
### [Reference](https://answers.psionline.com/knowledgebase/tls-1-2-faq/) - https://answers.psionline.com/knowledgebase/tls-1-2-faq/
### [Reference](https://community.qualys.com/blogs/securitylabs/2013/03/19/rc4-in-tls-is-broken-now-what) - https://community.qualys.com/blogs/securitylabs/2013/03/19/rc4-in-tls-is-broken-now-what
### [Reference](https://community.qualys.com/blogs/securitylabs/2013/06/25/ssl-labs-deploying-forward-secrecy) - https://community.qualys.com/blogs/securitylabs/2013/06/25/ssl-labs-deploying-forward-secrecy
### [Reference](https://community.qualys.com/blogs/securitylabs/2013/09/10/is-beast-still-a-threat) - https://community.qualys.com/blogs/securitylabs/2013/09/10/is-beast-still-a-threat
### [Reference](https://community.qualys.com/blogs/securitylabs/2013/10/31/apple-enabled-beast-mitigations-in-os-x-109-mavericks) - https://community.qualys.com/blogs/securitylabs/2013/10/31/apple-enabled-beast-mitigations-in-os-x-109-mavericks
### [Reference](https://community.qualys.com/thread/12092) - https://community.qualys.com/thread/12092
### [Reference](https://community.qualys.com/thread/12496) - https://community.qualys.com/thread/12496
### [Reference](https://access.redhat.com/articles/1232123) - https://access.redhat.com/articles/1232123
### [Reference](https://www.rsaconference.com/writable/presentations/file_upload/sec-t02_final.pdf) - https://www.rsaconference.com/writable/presentations/file_upload/sec-t02_final.pdf
### [Reference](https://www.smacktls.com) - https://www.smacktls.com
### [Reference](https://www.smacktls.com/#freak) - https://www.smacktls.com/#freak
### [Reference](https://dev.ssllabs.com/ssltest/clients.html) - https://dev.ssllabs.com/ssltest/clients.html
### [Reference](https://www.ssllabs.com/projects/best-practices/index.html) - https://www.ssllabs.com/projects/best-practices/index.html
### [Reference](https://www.ssllabs.com/ssl-pulse/) - https://www.ssllabs.com/ssl-pulse/
### [Reference](https://www.ssllabs.com/ssltest/analyze.html?d=google.co.uk&s=74.125.227.183) - https://www.ssllabs.com/ssltest/analyze.html?d=google.co.uk&s=74.125.227.183
### [Reference](https://www.ssllabs.com/ssltest/viewClient.html?name=IE%20Mobile&version=10&platform=Win%20Phone%208.0) - https://www.ssllabs.com/ssltest/viewClient.html?name=IE%20Mobile&version=10&platform=Win%20Phone%208.0
### [Reference](https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=8&platform=OS%20X%2010.10) - https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=8&platform=OS%20X%2010.10
### [Reference](https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=7&platform=iOS%207.1) - https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=7&platform=iOS%207.1
### [Reference](https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=8&platform=iOS%208.1.2) - https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=8&platform=iOS%208.1.2
### [Reference](https://crypto.stackexchange.com/questions/27131/differences-between-the-terms-pre-master-secret-master-secret-private-key) - https://crypto.stackexchange.com/questions/27131/differences-between-the-terms-pre-master-secret-master-secret-private-key
### [Reference](https://security.stackexchange.com/a/93338) - https://security.stackexchange.com/a/93338
### [Reference](https://stackoverflow.com/q/19221568) - https://stackoverflow.com/q/19221568
### [Reference](https://stackoverflow.com/q/881563) - https://stackoverflow.com/q/881563
### [Reference](https://blogs.technet.com/b/pki/archive/2010/09/30/sha2-and-windows.aspx) - https://blogs.technet.com/b/pki/archive/2010/09/30/sha2-and-windows.aspx
### [Reference](https://www.thesslstore.com/blog/twitter-will-deprecate-support-for-tls-1-0-tls-1-1-on-july-15/) - https://www.thesslstore.com/blog/twitter-will-deprecate-support-for-tls-1-0-tls-1-1-on-july-15/
### [Reference](https://blog.twitter.com/2013/forward-secrecy-at-twitter-0) - https://blog.twitter.com/2013/forward-secrecy-at-twitter-0
### [Reference](https://venturebeat.com/2015/09/01/google-microsoft-and-mozilla-will-drop-rc4-support-in-chrome-edge-ie-and-firefox-next-year/) - https://venturebeat.com/2015/09/01/google-microsoft-and-mozilla-will-drop-rc4-support-in-chrome-edge-ie-and-firefox-next-year/
### [Reference](https://knowledge.verisign.com/support/ssl-certificates-support/index?page=content&id=SO10090&actp=search&viewlocale=en_US&searchid=1406590748892) - https://knowledge.verisign.com/support/ssl-certificates-support/index?page=content&id=SO10090&actp=search&viewlocale=en_US&searchid=1406590748892
### [Reference](https://w3techs.com/technologies/history_overview/ssl_certificate) - https://w3techs.com/technologies/history_overview/ssl_certificate
### [Reference](https://www.washingtonpost.com/blogs/style-blog/wp/2014/04/09/why-is-it-called-the-heartbleed-bug/) - https://www.washingtonpost.com/blogs/style-blog/wp/2014/04/09/why-is-it-called-the-heartbleed-bug/
### [Reference](https://blogs.windows.com/msedgedev/2015/09/01/ending-support-for-the-rc4-cipher-in-microsoft-edge-and-internet-explorer-11/) - https://blogs.windows.com/msedgedev/2015/09/01/ending-support-for-the-rc4-cipher-in-microsoft-edge-and-internet-explorer-11/
### [Reference](https://blogs.windows.com/msedgedev/2016/08/09/rc4-now-deprecated/) - https://blogs.windows.com/msedgedev/2016/08/09/rc4-now-deprecated/
### [Reference](https://www.wired.com/threatlevel/2010/03/packet-forensics/) - https://www.wired.com/threatlevel/2010/03/packet-forensics/
### [Reference](https://www.wolfssl.com/differences-between-tls-12-and-tls-13-9/) - https://www.wolfssl.com/differences-between-tls-12-and-tls-13-9/
### [Reference](https://www.wolfssl.com/docs/tls13/) - https://www.wolfssl.com/docs/tls13/
### [Reference](https://www.wolfssl.com/tls-1-3-draft-28-support-wolfssl/) - https://www.wolfssl.com/tls-1-3-draft-28-support-wolfssl/
### [Reference](https://www.wolfssl.com/wolfssl-tls-1-3-beta-release-now-available/) - https://www.wolfssl.com/wolfssl-tls-1-3-beta-release-now-available/
### [Reference](https://www.youtube.com/watch?v=33XW5yzjtME&t=2338) - https://www.youtube.com/watch?v=33XW5yzjtME&t=2338
### [Reference](https://www.youtube.com/watch?v=u6rz4PWA_As&t=4526) - https://www.youtube.com/watch?v=u6rz4PWA_As&t=4526
### [Reference](https://hal.inria.fr/hal-01102013) - https://hal.inria.fr/hal-01102013
### [Reference](https://marc.info/?l=openbsd-announce&m=141486254309079&w=2) - https://marc.info/?l=openbsd-announce&m=141486254309079&w=2
### [Reference](https://marc.info/?l=openbsd-announce&m=144304330731220) - https://marc.info/?l=openbsd-announce&m=144304330731220
### [Reference](https://sweet32.info/SWEET32_CCS16.pdf) - https://sweet32.info/SWEET32_CCS16.pdf
### [Reference](https://blog.filippo.io/komodia-superfish-ssl-validation-is-broken/) - https://blog.filippo.io/komodia-superfish-ssl-validation-is-broken/
### [Reference](https://boingboing.net/2019/02/26/monumental-recklessness.html) - https://boingboing.net/2019/02/26/monumental-recklessness.html
### [Reference](https://www.ghacks.net/2020/03/10/here-is-what-is-new-and-changed-in-firefox-74-0-stable/) - https://www.ghacks.net/2020/03/10/here-is-what-is-new-and-changed-in-firefox-74-0-stable/
### [Reference](https://bugs.openjdk.java.net/browse/JDK-8256490) - https://bugs.openjdk.java.net/browse/JDK-8256490
### [Reference](https://dl.acm.org/citation.cfm?id=3139294) - https://dl.acm.org/citation.cfm?id=3139294
### [Reference](https://archive.org/details/ssltls00eric) - https://archive.org/details/ssltls00eric
### [Reference](https://web.archive.org/web/19970614020952/http://home.netscape.com/newsref/std/SSL.html) - https://web.archive.org/web/19970614020952/http://home.netscape.com/newsref/std/SSL.html
### [Reference](https://web.archive.org/web/20080313081157/http://citeseer.ist.psu.edu/diffie92authentication.html) - https://web.archive.org/web/20080313081157/http://citeseer.ist.psu.edu/diffie92authentication.html
### [Reference](https://web.archive.org/web/20090403074546/http://www.theiphoneblog.com/2009/03/31/iphone-30-mobile-safari-enhanced-security-certificate-visualization/) - https://web.archive.org/web/20090403074546/http://www.theiphoneblog.com/2009/03/31/iphone-30-mobile-safari-enhanced-security-certificate-visualization/
### [Reference](https://web.archive.org/web/20101007061707/http://www.conceivablytech.com/3299/products/false-start-google-proposes-faster-web-chrome-supports-it-already/) - https://web.archive.org/web/20101007061707/http://www.conceivablytech.com/3299/products/false-start-google-proposes-faster-web-chrome-supports-it-already/
### [Reference](https://web.archive.org/web/20101126121933/http://openssl.org/docs/ssl/SSL_CTX_set_options.html#SECURE_RENEGOTIATION) - https://web.archive.org/web/20101126121933/http://openssl.org/docs/ssl/SSL_CTX_set_options.html#SECURE_RENEGOTIATION
### [Reference](https://web.archive.org/web/20110504014418/http://www.ietf.org/mail-archive/web/tls/current/msg06933.html) - https://web.archive.org/web/20110504014418/http://www.ietf.org/mail-archive/web/tls/current/msg06933.html
### [Reference](https://web.archive.org/web/20110504060256/http://www.carbonwind.net/blog/post/Random-SSLTLS-101-False-Start.aspx) - https://web.archive.org/web/20110504060256/http://www.carbonwind.net/blog/post/Random-SSLTLS-101-False-Start.aspx
### [Reference](https://web.archive.org/web/20110907013839/http://developer.apple.com/library/iOS/#technotes/tn2287/_index.html) - https://web.archive.org/web/20110907013839/http://developer.apple.com/library/iOS/#technotes/tn2287/_index.html
### [Reference](https://web.archive.org/web/20120306184633/https://developer.mozilla.org/NSS_3.12.6_release_notes) - https://web.archive.org/web/20120306184633/https://developer.mozilla.org/NSS_3.12.6_release_notes
### [Reference](https://web.archive.org/web/20120630143111/http://www.openssl.org/~bodo/tls-cbc.txt) - https://web.archive.org/web/20120630143111/http://www.openssl.org/~bodo/tls-cbc.txt
### [Reference](https://web.archive.org/web/20120707213409/http://scarybeastsecurity.blogspot.com/2009/02/vsftpd-210-released.html) - https://web.archive.org/web/20120707213409/http://scarybeastsecurity.blogspot.com/2009/02/vsftpd-210-released.html
### [Reference](https://web.archive.org/web/20120803022659/https://www.switch.ch/pki/meetings/2007-01/namebased_ssl_virtualhosts.pdf) - https://web.archive.org/web/20120803022659/https://www.switch.ch/pki/meetings/2007-01/namebased_ssl_virtualhosts.pdf
### [Reference](https://web.archive.org/web/20120825192441/http://googlechromereleases.blogspot.co.uk/2012/08/stable-channel-update_21.html) - https://web.archive.org/web/20120825192441/http://googlechromereleases.blogspot.co.uk/2012/08/stable-channel-update_21.html
### [Reference](https://web.archive.org/web/20120827064047/http://vincent.bernat.im/en/blog/2011-ssl-perfect-forward-secrecy.html) - https://web.archive.org/web/20120827064047/http://vincent.bernat.im/en/blog/2011-ssl-perfect-forward-secrecy.html
### [Reference](https://web.archive.org/web/20120829025314/http://msdn.microsoft.com/en-us/library/aa380123.aspx) - https://web.archive.org/web/20120829025314/http://msdn.microsoft.com/en-us/library/aa380123.aspx
### [Reference](https://web.archive.org/web/20120915224635/http://threatpost.com/en_us/blogs/crime-attack-uses-compression-ratio-tls-requests-side-channel-hijack-secure-sessions-091312) - https://web.archive.org/web/20120915224635/http://threatpost.com/en_us/blogs/crime-attack-uses-compression-ratio-tls-requests-side-channel-hijack-secure-sessions-091312
### [Reference](https://web.archive.org/web/20130117130029/https://developer.mozilla.org/en-US/docs/NSS/NSS_3.14_release_notes) - https://web.archive.org/web/20130117130029/https://developer.mozilla.org/en-US/docs/NSS/NSS_3.14_release_notes
### [Reference](https://web.archive.org/web/20130302032339/http://googlechromereleases.blogspot.nl/2012/05/dev-channel-update_29.html) - https://web.archive.org/web/20130302032339/http://googlechromereleases.blogspot.nl/2012/05/dev-channel-update_29.html
### [Reference](https://web.archive.org/web/20130314214026/http://blog.cryptographyengineering.com/2013/03/attack-of-week-rc4-is-kind-of-broken-in.html) - https://web.archive.org/web/20130314214026/http://blog.cryptographyengineering.com/2013/03/attack-of-week-rc4-is-kind-of-broken-in.html
### [Reference](https://web.archive.org/web/20130315084623/http://www.isg.rhul.ac.uk/tls/) - https://web.archive.org/web/20130315084623/http://www.isg.rhul.ac.uk/tls/
### [Reference](https://web.archive.org/web/20130506184654/http://googleonlinesecurity.blogspot.com.au/2011/11/protecting-data-for-long-term-with.html) - https://web.archive.org/web/20130506184654/http://googleonlinesecurity.blogspot.com.au/2011/11/protecting-data-for-long-term-with.html
### [Reference](https://web.archive.org/web/20130626193314/https://community.qualys.com/blogs/securitylabs/2013/06/25/ssl-labs-deploying-forward-secrecy) - https://web.archive.org/web/20130626193314/https://community.qualys.com/blogs/securitylabs/2013/06/25/ssl-labs-deploying-forward-secrecy
### [Reference](https://web.archive.org/web/20130703043525/https://sites.google.com/site/tlsssloverview/ssl-v-tls/tls-versions-and-browser-compatability) - https://web.archive.org/web/20130703043525/https://sites.google.com/site/tlsssloverview/ssl-v-tls/tls-versions-and-browser-compatability
### [Reference](https://web.archive.org/web/20130730124037/http://www.blackhat.com/us-13/briefings.html#Smyth) - https://web.archive.org/web/20130730124037/http://www.blackhat.com/us-13/briefings.html#Smyth
### [Reference](https://web.archive.org/web/20130801104610/http://arstechnica.com/security/2012/09/crime-hijacks-https-sessions/) - https://web.archive.org/web/20130801104610/http://arstechnica.com/security/2012/09/crime-hijacks-https-sessions/
### [Reference](https://web.archive.org/web/20130801193054/http://www.theregister.co.uk/2013/08/01/gmail_hotmail_hijacking/) - https://web.archive.org/web/20130801193054/http://www.theregister.co.uk/2013/08/01/gmail_hotmail_hijacking/
### [Reference](https://web.archive.org/web/20130803110745/http://code.google.com/p/chromium/issues/detail?id=90392) - https://web.archive.org/web/20130803110745/http://code.google.com/p/chromium/issues/detail?id=90392
### [Reference](https://web.archive.org/web/20130803181144/http://arstechnica.com/security/2013/08/gone-in-30-seconds-new-attack-plucks-secrets-from-https-protected-pages/) - https://web.archive.org/web/20130803181144/http://arstechnica.com/security/2013/08/gone-in-30-seconds-new-attack-plucks-secrets-from-https-protected-pages/
### [Reference](https://web.archive.org/web/20130805134805/https://media.blackhat.com/us-13/US-13-Daigniere-TLS-Secrets-Slides.pdf) - https://web.archive.org/web/20130805134805/https://media.blackhat.com/us-13/US-13-Daigniere-TLS-Secrets-Slides.pdf
### [Reference](https://web.archive.org/web/20130805233414/http://www.theregister.co.uk/2013/08/02/breach_crypto_attack/) - https://web.archive.org/web/20130805233414/http://www.theregister.co.uk/2013/08/02/breach_crypto_attack/
### [Reference](https://web.archive.org/web/20130806233112/https://media.blackhat.com/us-13/US-13-Daigniere-TLS-Secrets-WP.pdf) - https://web.archive.org/web/20130806233112/https://media.blackhat.com/us-13/US-13-Daigniere-TLS-Secrets-WP.pdf
### [Reference](https://web.archive.org/web/20130808221614/https://www.imperialviolet.org/2013/06/27/botchingpfs.html) - https://web.archive.org/web/20130808221614/https://www.imperialviolet.org/2013/06/27/botchingpfs.html
### [Reference](https://web.archive.org/web/20130827044512/https://community.qualys.com/blogs/securitylabs/2013/03/19/rc4-in-tls-is-broken-now-what) - https://web.archive.org/web/20130827044512/https://community.qualys.com/blogs/securitylabs/2013/03/19/rc4-in-tls-is-broken-now-what
### [Reference](https://web.archive.org/web/20130905074722/http://tools.ietf.org/html/rfc4279) - https://web.archive.org/web/20130905074722/http://tools.ietf.org/html/rfc4279
### [Reference](https://web.archive.org/web/20130905215608/http://tools.ietf.org/html/draft-bmoeller-tls-falsestart-00) - https://web.archive.org/web/20130905215608/http://tools.ietf.org/html/draft-bmoeller-tls-falsestart-00
### [Reference](https://web.archive.org/web/20130920150259/https://community.qualys.com/blogs/securitylabs/2013/06/25/ssl-labs-deploying-forward-secrecy) - https://web.archive.org/web/20130920150259/https://community.qualys.com/blogs/securitylabs/2013/06/25/ssl-labs-deploying-forward-secrecy
### [Reference](https://web.archive.org/web/20130922082322/http://www.computing.co.uk/ctg/news/2285984/google-updates-ssl-certificates-to-2048bit-encryption) - https://web.archive.org/web/20130922082322/http://www.computing.co.uk/ctg/news/2285984/google-updates-ssl-certificates-to-2048bit-encryption
### [Reference](https://web.archive.org/web/20130922103746/http://www.ietf.org/mail-archive/web/tls/current/msg02134.html) - https://web.archive.org/web/20130922103746/http://www.ietf.org/mail-archive/web/tls/current/msg02134.html
### [Reference](https://web.archive.org/web/20130922133950/https://www.usenix.org/sites/default/files/conference/protected-files/alfardan_sec13_slides.pdf) - https://web.archive.org/web/20130922133950/https://www.usenix.org/sites/default/files/conference/protected-files/alfardan_sec13_slides.pdf
### [Reference](https://web.archive.org/web/20130922170155/http://www.isg.rhul.ac.uk/tls/RC4biases.pdf) - https://web.archive.org/web/20130922170155/http://www.isg.rhul.ac.uk/tls/RC4biases.pdf
### [Reference](https://web.archive.org/web/20130922223238/https://developer.mozilla.org/en-US/docs/NSS/NSS_3.15.1_release_notes) - https://web.archive.org/web/20130922223238/https://developer.mozilla.org/en-US/docs/NSS/NSS_3.15.1_release_notes
### [Reference](https://web.archive.org/web/20130927055954/http://msdn.microsoft.com/en-us/library/dd208005.aspx) - https://web.archive.org/web/20130927055954/http://msdn.microsoft.com/en-us/library/dd208005.aspx
### [Reference](https://web.archive.org/web/20131005021656/http://code.google.com/p/chromium/issues/detail?id=278370) - https://web.archive.org/web/20131005021656/http://code.google.com/p/chromium/issues/detail?id=278370
### [Reference](https://web.archive.org/web/20131010205312/http://msdn.microsoft.com/en-us/library/bb250503.aspx) - https://web.archive.org/web/20131010205312/http://msdn.microsoft.com/en-us/library/bb250503.aspx
### [Reference](https://web.archive.org/web/20131030114356/http://blogs.msdn.com/b/ieinternals/archive/2013/09/24/internet-explorer-11-changelist-change-log.aspx) - https://web.archive.org/web/20131030114356/http://blogs.msdn.com/b/ieinternals/archive/2013/09/24/internet-explorer-11-changelist-change-log.aspx
### [Reference](https://web.archive.org/web/20131107045223/http://blog.ivanristic.com/2013/10/apple-enabled-beast-mitigations-in-mavericks.html) - https://web.archive.org/web/20131107045223/http://blog.ivanristic.com/2013/10/apple-enabled-beast-mitigations-in-mavericks.html
### [Reference](https://web.archive.org/web/20131118081816/http://blogs.technet.com/b/srd/archive/2013/11/12/security-advisory-2868725-recommendation-to-disable-rc4.aspx) - https://web.archive.org/web/20131118081816/http://blogs.technet.com/b/srd/archive/2013/11/12/security-advisory-2868725-recommendation-to-disable-rc4.aspx
### [Reference](https://web.archive.org/web/20131226222853/http://blogs.msdn.com/b/ieinternals/archive/2009/06/19/windows-7-support-for-tls-and-ciphers.aspx) - https://web.archive.org/web/20131226222853/http://blogs.msdn.com/b/ieinternals/archive/2009/06/19/windows-7-support-for-tls-and-ciphers.aspx
### [Reference](https://web.archive.org/web/20140207095334/https://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes/en-US/firefox/27.0/releasenotes/) - https://web.archive.org/web/20140207095334/https://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes/en-US/firefox/27.0/releasenotes/
### [Reference](https://web.archive.org/web/20140212214518/http://googleonlinesecurity.blogspot.com.au/2011/11/protecting-data-for-long-term-with.html) - https://web.archive.org/web/20140212214518/http://googleonlinesecurity.blogspot.com.au/2011/11/protecting-data-for-long-term-with.html
### [Reference](https://web.archive.org/web/20140216041202/https://blog.twitter.com/2013/forward-secrecy-at-twitter-0) - https://web.archive.org/web/20140216041202/https://blog.twitter.com/2013/forward-secrecy-at-twitter-0
### [Reference](https://web.archive.org/web/20140226230020/https://codereview.chromium.org/23503030/) - https://web.archive.org/web/20140226230020/https://codereview.chromium.org/23503030/
### [Reference](https://web.archive.org/web/20140315064727/http://www.wired.com/threatlevel/2010/03/packet-forensics) - https://web.archive.org/web/20140315064727/http://www.wired.com/threatlevel/2010/03/packet-forensics
### [Reference](https://web.archive.org/web/20140508025330/http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r1.pdf) - https://web.archive.org/web/20140508025330/http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r1.pdf
### [Reference](https://web.archive.org/web/20140531105257/http://www.networkworld.com/news/2011/101111-elgamal-251806.html) - https://web.archive.org/web/20140531105257/http://www.networkworld.com/news/2011/101111-elgamal-251806.html
### [Reference](https://web.archive.org/web/20140531105537/http://www.networkworld.com/news/2012/120412-elgamal-264739.html) - https://web.archive.org/web/20140531105537/http://www.networkworld.com/news/2012/120412-elgamal-264739.html
### [Reference](https://web.archive.org/web/20140603102506/https://bug665814.bugzilla.mozilla.org/attachment.cgi?id=540839) - https://web.archive.org/web/20140603102506/https://bug665814.bugzilla.mozilla.org/attachment.cgi?id=540839
### [Reference](https://web.archive.org/web/20140604052511/https://developer.apple.com/library/Mac/documentation/Security/Reference/secureTransportRef/Reference/reference.html#//apple_ref/c/tdef/SSLProtocol) - https://web.archive.org/web/20140604052511/https://developer.apple.com/library/Mac/documentation/Security/Reference/secureTransportRef/Reference/reference.html#//apple_ref/c/tdef/SSLProtocol
### [Reference](https://web.archive.org/web/20140605001016/https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.15.3_release_notes) - https://web.archive.org/web/20140605001016/https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.15.3_release_notes
### [Reference](https://web.archive.org/web/20140606050814/http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf) - https://web.archive.org/web/20140606050814/http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf
### [Reference](https://web.archive.org/web/20140704220956/http://support.apple.com/kb/HT6011) - https://web.archive.org/web/20140704220956/http://support.apple.com/kb/HT6011
### [Reference](https://web.archive.org/web/20140705212748/https://blogs.comodo.com/e-commerce/heartbleed-bug-comodo-urges-openssl-users-to-apply-patch/) - https://web.archive.org/web/20140705212748/https://blogs.comodo.com/e-commerce/heartbleed-bug-comodo-urges-openssl-users-to-apply-patch/
### [Reference](https://web.archive.org/web/20140708195022/http://www.esecurityplanet.com/mac-os-security/apple-secures-mac-os-x-with-mavericks-release.html) - https://web.archive.org/web/20140708195022/http://www.esecurityplanet.com/mac-os-security/apple-secures-mac-os-x-with-mavericks-release.html
### [Reference](https://web.archive.org/web/20140714121632/http://www.mozilla.org/security/announce/2013/mfsa2013-103.html) - https://web.archive.org/web/20140714121632/http://www.mozilla.org/security/announce/2013/mfsa2013-103.html
### [Reference](https://web.archive.org/web/20140714142705/https://developer.mozilla.org/en-US/Firefox/Releases/2/Security_changes) - https://web.archive.org/web/20140714142705/https://developer.mozilla.org/en-US/Firefox/Releases/2/Security_changes
### [Reference](https://web.archive.org/web/20140714162556/https://community.qualys.com/thread/12496) - https://web.archive.org/web/20140714162556/https://community.qualys.com/thread/12496
### [Reference](https://web.archive.org/web/20140714205945/https://developer.mozilla.org/en-US/docs/Introduction_to_SSL) - https://web.archive.org/web/20140714205945/https://developer.mozilla.org/en-US/docs/Introduction_to_SSL
### [Reference](https://web.archive.org/web/20140716230537/http://blogs.technet.com/b/pki/archive/2010/09/30/sha2-and-windows.aspx) - https://web.archive.org/web/20140716230537/http://blogs.technet.com/b/pki/archive/2010/09/30/sha2-and-windows.aspx
### [Reference](https://web.archive.org/web/20141009063758/http://www.washingtonpost.com/blogs/style-blog/wp/2014/04/09/why-is-it-called-the-heartbleed-bug/) - https://web.archive.org/web/20141009063758/http://www.washingtonpost.com/blogs/style-blog/wp/2014/04/09/why-is-it-called-the-heartbleed-bug/
### [Reference](https://web.archive.org/web/20141012121824/https://community.qualys.com/blogs/securitylabs/2013/09/10/is-beast-still-a-threat) - https://web.archive.org/web/20141012121824/https://community.qualys.com/blogs/securitylabs/2013/09/10/is-beast-still-a-threat
### [Reference](https://web.archive.org/web/20141012122536/https://community.qualys.com/blogs/securitylabs/2013/10/31/apple-enabled-beast-mitigations-in-os-x-109-mavericks) - https://web.archive.org/web/20141012122536/https://community.qualys.com/blogs/securitylabs/2013/10/31/apple-enabled-beast-mitigations-in-os-x-109-mavericks
### [Reference](https://web.archive.org/web/20141014224443/https://www.openssl.org/~bodo/ssl-poodle.pdf) - https://web.archive.org/web/20141014224443/https://www.openssl.org/~bodo/ssl-poodle.pdf
### [Reference](https://web.archive.org/web/20141018231351/https://blog.mozilla.org/security/2014/10/14/the-poodle-attack-and-the-end-of-ssl-3-0/) - https://web.archive.org/web/20141018231351/https://blog.mozilla.org/security/2014/10/14/the-poodle-attack-and-the-end-of-ssl-3-0/
### [Reference](https://web.archive.org/web/20141023104948/http://support.apple.com/kb/HT6541) - https://web.archive.org/web/20141023104948/http://support.apple.com/kb/HT6541
### [Reference](https://web.archive.org/web/20141024181953/https://support.apple.com/kb/HT6531) - https://web.archive.org/web/20141024181953/https://support.apple.com/kb/HT6531
### [Reference](https://web.archive.org/web/20141024210105/http://googlechromereleases.blogspot.com/2014/02/stable-channel-update_20.html) - https://web.archive.org/web/20141024210105/http://googlechromereleases.blogspot.com/2014/02/stable-channel-update_20.html
### [Reference](https://web.archive.org/web/20141028003952/http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-exploiting-ssl-30.html) - https://web.archive.org/web/20141028003952/http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-exploiting-ssl-30.html
### [Reference](https://web.archive.org/web/20141104093736/https://community.qualys.com/thread/12092) - https://web.archive.org/web/20141104093736/https://community.qualys.com/thread/12092
### [Reference](https://web.archive.org/web/20141114143813/http://blogs.microsoft.com/cybertrust/2014/11/11/hundreds-of-millions-of-microsoft-customers-now-benefit-from-best-in-class-encryption/) - https://web.archive.org/web/20141114143813/http://blogs.microsoft.com/cybertrust/2014/11/11/hundreds-of-millions-of-microsoft-customers-now-benefit-from-best-in-class-encryption/
### [Reference](https://web.archive.org/web/20141205124712/https://access.redhat.com/articles/1232123) - https://web.archive.org/web/20141205124712/https://access.redhat.com/articles/1232123
### [Reference](https://web.archive.org/web/20141207151603/http://tools.ietf.org/html/rfc5054) - https://web.archive.org/web/20141207151603/http://tools.ietf.org/html/rfc5054
### [Reference](https://web.archive.org/web/20141208200653/https://www.imperialviolet.org/2014/12/08/poodleagain.html) - https://web.archive.org/web/20141208200653/https://www.imperialviolet.org/2014/12/08/poodleagain.html
### [Reference](https://web.archive.org/web/20141216203704/http://www.imc.org/ietf-openpgp/mail-archive/msg06063.html) - https://web.archive.org/web/20141216203704/http://www.imc.org/ietf-openpgp/mail-archive/msg06063.html
### [Reference](https://web.archive.org/web/20150103093047/https://wiki.mozilla.org/Security/Server_Side_TLS) - https://web.archive.org/web/20150103093047/https://wiki.mozilla.org/Security/Server_Side_TLS
### [Reference](https://web.archive.org/web/20150109154102/http://botan.randombit.net/relnotes/1_11_13.html) - https://web.archive.org/web/20150109154102/http://botan.randombit.net/relnotes/1_11_13.html
### [Reference](https://web.archive.org/web/20150110195746/https://www.imperialviolet.org/2012/09/21/crime.html) - https://web.archive.org/web/20150110195746/https://www.imperialviolet.org/2012/09/21/crime.html
### [Reference](https://web.archive.org/web/20150112014148/http://msdn.microsoft.com/en-us/library/windows/desktop/ff468651(v=vs.85).aspx) - https://web.archive.org/web/20150112014148/http://msdn.microsoft.com/en-us/library/windows/desktop/ff468651(v=vs.85).aspx
### [Reference](https://web.archive.org/web/20150112153121/http://www.intelsecurity.com/advanced-threat-research/) - https://web.archive.org/web/20150112153121/http://www.intelsecurity.com/advanced-threat-research/
### [Reference](https://web.archive.org/web/20150118053924/http://msdn.microsoft.com/en-us/library/windows/desktop/aa380512(v=vs.85).aspx) - https://web.archive.org/web/20150118053924/http://msdn.microsoft.com/en-us/library/windows/desktop/aa380512(v=vs.85).aspx
### [Reference](https://web.archive.org/web/20150120120428/https://www.openssl.org/news/openssl-1.0.1-notes.html) - https://web.archive.org/web/20150120120428/https://www.openssl.org/news/openssl-1.0.1-notes.html
### [Reference](https://web.archive.org/web/20150121105601/http://www.oracle.com/technetwork/java/javase/8u31-relnotes-2389094.html) - https://web.archive.org/web/20150121105601/http://www.oracle.com/technetwork/java/javase/8u31-relnotes-2389094.html
### [Reference](https://web.archive.org/web/20150211031724/http://blogs.msdn.com/b/ie/archive/2015/02/10/february-2015-security-updates-for-internet-explorer.aspx) - https://web.archive.org/web/20150211031724/http://blogs.msdn.com/b/ie/archive/2015/02/10/february-2015-security-updates-for-internet-explorer.aspx
### [Reference](https://web.archive.org/web/20150212105201/https://www.instantssl.com/ssl-certificate-products/https.html) - https://web.archive.org/web/20150212105201/https://www.instantssl.com/ssl-certificate-products/https.html
### [Reference](https://web.archive.org/web/20150214082207/http://support.microsoft.com/kb/3038778) - https://web.archive.org/web/20150214082207/http://support.microsoft.com/kb/3038778
### [Reference](https://web.archive.org/web/20150214105056/http://www.matrixssl.org/news.html) - https://web.archive.org/web/20150214105056/http://www.matrixssl.org/news.html
### [Reference](https://web.archive.org/web/20150220020306/http://googlechromereleases.blogspot.jp/2011/10/chrome-stable-release.html) - https://web.archive.org/web/20150220020306/http://googlechromereleases.blogspot.jp/2011/10/chrome-stable-release.html
### [Reference](https://web.archive.org/web/20150224112141/https://blog.filippo.io/komodia-superfish-ssl-validation-is-broken/) - https://web.archive.org/web/20150224112141/https://blog.filippo.io/komodia-superfish-ssl-validation-is-broken/
### [Reference](https://web.archive.org/web/20150304221307/https://blog.mozilla.org/security/2011/09/27/attack-against-tls-protected-communications/) - https://web.archive.org/web/20150304221307/https://blog.mozilla.org/security/2011/09/27/attack-against-tls-protected-communications/
### [Reference](https://web.archive.org/web/20150306174623/https://freakattack.com/) - https://web.archive.org/web/20150306174623/https://freakattack.com/
### [Reference](https://web.archive.org/web/20150309000956/http://developer.android.com/about/versions/android-5.0-changes.html#ssl) - https://web.archive.org/web/20150309000956/http://developer.android.com/about/versions/android-5.0-changes.html#ssl
### [Reference](https://web.archive.org/web/20150309201042/https://support.apple.com/en-us/HT204423) - https://web.archive.org/web/20150309201042/https://support.apple.com/en-us/HT204423
### [Reference](https://web.archive.org/web/20150311053342/http://support.microsoft.com/kb/2868725) - https://web.archive.org/web/20150311053342/http://support.microsoft.com/kb/2868725
### [Reference](https://web.archive.org/web/20150311105145/http://support.microsoft.com/kb/948963) - https://web.archive.org/web/20150311105145/http://support.microsoft.com/kb/948963
### [Reference](https://web.archive.org/web/20150311112517/https://www.smacktls.com/#freak) - https://web.archive.org/web/20150311112517/https://www.smacktls.com/#freak
### [Reference](https://web.archive.org/web/20150312074827/https://www.smacktls.com/) - https://web.archive.org/web/20150312074827/https://www.smacktls.com/
### [Reference](https://web.archive.org/web/20150315043755/https://code.google.com/p/chromium/issues/detail?id=318442) - https://web.archive.org/web/20150315043755/https://code.google.com/p/chromium/issues/detail?id=318442
### [Reference](https://web.archive.org/web/20150316081731/https://support.apple.com/en-us/HT204413) - https://web.archive.org/web/20150316081731/https://support.apple.com/en-us/HT204413
### [Reference](https://web.archive.org/web/20150318121117/http://developer.android.com/reference/javax/net/ssl/SSLSocket.html) - https://web.archive.org/web/20150318121117/http://developer.android.com/reference/javax/net/ssl/SSLSocket.html
### [Reference](https://web.archive.org/web/20150319043951/https://msdn.microsoft.com/en-us/library/windows/desktop/aa374757(v=vs.85).aspx) - https://web.archive.org/web/20150319043951/https://msdn.microsoft.com/en-us/library/windows/desktop/aa374757(v=vs.85).aspx
### [Reference](https://web.archive.org/web/20150403092122/https://developer.apple.com/library/ios/technotes/tn2287/) - https://web.archive.org/web/20150403092122/https://developer.apple.com/library/ios/technotes/tn2287/
### [Reference](https://web.archive.org/web/20150409022558/https://www.mozilla.org/en-US/firefox/34.0/releasenotes/) - https://web.archive.org/web/20150409022558/https://www.mozilla.org/en-US/firefox/34.0/releasenotes/
### [Reference](https://web.archive.org/web/20150416005543/http://lists.gnutls.org/pipermail/gnutls-devel/2015-April/007535.html) - https://web.archive.org/web/20150416005543/http://lists.gnutls.org/pipermail/gnutls-devel/2015-April/007535.html
### [Reference](https://web.archive.org/web/20150416072943/https://codereview.chromium.org/693963003) - https://web.archive.org/web/20150416072943/https://codereview.chromium.org/693963003
### [Reference](https://web.archive.org/web/20150418095600/http://code.google.com/p/chromium/issues/detail?id=436391) - https://web.archive.org/web/20150418095600/http://code.google.com/p/chromium/issues/detail?id=436391
### [Reference](https://web.archive.org/web/20150512214100/https://tools.ietf.org/html/rfc7366) - https://web.archive.org/web/20150512214100/https://tools.ietf.org/html/rfc7366
### [Reference](https://web.archive.org/web/20150516035536/http://news.netcraft.com/archives/2015/05/13/counting-ssl-certificates.html) - https://web.archive.org/web/20150516035536/http://news.netcraft.com/archives/2015/05/13/counting-ssl-certificates.html
### [Reference](https://web.archive.org/web/20150605054647/https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.19_release_notes) - https://web.archive.org/web/20150605054647/https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.19_release_notes
### [Reference](https://web.archive.org/web/20150623231035/https://ssl.comodo.com/wildcard-ssl-certificates.php) - https://web.archive.org/web/20150623231035/https://ssl.comodo.com/wildcard-ssl-certificates.php
### [Reference](https://web.archive.org/web/20150701004324/https://support.globalsign.com/customer/portal/articles/1499561-sha-256-compatibility) - https://web.archive.org/web/20150701004324/https://support.globalsign.com/customer/portal/articles/1499561-sha-256-compatibility
### [Reference](https://web.archive.org/web/20150702202131/https://support.apple.com/en-us/HT204942) - https://web.archive.org/web/20150702202131/https://support.apple.com/en-us/HT204942
### [Reference](https://web.archive.org/web/20150703014410/https://support.apple.com/en-us/HT204941) - https://web.archive.org/web/20150703014410/https://support.apple.com/en-us/HT204941
### [Reference](https://web.archive.org/web/20150703163249/https://www.mozilla.org/en-US/firefox/39.0/releasenotes/) - https://web.archive.org/web/20150703163249/https://www.mozilla.org/en-US/firefox/39.0/releasenotes/
### [Reference](https://web.archive.org/web/20150704101956/https://www.ssllabs.com/projects/best-practices/index.html) - https://web.archive.org/web/20150704101956/https://www.ssllabs.com/projects/best-practices/index.html
### [Reference](https://web.archive.org/web/20150706104327/https://www.cosic.esat.kuleuven.be/publications/article-2216.pdf) - https://web.archive.org/web/20150706104327/https://www.cosic.esat.kuleuven.be/publications/article-2216.pdf
### [Reference](https://web.archive.org/web/20150716084138/http://arstechnica.com/security/2015/07/once-theoretical-crypto-attack-against-https-now-verges-on-practicality/) - https://web.archive.org/web/20150716084138/http://arstechnica.com/security/2015/07/once-theoretical-crypto-attack-against-https-now-verges-on-practicality/
### [Reference](https://web.archive.org/web/20150902054341/http://blogs.windows.com/msedgedev/2015/09/01/ending-support-for-the-rc4-cipher-in-microsoft-edge-and-internet-explorer-11/) - https://web.archive.org/web/20150902054341/http://blogs.windows.com/msedgedev/2015/09/01/ending-support-for-the-rc4-cipher-in-microsoft-edge-and-internet-explorer-11/
### [Reference](https://web.archive.org/web/20150905214154/http://venturebeat.com/2015/09/01/google-microsoft-and-mozilla-will-drop-rc4-support-in-chrome-edge-ie-and-firefox-next-year/) - https://web.archive.org/web/20150905214154/http://venturebeat.com/2015/09/01/google-microsoft-and-mozilla-will-drop-rc4-support-in-chrome-edge-ie-and-firefox-next-year/
### [Reference](https://web.archive.org/web/20150906044018/https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=8&platform=OS%20X%2010.10) - https://web.archive.org/web/20150906044018/https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=8&platform=OS%20X%2010.10
### [Reference](https://web.archive.org/web/20150912071452/https://code.google.com/p/chromium/issues/detail?id=375342) - https://web.archive.org/web/20150912071452/https://code.google.com/p/chromium/issues/detail?id=375342
### [Reference](https://web.archive.org/web/20150912081831/https://code.google.com/p/chromium/issues/detail?id=490240) - https://web.archive.org/web/20150912081831/https://code.google.com/p/chromium/issues/detail?id=490240
### [Reference](https://web.archive.org/web/20150919073935/https://dev.ssllabs.com/ssltest/clients.html) - https://web.archive.org/web/20150919073935/https://dev.ssllabs.com/ssltest/clients.html
### [Reference](https://web.archive.org/web/20150920011317/http://crypto.stanford.edu/~dabo/pubs/abstracts/websec_ecc.html) - https://web.archive.org/web/20150920011317/http://crypto.stanford.edu/~dabo/pubs/abstracts/websec_ecc.html
### [Reference](https://web.archive.org/web/20150923033459/http://www.chromium.org/Home/chromium-security/boringssl) - https://web.archive.org/web/20150923033459/http://www.chromium.org/Home/chromium-security/boringssl
### [Reference](https://web.archive.org/web/20150925030547/https://tls.mbed.org/tech-updates/releases/mbedtls-2.0.0-released) - https://web.archive.org/web/20150925030547/https://tls.mbed.org/tech-updates/releases/mbedtls-2.0.0-released
### [Reference](https://web.archive.org/web/20151003193113/http://www.ietf.org/mail-archive/web/tls/current/msg17680.html) - https://web.archive.org/web/20151003193113/http://www.ietf.org/mail-archive/web/tls/current/msg17680.html
### [Reference](https://web.archive.org/web/20151017033726/https://wolfssl.com/wolfSSL/Blog/Entries/2015/8/24_wolfSSL_3.6.6_is_Now_Available.html) - https://web.archive.org/web/20151017033726/https://wolfssl.com/wolfSSL/Blog/Entries/2015/8/24_wolfSSL_3.6.6_is_Now_Available.html
### [Reference](https://web.archive.org/web/20151106110117/https://hal.inria.fr/hal-01102013) - https://web.archive.org/web/20151106110117/https://hal.inria.fr/hal-01102013
### [Reference](https://web.archive.org/web/20151218214756/https://googleonlinesecurity.blogspot.com/2015/12/an-update-on-sha-1-certificates-in.html) - https://web.archive.org/web/20151218214756/https://googleonlinesecurity.blogspot.com/2015/12/an-update-on-sha-1-certificates-in.html
### [Reference](https://web.archive.org/web/20151231171309/https://knowledge.verisign.com/support/ssl-certificates-support/index?page=content&id=SO10090&actp=search&viewlocale=en_US&searchid=1406590748892) - https://web.archive.org/web/20151231171309/https://knowledge.verisign.com/support/ssl-certificates-support/index?page=content&id=SO10090&actp=search&viewlocale=en_US&searchid=1406590748892
### [Reference](https://web.archive.org/web/20160104234608/http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3555) - https://web.archive.org/web/20160104234608/http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3555
### [Reference](https://web.archive.org/web/20160104234608/https://www.eff.org/deeplinks/2010/03/researchers-reveal-likelihood-governments-fake-ssl) - https://web.archive.org/web/20160104234608/https://www.eff.org/deeplinks/2010/03/researchers-reveal-likelihood-governments-fake-ssl
### [Reference](https://web.archive.org/web/20160217122951/https://support.globalsign.com/customer/portal/articles/1995283-ecc-compatibility) - https://web.archive.org/web/20160217122951/https://support.globalsign.com/customer/portal/articles/1995283-ecc-compatibility
### [Reference](https://web.archive.org/web/20160301191108/http://arstechnica.com/security/2016/03/more-than-13-million-https-websites-imperiled-by-new-decryption-attack/) - https://web.archive.org/web/20160301191108/http://arstechnica.com/security/2016/03/more-than-13-million-https-websites-imperiled-by-new-decryption-attack/
### [Reference](https://web.archive.org/web/20160301215536/http://www.theregister.co.uk/2016/03/01/drown_tls_protocol_flaw/) - https://web.archive.org/web/20160301215536/http://www.theregister.co.uk/2016/03/01/drown_tls_protocol_flaw/
### [Reference](https://web.archive.org/web/20160304023941/https://support.cloudflare.com/hc/en-us/articles/203041594-What-browsers-work-with-Universal-SSL) - https://web.archive.org/web/20160304023941/https://support.cloudflare.com/hc/en-us/articles/203041594-What-browsers-work-with-Universal-SSL
### [Reference](https://web.archive.org/web/20160304025010/https://www.mozilla.org/en-US/firefox/44.0/releasenotes/) - https://web.archive.org/web/20160304025010/https://www.mozilla.org/en-US/firefox/44.0/releasenotes/
### [Reference](https://web.archive.org/web/20160304062526/https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=8&platform=iOS%208.1.2) - https://web.archive.org/web/20160304062526/https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=8&platform=iOS%208.1.2
### [Reference](https://web.archive.org/web/20160304063257/https://social.msdn.microsoft.com/Forums/windowsapps/en-US/2ddee177-5086-4453-987b-d02b6a7ec62d/what-tls-version-is-used-in-windows-phone-8-for-secure-http-connections?forum=wpdevelop) - https://web.archive.org/web/20160304063257/https://social.msdn.microsoft.com/Forums/windowsapps/en-US/2ddee177-5086-4453-987b-d02b6a7ec62d/what-tls-version-is-used-in-windows-phone-8-for-secure-http-connections?forum=wpdevelop
### [Reference](https://web.archive.org/web/20160304201813/https://tools.ietf.org/html/rfc7457) - https://web.archive.org/web/20160304201813/https://tools.ietf.org/html/rfc7457
### [Reference](https://web.archive.org/web/20160304202641/https://developer.android.com/reference/javax/net/ssl/SSLSocket.html) - https://web.archive.org/web/20160304202641/https://developer.android.com/reference/javax/net/ssl/SSLSocket.html
### [Reference](https://web.archive.org/web/20160526175713/http://arstechnica.com/security/2016/05/faulty-https-settings-leave-dozens-of-visa-sites-vulnerable-to-forgery-attacks/) - https://web.archive.org/web/20160526175713/http://arstechnica.com/security/2016/05/faulty-https-settings-leave-dozens-of-visa-sites-vulnerable-to-forgery-attacks/
### [Reference](https://web.archive.org/web/20160727160434/http://arstechnica.com/security/2016/07/new-attack-that-cripples-https-crypto-works-on-macs-windows-and-linux/) - https://web.archive.org/web/20160727160434/http://arstechnica.com/security/2016/07/new-attack-that-cripples-https-crypto-works-on-macs-windows-and-linux/
### [Reference](https://web.archive.org/web/20160821091621/https://blogs.windows.com/msedgedev/2016/08/09/rc4-now-deprecated/) - https://web.archive.org/web/20160821091621/https://blogs.windows.com/msedgedev/2016/08/09/rc4-now-deprecated/
### [Reference](https://web.archive.org/web/20160824181630/http://arstechnica.com/security/2016/08/new-attack-can-pluck-secrets-from-1-of-https-traffic-affects-top-sites/) - https://web.archive.org/web/20160824181630/http://arstechnica.com/security/2016/08/new-attack-can-pluck-secrets-from-1-of-https-traffic-affects-top-sites/
### [Reference](https://web.archive.org/web/20160825171308/https://www.openssl.org/news/openssl-1.1.0-notes.html) - https://web.archive.org/web/20160825171308/https://www.openssl.org/news/openssl-1.1.0-notes.html
### [Reference](https://web.archive.org/web/20160826100711/https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.24_release_notes) - https://web.archive.org/web/20160826100711/https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.24_release_notes
### [Reference](https://web.archive.org/web/20160923053812/http://forum.xda-developers.com/windows-phone-8/development/poodle-ssl-vulnerability-secure-windows-t2906203) - https://web.archive.org/web/20160923053812/http://forum.xda-developers.com/windows-phone-8/development/poodle-ssl-vulnerability-secure-windows-t2906203
### [Reference](https://web.archive.org/web/20161007222635/https://www.rsaconference.com/writable/presentations/file_upload/sec-t02_final.pdf) - https://web.archive.org/web/20161007222635/https://www.rsaconference.com/writable/presentations/file_upload/sec-t02_final.pdf
### [Reference](https://web.archive.org/web/20170222052829/https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.29_release_notes) - https://web.archive.org/web/20170222052829/https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.29_release_notes
### [Reference](https://web.archive.org/web/20170225013516/http://gizmodo.com/everything-you-need-to-know-about-cloudbleed-the-lates-1792710616) - https://web.archive.org/web/20170225013516/http://gizmodo.com/everything-you-need-to-know-about-cloudbleed-the-lates-1792710616
### [Reference](https://web.archive.org/web/20170301141459/https://www.ssllabs.com/ssltest/viewClient.html?name=IE%20Mobile&version=10&platform=Win%20Phone%208.0) - https://web.archive.org/web/20170301141459/https://www.ssllabs.com/ssltest/viewClient.html?name=IE%20Mobile&version=10&platform=Win%20Phone%208.0
### [Reference](https://web.archive.org/web/20170301142904/https://curl.haxx.se/mail/lib-2012-08/0120.html) - https://web.archive.org/web/20170301142904/https://curl.haxx.se/mail/lib-2012-08/0120.html
### [Reference](https://web.archive.org/web/20170313125201/https://msdn.microsoft.com/en-us/library/windows/desktop/aa380512.aspx) - https://web.archive.org/web/20170313125201/https://msdn.microsoft.com/en-us/library/windows/desktop/aa380512.aspx
### [Reference](https://web.archive.org/web/20170313130545/https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=7&platform=iOS%207.1) - https://web.archive.org/web/20170313130545/https://www.ssllabs.com/ssltest/viewClient.html?name=Safari&version=7&platform=iOS%207.1
### [Reference](https://web.archive.org/web/20170320192352/https://www.ssllabs.com/ssltest/analyze.html?d=google.co.uk&s=74.125.227.183) - https://web.archive.org/web/20170320192352/https://www.ssllabs.com/ssltest/analyze.html?d=google.co.uk&s=74.125.227.183
### [Reference](https://web.archive.org/web/20170424021101/https://sweet32.info/SWEET32_CCS16.pdf) - https://web.archive.org/web/20170424021101/https://sweet32.info/SWEET32_CCS16.pdf
### [Reference](https://web.archive.org/web/20170519130937/https://arstechnica.com/security/2015/05/https-crippling-attack-threatens-tens-of-thousands-of-web-and-mail-servers/) - https://web.archive.org/web/20170519130937/https://arstechnica.com/security/2015/05/https-crippling-attack-threatens-tens-of-thousands-of-web-and-mail-servers/
### [Reference](https://web.archive.org/web/20170912061432/http://bluecoat.force.com/knowledgebase/articles/Technical_Alert/000032878) - https://web.archive.org/web/20170912061432/http://bluecoat.force.com/knowledgebase/articles/Technical_Alert/000032878
### [Reference](https://web.archive.org/web/20170912103610/https://arstechnica.com/information-technology/2015/02/lenovo-pcs-ship-with-man-in-the-middle-adware-that-breaks-https-connections/) - https://web.archive.org/web/20170912103610/https://arstechnica.com/information-technology/2015/02/lenovo-pcs-ship-with-man-in-the-middle-adware-that-breaks-https-connections/
### [Reference](https://web.archive.org/web/20171022194807/http://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf) - https://web.archive.org/web/20171022194807/http://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf
### [Reference](https://web.archive.org/web/20171201042705/https://developer.android.com/about/versions/oreo/android-8.0-changes.html) - https://web.archive.org/web/20171201042705/https://developer.android.com/about/versions/oreo/android-8.0-changes.html
### [Reference](https://web.archive.org/web/20171224222709/https://tools.ietf.org/html/rfc5246) - https://web.archive.org/web/20171224222709/https://tools.ietf.org/html/rfc5246
### [Reference](https://web.archive.org/web/20171224222709/https://tools.ietf.org/html/rfc5246#ref-TLS1.1) - https://web.archive.org/web/20171224222709/https://tools.ietf.org/html/rfc5246#ref-TLS1.1
### [Reference](https://web.archive.org/web/20180115220635/https://datatracker.ietf.org/meeting/100/materials/slides-100-hackathon-sessa-tls-13/) - https://web.archive.org/web/20180115220635/https://datatracker.ietf.org/meeting/100/materials/slides-100-hackathon-sessa-tls-13/
### [Reference](https://web.archive.org/web/20180116081141/http://searchsecurity.techtarget.com/answer/From-1024-to-2048-bit-The-security-effect-of-encryption-key-length) - https://web.archive.org/web/20180116081141/http://searchsecurity.techtarget.com/answer/From-1024-to-2048-bit-The-security-effect-of-encryption-key-length
### [Reference](https://web.archive.org/web/20190919000200/https://www.wolfssl.com/differences-between-tls-12-and-tls-13-9/) - https://web.archive.org/web/20190919000200/https://www.wolfssl.com/differences-between-tls-12-and-tls-13-9/
### [Reference](https://build.chromium.org/f/chromium/perf/dashboard/ui/changelog.html?url=/trunk/src&range=72316:67679&mode=html) - https://build.chromium.org/f/chromium/perf/dashboard/ui/changelog.html?url=/trunk/src&range=72316:67679&mode=html
### [Reference](https://build.chromium.org/f/chromium/perf/dashboard/ui/changelog.html?url=/trunk/src&range=232870:241107&mode=html) - https://build.chromium.org/f/chromium/perf/dashboard/ui/changelog.html?url=/trunk/src&range=232870:241107&mode=html
### [Reference](https://codereview.chromium.org/23503030/) - https://codereview.chromium.org/23503030/
### [Reference](https://codereview.chromium.org/693963003) - https://codereview.chromium.org/693963003
### [Reference](https://src.chromium.org/viewvc/chrome?revision=203090&view=revision) - https://src.chromium.org/viewvc/chrome?revision=203090&view=revision
### [Reference](https://www.chromium.org/Home/chromium-security/boringssl) - https://www.chromium.org/Home/chromium-security/boringssl
### [Reference](https://cve.org/CVERecord?id=CVE-2014-3566) - https://cve.org/CVERecord?id=CVE-2014-3566
### [Reference](https://www.eff.org/deeplinks/2010/03/researchers-reveal-likelihood-governments-fake-ssl) - https://www.eff.org/deeplinks/2010/03/researchers-reveal-likelihood-governments-fake-ssl
### [Reference](https://www.eff.org/deeplinks/2019/02/ets-isnt-tls-and-you-shouldnt-use-it) - https://www.eff.org/deeplinks/2019/02/ets-isnt-tls-and-you-shouldnt-use-it
### [Reference](https://www.etsi.org/deliver/etsi_ts/103500_103599/10352303/01.01.01_60/ts_10352303v010101p.pdf#page=5) - https://www.etsi.org/deliver/etsi_ts/103500_103599/10352303/01.01.01_60/ts_10352303v010101p.pdf#page=5
### [Reference](https://ghostarchive.org/varchive/youtube/20211028/33XW5yzjtME) - https://ghostarchive.org/varchive/youtube/20211028/33XW5yzjtME
### [Reference](https://ghostarchive.org/varchive/youtube/20211028/u6rz4PWA_As) - https://ghostarchive.org/varchive/youtube/20211028/u6rz4PWA_As
### [Reference](https://lists.gnupg.org/pipermail/gnutls-help/2018-September/004457.html) - https://lists.gnupg.org/pipermail/gnutls-help/2018-September/004457.html
### [Reference](https://datatracker.ietf.org/doc/html/rfc2246) - https://datatracker.ietf.org/doc/html/rfc2246
### [Reference](https://datatracker.ietf.org/doc/html/rfc2595) - https://datatracker.ietf.org/doc/html/rfc2595
### [Reference](https://datatracker.ietf.org/doc/html/rfc2712) - https://datatracker.ietf.org/doc/html/rfc2712
### [Reference](https://datatracker.ietf.org/doc/html/rfc2817) - https://datatracker.ietf.org/doc/html/rfc2817
### [Reference](https://datatracker.ietf.org/doc/html/rfc2818) - https://datatracker.ietf.org/doc/html/rfc2818
### [Reference](https://datatracker.ietf.org/doc/html/rfc3207) - https://datatracker.ietf.org/doc/html/rfc3207
### [Reference](https://datatracker.ietf.org/doc/html/rfc3268) - https://datatracker.ietf.org/doc/html/rfc3268
### [Reference](https://datatracker.ietf.org/doc/html/rfc3546) - https://datatracker.ietf.org/doc/html/rfc3546
### [Reference](https://datatracker.ietf.org/doc/html/rfc3749) - https://datatracker.ietf.org/doc/html/rfc3749
### [Reference](https://datatracker.ietf.org/doc/html/rfc3943) - https://datatracker.ietf.org/doc/html/rfc3943
### [Reference](https://datatracker.ietf.org/doc/html/rfc4132) - https://datatracker.ietf.org/doc/html/rfc4132
### [Reference](https://datatracker.ietf.org/doc/html/rfc4162) - https://datatracker.ietf.org/doc/html/rfc4162
### [Reference](https://datatracker.ietf.org/doc/html/rfc4217) - https://datatracker.ietf.org/doc/html/rfc4217
### [Reference](https://datatracker.ietf.org/doc/html/rfc4279) - https://datatracker.ietf.org/doc/html/rfc4279
### [Reference](https://datatracker.ietf.org/doc/html/rfc4346) - https://datatracker.ietf.org/doc/html/rfc4346
### [Reference](https://datatracker.ietf.org/doc/html/rfc4347) - https://datatracker.ietf.org/doc/html/rfc4347
### [Reference](https://datatracker.ietf.org/doc/html/rfc4357) - https://datatracker.ietf.org/doc/html/rfc4357
### [Reference](https://datatracker.ietf.org/doc/html/rfc4366) - https://datatracker.ietf.org/doc/html/rfc4366
### [Reference](https://datatracker.ietf.org/doc/html/rfc4492) - https://datatracker.ietf.org/doc/html/rfc4492
### [Reference](https://datatracker.ietf.org/doc/html/rfc4680) - https://datatracker.ietf.org/doc/html/rfc4680
### [Reference](https://datatracker.ietf.org/doc/html/rfc4681) - https://datatracker.ietf.org/doc/html/rfc4681
### [Reference](https://datatracker.ietf.org/doc/html/rfc4785) - https://datatracker.ietf.org/doc/html/rfc4785
### [Reference](https://datatracker.ietf.org/doc/html/rfc5054) - https://datatracker.ietf.org/doc/html/rfc5054
### [Reference](https://datatracker.ietf.org/doc/html/rfc5077) - https://datatracker.ietf.org/doc/html/rfc5077
### [Reference](https://datatracker.ietf.org/doc/html/rfc5081) - https://datatracker.ietf.org/doc/html/rfc5081
### [Reference](https://datatracker.ietf.org/doc/html/rfc5216) - https://datatracker.ietf.org/doc/html/rfc5216
### [Reference](https://datatracker.ietf.org/doc/html/rfc5246) - https://datatracker.ietf.org/doc/html/rfc5246
### [Reference](https://datatracker.ietf.org/doc/html/rfc5246#section-1) - https://datatracker.ietf.org/doc/html/rfc5246#section-1
### [Reference](https://datatracker.ietf.org/doc/html/rfc5246#section-7.4.9) - https://datatracker.ietf.org/doc/html/rfc5246#section-7.4.9
### [Reference](https://datatracker.ietf.org/doc/html/rfc5288) - https://datatracker.ietf.org/doc/html/rfc5288
### [Reference](https://datatracker.ietf.org/doc/html/rfc5289) - https://datatracker.ietf.org/doc/html/rfc5289
### [Reference](https://datatracker.ietf.org/doc/html/rfc5469) - https://datatracker.ietf.org/doc/html/rfc5469
### [Reference](https://datatracker.ietf.org/doc/html/rfc5746) - https://datatracker.ietf.org/doc/html/rfc5746
### [Reference](https://datatracker.ietf.org/doc/html/rfc5878) - https://datatracker.ietf.org/doc/html/rfc5878
### [Reference](https://datatracker.ietf.org/doc/html/rfc5932) - https://datatracker.ietf.org/doc/html/rfc5932
### [Reference](https://datatracker.ietf.org/doc/html/rfc6066) - https://datatracker.ietf.org/doc/html/rfc6066
### [Reference](https://datatracker.ietf.org/doc/html/rfc6091) - https://datatracker.ietf.org/doc/html/rfc6091
### [Reference](https://datatracker.ietf.org/doc/html/rfc6101) - https://datatracker.ietf.org/doc/html/rfc6101
### [Reference](https://datatracker.ietf.org/doc/html/rfc6176) - https://datatracker.ietf.org/doc/html/rfc6176
### [Reference](https://datatracker.ietf.org/doc/html/rfc6209) - https://datatracker.ietf.org/doc/html/rfc6209
### [Reference](https://datatracker.ietf.org/doc/html/rfc6347) - https://datatracker.ietf.org/doc/html/rfc6347
### [Reference](https://datatracker.ietf.org/doc/html/rfc6367) - https://datatracker.ietf.org/doc/html/rfc6367
### [Reference](https://datatracker.ietf.org/doc/html/rfc6460) - https://datatracker.ietf.org/doc/html/rfc6460
### [Reference](https://datatracker.ietf.org/doc/html/rfc6655) - https://datatracker.ietf.org/doc/html/rfc6655
### [Reference](https://datatracker.ietf.org/doc/html/rfc7027) - https://datatracker.ietf.org/doc/html/rfc7027
### [Reference](https://datatracker.ietf.org/doc/html/rfc7251) - https://datatracker.ietf.org/doc/html/rfc7251
### [Reference](https://datatracker.ietf.org/doc/html/rfc7301) - https://datatracker.ietf.org/doc/html/rfc7301
### [Reference](https://datatracker.ietf.org/doc/html/rfc7366) - https://datatracker.ietf.org/doc/html/rfc7366
### [Reference](https://datatracker.ietf.org/doc/html/rfc7457) - https://datatracker.ietf.org/doc/html/rfc7457
### [Reference](https://datatracker.ietf.org/doc/html/rfc7465) - https://datatracker.ietf.org/doc/html/rfc7465
### [Reference](https://datatracker.ietf.org/doc/html/rfc7507) - https://datatracker.ietf.org/doc/html/rfc7507
### [Reference](https://datatracker.ietf.org/doc/html/rfc7525) - https://datatracker.ietf.org/doc/html/rfc7525
### [Reference](https://datatracker.ietf.org/doc/html/rfc7568) - https://datatracker.ietf.org/doc/html/rfc7568
### [Reference](https://datatracker.ietf.org/doc/html/rfc7627) - https://datatracker.ietf.org/doc/html/rfc7627
### [Reference](https://datatracker.ietf.org/doc/html/rfc7685) - https://datatracker.ietf.org/doc/html/rfc7685
### [Reference](https://datatracker.ietf.org/doc/html/rfc7905) - https://datatracker.ietf.org/doc/html/rfc7905
### [Reference](https://datatracker.ietf.org/doc/html/rfc8446) - https://datatracker.ietf.org/doc/html/rfc8446
### [Reference](https://datatracker.ietf.org/doc/html/rfc8996) - https://datatracker.ietf.org/doc/html/rfc8996
### [Reference](https://datatracker.ietf.org/meeting/100/materials/slides-100-hackathon-sessa-tls-13/) - https://datatracker.ietf.org/meeting/100/materials/slides-100-hackathon-sessa-tls-13/
### [Reference](https://datatracker.ietf.org/wg/tls/) - https://datatracker.ietf.org/wg/tls/
### [Reference](https://mailarchive.ietf.org/arch/msg/tls/5QjzTilqjomSyzENtgfaAqQOhbA) - https://mailarchive.ietf.org/arch/msg/tls/5QjzTilqjomSyzENtgfaAqQOhbA
### [Reference](https://tools.ietf.org/html/rfc2817) - https://tools.ietf.org/html/rfc2817
### [Reference](https://tools.ietf.org/html/rfc4279) - https://tools.ietf.org/html/rfc4279
### [Reference](https://tools.ietf.org/html/rfc5054) - https://tools.ietf.org/html/rfc5054
### [Reference](https://tools.ietf.org/html/rfc5246#section-6.2.3.3) - https://tools.ietf.org/html/rfc5246#section-6.2.3.3
### [Reference](https://tools.ietf.org/html/rfc5630) - https://tools.ietf.org/html/rfc5630
### [Reference](https://tools.ietf.org/html/rfc7457) - https://tools.ietf.org/html/rfc7457
### [Reference](https://tools.ietf.org/html/rfc8446) - https://tools.ietf.org/html/rfc8446
### [Reference](https://www.ietf.org/mail-archive/web/tls/current/msg17680.html) - https://www.ietf.org/mail-archive/web/tls/current/msg17680.html
### [Reference](https://www.imperialviolet.org/2012/09/21/crime.html) - https://www.imperialviolet.org/2012/09/21/crime.html
### [Reference](https://www.imperialviolet.org/2013/06/27/botchingpfs.html) - https://www.imperialviolet.org/2013/06/27/botchingpfs.html
### [Reference](https://www.imperialviolet.org/2014/12/08/poodleagain.html) - https://www.imperialviolet.org/2014/12/08/poodleagain.html
### [Reference](https://tls.mbed.org/tech-updates/releases/mbedtls-2.0.0-released) - https://tls.mbed.org/tech-updates/releases/mbedtls-2.0.0-released
### [Reference](https://blog.mozilla.org/security/2011/09/27/attack-against-tls-protected-communications/) - https://blog.mozilla.org/security/2011/09/27/attack-against-tls-protected-communications/
### [Reference](https://blog.mozilla.org/security/2014/10/14/the-poodle-attack-and-the-end-of-ssl-3-0/) - https://blog.mozilla.org/security/2014/10/14/the-poodle-attack-and-the-end-of-ssl-3-0/
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=1036737) - https://bugzilla.mozilla.org/show_bug.cgi?id=1036737
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=1083058) - https://bugzilla.mozilla.org/show_bug.cgi?id=1083058
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=1088915) - https://bugzilla.mozilla.org/show_bug.cgi?id=1088915
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=1166031) - https://bugzilla.mozilla.org/show_bug.cgi?id=1166031
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=1310516) - https://bugzilla.mozilla.org/show_bug.cgi?id=1310516
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=1342082) - https://bugzilla.mozilla.org/show_bug.cgi?id=1342082
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=480514) - https://bugzilla.mozilla.org/show_bug.cgi?id=480514
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=565047) - https://bugzilla.mozilla.org/show_bug.cgi?id=565047
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=665814) - https://bugzilla.mozilla.org/show_bug.cgi?id=665814
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=733647) - https://bugzilla.mozilla.org/show_bug.cgi?id=733647
### [Reference](https://bugzilla.mozilla.org/show_bug.cgi?id=861266) - https://bugzilla.mozilla.org/show_bug.cgi?id=861266
### [Reference](https://bug665814.bugzilla.mozilla.org/attachment.cgi?id=540839) - https://bug665814.bugzilla.mozilla.org/attachment.cgi?id=540839
### [Reference](https://developer.mozilla.org/NSS_3.12.6_release_notes) - https://developer.mozilla.org/NSS_3.12.6_release_notes
### [Reference](https://developer.mozilla.org/en-US/Firefox/Releases/2/Security_changes) - https://developer.mozilla.org/en-US/Firefox/Releases/2/Security_changes
### [Reference](https://developer.mozilla.org/en-US/docs/Introduction_to_SSL) - https://developer.mozilla.org/en-US/docs/Introduction_to_SSL
### [Reference](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.15.3_release_notes) - https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.15.3_release_notes
### [Reference](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.19_release_notes) - https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.19_release_notes
### [Reference](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.39_release_notes#Notable_Changes_in_NSS_3.39) - https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.39_release_notes#Notable_Changes_in_NSS_3.39
### [Reference](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.24_release_notes) - https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.24_release_notes
### [Reference](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.29_release_notes) - https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_3.29_release_notes
### [Reference](https://developer.mozilla.org/en-US/docs/NSS/NSS_3.14_release_notes) - https://developer.mozilla.org/en-US/docs/NSS/NSS_3.14_release_notes
### [Reference](https://developer.mozilla.org/en-US/docs/NSS/NSS_3.15.1_release_notes) - https://developer.mozilla.org/en-US/docs/NSS/NSS_3.15.1_release_notes
### [Reference](https://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes/en-US/firefox/27.0/releasenotes/) - https://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes/en-US/firefox/27.0/releasenotes/
### [Reference](https://wiki.mozilla.org/Security/Server_Side_TLS) - https://wiki.mozilla.org/Security/Server_Side_TLS
### [Reference](https://www.mozilla.org/en-US/firefox/34.0/releasenotes/) - https://www.mozilla.org/en-US/firefox/34.0/releasenotes/
### [Reference](https://www.mozilla.org/en-US/firefox/39.0/releasenotes/) - https://www.mozilla.org/en-US/firefox/39.0/releasenotes/
### [Reference](https://www.mozilla.org/en-US/firefox/44.0/releasenotes/) - https://www.mozilla.org/en-US/firefox/44.0/releasenotes/
### [Reference](https://www.mozilla.org/en-US/firefox/60.0/releasenotes/) - https://www.mozilla.org/en-US/firefox/60.0/releasenotes/
### [Reference](https://www.mozilla.org/en-US/firefox/78.0/releasenotes/) - https://www.mozilla.org/en-US/firefox/78.0/releasenotes/
### [Reference](https://www.mozilla.org/security/announce/2013/mfsa2013-103.html) - https://www.mozilla.org/security/announce/2013/mfsa2013-103.html
### [Reference](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/security-impact-https-interception/) - https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/security-impact-https-interception/
### [Reference](https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-3.2.2-relnotes.txt) - https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-3.2.2-relnotes.txt
### [Reference](https://www.openssl.org/blog/blog/2018/09/11/release111/) - https://www.openssl.org/blog/blog/2018/09/11/release111/
### [Reference](https://www.openssl.org/docs/ssl/SSL_CTX_set_options.html#SECURE_RENEGOTIATION) - https://www.openssl.org/docs/ssl/SSL_CTX_set_options.html#SECURE_RENEGOTIATION
### [Reference](https://www.openssl.org/news/openssl-1.0.1-notes.html) - https://www.openssl.org/news/openssl-1.0.1-notes.html
### [Reference](https://www.openssl.org/news/openssl-1.1.0-notes.html) - https://www.openssl.org/news/openssl-1.1.0-notes.html
### [Reference](https://www.openssl.org/~bodo/ssl-poodle.pdf) - https://www.openssl.org/~bodo/ssl-poodle.pdf
### [Reference](https://blog.pcisecuritystandards.org/migrating-from-ssl-and-early-tls) - https://blog.pcisecuritystandards.org/migrating-from-ssl-and-early-tls
### [Reference](https://api.semanticscholar.org/CorpusID:11264303) - https://api.semanticscholar.org/CorpusID:11264303
### [Reference](https://api.semanticscholar.org/CorpusID:5869541) - https://api.semanticscholar.org/CorpusID:5869541
### [Reference](https://api.semanticscholar.org/CorpusID:7356608) - https://api.semanticscholar.org/CorpusID:7356608
### [Reference](https://www.usenix.org/sites/default/files/conference/protected-files/alfardan_sec13_slides.pdf) - https://www.usenix.org/sites/default/files/conference/protected-files/alfardan_sec13_slides.pdf
### [Reference](https://www.webcitation.org/65JSSbOus?url=http://www.theregister.co.uk/2011/09/19/beast_exploits_paypal_ssl/) - https://www.webcitation.org/65JSSbOus?url=http://www.theregister.co.uk/2011/09/19/beast_exploits_paypal_ssl/
### [Reference](https://www.webcitation.org/65JSTKRCA?url=http://www.educatedguesswork.org/2009/11/understanding_the_tls_renegoti.html) - https://www.webcitation.org/65JSTKRCA?url=http://www.educatedguesswork.org/2009/11/understanding_the_tls_renegoti.html
### [Reference](https://www.webcitation.org/65JSUYEDA?url=http://article.gmane.org/gmane.network.gnutls.general/2046) - https://www.webcitation.org/65JSUYEDA?url=http://article.gmane.org/gmane.network.gnutls.general/2046
### [Reference](https://www.webcitation.org/6FwL0CvUM?url=http://www.carbonwind.net/TLS_Cipher_Suites_Project/tls_ssl_cipher_suites_annex_a1_main.docx) - https://www.webcitation.org/6FwL0CvUM?url=http://www.carbonwind.net/TLS_Cipher_Suites_Project/tls_ssl_cipher_suites_annex_a1_main.docx
### [Reference](https://www.webcitation.org/6FwL0oLMO?url=http://www.apple.com/safari/features.html) - https://www.webcitation.org/6FwL0oLMO?url=http://www.apple.com/safari/features.html
### [Reference](https://www.webcitation.org/6FwL2M2Mc?url=http://labs.mwrinfosecurity.com/blog/2012/04/16/adventures-with-ios-uiwebviews/) - https://www.webcitation.org/6FwL2M2Mc?url=http://labs.mwrinfosecurity.com/blog/2012/04/16/adventures-with-ios-uiwebviews/
### [Reference](https://www.webcitation.org/6FwL5WZ8b?url=https://news.ycombinator.com/item?id=3015498) - https://www.webcitation.org/6FwL5WZ8b?url=https://news.ycombinator.com/item?id=3015498
### [Reference](https://archive.today/20140116153037/http://build.chromium.org/f/chromium/perf/dashboard/ui/changelog.html?url=/trunk/src&range=232870:241107&mode=html) - https://archive.today/20140116153037/http://build.chromium.org/f/chromium/perf/dashboard/ui/changelog.html?url=/trunk/src&range=232870:241107&mode=html
### [Reference](https://archive.today/20140619142454/http://build.chromium.org/f/chromium/perf/dashboard/ui/changelog.html?url=/trunk/src&range=72316:67679&mode=html) - https://archive.today/20140619142454/http://build.chromium.org/f/chromium/perf/dashboard/ui/changelog.html?url=/trunk/src&range=72316:67679&mode=html
### [Reference](https://googlechromereleases.blogspot.co.uk/2012/08/stable-channel-update_21.html) - https://googlechromereleases.blogspot.co.uk/2012/08/stable-channel-update_21.html
### [Reference](https://www.theregister.co.uk/2011/09/19/beast_exploits_paypal_ssl/) - https://www.theregister.co.uk/2011/09/19/beast_exploits_paypal_ssl/
### [Reference](https://www.theregister.co.uk/2013/08/01/gmail_hotmail_hijacking/) - https://www.theregister.co.uk/2013/08/01/gmail_hotmail_hijacking/
### [Reference](https://www.theregister.co.uk/2013/08/02/breach_crypto_attack/) - https://www.theregister.co.uk/2013/08/02/breach_crypto_attack/
### [Reference](https://www.theregister.co.uk/2016/03/01/drown_tls_protocol_flaw/) - https://www.theregister.co.uk/2016/03/01/drown_tls_protocol_flaw/
### [Reference](https://www.theregister.co.uk/2018/03/27/with_tls_13_signed_off_its_implementation_time) - https://www.theregister.co.uk/2018/03/27/with_tls_13_signed_off_its_implementation_time
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/d/d3/Full_TLS_1.2_Handshake.svg) - https://upload.wikimedia.org/wikipedia/commons/d/d3/Full_TLS_1.2_Handshake.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/3/32/Let%E2%80%99s_Encrypt_example_certificate_on_Firefox_94_screenshot.png) - https://upload.wikimedia.org/wikipedia/commons/3/32/Let%E2%80%99s_Encrypt_example_certificate_on_Firefox_94_screenshot.png
### [Image](https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg) - https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg