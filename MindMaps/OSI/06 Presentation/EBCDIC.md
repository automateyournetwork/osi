# EBCDIC
## [URL](https://en.wikipedia.org/wiki/EBCDIC) - https://en.wikipedia.org/wiki/EBCDIC
## Catagories
### All articles needing additional references
### All articles with unsourced statements
### Articles needing additional references from January 2019
### Articles with short description
### Articles with unsourced statements from July 2020
### CS1 Russian-language sources (ru)
### CS1 errors: missing periodical
### EBCDIC code pages
### IBM mainframe operating systems
### Short description is different from Wikidata
### Use dmy dates from May 2019
### Webarchive template wayback links
### "Extended Binary Coded Decimal Interchange Code (EBCDIC; ) is an eight-bit character encoding used mainly on IBM mainframe and IBM midrange computer operating systems. It descended from the code used with punched cards and the corresponding six-bit binary-coded decimal code used with most of IBM's computer peripherals of the late 1950s and early 1960s. It is supported by various non-IBM platforms, such as Fujitsu-Siemens' BS2000/OSD, OS-IV, MSP, and MSP-EX, the SDS Sigma series, Unisys VS/9, Unisys MCP and ICL VME.
## History  

### EBCDIC was devised in 1963 and 1964 by IBM and was announced with the release of the IBM System/360 line of mainframe computers. It is an eight-bit character encoding, developed separately from the seven-bit ASCII encoding scheme. It was created to extend the existing Binary-Coded Decimal (BCD) Interchange Code, or BCDIC, which itself was devised as an efficient means of encoding the two zone and number punches on punched cards into six bits. The distinct encoding of 's' and 'S' (using position 2 instead of 1) was maintained from punched cards where it was desirable not to have hole punches too close to each other to ensure the integrity of the physical card.While IBM was a chief proponent of the ASCII standardization committee, the company did not have time to prepare ASCII peripherals (such as card punch machines) to ship with its System/360 computers, so the company settled on EBCDIC. The System/360 became wildly successful, together with clones such as RCA Spectra 70, ICL System 4, and Fujitsu FACOM, thus so did EBCDIC. 
### All IBM mainframe and midrange peripherals and operating systems use EBCDIC as their inherent encoding (with toleration for ASCII, for example, ISPF in z/OS can browse and edit both EBCDIC and ASCII encoded files). Software and many hardware peripherals can translate to and from encodings, and modern mainframes (such as IBM Z) include processor instructions, at the hardware level, to accelerate translation between character sets. 
### There is an EBCDIC-oriented Unicode Transformation Format called UTF-EBCDIC proposed by the Unicode consortium, designed to allow easy updating of EBCDIC software to handle Unicode, but not intended to be used in open interchange environments. Even on systems with extensive EBCDIC support, it has not been popular. For example, z/OS supports Unicode (preferring UTF-16 specifically), but z/OS only has limited support for UTF-EBCDIC. 
### Not all IBM products use EBCDIC; IBM AIX, Linux on IBM Z, and Linux on Power all use ASCII.
## Compatibility with ASCII  
### There were numerous difficulties to writing software that would work in both ASCII and EBCDIC. 

### The gaps between letters made simple code that worked in ASCII fail on EBCDIC. For example for (c  'A'; c < 'Z'; ++c) putchar(c); would print the alphabet from A to Z if ASCII is used, but print 41 characters (including a number of unassigned ones) in EBCDIC. Fixing this required complicating the code with function calls which was greatly resisted by programmers. 
### Sorting EBCDIC put lowercase letters before uppercase letters and letters before numbers, exactly the opposite of ASCII. 
### Programming languages and file formats and network protocols designed for ASCII quickly made use of available punctuation marks (such as the curly braces { and }) that did not exist in EBCDIC, making translation to EBCDIC systems difficult. Conversely EBCDIC had a few characters such as \u00a2 (US cent) that got used on IBM systems and could not be translated to ASCII. 
### The most common newline convention used with EBCDIC is to use a NEL (NEXT LINE) code between lines. Converters to other encodings often replace NEL with LF or CR/LF, even if there is a NEL in the target encoding. This causes the LF and NEL to translate to the same character and be unable to be distinguished. 
### If seven-bit ASCII was used, there was an \"unused\" high bit in 8-bit bytes, and many pieces of software stored other information there. Software would also pack the seven bits and discard the eighth, such as packing five seven-bit ASCII characters in a 36-bit word. On the PDP-11 bytes with the high bit set were treated as negative numbers, behavior that was copied to C, causing unexpected problems if the high bit was set. These all made it difficult to switch from ASCII to the 8-bit EBCDIC (and also made it difficult to switch to 8-bit extended ASCII encodings).
## Code page layout  

