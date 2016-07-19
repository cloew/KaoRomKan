
HIRAGANA = "あいうえおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもやゆよらりるれろわをん"

HIRAGANA_MAP = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'っ':"'", 'を':'wo', 'ん':'n'}
CONS_HIRAGANA_MAP = {
    'か':'ka', 'が':'ga', 'さ':'sa',  'ざ':'za', 'た':'ta',   'だ':'da', 'な':'na', 'は':'ha', 'ば':'ba', 'ぱ':'pa', 'ま':'ma', 'や':'ya', 'わ':'wa',
    'き':'ki', 'ぎ':'gi', 'し':'shi', 'じ':'ji', 'ち':'chi',  'ぢ':'ji', 'に':'ni', 'ひ':'hi', 'び':'bi', 'ぴ':'pi', 'み':'mi',
    'く':'ku', 'ぐ':'gu', 'す':'su',  'ず':'zu', 'つ':'tsu',  'づ':'zu', 'ぬ':'nu', 'ふ':'hu', 'ぶ':'bu', 'ぷ':'pu', 'む':'mu', 'ゆ':'yu',
    'け':'ke', 'げ':'ge', 'せ':'se', 'ぜ':'ze', 'て':'te',  'で':'de', 'ね':'ne', 'へ':'he', 'べ':'be', 'ぺ':'pe', 'め':'me',
    'こ':'ko', 'ご':'go', 'そ':'so',  'ぞ':'zo', 'と':'to',  'ど':'do', 'の':'no', 'ほ':'ho', 'ぼ':'bo', 'ぽ':'po', 'も':'mo', 'よ':'yo',
}
COMPOUND_HIRAGANA_MAP = {key+yKana:CONS_HIRAGANA_MAP[key][:-1]+yKanaValue for key in 'きぎしじちにひびぴみ' for yKana, yKanaValue in {'ゃ':'ya', 'ゅ':'yu', 'ょ':'yo'}.items()}

DOUBLE_CONS_HIRAGANA_MAP = {'っ'+key:value[0]+key for key, value in CONS_HIRAGANA_MAP.items()}