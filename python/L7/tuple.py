#タプルとは
#要素が変更されないタイプのリスト（コレクション)
#タプル名＝(値1,値2・・・)と入力
#タプル名＝値1,値2,・・・とも書ける
#タプル名＝tuple([リスト])でリストをタプルにできる
#readonlyなので変更、削除はできない
tp=(1,3,5,7,9)
print(tp[2])#not tp(2)
#辞書型とは
#データにキーをつけて読みだすことができるもの
#
mydict = {"apple":100, "orange":90, "banana":120}
print(mydict)
mydict["apple"]=150
onedict=mydict.copy()
print(onedict)
del mydict["banana"]
twodict=mydict.copy()
print(twodict)
'''
() : parentheses     tuple
[] : square brackets list
{} : braces          dict
さらにネストさせたい場合は {[({[()]})]} 
'''
#dictの高度な使い方

for i in mydict.keys():
    print(i,end="\t")
for j in mydict.values():
    print(j,end="\t")
for k in mydict.items():
    print(k,end="\t")

mydict.update(onedict)#辞書の結合
print(mydict)