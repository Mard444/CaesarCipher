import sys
import string
alphabet = string.printable


#key-n enq grum ,te inch chapova encode anelu u mer encode anelu bary
key = int(sys.argv[1])
encode = input('')
#mer outputy
encoded = ""

#for cikl enq frum dimum enq amen tari(i)positionin  u heto voroshenq nor positiony
for i in encode:
    p = alphabet.find(i)  #find()funkcian dimuma alphabetin hamynknumner gtnelu hamar, gtneluc heto veradardznuma tvi positioni arjeqy
    newP = (p + key)  % len(alphabet) #nor position enq sahmanum u % nel vor sax alphabetov fra
    if i in alphabet:
        encoded = encoded + alphabet[newP] # 1 tary encode a anum u heto arajin aracin gumarvuma erkrordy
    else:
        encoded = encoded + i #ete i-n orinak ,./;'=- senc nishera tox henc et nishern el tpi
print(encoded)

  