### There are hundreds of EBCDIC code pages based on the original EBCDIC character encoding; there are a variety of EBCDIC code pages intended for use in different parts of the world, including code pages for non-Latin scripts such as Chinese, Japanese (e.g., EBCDIC 930, JEF, and KEIS), Korean, and Greek (EBCDIC 875). There is also a huge number of variations with the letters swapped around for no discernible reason. 
### The table below shows the \"invariant subset\" of EBCDIC, which are characters that should have the same assignments on all EBCDIC code pages that use the Latin alphabet (this includes most of the ISO/IEC 646 invariant repertoire, except the exclamation mark). It also shows (in gray) missing ASCII and EBCDIC punctuation, located where they are in Code Page 37 (one of the code page variants of EBCDIC). The blank cells are filled with region-specific characters in the variants, but the characters in gray are often swapped around or replaced as well.
## Definitions of non-ASCII EBCDIC controls  
### Following are the definitions of EBCDIC control characters which either do not map onto the ASCII control characters, or have additional uses. When mapped to Unicode, these are mostly mapped to C1 control character codepoints in a manner specified by IBM's Character Data Representation Architecture (CDRA).Although the default mapping of New Line (NL) corresponds to the ISO/IEC 6429 Next Line (NEL) character (the behaviour of which is also specified, but not required, in Unicode Annex 14), most of these C1-mapped controls match neither those in the ISO/IEC 6429 C1 set, nor those in other registered C1 control sets such as ISO 6630. Although this effectively makes the non-ASCII EBCDIC controls a unique C1 control set, they are not among the C1 control sets registered in the ISO-IR registry, meaning that they do not have an assigned control set designation sequence (as specified by ISO/IEC 2022, and optionally permitted in ISO/IEC 10646 (Unicode)).Besides U+0085 (Next Line), the Unicode Standard does not prescribe an interpretation of C1 control characters, leaving their interpretation to higher level protocols (it suggests, but does not require, their ISO/IEC 6429 interpretations in the absence of use for other purposes), so this mapping is permissible in, but not specified by, Unicode.
## Code pages with Latin-1 character sets  
### The following code pages have the full Latin-1 character set (ISO/IEC 8859-1). The first column gives the original code page number. The second column gives the number of the code page updated with the euro sign (\u20ac) replacing the universal currency sign (\u00a4) (or in the case of EBCDIC 924, with the set changed to match ISO 8859-15)
## Criticism and humor  
### Open-source software advocate and software developer Eric S. Raymond writes in his Jargon File that EBCDIC was loathed by hackers, by which he meant members of a subculture of enthusiastic programmers. The Jargon File 4.4.7 gives the following definition: 
### EBCDIC: /eb\u00b4s@\u00b7dik/, /eb\u00b4see`dik/, /eb\u00b4k@\u00b7dik/, n. 
### [abbreviation, Extended Binary Coded Decimal Interchange Code] An alleged character set used on IBM dinosaurs. It exists in at least six mutually incompatible versions, all featuring such delights as non-contiguous letter sequences and the absence of several ASCII punctuation characters fairly important for modern computer languages (exactly which characters are absent varies according to which version of EBCDIC you're looking at). IBM adapted EBCDIC from punched card code in the early 1960s and promulgated it as a customer-control tactic (see connector conspiracy), spurning the already established ASCII standard. Today, IBM claims to be an open-systems company, but IBM's own description of the EBCDIC variants and how to convert between them is still internally classified top-secret, burn-before-reading. Hackers blanch at the very name of EBCDIC and consider it a manifestation of purest evil. 
### EBCDIC design was also the source of many jokes. One such joke, found in the Unix fortune file of 4.3BSD Tahoe (1990) went: 

