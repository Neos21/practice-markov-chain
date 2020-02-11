import MeCab

# Markovify で上手く解釈できない文字列を定義しておく : https://github.com/jsvine/markovify/issues/84
breaking_chars = ['(', ')', '[', ']', '"', "'"]

# 基となるテキストをファイルから読み込む
text = open('./input.txt', 'r').read()

#mecab = MeCab.Tagger()
mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

# 1行ごとに処理する
splitted_text = ''
for line in text.split():
  # テキストを一文ごとに改行し、一文の語句をスペースで分割する
  #print('Line : ', line)
  parsed_nodes = mecab.parseToNode(line)
  while parsed_nodes:
    print('Surface : ', parsed_nodes.surface)
    try:
      # 上手く解釈できない文字列は飛ばして結合する
      if parsed_nodes.surface not in breaking_chars:
        #print('  OK')
        splitted_text += parsed_nodes.surface
      # 句読点でなければスペースで分かち書きする
      if parsed_nodes.surface != '。' and parsed_nodes.surface != '、':
        #print('  スペース付与')
        splitted_text += ' '
      # 句点が登場したら改行で文章を分割する
      if parsed_nodes.surface == '。':
        #print('  改行付与')
        splitted_text += '\n'
    except UnicodeDecodeError as error:
      print('Error : ', line)
    finally:
      parsed_nodes = parsed_nodes.next

#print('Result :\n', splitted_text)

with open('./splitted.txt', 'w') as file:
  file.write(splitted_text)

print('End')
