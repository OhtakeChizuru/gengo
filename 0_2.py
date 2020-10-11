"""
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

a="パタクトカシー"
print(a[::2])
words=[]
for i in range(len(a)):
    if i % 2 ==0:
        words.append(a[i]) #This expression is Nonetype so words = words.append(a[i]) will return None.
        
words="".join(words)
print(words)
        

        
