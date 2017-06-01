def encrypt(x, y):
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    output = []
    keyoutput = []
    messagenumber = len(x)
    keynumber = len(y)
    if messagenumber == keynumber:
        for c in x:
            output.append(associations.find(c))
        for c in y:
            keyoutput.append(associations.find(c))
        for i in range(0,len(y)):
            output[i] = (output[i] + keyoutput[i])%len(associations)
        encrypted = []
        for n in output:
            encrypted.append(associations[n])
        return("".join(encrypted))
    elif messagenumber > keynumber:
            newkey = y * messagenumber
            newkeytwo = newkey[0:messagenumber]
            for c in x:
                output.append(associations.find(c))
            for c in newkeytwo:
                keyoutput.append(associations.find(c))
            for i in range(0,len(newkeytwo)):
                output[i] = (output[i] + keyoutput[i])%len(associations)
            encrypted = []
            for n in output:
                encrypted.append(associations[n])
            return("".join(encrypted))
    else:
            memes = y[0:messagenumber]
            for c in x:
                output.append(associations.find(c))
            for c in memes:
                keyoutput.append(associations.find(c))
            for i in range(0,len(memes)):
                output[i] = (output[i] + keyoutput[i])%len(associations)
            encrypted = []
            for n in output:
                encrypted.append(associations[n])
            return("".join(encrypted))


def decrypt(x, y):
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    output = []
    keyoutput = []
    messagenumber = len(x)
    keynumber = len(y)
    if messagenumber == keynumber:
        for c in x:
            output.append(associations.find(c))
        for c in y:
            keyoutput.append(associations.find(c))
        for i in range(0,len(y)):
            output[i] = (output[i] - keyoutput[i])%len(associations)
        encrypted = []
        for n in output:
            encrypted.append(associations[n])
        return("".join(encrypted))
    elif keynumber < messagenumber:
        newkey = y * messagenumber
        newkeytwo = newkey[0:messagenumber]
        for c in x:
            output.append(associations.find(c))
        for c in newkeytwo:
            keyoutput.append(associations.find(c))
        for i in range(0,len(newkeytwo)):
            output[i] = (output[i] - keyoutput[i])%len(associations)
        encrypted = []
        for n in output:
            encrypted.append(associations[n])
        return("".join(encrypted))
    else:
        memes = y[0:messagenumber]
        for c in x:
            output.append(associations.find(c))
        for c in memes:
            keyoutput.append(associations.find(c))
        for i in range(0,len(memes)):
            output[i] = (output[i] - keyoutput[i])%len(associations)
        encrypted = []
        for n in output:
            encrypted.append(associations[n])
        return("".join(encrypted))
