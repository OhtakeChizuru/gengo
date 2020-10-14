"""
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. 
Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

target_sentense="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

tl=target_sentense.split(" ") #This statement splits target_sentense at a space.
print(tl) #Check that tl was splitted correctly.
print(range(len(tl)))
dictionary={}

for i in range(len(tl)-1): 
    if i == 0 :
        chara=tl[i][0]
        dictionary[chara]=i
        
    elif i == range(4,8):
        chara=tl[i][0]
        dictionary[chara]=i
        
    elif i == range(14,18):
        chara=tl[i][0]
        dictionary[chara]=i
        
    else:
        chara=tl[i][1]
        dictionary[chara]=i

print(dictionary)
    
    