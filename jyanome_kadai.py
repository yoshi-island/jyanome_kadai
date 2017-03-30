# -*- coding: utf-8 -*-
# ~/.pyenv/shims/python
# ~/.pyenv/versions/3.5.0/envs/jyanome_kadai

# max value to compare
max_value = 100000
# max indexes
max_index = 100

# get sosu
## num_listをtargetで割っていってどれも割り切れなければ素数として追記する
num_list = [2] # ここに追記していく
target = 3 # 比べる数
flag = 0 # 判定用
hop = 3 # 三つ飛ばしで省く
skip_sum = 0 # 飛ばした数

while flag == 0:
  count = 0 # targetがそれまででた数字(すでにnum_listにある中身)で割り切れたら増やすカウンタ
#  print("num_list %s" % num_list)
  print("target %s" % target)
  for l in num_list:
    if target % l == 0:
      count += 1
  if count == 0:
    num_list.append(target)
  target += 1

#  if target >= max_value:
  if len(num_list) == max_index:
    flag = 1

#  print("num_list %s" % num_list)
#  print("len num_list %s" % len(num_list))
#  print((len(num_list) + 1 + skip_sum) % (hop + 1))
  if (len(num_list) + 1 + skip_sum) % (hop + 1) == 0:
    target += 2
    skip_sum += 1

print("num_list %s" % num_list )
print("num_list %s" % len(num_list) )
