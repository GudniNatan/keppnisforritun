from random import randint

hand = [bool(randint(0, 1)) for i in range(6)]


print(hand)


def flip(card):
    if card is not None:
        return not card


def resolve(hand):
    while hand:
        for index, val in enumerate(hand):
            if val:
                if index > 0:
                    hand[index - 1] = flip(hand[index - 1])
                if index < len(hand) - 1:
                    hand[index + 1] = flip(hand[index + 1])
                hand[index] = None
                print(hand)
                break
        else:
            if hand.count(True) == 0 and hand.count(False) == 0:
                print("success!")
            else:
                print(hand)
                print("fail!")
            return


def resolve(hand):
    if not hand:
        return True
    if hand.count(True) % 2 == 0:
        return False
    for i in range(len(hand)):
        if hand[i]:
            if count == upcount // 2:
                return resolve(hand[:i]) and resolve(hand[i:])
            count += 1

print(resolve(hand))
