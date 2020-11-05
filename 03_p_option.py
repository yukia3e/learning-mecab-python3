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
	# MeCab Node Structure 概要
	# https://taku910.github.io/mecab/doxygen/structmecab__node__t.html
	# 
	# prev: 前のnodeへのポインタを取得
	# next:  次のnodeへのポインタを取得
	# enext: 同じ位置で終了するノードへのポインタ
	# bnext: 同じ位置から始まるノードへのポインタ
	# rpath: 右パスへのポインタ
	# lpath:　左パスへのポインタ
	# 
	# surface: 形態素の表層文字列
	# feature: 特徴文字列 (CSVで品詞などが返ってくる)
	# id: ユニークなノードID
	# length: 表層文字列の長さ
	# rlength: 形態素解析を実行する前の空白を含む表層文字列の長さ。
	# rcAttr: 右文脈ID
	# lcAttr: 左文脈ID
	# posid: ユニークな品詞ID (pos-id.def参照)
	# char_type: 文字種情報 (char.def参照)
	# stat: 形態素種類 (0: 通常, 1: 未知語, 2:文頭BOS, 3:文末EOS)
	# isbest: このノードが最適なノード=bestであれば1
	# alpha: 前方累積ログ（forward accumulative log）の合計
	# beta: 後方累積ログ（backword accumulative log）の合計
	# prob: 周辺確率
	# wcost: 単語生起コスト
	# cost: BOSノードからこのノードまでの最高の累積コスト
	word = node.surface
	stat = node.stat
	cost = node.cost
	wcost = node.wcost
	nodes.append([word, stat, cost, wcost])
	node = node.next

print(nodes)
