# Post Office Protocol
## [URL](https://en.wikipedia.org/wiki/Post_Office_Protocol) - https://en.wikipedia.org/wiki/Post_Office_Protocol
## Catagories
### All Wikipedia articles needing context
### All articles needing additional references
### All articles with failed verification
### All pages needing cleanup
### Articles needing additional references from November 2007
### Articles with Japanese-language sources (ja)
### Articles with failed verification from January 2022
### Articles with short description
### Internet mail protocols
### Short description matches Wikidata
### Webarchive template archiveis links
### Webarchive template wayback links
### Wikipedia articles needing context from July 2020
### Wikipedia introduction cleanup from July 2020
### "In computing, the Post Office Protocol (POP) is an application-layer Internet standard protocol used by e-mail clients to retrieve e-mail from a mail server. POP version 3 (POP3) is the version in common use.
## Purpose  
### The Post Office Protocol provides access via an Internet Protocol (IP) network for a user client application to a mailbox (maildrop) maintained on a mail server. The protocol supports download and delete operations for messages. POP3 clients connect, retrieve all messages, store them on the client computer, and finally delete them from the server. This design of POP and its procedures was driven by the need of users having only temporary Internet connections, such as dial-up access, allowing these users to retrieve e-mail when connected, and subsequently to view and manipulate the retrieved messages when offline. 
### POP3 clients also have an option to leave mail on the server after download. By contrast, the Internet Message Access Protocol (IMAP) was designed to normally leave all messages on the server to permit management with multiple client applications, and to support both connected (online) and disconnected (offline) modes of operation. 
### A POP3 server listens on well-known port number 110 for service requests. Encrypted communication for POP3 is either requested after protocol initiation, using the STLS command, if supported, or by POP3S, which connects to the server using Transport Layer Security (TLS) or Secure Sockets Layer (SSL) on well-known TCP port number 995. 
### Messages available to the client are determined when a POP3 session opens the maildrop, and are identified by message-number local to that session or, optionally, by a unique identifier assigned to the message by the POP server. This unique identifier is permanent and unique to the maildrop and allows a client to access the same message in different POP sessions. Mail is retrieved and marked for deletion by the message-number. When the client exits the session, mail marked for deletion is removed from the maildrop.
## History  
### The first version of the Post Office Protocol, POP1, was specified in RFC 918 (1984). POP2 was specified in RFC 937 (1985). 
### POP3 is the version in most common use. It originated with RFC 1081 (1988) but the most recent specification is RFC 1939, updated with an extension mechanism (RFC 2449) and an authentication mechanism in RFC 1734. This led to a number of POP implementations such as Pine, POPmail, and other early mail clients.  
### While the original POP3 specification supported only an unencrypted USER/PASS login mechanism or Berkeley .rhosts access control, today POP3 supports several authentication methods to provide varying levels of protection against illegitimate access to a user's e-mail. Most are provided by the POP3 extension mechanisms. POP3 clients support SASL authentication methods via the AUTH extension. MIT Project Athena also produced a Kerberized version. RFC 1460 introduced APOP into the core protocol. APOP is a challenge/response protocol which uses the MD5 hash function in an attempt to avoid replay attacks and disclosure of the shared secret. Clients implementing APOP include Mozilla Thunderbird, Opera Mail, Eudora, KMail, Novell Evolution, RimArts' Becky!, Windows Live Mail, PowerMail, Apple Mail, and Mutt. RFC 1460 was obsoleted by RFC 1725, which was in turn obsoleted by RFC 1939.
## POP4  
### POP4 exists only as an informal proposal adding basic folder management, multipart message support, as well as message flag management to compete with IMAP; however, its development has not progressed since 2003.
## Extensions and specifications  
### An extension mechanism was proposed in RFC 2449 to accommodate general extensions as well as announce in an organized manner support for optional commands, such as TOP and UIDL. The RFC did not intend to encourage extensions, and reaffirmed that the role of POP3 is to provide simple support for mainly download-and-delete requirements of mailbox handling. 
### The extensions are termed capabilities and are listed by the CAPA command. With the exception of APOP, the optional commands were included in the initial set of capabilities. Following the lead of ESMTP (RFC 5321), capabilities beginning with an X signify local capabilities.
## STARTTLS  
### The STARTTLS extension allows the use of Transport Layer Security (TLS) or Secure Sockets Layer (SSL) to be negotiated using the STLS command, on the standard POP3 port, rather than an alternate. Some clients and servers instead use the alternate-port method, which uses TCP port 995 (POP3S).
## SDPS  
### Demon Internet introduced extensions to POP3 that allow multiple accounts per domain, and has become known as Standard Dial-up POP3 Service (SDPS). To access each account, the username includes the hostname, as john@hostname or john+hostname. 
### Google Apps uses the same method.
## Kerberized Post Office Protocol  
### In computing, local e-mail clients can use the Kerberized Post Office Protocol (KPOP), an application-layer Internet standard protocol, to retrieve e-mail from a remote server over a TCP/IP connection. The KPOP protocol is based on the POP3 protocol \u2013 differing in that it adds Kerberos security and that it runs by default over TCP port number 1109 instead of 110. One mail server software implementation is found in the Cyrus IMAP server.
## Session example  
### The following POP3 session dialog is an example in RFC 1939: 
### S: <wait for connection on TCP port 110> 
### C: <open connection> 
### S:    +OK POP3 server ready <1896.697170952@dbc.mtview.ca.us> 
### C:    APOP mrose c4c9334bac560ecc979e58001b3e22fb 
### S:    +OK mrose's maildrop has 2 messages (320 octets) 
### C:    STAT 
### S:    +OK 2 320 
### C:    LIST 
### S:    +OK 2 messages (320 octets) 
### S:    1 120 
### S:    2 200 
### S:    . 
### C:    RETR 1 
### S:    +OK 120 octets 
### S:    <the POP3 server sends message 1> 
### S:    . 
### C:    DELE 1 
### S:    +OK message 1 deleted 
### C:    RETR 2 
### S:    +OK 200 octets 
### S:    <the POP3 server sends message 2> 
### S:    . 
### C:    DELE 2 
### S:    +OK message 2 deleted 
### C:    QUIT 
### S:    +OK dewey POP3 server signing off (maildrop empty) 
### C: <close connection> 
### S: <wait for next connection> 

