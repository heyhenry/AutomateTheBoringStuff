
def checkPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print("")
print('Is number: 111-222-3333 valid?')
print(checkPhoneNumber('111-222-3333'))
print('Is number: 2222-123-2221 valid?')
print(checkPhoneNumber('2222-123-2221'))
print("")
message = 'My personal number is 041-921-1011 but you can also reach me at my office on 042-231-9821.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if checkPhoneNumber(chunk):
        print('Phone number found:' + chunk)
print('Done')



