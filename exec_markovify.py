import os
import sys

import markovify

# モデルを生成する
model = None
#if os.path.exists('./learned.json'):
#  # 既に学習済モデルがあればそれを利用する
#  #print('Use Learned JSON Data')
#  with open('./learned.json', 'r') as file:
#    model = markovify.NewlineText.from_json(file.read())
#else:
  # 学習済モデルがなければテキストファイルからモデルを生成する
  #print('Use Text File')
text = open('./splitted.txt', 'r').read()
model = markovify.NewlineText(text, state_size = 3)

"""
# 文章を生成する
sentence = model.make_sentence(tries = 1000)

# 文章生成に失敗したら None が返る
if sentence is None:
  print('上手く生成できませんでした')
  sys.exit()

# 分かち書きされているのを結合して出力する
#print('----------')
print(''.join(sentence.split()))
#print('----------')

if not os.path.exists('./learned.json'):
  #print('Write Learned JSON Data')
  with open('./learned.json', 'w') as file:
    file.write(model.to_json())
"""

# 異なる文章を10個列挙させる
sentences = []
while len(sentences) < 10:
  sentence = model.make_sentence(tries = 1000)
  if sentence is not None:
    new_sentence = ''.join(sentence.split())
    if new_sentence not in sentences:
      print(new_sentence)
      sentences.append(new_sentence)

print('\nEnd')
