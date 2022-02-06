# Bit numbering
## [URL](https://en.wikipedia.org/wiki/Bit_numbering) - https://en.wikipedia.org/wiki/Bit_numbering
## Catagories
### Articles with short description
### Assembly languages
### Binary arithmetic
### Short description matches Wikidata
### "In computing, bit numbering is the convention used to identify the bit positions in a binary number.
## Bit significance and indexing  

### In computing, the least significant bit (LSB) is the bit position in a binary integer representing the binary 1s place of the integer. Similarly, the most significant bit (MSB) represents the highest-order place of the binary integer. The LSB is sometimes referred to as the low-order bit or right-most bit, due to the convention in positional notation of writing less significant digits further to the right. The MSB is similarly referred to as the high-order bit or left-most bit. In both cases, the LSB and MSB correlate directly to the least significant digit and most significant digit of a decimal integer. 
### Bit indexing correlates to the positional notation of the value in base 2. For this reason, bit index is not affected by how the value is stored on the device, such as the value's byte order. Rather, it is a property of the numeric value in binary itself. This is often utilized in programming via bit shifting: A value of 1 << n corresponds to the nth bit of a binary integer (with a value of 2n).
## Least significant bit in digital steganography  

### In digital steganography, sensitive messages may be concealed by manipulating and storing information in the least significant bits of an image or a sound file. The user may later recover this information by extracting the least significant bits of the manipulated pixels to recover the original message. This allows the storage or transfer of digital information to remain concealed.
## Unsigned integer example  
### This table illustrates an example of decimal value of 149 and the location of LSB. In this particular example, the position of unit value (decimal 1 or 0) is located in bit position 0 (n  0). MSB stands for most significant bit, while LSB stands for least significant bit. 
## Most- vs least-significant bit first  
### The expressions most significant bit first and least significant bit at last are indications on the ordering of the sequence of the bits in the bytes sent over a wire in a serial transmission protocol or in a stream (e.g. an audio stream). 
### Most significant bit first means that the most significant bit will arrive first: hence e.g. the hexadecimal number 0x12, 00010010 in binary representation, will arrive as the sequence 0 0 0 1 0 0 1 0 . 
### Least significant bit first means that the least significant bit will arrive first: hence e.g. the same hexadecimal number 0x12, again 00010010 in binary representation, will arrive as the (reversed) sequence 0 1 0 0 1 0 0 0.
## LSB 0 bit numbering  

### When the bit numbering starts at zero for the least significant bit (LSB) the numbering scheme is called LSB 0. This bit numbering method has the advantage that for any unsigned number the value of the number can be calculated by using exponentiation with the bit number and a base of 2. The value of an unsigned binary integer is therefore 

  
    
      
        
         \u2211 
          
           i 
            
           0 
          
          
           N 
           \u2212 
           1 
          
        
        
         b 
          
           i 
          
        
       \u22c5 
        
         2 
          
           i 
          
        
      
    
   {\\displaystyle \\sum _{i0}^{N-1}b_{i}\\cdot 2^{i}} 
 where bi denotes the value of the bit with number i, and N denotes the number of bits in total.
## MSB 0 bit numbering  

### When the bit numbering starts at zero for the most significant bit (MSB) the numbering scheme is called MSB 0. 
### The value of an unsigned binary integer is therefore 

  
    
      
        
         \u2211 
          
           i 
            
           0 
          
          
           N 
           \u2212 
           1 
          
        
        
         b 
          
           i 
          
        
       \u22c5 
        
         2 
          
           N 
           \u2212 
           1 
           \u2212 
           i 
          
        
      
    
   {\\displaystyle \\sum _{i0}^{N-1}b_{i}\\cdot 2^{N-1-i}} 
 
## Other  
### ALGOL 68's elem operator is effectively \"MSB 1 bit numbering\" as the bits are numbered from left to right, with the first bit (bits elem 1) being the \"most significant bit\", and the expression (bits elem bits width) giving the \"least significant bit\".  Similarly, when bits are coerced (typecast) to an array of Boolean ([ ]bool bits), the first element of this array (bits[lwb bits]) is again the \"most significant bit\". 
### For MSB 1 numbering, the value of an unsigned binary integer is 

  
    
      
        
         \u2211 
          
           i 
            
           1 
          
          
           N 
          
        
        
         b 
          
           i 
          
        
       \u22c5 
        
         2 
          
           N 
           \u2212 
           i 
          
        
      
    
   {\\displaystyle \\sum _{i1}^{N}b_{i}\\cdot 2^{N-i}} 
 PL/I numbers BIT strings starting with 1 for the leftmost bit. 
### The Fortran BTEST function uses LSB 0 numbering.
## See also  
### ARINC 429 
### Binary numeral system 
### Signed number representations 
### Two's complement 
### Endianness 
### Binary logarithm 
### Unit in the last place (ULP) 
### Find first set 
### MAC address: Bit-reversed notation
## References "
## References
### [Reference](http://www.xcprod.com/titan/XCSB-DOC/bit_numbers.html) - http://www.xcprod.com/titan/XCSB-DOC/bit_numbers.html
### [Reference](https://archive.org/details/computerdesign00lang/page/52) - https://archive.org/details/computerdesign00lang/page/52
## Images
### [Image](https://upload.wikimedia.org/wikipedia/commons/0/0c/LeastSignificantBitDemonstration.jpg) - https://upload.wikimedia.org/wikipedia/commons/0/0c/LeastSignificantBitDemonstration.jpg
### [Image](https://upload.wikimedia.org/wikipedia/commons/a/a2/Least_significant_bit.svg) - https://upload.wikimedia.org/wikipedia/commons/a/a2/Least_significant_bit.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/8/84/Lsb0.svg) - https://upload.wikimedia.org/wikipedia/commons/8/84/Lsb0.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/7/76/Most_significant_bit.svg) - https://upload.wikimedia.org/wikipedia/commons/7/76/Most_significant_bit.svg
### [Image](https://upload.wikimedia.org/wikipedia/commons/5/54/Msb0.svg) - https://upload.wikimedia.org/wikipedia/commons/5/54/Msb0.svg