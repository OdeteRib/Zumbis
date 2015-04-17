def esconde(msg):
    s = ''
    for c in msg: s+= chr(ord(c) + 65)
    return s
def mostra (msg):
    s = ''
    for c in msg: s+= chr(ord(c) - 65)
    return s
