def main():
    rest_coins = 50
    accepted_denominations = {25, 10, 5}
    while rest_coins > 0:
        coin = int(input('Insert Coin: '))
        if coin in accepted_denominations:
            rest_coins -= coin
        if rest_coins > 0:
            print('Amount Due:', rest_coins)
    print('Change Owed:', abs(rest_coins))


if __name__ == '__main__':
    main()
