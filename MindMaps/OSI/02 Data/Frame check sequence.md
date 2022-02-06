# Frame check sequence
## [URL](https://en.wikipedia.org/wiki/Frame_check_sequence) - https://en.wikipedia.org/wiki/Frame_check_sequence
## Catagories
### All Wikipedia articles written in American English
### Articles with short description
### Link protocols
### Logical link control
### Packets (information technology)
### Short description is different from Wikidata
### Use American English from March 2019
### "A frame check sequence (FCS) is an error-detecting code added to a frame in a communication protocol.  Frames are used to send payload data from a source to a destination.
## Purpose  
### All frames and the bits, bytes, and fields contained within them, are susceptible to errors from a variety of sources. The FCS field contains a number that is calculated by the source node based on the data in the frame. This number is added to the end of a frame that is sent. When the destination node receives the frame the FCS number is recalculated and compared with the FCS number included in the frame. If the two numbers are different, an error is assumed and the frame is discarded. 
### The FCS provides error detection only. Error recovery must be performed through separate means. Ethernet, for example, specifies that a damaged frame should be discarded and does not specify any action to cause the frame to be retransmitted. Other protocols, notably the Transmission Control Protocol (TCP), can notice the data loss and initiate retransmission and error recovery.
## Implementation  

### The FCS is often transmitted in such a way that the receiver can compute a running sum over the entire frame, together with the trailing FCS, expecting to see a fixed result (such as zero) when it is correct. For Ethernet and other IEEE 802 protocols, the standard states that data is sent least significant bit first, while the FCS is sent most significant bit (bit 31) first. An alternative approach is to generate the bit reversal of the FCS so that the reversed FCS can be also sent least significant bit (bit 0) first. Refer to Ethernet frame \u00a7 Frame check sequence for more information.
## Types  
### By far the most popular FCS algorithm is a cyclic redundancy check (CRC), used in Ethernet and other IEEE 802 protocols with 32 bits, in X.25 with 16 or 32 bits, in HDLC with 16 or 32 bits, in Frame Relay with 16 bits, in Point-to-Point Protocol (PPP) with 16 or 32 bits, and in other data link layer protocols. 
### Protocols of the Internet protocol suite tend to use checksums.
## See also  
### Syncword
## References "
## References
### [Reference](http://www.cisco.com/c/en/us/support/docs/wan/frame-relay/47202-87.html) - http://www.cisco.com/c/en/us/support/docs/wan/frame-relay/47202-87.html
### [Reference](http://doi.org/10.17487%2FRFC1071) - http://doi.org/10.17487%2FRFC1071
### [Reference](https://books.google.com/books?id=LyCtDwAAQBAJ) - https://books.google.com/books?id=LyCtDwAAQBAJ
### [Reference](https://ecfsapi.fcc.gov/file/1050839507018/IEEE%20Standard%20for%20Ethernet.pdf) - https://ecfsapi.fcc.gov/file/1050839507018/IEEE%20Standard%20for%20Ethernet.pdf
### [Reference](https://datatracker.ietf.org/doc/html/rfc1071) - https://datatracker.ietf.org/doc/html/rfc1071
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/72/Ethernet_Frame.png) - https://upload.wikimedia.org/wikipedia/commons/7/72/Ethernet_Frame.png
### [Image](https://upload.wikimedia.org/wikipedia/commons/4/42/Ethernet_frame.svg) - https://upload.wikimedia.org/wikipedia/commons/4/42/Ethernet_frame.svg