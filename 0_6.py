"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""


#センテンスを空白でリスト化する。
target_list="I am an NLPer".split(" ")
print(target_list)


#単語bi-gramなら、単語が2つずつくっついた状態で再度リスト化されるようにする。
word_bi=[]
words=0
def word_bi_gram(a):
    print(a)
    i=0
    while i <= len(a)-1:
        print(i)
        words = a[i]
        words += a[i+1]
        print(words)
        word_bi.append(words)
        i=i+2
        print(i)
    return word_bi

print(word_bi_gram(target_list))

#文字bi-gramならリストを結合してひとつの文字列にし、二文字づつ取り出す。
character=[]
def chara_bi_gram(a):
    text="".join(a)
    print(text)
    i=0
    while i <=len(text)-1:
        if i==len(text)-1:
            bi_gram=text[i]
            character.append(bi_gram)
            break
        else:
            bi_gram=text[i]+text[i+1]
            character.append(bi_gram)
            i=i+2
    return character

print(chara_bi_gram(target_list))
        