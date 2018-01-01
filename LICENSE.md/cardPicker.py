def randomCardGenerator():
    import random
    a = ['As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks',
    'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh',
    'Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc',
    'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd']
    cardpick = random.sample(a,10)
    playercard1 = cardpick[0]
    dealercard1 = cardpick[1]
    playercard2 = cardpick[2]
    dealercard2 = cardpick[3]
    b = cardpick[4:]
    print(cardpick)
    return (cardpick)

def card_counting_unit(cardpick):
    cardcount = cardpick
    for count in range(0, len(cardpick)):
        if cardpick[count] == 'As' or cardpick[count] is 'Ah' or cardpick[count] is 'Ac' or cardpick[count] is 'Ad' :
            cardcount[count] = 11

        elif cardpick[count] == '2s' or cardpick[count] is '2h' or cardpick[count] is '2c' or cardpick[count] is '2d' :
            cardcount[count] = 2

        elif cardpick[count] == '3s' or cardpick[count] is '3h' or cardpick[count] is '3c' or cardpick[count] is '3d' :
            cardcount[count] = 3

        elif cardpick[count] == '4s' or cardpick[count] is '4h' or cardpick[count] is '4c' or cardpick[count] is '4d' :
            cardcount[count] = 4

        elif cardpick[count] == '5s' or cardpick[count] is '5h' or cardpick[count] is '5c' or cardpick[count] is '5d' :
            cardcount[count] = 5

        elif cardpick[count] == '6s' or cardpick[count] is '6h' or cardpick[count] is '6c' or cardpick[count] is '6d' :
            cardcount[count] = 6

        elif cardpick[count] == '7s' or cardpick[count] is '7h' or cardpick[count] is '7c' or cardpick[count] is '7d' :
            cardcount[count] = 7

        elif cardpick[count] == '8s' or cardpick[count] is '8h' or cardpick[count] is '8c' or cardpick[count] is '8d' :
            cardcount[count] = 8

        elif cardpick[count] == '9s' or cardpick[count] is '9h' or cardpick[count] is '9c' or cardpick[count] is '9d' :
            cardcount[count] = 9

        elif cardpick[count] == '10s' or cardpick[count] is '10h' or cardpick[count] is '10c' or cardpick[count] is '10d' :
            cardcount[count] = 10

        elif cardpick[count] == 'Js' or cardpick[count] is 'Jh' or cardpick[count] is 'Jc' or cardpick[count] is 'Jd' :
            cardcount[count] = 10

        elif cardpick[count] == 'Qs' or cardpick[count] is 'Qh' or cardpick[count] is 'Qc' or cardpick[count] is 'Qd' :
            cardcount[count] = 10

        elif cardpick[count] == 'Ks' or cardpick[count] is 'Kh' or cardpick[count] is 'Kc' or cardpick[count] is 'Kd' :
            cardcount[count] = 10

    print(cardcount)
    return cardcount