### Professor: \"So the American government went to IBM to come up with an encryption standard, and they came up with\u2014\"Student: \"EBCDIC!\" 
### References to the EBCDIC character set are made in the 1979 computer game series Zork. In the \"Machine Room\" in Zork II, EBCDIC is used to imply an incomprehensible language: 

### This is a large room full of assorted heavy machinery, whirring noisily. The room smells of burned resistors. Along one wall are three buttons which are, respectively, round, triangular, and square. Naturally, above these buttons are instructions written in EBCDIC... 
### In 2021, it became public that a Belgian bank was still using EBCDIC internally in 2019. This came to attention because a customer insisted that the correct spelling of his surname included an umlaut, which the bank omitted. The customer filed a complaint citing the guarantee in the General Data Protection Regulation of the right to timely \"rectification of inaccurate personal data.\" The bank argued in part that it could not comply because its computer system was only compatible with EBCDIC, which does not support umlauted letters. The appeals court ruled in favor of the customer.
## See also  
### UTF-EBCDIC
## References 
## External links  
### Character Data Representation Architecture (CDRA) from IBM at the Wayback Machine (archived 2018-05-13). Contains IBM's official information on code pages and character sets. 
### Code page 37 
### Code page 1047 
### Host Code Page Reference from IBM, shows code charts for several single-byte EBCDIC pages. 
### \"Code Pages\". from \"IBM i globalization\". 
### ICU Converter Explorer Contains more information about EBCDIC derived from IBM's CDRA, including DBCS EBCDIC (Double Byte Character Set EBCDIC) 
### ICU Charset Mapping Tables Contains computer readable Unicode mapping tables for EBCDIC and many other character sets 
### EBCDIC character list, including decimal and hex values, symbolic name, and character/function 
### EBCDIC-code pages with Latin-1-charset (JavaScript) 
### All EBCDIC code pages and 3270 graphics escape codes at the Wayback Machine (archived August 27, 2016)"
## References
### [Reference](http:ftp://ftp.software.ibm.com/software/globalization/gcoc/attachments/CP00037.pdf) - http:ftp://ftp.software.ibm.com/software/globalization/gcoc/attachments/CP00037.pdf
### [Reference](http:ftp://ftp.software.ibm.com/software/globalization/gcoc/attachments/CP01047.pdf) - http:ftp://ftp.software.ibm.com/software/globalization/gcoc/attachments/CP01047.pdf
### [Reference](http://www.bobbemer.com/P-BIT.HTM) - http://www.bobbemer.com/P-BIT.HTM
### [Reference](http://scholar.google.com/scholar?q=%22EBCDIC%22) - http://scholar.google.com/scholar?q=%22EBCDIC%22
### [Reference](http://www.google.com/search?&q=%22EBCDIC%22&tbs=bkt:s&tbm=bks) - http://www.google.com/search?&q=%22EBCDIC%22&tbs=bkt:s&tbm=bks
### [Reference](http://www.google.com/search?as_eq=wikipedia&q=%22EBCDIC%22) - http://www.google.com/search?as_eq=wikipedia&q=%22EBCDIC%22
### [Reference](http://www.google.com/search?tbm=nws&q=%22EBCDIC%22+-wikipedia&tbs=ar:1) - http://www.google.com/search?tbm=nws&q=%22EBCDIC%22+-wikipedia&tbs=ar:1
### [Reference](http://www.google.com/search?tbs=bks:1&q=%22EBCDIC%22+-wikipedia) - http://www.google.com/search?tbs=bks:1&q=%22EBCDIC%22+-wikipedia
### [Reference](http://publib.boulder.ibm.com/infocenter/zos/v1r9/index.jsp?topic=/com.ibm.zos.r9.adms700/adms7a05158.htm) - http://publib.boulder.ibm.com/infocenter/zos/v1r9/index.jsp?topic=/com.ibm.zos.r9.adms700/adms7a05158.htm
### [Reference](http://worldpowersystems.com/archives/codes/X3.4-1963/page4.JPG) - http://worldpowersystems.com/archives/codes/X3.4-1963/page4.JPG
### [Reference](http://wzwz.de/prog/ebcdic/cc_en.htm) - http://wzwz.de/prog/ebcdic/cc_en.htm
### [Reference](http://lccn.loc.gov/77-90165) - http://lccn.loc.gov/77-90165
### [Reference](http://manybooks.net/titles/anonetext02jarg422.html) - http://manybooks.net/titles/anonetext02jarg422.html
### [Reference](http://www.bitsavers.org/pdf/dec/pdp10/1970_PDP-10_Ref/1970PDP10Ref_Part2.pdf) - http://www.bitsavers.org/pdf/dec/pdp10/1970_PDP-10_Ref/1970PDP10Ref_Part2.pdf
### [Reference](http://catb.org/jargon/html/E/EBCDIC.html) - http://catb.org/jargon/html/E/EBCDIC.html
### [Reference](http://www.icu-project.org/charts/charset/) - http://www.icu-project.org/charts/charset/
### [Reference](http://www.unicode.org/reports/tr14/tr14-43.html#NL) - http://www.unicode.org/reports/tr14/tr14-43.html#NL
### [Reference](http://docs.cntd.ru/document/gost-19768-93) - http://docs.cntd.ru/document/gost-19768-93
### [Reference](https://books.google.com/books?id=6-tQAAAAMAAJ) - https://books.google.com/books?id=6-tQAAAAMAAJ
### [Reference](https://www-01.ibm.com/software/globalization/cdra/appendix_g1.html) - https://www-01.ibm.com/software/globalization/cdra/appendix_g1.html
### [Reference](https://www.ibm.com/support/knowledgecenter/SSEQ5Y_5.9.0/com.ibm.pcomm.doc/reference/pdf/hcp_referenceV58.pdf) - https://www.ibm.com/support/knowledgecenter/SSEQ5Y_5.9.0/com.ibm.pcomm.doc/reference/pdf/hcp_referenceV58.pdf
### [Reference](https://www.ibm.com/support/knowledgecenter/en/ssw_ibm_i_71/nls/rbagsinvariantcharset.htm) - https://www.ibm.com/support/knowledgecenter/en/ssw_ibm_i_71/nls/rbagsinvariantcharset.htm
### [Reference](https://www.ibm.com/support/knowledgecenter/ssw_ibm_i_74/nls/rbagscodepages.htm) - https://www.ibm.com/support/knowledgecenter/ssw_ibm_i_74/nls/rbagscodepages.htm
### [Reference](https://www.ibm.com/support/knowledgecenter/ssw_ibm_i_74/nls/rbagsglobalmain.htm) - https://www.ibm.com/support/knowledgecenter/ssw_ibm_i_74/nls/rbagsglobalmain.htm
### [Reference](https://gdprhub.eu/index.php?title=Court_of_Appeal_of_Brussels_-_2019/AR/1006) - https://gdprhub.eu/index.php?title=Court_of_Appeal_of_Brussels_-_2019/AR/1006
### [Reference](https://www.itscj.ipsj.or.jp/iso-ir/124.pdf) - https://www.itscj.ipsj.or.jp/iso-ir/124.pdf
### [Reference](https://www.itscj.ipsj.or.jp/itscj_english/iso-ir/ISO-IR.pdf) - https://www.itscj.ipsj.or.jp/itscj_english/iso-ir/ISO-IR.pdf
### [Reference](https://shkspr.mobi/blog/2021/10/ebcdic-is-incompatible-with-gdpr/) - https://shkspr.mobi/blog/2021/10/ebcdic-is-incompatible-with-gdpr/
### [Reference](https://web.archive.org/web/20160303222819/http://www.hansenb.pdx.edu/DMKB/dict/tutorials/ebcdic.php) - https://web.archive.org/web/20160303222819/http://www.hansenb.pdx.edu/DMKB/dict/tutorials/ebcdic.php
### [Reference](https://web.archive.org/web/20160526172151/https://textfiles.meulie.net/bitsaved/Books/Mackenzie_CodedCharSets.pdf) - https://web.archive.org/web/20160526172151/https://textfiles.meulie.net/bitsaved/Books/Mackenzie_CodedCharSets.pdf
### [Reference](https://web.archive.org/web/20160812085410/http://worldpowersystems.com/projects/codes/X3.4-1963/page4.JPG) - https://web.archive.org/web/20160812085410/http://worldpowersystems.com/projects/codes/X3.4-1963/page4.JPG
### [Reference](https://web.archive.org/web/20160827044130/http://mainframe.wiki/ebcdicTbl.php) - https://web.archive.org/web/20160827044130/http://mainframe.wiki/ebcdicTbl.php
### [Reference](https://web.archive.org/web/20180513204153/http://www.bobbemer.com/P-BIT.HTM) - https://web.archive.org/web/20180513204153/http://www.bobbemer.com/P-BIT.HTM
### [Reference](https://web.archive.org/web/20180513205203/http://catb.org/jargon/html/E/EBCDIC.html) - https://web.archive.org/web/20180513205203/http://catb.org/jargon/html/E/EBCDIC.html
### [Reference](https://web.archive.org/web/20180513205355/https://www-01.ibm.com/software/globalization/g11n-res.html) - https://web.archive.org/web/20180513205355/https://www-01.ibm.com/software/globalization/g11n-res.html
### [Reference](https://web.archive.org/web/20180911044845/https://www-01.ibm.com/software/globalization/cdra/appendix_g1.html) - https://web.archive.org/web/20180911044845/https://www-01.ibm.com/software/globalization/cdra/appendix_g1.html
### [Reference](https://web.archive.org/web/20190321232630/http://publib.boulder.ibm.com/infocenter/zos/v1r9/index.jsp?topic=/com.ibm.zos.r9.adms700/adms7a05158.htm) - https://web.archive.org/web/20190321232630/http://publib.boulder.ibm.com/infocenter/zos/v1r9/index.jsp?topic=/com.ibm.zos.r9.adms700/adms7a05158.htm
### [Reference](https://standards.iso.org/ittf/PubliclyAvailableStandards/c069119_ISO_IEC_10646_2017.zip) - https://standards.iso.org/ittf/PubliclyAvailableStandards/c069119_ISO_IEC_10646_2017.zip
### [Reference](https://www.jstor.org/action/doBasicSearch?Query=%22EBCDIC%22&acc=on&wc=on) - https://www.jstor.org/action/doBasicSearch?Query=%22EBCDIC%22&acc=on&wc=on
### [Reference](https://minnie.tuhs.org/cgi-bin/utree.pl?file=4.3BSD-Reno/share/games/fortune/fortunes) - https://minnie.tuhs.org/cgi-bin/utree.pl?file=4.3BSD-Reno/share/games/fortune/fortunes
### [Reference](https://icu4c-demos.unicode.org/icu-bin/convexp) - https://icu4c-demos.unicode.org/icu-bin/convexp
### [Reference](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/EBCDIC/CP037.TXT) - https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/EBCDIC/CP037.TXT
### [Reference](https://www.unicode.org/reports/tr16/tr16-6.html#Step%202) - https://www.unicode.org/reports/tr16/tr16-6.html#Step%202
### [Reference](https://www.unicode.org/versions/Unicode12.0.0/ch23.pdf#page=3) - https://www.unicode.org/versions/Unicode12.0.0/ch23.pdf#page=3
## Images
### [Image](https://upload.wikimedia.org/wikipedia/en/1/16/Blue-punch-card-front-horiz_top-char-contrast-stretched.png) - https://upload.wikimedia.org/wikipedia/en/1/16/Blue-punch-card-front-horiz_top-char-contrast-stretched.png
### [Image](https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg) - https://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg
### [Image](https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg) - https://upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg