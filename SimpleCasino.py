from random import randint

print('How much money would you like to charge?')
startmoney = float(input())
moneycounter = startmoney
print('You have charged {}'.format(moneycounter))
print('How many spins you would like to take?')
spins = int(input())

x = 0

for game in range(0,spins):
    x = randint(0,100)
    if game == spins-4:
        print('Youre Last 3 Games')
    if x in range(5,10):
        print(x)
        print('You Won 50 Bucks')
        moneycounter +=50
        continue
    elif x in range(0,5):
        print(x)
        print('You Lost 15 Bucks')
        moneycounter -= 15
    elif moneycounter <= 0:
        print('Please Charge Some Money. You only got{}'.format(moneycounter))
        break
    elif game == spins-1: 
        accountmoney = moneycounter-startmoney
        if accountmoney > 0:
            print('You have won {} and your total money on your account is {}'.format(accountmoney,moneycounter))
            break
        if accountmoney < 0:
             print('You have lost {} and your total money on your account is {}'.format(accountmoney,moneycounter))
             break
        else: print('You Lost nothing')
    else:
        moneycounter -= 0.5
        print('Everyspin costs you 0.6ct! You hit the Number: {}'.format(x))
        continue