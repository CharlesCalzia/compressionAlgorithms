
class compress:
    def __init__(self, text):
        self.text = text

    def RLE(self): #run length encoding
        returnText = ""
        current = 0
        loop = True
        while loop:
            count = 1
            while True:
                if current==len(self.text)-1:
                    returnText+=f"{count}{self.text[current]}"
                    loop = False
                    break
                current+=1
                if self.text[current]!=self.text[current-1]: break
                count+=1
            if loop==True: returnText+=str(count)+self.text[current-1]
        return returnText
    
    def LempelZiv(self): #Lempel–Ziv–Welch (LZW) compression algorithm
        current = 0
        dict = {}
        currentMaxDict = 1
        send = ""
        run = True
        while run:
            try: currentChars = [self.text[current]]
            except: break
            while True:
                current+=1
                if ''.join(currentChars) not in dict:
                    dict[''.join(currentChars)]=currentMaxDict
                    currentMaxDict+=1
                    send+=''.join(currentChars)
                    break
                elif current!=len(self.text)-1:
                    currentChars[-1]=dict[''.join(currentChars)]
                    currentChars.append(self.text[current])
                else:
                    run = False
                    break
        return send

                
            
                

text = compress("abba")
print(text.RLE())
print(text.LempelZiv())

                