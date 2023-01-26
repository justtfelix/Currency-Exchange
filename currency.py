usd = 3.4174
euro = 4.1590

money = float(input('შეიყვანეთ თანხა, რომლის გადაცვლაც გსურთ: '))
currency = int(input('შეიყვანეთ ვალუტის კოდი: (აშშ დოლარი - 101, ევრო - 102): '))

if currency == 101:
    cash = round(money / usd, 2)
    print('ვალუტა: აშშ დოლარი')
elif currency == 102:
    cash = round(money / euro, 2)
    print('ვალუტა: ევრო')
else:
    cash = 0
    print('უცნობი ვალუტა')

print('გასაცემია: ', cash)