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
'''
() : parentheses
[] : square brackets
{} : braces
さらにネストさせたい場合は {[({[()]})]} 
'''