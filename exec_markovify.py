import os
import random
import sys

import markovify

# パラメータを生成する
state_size           = random.randint(1, 5)          # state_size : 1〜5 の間くらいがまともな文章になる
is_use_make_sentence = random.choice((True, False))  # make_sentence() を使うか make_short_sentence() を使うか
max_chars            = random.randint(20, 280)       # make_short_sentence() の場合の最大文字数 : 20 以上で日本語10文字程度の文章が成り立つようになる

print('State Size : ', state_size)
print('Method     : ', 'make_sentence' if is_use_make_sentence else 'make_short_sentence')
print('Max Chars  : ', max_chars if not is_use_make_sentence else '(Not Use)')
print('')

# モデルを生成する
text = open('./splitted.txt', 'r', encoding = 'utf-8').read()
model = markovify.NewlineText(text, state_size = state_size)

# リトライ回数の管理用
retry_count = 0
max_retry_count = 5

# 異なる文章を10個列挙させる
sentences = []
while len(sentences) < 10:
  # 文章生成を試みる
  sentence = None
  if is_use_make_sentence:
    sentence = model.make_sentence(tries = 1000)
  else:
    sentence = model.make_short_sentence(tries = 1000, max_chars = 40)
  
  # 文章が生成できなかったらリトライする
  if sentence is None:
    retry_count += 1
    if retry_count <= max_retry_count:
      continue
    else:
      break
  
  # 文章の分かち書きのスペースを除去する
  new_sentence = ''.join(sentence.split())
  
  # 既出の文章の場合はリトライする
  if new_sentence in sentences:
    retry_count += 1
    if retry_count <= max_retry_count:
      continue
    else:
      break
  
  # 初出の文章を出力する
  print(new_sentence)
  sentences.append(new_sentence)

print('')
print('Created : ', len(sentences))

print('\nEnd')
