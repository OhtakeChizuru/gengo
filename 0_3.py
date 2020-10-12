"""
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

pre="パトカー"
after="タクシー"

tl=[]

for i in range(0,4): #preとafterを一文字ずつtlリストに加えていく
    tl.append(pre[i])
    tl.append(after[i])

print("".join(tl))#tlリストの要素を結合し文字列にする。