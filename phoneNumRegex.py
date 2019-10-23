import re

# First example of regex use:
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())

#############################################################

# Second example of regex use:
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Area code of phone number found: ' + mo.group(1))
# print('Phone number excluding area code found: ' + mo.group(2))
# print('Phone number found: ' + mo.group(0))
# print('Phone number found: ' + mo.group())
# print('')
#
# # Retrieving all groups at once
# print('All groups displayed: ')
# print(mo.groups())
#
# # Renaming group variables
# areaCode, mainNumber = mo.groups()
# print('Printing area code: ' + areaCode)
# print('Printing main number: ' + mainNumber)

#############################################################

# Third example of regex use:
# \( and \) will match parenthesis
# phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
# print(mo.group(1))
# print(mo.group(2))

#############################################################

# Fourth example of regex use:
# heroRegex = re.compile(r'Batman|Tina Fey')
#
# # First name to come up is given priority match
# mo1 = heroRegex.search('Batman and Tina Fey.')
# print(mo1.group())
#
# mo2 = heroRegex.search('Tina Fey and Batman.')
# print(mo2.group())

#############################################################

# Fifth example of regex use:
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel.')
# print(mo.group())
# print(mo.group(1))

#############################################################

# Sixth example of regex use:
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
#
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())

#############################################################

# Seventh example of regex use:
# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('My number is 415-555-4242.')
# print(mo1.group())
#
# mo2 = phoneRegex.search('My number is 555-4242.')
# print(mo2.group())

#############################################################

# Eighth example of regex use:
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
#
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())
#
# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo3.group())

#############################################################

# Ninth example of regex use:
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
