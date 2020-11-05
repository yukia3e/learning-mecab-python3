import MeCab

text = "テストメッセージ"

# default
wakati = MeCab.Tagger()
print(wakati.parse(text))

# chasen
wakati = MeCab.Tagger("-Ochasen")
print(wakati.parse(text))

# dump
wakati = MeCab.Tagger("-Odump")
print(wakati.parse(text))

# custom
# optionの参考ページ
# http://www.mwsoft.jp/programming/munou/mecab_command.html
wakati = MeCab.Tagger("-F '%m\t%H\t%pw,%pC,%pc\n' -U '%m\t%H\t%pw,%pC,%pc\n'")
print(wakati.parse(text))
