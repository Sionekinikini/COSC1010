#
# Sione Kinikini
# 4/27/25
# File Encryption and Decryption Programming Project
# COSC 1010
#
encryption_library = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
                      'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
                      'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
                      'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
                      'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
                      't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}

orig_file = open('text.txt','r')
file_read = orig_file.read()    
orig_file.close()
encrypt_file = open('encrypted.txt','w')

for ch in file_read:
    if ch in encryption_library:
        encrypt_file.write(encryption_library[ch])
    else:
        encrypt_file.write(ch)

encrypt_file.close()
encrypt_file = open('text.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()
codes_items = encryption_library.items()

for ch in file_read:
    if not ch in encryption_library.values() or ch == '.' or ch == ',' or ch == '!':
        print(ch)
    else:
        for k,v in codes_items:
            if ch == v and ch != '.':
                print(k,end='')
# Code to decrypt the encrypted file
decryption_library = {'!':'A','@':'B','#':'C','$':'D','%':'E','^':'F','&':'G','*':'H','(':'I',
                      ')':'J','-':'K','_':'L','+':'M','=':'N','`':'O','~':'P','{':'Q','[':'R',
                      '}':'S',']':'T',':':'U',';':'V','"':'W','<':'X','>':'Y','0':'Z','1':'a',
                      '2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','a':'j',
                      'b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'s',
                      'k':'t','l':'u','m':'v','n':'w','o':'x','p':'y','q':'z'}

orig_file = open('encrypted.txt','r')
file_read = orig_file.read()
orig_file.close()
encrypt_file = open('main.py','w')

for ch in file_read:
    if ch in decryption_library:
        encrypt_file.write(decryption_library[ch])
    else:
        encrypt_file.write(ch)

encrypt_file.close()
encrypt_file = open('encrypted.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()    
codes_items = decryption_library.items()

for ch in file_read:
    if not ch in decryption_library.values() or ch == '.' or ch == ',' or ch == '!':
        print(ch)
    else:
        for k,v in codes_items:
            if ch == v and ch != '.':
                print(k,end='')