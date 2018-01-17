import itertools

class randU(object):
    ''' Produce a random number using the Park-Miller method.

    See http://www.firstpr.com.au/dsp/rand31/ for further details of this
    method. It is recommended to use the returned value as the value for x1,
    when next calling the method.'''

    randU_c = 65539
    randU_m = 2147483648

    def __init__(self):
        from datetime import datetime

        self.seed = int((datetime.utcnow() - datetime.min).total_seconds())

    def randint(self, upper_limit = randU_m):
        self.seed = (randU_c * seed) % randU_m
        return self.seed % upper_limit

class Mersenne(object):
    """ 
    Based on the pseudocode in https://en.wikipedia.org/wiki/Mersenne_Twister.
    Modified by Philip Sterne <psterne at minervaproject dot com>
    """

    bitmask_1 = (2**32) - 1  # To get last 32 bits
    bitmask_2 = 2**31  # To get 32nd bit
    bitmask_3 = (2**31) - 1  # To get last 31 bits

    def __init__(self):
        from datetime import datetime

        self.seed = int((datetime.utcnow() - datetime.min).total_seconds())
        (self.MT, self.index) = self.__initialize_generator(self.seed)

    def randint(self, upper_limit = 2**31):
        (self.MT, self.index, self.y) = self.__extract_number(self.MT, self.index)
        return self.y % upper_limit

    def __initialize_generator(self, seed):
        "Initialize the generator from a seed"
        # Create a length 624 list to store the state of the generator
        MT = [0 for i in range(624)]
        index = 0
        MT[0] = seed
        for i in range(1, 624):
            MT[i] = ((1812433253 * MT[i - 1]) ^ (
                (MT[i - 1] >> 30) + i)) & self.bitmask_1
        return (MT, index)  
    
    def __generate_numbers(self, MT):
        "Generate an array of 624 untempered numbers"
        for i in range(624):
            y = (MT[i] & self.bitmask_2) + (MT[(i + 1) % 624] & self.bitmask_3)
            MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                MT[i] ^= 2567483615
        return MT   
    

    def __extract_number(self, MT, index):
        """
        Extract a tempered pseudorandom number based on the index-th value,
        calling generate_numbers() every 624 numbers
        """
        if index == 0:
            MT = self.__generate_numbers(MT)
        y = MT[index]
        y ^= y >> 11
        y ^= (y << 7) & 2636928640
        y ^= (y << 15) & 4022730752
        y ^= y >> 18    

        index = (index + 1) % 624
        return (MT, index, y)


class translator(object):
    """Tranlator for multiple language support"""
    
    # Possible improvement: if we load the class after the arg list, 
    # We could load even less languages!

    def __init__(self):
        self.supported_langs = ['en', 'de', 'sp', 'zh_cn']
        self.main_lang = 0

        self.langs = []

        for lang in self.supported_langs:
            self.langs.append([line.rstrip() 
                for line in open('lang_' + lang.upper() + '.ini', encoding="utf-8")])
    
    def translate(self, sentence, target_lang):
        #print('translating', sentence, 'to', target_lang)

        m_sentence = sentence.rstrip()
        ending_spaces = len(sentence) - len(m_sentence)
        target_lang_index = self.supported_langs.index(target_lang)

        try:
            target_sent_index = self.langs[self.main_lang].index(m_sentence)
            return self.langs[target_lang_index][target_sent_index] + ' ' * ending_spaces
        except:
            return sentence

    def print(self, st, args, newline = True):
        if newline:
            print(self.translate(st, args.language))
        else:
            print(self.translate(st, args.language), end = '')    

    def input(self, st, args):
        return input(self.translate(st, args.language))

def get_deck():
    '''Return a list of the all 52 playing cards.

    This list is sorted and always in the same order.
    '''
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    rank = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    cards = list(itertools.product(rank, ['of'], suits))
    return [" ".join(l) for l in cards]


def get_random_card_from_deck(deck, args):
    ''' This element returns a random card from a given list of cards.

    Input:
      deck: list of available cards to return.
      x1: variable for use in the generation of random numbers.
      x2: variable for use in the generation of random numbers.
    '''

    # Constants given by the RANDU algorithm:
    # https://en.wikipedia.org/wiki/RANDU
    if args.rand_method.lower() == 'randu':
        if not '__randUfunction' in globals():
            __randUfunction = randU()
        x1 = __randUfunction.randint(len(deck))
    elif args.rand_method.lower() == 'mersenne':
        if not '__Mersennefunction' in globals():
            __Mersennefunction = Mersenne()
        x1 = __Mersennefunction.randint(len(deck))
    else:
        raise Exception('Unknown randomization method; Check your rand_method argument.')

    card = deck.pop(x1) 
    return (card, deck)


