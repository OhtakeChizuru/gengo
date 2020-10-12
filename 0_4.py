"""
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

target_word="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
tl=target_word.split(" ") #空白で文を区切りリスト化する。
print(tl)　#リストを表示する。
numbers=[]　#文字数リスト用の空リスト

for i in tl:
    numbers.append(len(i))　#単語ごとに文字数を数え、空リストに入れていく。
    
print(numbers)　#文字数のリストを表示
    