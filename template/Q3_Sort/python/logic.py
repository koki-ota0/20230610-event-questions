class Logic:
    def __init__(self):
        self.tmp = 0    # 一時変数
    
    def sort(self, array):
        n = len(array)
        group = n // 2          # 分割するグループ数は配列の要素数の半分
        
        while group >= 1:       # グルーピングの間隔が1になるまで繰り返す

            for i in range(group, n):       # グループの2つ目の要素以降の要素数分のループを実行
                self.tmp = array[i]         # 一時変数に未ソート部分の最小値のインデックスにある要素を代入
                
                for j in range(1, (i + 1) // group): 
                    if self.tmp < array[i - j*group]:                     # 同一グループ内のソート済みの要素と大きい方から比較
                        array[i - (j - 1)*group] = array[i - j*group]   # ソート済みの要素の方が大きければ、それを一つずらす
                        if (i - j*group) <= group:
                            array[i - j*group] = self.tmp                 # 一次変数がグループの先頭に来る場合は、そこに代入
                    
                    else:
                        array[i - (j - 1)*group] = self.tmp               # 一次変数の要素の方が大きければ、比較した要素の（同一グループ内の）後の位置に一次変数の要素を代入
                        break
            
            group = group // 2  # グルーピングの間隔を半分にする

        return array