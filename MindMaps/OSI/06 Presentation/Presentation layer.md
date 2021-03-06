# Presentation layer
## [URL](https://en.wikipedia.org/wiki/Presentation_layer) - https://en.wikipedia.org/wiki/Presentation_layer
## Catagories
### All Wikipedia articles written in American English
### Articles with long short description
### Articles with short description
### OSI model
### Short description matches Wikidata
### Use American English from March 2019
### Use mdy dates from March 2019
### "In the seven-layer OSI model of computer networking, the presentation layer is layer 6 and serves as the data translator for the network. It is sometimes called the syntax layer.
## Description  
### Within the service layering semantics of the OSI network architecture, the presentation layer responds to service requests from the application layer and issues service requests to the session layer through a unique presentation service access point (PSAP).The presentation layer ensures the information that the application layer of one system sends out is readable by the application layer of another system. On the sending system it is responsible for conversion to standard, transmittable formats. On the receiving system it is responsible for the translation, formatting, and delivery of information for processing or display.  In theory, it relieves application layer protocols of concern regarding syntactical differences in data representation within the end-user systems. An example of a presentation service would be the conversion of an extended binary coded decimal interchange code (EBCDIC-coded) text computer file to an ASCII-coded file. If necessary, the presentation layer might be able to translate between multiple data formats using a common format. 
### In many widely used applications and protocols no distinction is actually made between the presentation and application layers. For example, HyperText Transfer Protocol (HTTP), generally regarded as an application-layer protocol, has presentation-layer aspects such as the ability to identify character encoding for proper conversion, which is then done in the application layer. 
### The presentation layer is the lowest layer at which application programmers consider data structure and presentation, instead of simply sending data in the form of datagrams or packets between hosts. This layer deals with issues of string representation - whether they use the Pascal method (an integer length field followed by the specified amount of bytes) or the C/C++ method (null-terminated strings, e.g. \"thisisastring\\0\"). The idea is that the application layer should be able to point at the data to be moved, and the presentation layer will translate this to commands able to be understood by other applications and processes. 
### Serialization of complex data structures into flat byte-strings (using mechanisms such as TLV or XML) can be thought of as the key functionality of the presentation layer. Structure representation is normally standardized at this level, often by using XML. As well as simple pieces of data, like strings, more complicated things are standardized in this layer. Two common examples are 'objects' in object-oriented programming, and the exact way that streaming video is transmitted. 
### Encryption and Decryption are typically done at this level too, although it can be done on the application, session, transport, or network layers, each having its own advantages and disadvantages. For example, when logging on to bank account sites the presentation layer will decrypt the data as it is received.
## Services  
### Data conversion 
### Character code translation 
### Compression 
### Encryption and Decryption 
### Serialization
## Protocols  
### Protocols sometimes considered at this level (though perhaps not strictly adhering to the OSI model) include: 

### Apple Filing Protocol (AFP) 
### Independent Computing Architecture (ICA), the Citrix system core protocol 
### Lightweight Presentation Protocol (LPP) 
### NetWare Core Protocol (NCP) 
### Network Data Representation (NDR) 
### Tox, The Tox protocol is sometimes regarded as part of both the presentation and application layer 
### eXternal Data Representation (XDR) 
### X.25 Packet Assembler/Disassembler Protocol (PAD)
## See also  
### ASN.1 
### X.690
## References "
## References
### [Reference](http://www.linfo.org/presentation_layer.html) - http://www.linfo.org/presentation_layer.html
### [Reference](https://books.google.com/books?id=UD0h_GqgbHgC&q=network%2B+guide+to+networks) - https://books.google.com/books?id=UD0h_GqgbHgC&q=network%2B+guide+to+networks
### [Reference](https://books.google.com/books?id=cUYk0ZhOxpEC&q=computer+telephony+encyclopedia) - https://books.google.com/books?id=cUYk0ZhOxpEC&q=computer+telephony+encyclopedia
### [Reference](https://technet.microsoft.com/en-us/library/cc959885.aspx) - https://technet.microsoft.com/en-us/library/cc959885.aspx
### [Reference](https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://www.itu.int/rec/T-REC-X.225-199511-I/en
### [Reference](https://archive.org/details/datacomputercomm0000hura) - https://archive.org/details/datacomputercomm0000hura
### [Reference](https://archive.org/details/datacomputercomm0000hura/page/671) - https://archive.org/details/datacomputercomm0000hura/page/671
### [Reference](https://archive.org/details/datacomputercomm0000hura/page/710) - https://archive.org/details/datacomputercomm0000hura/page/710
### [Reference](https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en) - https://web.archive.org/web/20210201064044/https://www.itu.int/rec/T-REC-X.225-199511-I/en
## Images