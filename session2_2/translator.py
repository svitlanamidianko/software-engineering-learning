class translator(object):
    """Tranlator for multiple language support"""

    supported_langs = ['en', 'de', 'sp', 'zh_cn']

    def __init__(self, target_lang = 'en'):
        self.main_lang = 0
        self.target_lang = self.supported_langs.index(target_lang)

        self.main_lang_list = \
            [line.rstrip() for line in open('lang_' + self.supported_langs[self.main_lang].upper() + '.ini', encoding="utf-8")]

        self.target_lang_list = \
            [line.rstrip() for line in open('lang_' + self.supported_langs[self.target_lang].upper().upper() + '.ini', encoding="utf-8")]
        print(self.main_lang_list.index('You won!'))

    def translate(self, sentence):
        if self.target_lang == self.main_lang:
            return sentence

        m_sentence = sentence.rstrip()
        ending_spaces = len(sentence) - len(m_sentence)

        try:
            sent_index = self.main_lang_list.index(m_sentence)
            return self.target_lang_list[sent_index] + ' ' * ending_spaces
        except:
            return sentence

def trans_init(args):
    if not args.language in translator.supported_langs:
        raise ValueError("Language not recognized or implemented.")

    global trans
    trans = translator(target_lang = args.language)

def _(original_string):
    '''Return the value of a card when in the game of Blackjack.    

    Input:
        original_string: A string with sentence.

    Returns:
        string, the translated version of the string

    Strictly speaking, Aces can be valued at either 1 or 10, this
    implementation assumes that the value is always 1, and then determines
    later how many aces can be valued at 10.  (This occurs in
    blackjack_value.)
    '''
    if not 'trans' in globals():
        raise Exception('Undefined translator')

    return trans.translate(original_string)