### POP3 servers without the optional APOP command expect the client to log in with the USER and PASS commands: 

### C:    USER mrose 
### S:    +OK User accepted 
### C:    PASS tanstaaf 
### S:    +OK Pass accepted
## Server implementations 
## Comparison with IMAP  
### The Internet Message Access Protocol (IMAP) is an alternative and more recent mailbox access protocol. The highlights of differences are: 

### POP is a simpler protocol, making implementation easier. 
### POP moves the message from the email server to the local computer, although there is usually an option to leave the messages on the email server as well. 
### IMAP defaults to leaving the message on the email server, simply downloading a local copy. 
### POP treats the mailbox as a single store, and has no concept of folders 
### An IMAP client performs complex queries, asking the server for headers, or the bodies of specified messages, or to search for messages meeting certain criteria. Messages in the mail repository can be marked with various status flags (e.g. \"deleted\" or \"answered\") and they stay in the repository until explicitly removed by the user\u2014which may not be until a later session. In short: IMAP is designed to permit manipulation of remote mailboxes as if they were local. Depending on the IMAP client implementation and the mail architecture desired by the system manager, the user may save messages directly on the client machine, or save them on the server, or be given the choice of doing either. 
### The POP protocol requires the currently connected client to be the only client connected to the mailbox.  In contrast, the IMAP protocol specifically allows simultaneous access by multiple clients and provides mechanisms for clients to detect changes made to the mailbox by other, concurrently connected, clients.  See for example RFC3501 section 5.2 which specifically cites \"simultaneous access to the same mailbox by multiple agents\" as an example. 
### When POP retrieves a message, it receives all parts of it, whereas the IMAP4 protocol allows clients to retrieve any of the individual MIME parts separately \u2013 for example, retrieving the plain text without retrieving attached files. 
### IMAP supports flags on the server to keep track of message state: for example, whether or not the message has been read, replied to, forwarded, or deleted.
## Related requests for comments (RFCs)  
### RFC 918 \u2013 POST OFFICE PROTOCOL 
### RFC 937 \u2013 POST OFFICE PROTOCOL \u2013 VERSION 2 
### RFC 1081 \u2013 Post Office Protocol \u2013 Version 3 
### RFC 1939 \u2013 Post Office Protocol \u2013 Version 3 (STD 53) 
### RFC 1957 \u2013 Some Observations on Implementations of the Post Office Protocol (POP3) 
### RFC 2195 \u2013 IMAP/POP AUTHorize Extension for Simple Challenge/Response 
### RFC 2384 \u2013 POP URL Scheme 
### RFC 2449 \u2013 POP3 Extension Mechanism 
### RFC 2595 \u2013 Using TLS with IMAP, POP3 and ACAP 
### RFC 3206 \u2013 The SYS and AUTH POP Response Codes 
### RFC 5034 \u2013 The Post Office Protocol (POP3) Simple Authentication and Security Layer (SASL) Authentication Mechanism 
### RFC 8314 \u2013 Cleartext Considered Obsolete: Use of Transport Layer Security (TLS) for Email Submission and Access
## See also  
### Email encryption 
### Internet Message Access Protocol
## References 
## Further reading 
## External links  
### IANA port number assignments 
### POP3 Sequence Diagram (PDF)"
## References
### [Reference](http://www.eventhelix.com/RealtimeMantra/Networking/POP3.pdf) - http://www.eventhelix.com/RealtimeMantra/Networking/POP3.pdf
### [Reference](http://mail.google.com/support/bin/answer.py?answer=34383) - http://mail.google.com/support/bin/answer.py?answer=34383
### [Reference](http://scholar.google.com/scholar?q=%22Post+Office+Protocol%22) - http://scholar.google.com/scholar?q=%22Post+Office+Protocol%22
### [Reference](http://www.google.com/search?&q=%22Post+Office+Protocol%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22Post+Office+Protocol%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22Post+Office+Protocol%22) - http://www.google.com/search?as_eq=wikipedia&q=%22Post+Office+Protocol%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22Post+Office+Protocol%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22Post+Office+Protocol%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22Post+Office+Protocol%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22Post+Office+Protocol%22+-wikipedia
### [Reference](http://journal.mycom.co.jp/special/2001/onlinenote/005.html) - http://journal.mycom.co.jp/special/2001/onlinenote/005.html
### [Reference](http://e.demon.net/helpdesk/producthelp/mail/sdps-tech.html/) - http://e.demon.net/helpdesk/producthelp/mail/sdps-tech.html/
### [Reference](http://www.pop4.org/pop4/pop4spec.html) - http://www.pop4.org/pop4/pop4spec.html
### [Reference](http://www.rfc-editor.org/std/std53.txt) - http://www.rfc-editor.org/std/std53.txt
### [Reference](https://books.google.com/books?id=UD0h_GqgbHgC&q=network%2B+guide+to+networks) - https://books.google.com/books?id=UD0h_GqgbHgC&q=network%2B+guide+to+networks
### [Reference](https://archive.org/details/livesofcaptivere00petz) - https://archive.org/details/livesofcaptivere00petz
### [Reference](https://web.archive.org/web/20080913155355/http://mail.google.com/support/bin/answer.py?answer=34383) - https://web.archive.org/web/20080913155355/http://mail.google.com/support/bin/answer.py?answer=34383
### [Reference](https://web.archive.org/web/20100131223322/http://journal.mycom.co.jp/special/2001/onlinenote/005.html) - https://web.archive.org/web/20100131223322/http://journal.mycom.co.jp/special/2001/onlinenote/005.html
### [Reference](https://web.archive.org/web/20171021231958/http://www.pop4.org/pop4/pop4spec.html) - https://web.archive.org/web/20171021231958/http://www.pop4.org/pop4/pop4spec.html
### [Reference](https://www.iana.org/assignments/port-numbers) - https://www.iana.org/assignments/port-numbers
### [Reference](https://datatracker.ietf.org/doc/html/rfc1081) - https://datatracker.ietf.org/doc/html/rfc1081
### [Reference](https://datatracker.ietf.org/doc/html/rfc1939) - https://datatracker.ietf.org/doc/html/rfc1939
### [Reference](https://datatracker.ietf.org/doc/html/rfc1957) - https://datatracker.ietf.org/doc/html/rfc1957
### [Reference](https://datatracker.ietf.org/doc/html/rfc2195) - https://datatracker.ietf.org/doc/html/rfc2195
### [Reference](https://datatracker.ietf.org/doc/html/rfc2384) - https://datatracker.ietf.org/doc/html/rfc2384
### [Reference](https://datatracker.ietf.org/doc/html/rfc2449) - https://datatracker.ietf.org/doc/html/rfc2449
### [Reference](https://datatracker.ietf.org/doc/html/rfc2595) - https://datatracker.ietf.org/doc/html/rfc2595
### [Reference](https://datatracker.ietf.org/doc/html/rfc3206) - https://datatracker.ietf.org/doc/html/rfc3206
### [Reference](https://datatracker.ietf.org/doc/html/rfc5034) - https://datatracker.ietf.org/doc/html/rfc5034
### [Reference](https://datatracker.ietf.org/doc/html/rfc8314) - https://datatracker.ietf.org/doc/html/rfc8314
### [Reference](https://datatracker.ietf.org/doc/html/rfc918) - https://datatracker.ietf.org/doc/html/rfc918
### [Reference](https://datatracker.ietf.org/doc/html/rfc937) - https://datatracker.ietf.org/doc/html/rfc937
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22Post+Office+Protocol%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22Post+Office+Protocol%22&acc=on&wc=on
### [Reference](https://archive.today/20110723084318/http://e.demon.net/helpdesk/producthelp/mail/sdps-tech.html/) - https://archive.today/20110723084318/http://e.demon.net/helpdesk/producthelp/mail/sdps-tech.html/
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg) - https://upload.wikimedia.org/wikipedia/en/f/f2/Edit-clear.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg