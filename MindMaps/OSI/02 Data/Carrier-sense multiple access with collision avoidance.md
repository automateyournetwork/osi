# Carrier-sense multiple access with collision avoidance
## [URL](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_avoidance) - https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_avoidance
## Catagories
### All Wikipedia articles written in American English
### Articles with short description
### Channel access methods
### IEEE 802.11
### Short description matches Wikidata
### Use American English from March 2019
### "Carrier-sense multiple access with collision avoidance (CSMA/CA) in computer networking, is a network multiple access method in which carrier sensing is used, but nodes attempt to avoid collisions by beginning transmission only after the channel is sensed to be \"idle\". When they do transmit, nodes transmit their packet data in its entirety. 
### It is particularly important for wireless networks, where the collision detection of the alternative CSMA/CD is not possible due to wireless transmitters desensing their receivers during packet transmission. 
### CSMA/CA is unreliable due to the hidden node problem.CSMA/CA is a protocol that operates in the Data Link Layer (Layer 2) of the OSI model.
## Details  
### Collision avoidance is used to improve the performance of the CSMA method by attempting to divide the channel somewhat equally among all transmitting nodes within the collision domain. 

### Carrier Sense: prior to transmitting, a node first listens to the shared medium (such as listening for wireless signals in a wireless network) to determine whether another node is transmitting or not. Note that the hidden node problem means another node may be transmitting which goes undetected at this stage. 
### Collision Avoidance: if another node was heard, we wait for a period of time (usually random) for the node to stop transmitting before listening again for a free communications channel.Request to Send/Clear to Send (RTS/CTS) may optionally be used at this point to mediate access to the shared medium. This goes some way to alleviating the problem of hidden nodes because, for instance, in a wireless network, the Access Point only issues a Clear to Send to one node at a time. However, wireless 802.11 implementations do not typically implement RTS/CTS for all transmissions; they may turn it off completely, or at least not use it for small packets (the overhead of RTS, CTS and transmission is too great for small data transfers). 
### Transmission: if the medium was identified as being clear or the node received a CTS to explicitly indicate it can send, it sends the frame in its entirety. Unlike CSMA/CD, it is very challenging for a wireless node to listen at the same time as it transmits (its transmission will dwarf any attempt to listen). Continuing the wireless example, the node awaits receipt of an acknowledgement packet from the Access Point to indicate the packet was received and checksummed correctly. If such acknowledgement does not arrive in a timely manner, it assumes the packet collided with some other transmission, causing the node to enter a period of binary exponential backoff prior to attempting to re-transmit.Although CSMA/CA has been used in a variety of wired communication systems, it is particularly beneficial in a wireless LAN due to a common problem of multiple stations being able to see the Access Point, but not each other. This is due to differences in transmit power, and receive sensitivity, as well as distance, and location with respect to the AP. This will cause a station to not be able to 'hear' another station's broadcast. This is the so-called 'hidden node', or 'hidden station' problem. Devices utilizing 802.11 based standards can enjoy the benefits of collision avoidance (RTS / CTS handshake, also Point coordination function), although they do not do so by default. By default they use a Carrier sensing mechanism called 'exponential backoff', or (Distributed coordination function) that relies upon a station attempting to 'listen' for another station's broadcast before sending. CA, or PCF relies upon the AP (or the 'receiver' for Ad hoc networks) granting a station the exclusive right to transmit for a given period of time after requesting it (Request to Send / Clear to Send).CSMA-CA requires a determination of whether a channel is 'idle', even when incompatible standards and overlapping transmission frequencies are used. Per the standards, for 802.11/Wi-Fi transmitters on the same channel, transmitters must take turns to transmit if they can detect each other even 3 dB above the noise floor (the thermal noise floor is around -101 dBm for 20 MHz channels). On the other hand, transmitters will ignore transmitters with incompatible standards or on overlapping channels if the received signal strength from them is below a threshold Pth which, for non Wi-Fi 6 systems, is between -76 and -80 dBm.
## IEEE 802.11 RTS/CTS Exchange  
### CSMA/CA can optionally be supplemented by the exchange of a Request to Send (RTS) packet sent by the sender S, and a Clear to Send (CTS) packet sent by the intended receiver R. Thus alerting all nodes within range of the sender, receiver or both, to not transmit for the duration of the main transmission. This is known as the IEEE 802.11 RTS/CTS exchange. Implementation of RTS/CTS helps to partially solve the hidden node problem that is often found in wireless networking.
## Performance  
### CSMA/CA performance is based largely upon the modulation technique used to transmit the data between nodes. Studies show that under ideal propagation conditions (simulations), direct-sequence spread spectrum (DSSS) provides the highest throughput for all nodes on a network when used in conjunction with CSMA/CA and the IEEE 802.11 RTS/CTS exchange under light network load conditions. Frequency hopping spread spectrum (FHSS) follows distantly behind DSSS with regard to throughput with a greater throughput once network load becomes substantially heavy. However, the throughput is generally the same under real world conditions due to radio propagation factors.
## Usage  
### GNET \u2013 an early proprietary LAN protocol 
### Apple's LocalTalk implemented CSMA/CA on an electrical bus using a three-byte jamming signal. 
### 802.11 RTS/CTS implements virtual carrier sensing using short request to send and clear to send messages for WLANs (802.11 mainly relies on physical carrier sensing though). 
### IEEE 802.15.4 (Wireless PAN) uses CSMA/CA 
### NCR WaveLAN \u2013 an early proprietary wireless network protocol 
### HomePNA 
### Bus networks 
### The ITU-T G.hn standard, which provides a way to create a high-speed (up to 1 Gigabit/s) local area network using existing home wiring (power lines, phone lines and coaxial cables), uses CSMA/CA as a channel access method for flows that do not require guaranteed quality of service, specifically the CSMA/CARP variant.
## See also  
### Carrier-sense multiple access 
### Carrier-sense multiple access with collision detection 
### CSMA/CARP 
### IEEE 802.11 RTS/CTS 
### Network allocation vector 
### Truncated binary exponential backoff
## References  

### Computer Networks: a Systems Approach. Peterson & Davie. Morgan Kaufmann, Burlington, MA, USA. ISBN 978-0-12-385138-3. pp128\u2013139
## External links  
### CSMA/CA RTS/CTS Simulation"
## References
### [Reference](http://media.pearsoncmg.com/aw/aw_kurose_network_2/applets/csma-ca/withhidden.html) - http://media.pearsoncmg.com/aw/aw_kurose_network_2/applets/csma-ca/withhidden.html
### [Reference](http://ocw.mit.edu/courses/aeronautics-and-astronautics/16-36-communication-systems-engineering-spring-2009/lecture-notes/MIT16_36s09_lec21_22.pdf) - http://ocw.mit.edu/courses/aeronautics-and-astronautics/16-36-communication-systems-engineering-spring-2009/lecture-notes/MIT16_36s09_lec21_22.pdf
### [Reference](http://www.cs.purdue.edu/homes/park/cs536-wireless-3.pdf) - http://www.cs.purdue.edu/homes/park/cs536-wireless-3.pdf
### [Reference](http://www.its.bldrdoc.gov/fs-1037/fs-1037c.htm) - http://www.its.bldrdoc.gov/fs-1037/fs-1037c.htm
### [Reference](http://arxiv.org/abs/1003.4070) - http://arxiv.org/abs/1003.4070
### [Reference](http://arxiv.org/archive/cs.NI) - http://arxiv.org/archive/cs.NI
### [Reference](http://www.atis.org/tg2k/) - http://www.atis.org/tg2k/
### [Reference](http://www.eunice-forum.org/eunice99/027.pdf) - http://www.eunice-forum.org/eunice99/027.pdf
### [Reference](https://www.networkcomputing.com/wireless-infrastructure/channel-bonding-wifi-and-radio-frequency-physics) - https://www.networkcomputing.com/wireless-infrastructure/channel-bonding-wifi-and-radio-frequency-physics
### [Reference](https://web.archive.org/web/20080302071329/http://www.atis.org/tg2k/) - https://web.archive.org/web/20080302071329/http://www.atis.org/tg2k/
### [Reference](https://web.archive.org/web/20120306051958/http://www.eunice-forum.org/eunice99/027.pdf#) - https://web.archive.org/web/20120306051958/http://www.eunice-forum.org/eunice99/027.pdf#
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/1/1d/Csma_ca.svg) - https://upload.wikimedia.org/wikipedia/commons/1/1d/Csma_ca.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/archive/1/1d/20200123103132%21Csma_ca.svg) - https://upload.wikimedia.org/wikipedia/commons/archive/1/1d/20200123103132%21Csma_ca.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/archive/1/1d/20151130213630%21Csma_ca.svg) - https://upload.wikimedia.org/wikipedia/commons/archive/1/1d/20151130213630%21Csma_ca.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/archive/1/1d/20110111120447%21Csma_ca.svg) - https://upload.wikimedia.org/wikipedia/commons/archive/1/1d/20110111120447%21Csma_ca.svg