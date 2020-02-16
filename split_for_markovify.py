import MeCab

# Markovify で上手く解釈できない文字列を定義しておく : https://github.com/jsvine/markovify/issues/84
breaking_chars = ['(', ')', '[', ']', '"', "'"]

# 基となるテキストをファイルから読み込む
text = open('./input.txt', 'r', encoding = 'utf-8').read()

#mecab = MeCab.Tagger()
mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

# テキストを一文ごとに改行し、一文の語句をスペースで分割する
splitted_text = ''
for line in text.splitlines():
  #print('Line : ', line)
  parsed_nodes = mecab.parseToNode(line)
  while parsed_nodes:
    #print('Surface : ', parsed_nodes.surface, ' : ', len(parsed_nodes.surface))
    try:
      if len(parsed_nodes.surface) == 0:  # 空文字は飛ばす
        continue
      if parsed_nodes.surface not in breaking_chars:  # うまく結合できない文字のみ除外し結合する
        splitted_text += parsed_nodes.surface
      if parsed_nodes.surface != '。' and parsed_nodes.surface != '、':  # 句読点でなければスペースで分かち書きする
        splitted_text += ' '
      if parsed_nodes.surface == '。':  # 句点が登場したら改行する
        splitted_text += '\n'
    except UnicodeDecodeError as error:
      print('Error : ', line)
    finally:
      parsed_nodes = parsed_nodes.next
  # 1行終了
  splitted_text += '\n'

# 空白行を消す
splitted_text = '\n'.join(filter(lambda x: x.strip(), splitted_text.split('\n')))

with open('./splitted.txt', 'w', encoding = 'utf-8') as file:
  file.write(splitted_text)

print('\nEnd')