def blackjack_value(card):
    '''Return the value of a card when in the game of Blackjack.

    Input:
        card: A string which identifies the playing card.
    Strictly speaking, Aces can be valued at either 1 or 10, this
    implementation assumes that the value is always 1, and then determines
    later how many aces can be valued at 10.  (This occurs in
    blackjack_hand_value.)
    '''
    try:
        return int(card[:2])
    except ValueError:
        if card[:2] == 'Ac':
            return 1
        else:
            return 10


def is_ace(card):
    '''Identify whether or not a card is an ace.

    In put:
        card: A string which identifies the playing card.

    Returns:
        true or false, depending on whether the card is an ace or not.
    '''
    return card[:2] == 'Ac'


def blackjack_hand_value(cards):
    '''Calculate the maximal value of a given hand in Blackjack.

    Input:
        cards: A list of strings, with each string identifying a playing card.

    Returns:
        The highest possible value of this hand if it is a legal blackjack
        hand, or -1 if it is an illegal hand.
    '''
    sum_cards = sum([blackjack_value(card) for card in cards])
    num_aces = sum([is_ace(card) for card in cards])
    aces_to_use = max(int((21 - sum_cards) / 10.0), num_aces)
    final_value = sum_cards + 10 * aces_to_use
    if final_value > 21:
        return -1
    else:
        return final_value


def display(player, dealer, trans, args):
    '''Display the current information available to the player.'''
    trans.print('The dealer is showing: ', args, newline = False)
    trans.print(dealer[0], args)
    trans.print('Your hand is: ', args, newline = False)
    trans.print(repr(player), args) 


def hit_me(trans, args):
    '''Query the user as to whether they want another car or not.

    Returns:
        A boolean value of True or False.  True means that the user does want
        another card.
    '''
    ans = ""
    while ans.lower() not in ('y', 'n'):
        ans = trans.input("Would you like another card? (y/n):", args)
    return ans.lower() == 'y'


def game(args):
    if not args.language in ['en', 'de', 'sp', 'zh_cn']:
        raise ValueError("Language not recognized or implemented.")

    trans = translator()

    # Initialize everything

    deck = get_deck()
    my_hand = []
    dealer_hand = []

    # Deal the initial cards
    for a in range(2):
        (card, deck) = get_random_card_from_deck(deck, args)
        my_hand.append(card)
        (card, deck) = get_random_card_from_deck(deck, args)
        dealer_hand.append(card)

    # Give the user as many cards as they want (without going bust).
    display(my_hand, dealer_hand, trans, args)
    while hit_me(trans, args):
        (card, deck) = get_random_card_from_deck(deck, args)
        my_hand.append(card)
        display(my_hand, dealer_hand, trans, args)
        if blackjack_hand_value(my_hand) < 0:
            trans.print('You have gone bust!', args)
            break

    # Now deal cards to the dealer:
    trans.print("The dealer has: ", args, newline = False)
    trans.print(repr(dealer_hand), args)
    while 0 < blackjack_hand_value(dealer_hand) < 17:
        (card, deck) = get_random_card_from_deck(deck, args)
        dealer_hand.append(card)
        trans.print("The dealer hits", args)
        trans.print("The dealer has: ", args, newline = False)
        trans.print(repr(dealer_hand), args)

    if blackjack_hand_value(dealer_hand) < 0:
        trans.print("The dealer has gone bust!", args)
    else:
        trans.print('The dealer sticks with: ', args, newline = False)
        trans.print(repr(dealer_hand), args)

    # Determine who has won the game:
    my_total = blackjack_hand_value(my_hand)
    dealer_total = blackjack_hand_value(dealer_hand)
    if dealer_total == my_total:
        trans.print("It's a draw!", args)
    if dealer_total > my_total:
        trans.print("The dealer won!", args)
    if dealer_total < my_total:
        trans.print("You won!", args)


if __name__ == '__main__':

    import argparse 

    parser = argparse.ArgumentParser(description="BlackJack Game.")
    parser.add_argument('--rand_method', default='Mersenne', 
                        help='The random number generator method. Choose between \'Mersenne\' and \'randU\'.')
    parser.add_argument('--language', default='en',
                        help='The language to play blackjack in, e.g. "en"')
    args = parser.parse_args()

    print('-' * 30)
    print(args)
    print('-' * 30)
    print()

    game(args)

    print()
