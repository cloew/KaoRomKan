from .kana_map import KanaMap

_HIRAGANA_MAP = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'っ':"'", 'を':'wo', 'ん':'n'}
CONS_HIRAGANA_MAP = {
    'か':'ka', 'が':'ga', 'さ':'sa',  'ざ':'za', 'た':'ta',   'だ':'da', 'な':'na', 'は':'ha', 'ば':'ba', 'ぱ':'pa', 'ま':'ma', 'ら':'ra', 'や':'ya', 'わ':'wa',
    'き':'ki', 'ぎ':'gi', 'し':'shi', 'じ':'ji', 'ち':'chi',  'ぢ':'ji', 'に':'ni', 'ひ':'hi', 'び':'bi', 'ぴ':'pi', 'み':'mi', 'り':'ri',
    'く':'ku', 'ぐ':'gu', 'す':'su',  'ず':'zu', 'つ':'tsu',  'づ':'zu', 'ぬ':'nu', 'ふ':'fu', 'ぶ':'bu', 'ぷ':'pu', 'む':'mu', 'る':'ru', 'ゆ':'yu',
    'け':'ke', 'げ':'ge', 'せ':'se', 'ぜ':'ze', 'て':'te',  'で':'de', 'ね':'ne', 'へ':'he', 'べ':'be', 'ぺ':'pe', 'め':'me', 'れ':'re',
    'こ':'ko', 'ご':'go', 'そ':'so',  'ぞ':'zo', 'と':'to',  'ど':'do', 'の':'no', 'ほ':'ho', 'ぼ':'bo', 'ぽ':'po', 'も':'mo', 'ろ':'ro', 'よ':'yo',
}

HIRAGANA_MAP = KanaMap(_HIRAGANA_MAP, CONS_HIRAGANA_MAP, yIChars='きぎにひびぴみり', otherIChars='しじち', yMappings={'ゃ':'ya', 'ゅ':'yu', 'ょ':'yo'}, doubleChar='っ')

_KATAKANA_MAP = {'ア':'a', 'イ':'i', 'ウ':'u', 'エ':'e', 'オ':'o', 'ッ':"'", 'ヲ':'wo', 'ン':'n'}
CONS_KATAKANA_MAP = {
    'カ':'ka', 'ガ':'ga', 'サ':'sa',  'ザ':'za', 'タ':'ta',   'ダ':'da', 'ナ':'na', 'ハ':'ha', 'バ':'ba', 'パ':'pa', 'マ':'ma', 'ラ':'ra', 'ヤ':'ya', 'ワ':'wa',
    'キ':'ki', 'ギ':'gi', 'シ':'shi', 'ジ':'ji', 'チ':'chi',  'ヂ':'ji', 'ニ':'ni', 'ヒ':'hi', 'ビ':'bi', 'ピ':'pi', 'ミ':'mi', 'リ':'ri',
    'ク':'ku', 'グ':'gu', 'ス':'su',  'ズ':'zu', 'ツ':'tsu',  'ヅ':'zu', 'ヌ':'nu', 'フ':'fu', 'ブ':'bu', 'プ':'pu', 'ム':'mu', 'ル':'ru', 'ユ':'yu',
    'ケ':'ke', 'ゲ':'ge', 'セ':'se', 'ゼ':'ze', 'テ':'te',  'デ':'de', 'ネ':'ne', 'ヘ':'he', 'ベ':'be', 'ペ':'pe', 'メ':'me', 'レ':'re',
    'コ':'ko', 'ゴ':'go', 'ソ':'so',  'ゾ':'zo', 'ト':'to',  'ド':'do', 'ノ':'no', 'ホ':'ho', 'ボ':'bo', 'ポ':'po', 'モ':'mo', 'ロ':'ro', 'ヨ':'yo',
}
ADDT_SOUNDS = [{
    'ヴァ':'va', 'ファ':'fa',
    'ヴィ':'vi', 'ウィ':'wi', 'フィ':'fi', 'ディ':'di', 'ティ':'ti',
    'ドゥ':'du', 'トゥ':'tu',
    'ヴェ':'ve', 'ウェ':'we', 'フェ':'fe', 'チェ':'che', 'ジェ':'je', 'シェ':'she',
    'ヴォ':'vo', 'ウォ':'wo',	'フォ':'fo'
}, {'ヴ':'vu'}]
KATAKANA_MAP = KanaMap(_KATAKANA_MAP, CONS_KATAKANA_MAP, yIChars='キギニヒビピミリ', otherIChars='シジチ', yMappings={'ャ':'ya', 'ュ':'yu', 'ョ':'yo'}, doubleChar='ッ', extras=ADDT_SOUNDS)