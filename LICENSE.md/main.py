confirm  = 5
while confirm == 5:
    print('welcome to blackjack,do you want to play?[y/n]')
    startgame = input('')

    if startgame == 'y' or startgame == 'Y':
        import cardPicker
        import handCardValue

        playgameconfirm = 5
        while playgameconfirm == 5:
            cardpick = cardPicker.randomCardGenerator()
            playercard1 = cardpick[0]
            dealercard1 = cardpick[1]
            playercard2 = cardpick[2]
            dealercard2 = cardpick[3]
            b = cardpick[4:]
            cardcount = cardPicker.card_counting_unit(cardpick)
            playercard1value = cardcount[0]
            dealercard1value = cardcount[1]
            playercard2value = cardcount[2]
            dealercard2value = cardcount[3]
            bvalues = cardcount[4:]
            print('your cards are ', playercard1, ' ', playercard2)
            valueplayer = handCardValue.playerhandvalue(playercard1value, playercard2value)
            print(valueplayer)
            print('dealer face-up card is ', dealercard1)

            nextstepconfirm = 5
            nextcardcounter = 0
            while nextstepconfirm is 5:
                nextstep = input('hit/stand = ')
                if nextstep == 'hit':
                    if playercard1value == 11 or playercard2value == 11:
                        valueplayer = valueplayer - 10
                    if b[nextcardcounter] == 11:
                        b[nextcardcounter] = b[nextcardcounter] - 10
                    print('your next card is ', b[nextcardcounter])
                    valueplayer = handCardValue.hitvalue(bvalues[nextcardcounter], valueplayer)
                    print(valueplayer)
                    nextcardcounter += 1

                elif nextstep == 'stand':
                    nextstepconfirm = 1

                else:
                    print('do not understand')

            if valueplayer <= 21:
                valuedealer = handCardValue.dealerhandvalue(dealercard1value, dealercard2value)
                print('dealer cards are ', dealercard1, dealercard2)
                print(valuedealer)
                while valuedealer < 17:
                    if dealercard1value == 11 or dealercard2value == 11:
                        valuedealer = valuedealer - 10
                    if b[nextcardcounter] == 11:
                        b[nextcardcounter] = b[nextcardcounter] - 10
                    print('dealer next card is ', b[nextcardcounter])
                    valuedealer = handCardValue.hitvalue(bvalues[nextcardcounter], valuedealer)
                    print(valuedealer)
                    nextcardcounter += 1

                if valuedealer <= 21:
                    if valueplayer > valuedealer:
                        print('you win')

                    else:
                        print('you lose')

                else:
                    print('you win')

            else:
                print('you lose')

            gameconfirm = 5
            while gameconfirm == 5:
                confirmation = input('do you want to play again? [y/n] ')
                if confirmation == 'y' or confirmation == 'Y':
                    print('play again')
                    gameconfirm = 10

                elif confirmation == 'n' or confirmation == 'N':
                    playgameconfirm = 10
                    gameconfirm = 10

                else:
                    print('do not understand')

        confirm = 10

    elif startgame == 'n' or startgame == 'N':
        print('exiting game now')
        confirm = 10

    else:
        print('do not understand')




