import MeCab

def convert_to_partial_format(csv_partial_words):
  partial_words_arr = csv_partial_words.split(',')
  partial_words_arr = [partial_word + "\t*" for partial_word in partial_words_arr]
  expected = "{}\nEOS".format("\n".join(partial_words_arr))
  return expected
  
text = convert_to_partial_format("テスト,メッセージ")

wakati = MeCab.Tagger("-p")
node = wakati.parseToNode(text)

nodes = []
while node:
	# surface: 形態素の表層文字列
	# stat: 形態素種類 (0: 通常, 1: 未知語, 2:文頭BOS, 3:文末EOS)
	# cost: BOSノードからこのノードまでの最高の累積コスト
	# wcost: 単語生起コスト
	word = node.surface
	stat = node.stat
	wcost = node.wcost
	cost = node.cost
	nodes.append([word, stat, wcost, cost])
	node = node.next

print(nodes)
