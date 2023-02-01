
import secrets
#write a diceware passphrase generator in python. The function takes a single argument, the number of words in the passphrase. The function should return a string containing the passphrase.

#The diceware list is a list of words from the diceware word list.

#The diceware word list is a list of words from the diceware word list.

def passphrase(n):
    return ''.join(secrets.choice(words) for _ in range(n))


words = ['aback', 'abaft', 'abandon', 'abashed', 'abate', 'abbey', 'abbot', 'abbreviate', 'abdicate', 'abdomen', 'abdominal', 'abduct', 'aberrant', 'aberration', 'abet', 'abeyance', 'abhor', 'abhorrent', 'abide', 'abiding', 'abilities', 'ability', 'abject', 'abjure', 'ablate', 'ablative', 'ablaze', 'able', 'abler', 'ablest', 'abloom', 'ablution', 'abnegate', 'abnormal', 'aboard', 'abode', 'abolish', 'abolition', 'abominable', 'abominate', 'aboriginal', 'abort', 'abortion', 'abortive', 'abound', 'about', 'above', 'aboveboard', 'abracadabra', 'abrade', 'abrasion', 'abrasive', 'abreast', 'abridge', 'abroad', 'abrogate', 'abrupt', 'abscess', 'abscond', 'absence', 'absent', 'absentee', 'absentminded', 'absinthe', 'absolute', 'absolve', 'absorb', 'absorption', 'abstain', 'abstemious', 'abstinence', 'abstract', 'abstruse', 'absurd', 'absurdity', 'abundant', 'abuse', 'abusive', 'abut', 'abysmal', 'abyss', 'acacia', 'academe', 'academia', 'academic', 'academy', 'accede', 'accelerate', 'accent', 'accentuate', 'accept']

#print(len(words))

#print(words[:10])

print(passphrase(2))

