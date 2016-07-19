
HIRAGANA = "あいうえおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもやゆよらりるれろわをん"

HIRAGANA_MAP = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'っ':"'", 'を':'wo', 'ん':'n'}
CONS_HIRAGANA_MAP = {
    'き':'ki', 'ぎ':'gi',
    'し':'shi', 'じ':'ji',
    'ち':'chi'
}
COMPOUND_HIRAGANA_MAP = {
    'きゃ':'kya', 'ぎゃ':'gya',
    'しゅ':'shu', 'じゅ':'ju',
    'ちょ':'cho'
}

DOUBLE_CONS_HIRAGANA_MAP = {'っ'+key:value[0]+value for key, value in CONS_HIRAGANA_MAP.items()}
DOUBLE_CONS_COMPOUND_HIRAGANA_MAP = {'っ'+key:value[0]+value for key, value in COMPOUND_HIRAGANA_MAP.items()}