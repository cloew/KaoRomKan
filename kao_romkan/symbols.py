from .kana_map import KanaMap

_HIRAGANA_MAP = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'っ':"'", 'を':'wo', 'ん':'n'}
CONS_HIRAGANA_MAP = {
    'か':'ka', 'が':'ga', 'さ':'sa',  'ざ':'za', 'た':'ta',   'だ':'da', 'な':'na', 'は':'ha', 'ば':'ba', 'ぱ':'pa', 'ま':'ma', 'や':'ya', 'わ':'wa',
    'き':'ki', 'ぎ':'gi', 'し':'shi', 'じ':'ji', 'ち':'chi',  'ぢ':'ji', 'に':'ni', 'ひ':'hi', 'び':'bi', 'ぴ':'pi', 'み':'mi',
    'く':'ku', 'ぐ':'gu', 'す':'su',  'ず':'zu', 'つ':'tsu',  'づ':'zu', 'ぬ':'nu', 'ふ':'hu', 'ぶ':'bu', 'ぷ':'pu', 'む':'mu', 'ゆ':'yu',
    'け':'ke', 'げ':'ge', 'せ':'se', 'ぜ':'ze', 'て':'te',  'で':'de', 'ね':'ne', 'へ':'he', 'べ':'be', 'ぺ':'pe', 'め':'me',
    'こ':'ko', 'ご':'go', 'そ':'so',  'ぞ':'zo', 'と':'to',  'ど':'do', 'の':'no', 'ほ':'ho', 'ぼ':'bo', 'ぽ':'po', 'も':'mo', 'よ':'yo',
}

HIRAGANA_MAP = KanaMap(_HIRAGANA_MAP, CONS_HIRAGANA_MAP, iChars='きぎしじちにひびぴみ', yMappings={'ゃ':'ya', 'ゅ':'yu', 'ょ':'yo'}, doubleChar='っ')

# KATAKANA_MAP = {'ア':'a', 'イ':'i', 'ウ':'u', 'エ':'e', 'オ':'o', 'ッ':"'", 'ヲ':'wo', 'ン':'n'}
# CONS_KATAKANA_MAP = {
    # 'カ':'ka', 'ガ':'ga', 'サ':'sa',  'ザ':'za', 'タ':'ta',   'ダ':'da', 'ナ':'na', 'ハ':'ha', 'バ':'ba', 'パ':'pa', 'マ':'ma', 'ヤ':'ya', 'ワ':'wa',
    # 'キ':'ki', 'ギ':'gi', 'シ':'shi', 'ジ':'ji', 'チ':'chi',  'ヂ':'ji', 'ニ':'ni', 'ヒ':'hi', 'ビ':'bi', 'ピ':'pi', 'ミ':'mi',
    # 'ク':'ku', 'グ':'gu', 'ス':'su',  'ズ':'zu', 'ツ':'tsu',  'ヅ':'zu', 'ヌ':'nu', 'フ':'hu', 'ブ':'bu', 'プ':'pu', 'ム':'mu', 'ユ':'yu',
    # 'ケ':'ke', 'ゲ':'ge', 'セ':'se', 'ゼ':'ze', 'テ':'te',  'デ':'de', 'ネ':'ne', 'ヘ':'he', 'ベ':'be', 'ペ':'pe', 'メ':'me',
    # 'コ':'ko', 'ゴ':'go', 'ソ':'so',  'ゾ':'zo', 'ト':'to',  'ド':'do', 'ノ':'no', 'ホ':'ho', 'ボ':'bo', 'ポ':'po', 'モ':'mo', 'ヨ':'yo',
# }
# COMPOUND_KATAKANA_MAP = {key+yKana:CONS_KATAKANA_MAP[key][:-1]+yKanaValue for key in 'キギシジチニヒビピミ' for yKana, yKanaValue in {'ャ':'ya', 'ュ':'yu', 'ョ':'yo'}.items()}

# DOUBLE_CONS_KATAKANA_MAP = {'ッ'+key:value[0]+key for key, value in CONS_KATAKANA_MAP.items()}
# KATAKANA_MAP.update(CONS_KATAKANA_MAP)