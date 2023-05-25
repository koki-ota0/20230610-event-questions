class Logic:
    def __init__(self):
        self.tmp = 0    # 一時変数
    
    def sort(self, array):
        n = len(array)
        
        for i in range(1, n):       # 2つ目の要素以降の要素数分のループを実行
            self.tmp = array[i]     # 一時変数に未ソート部分の最小値のインデックスにある要素を代入
            
            for j in range(i): 
                if self.tmp < array[i - j - 1]:         # ソート済みの要素と大きい方から比較
                    array[i - j] = array[i - j - 1]     # ソート済みの要素の方が大きければ、それを一つずらす
                    if (i - j - 1) == 0:
                        array[i - j - 1] = self.tmp         # 一次変数が先頭に来る場合は、そこに代入
                
                else: 
                    array[i - j] = self.tmp             # 一次変数の要素の方が大きければ、比較した要素の後の位置に一次変数の要素を代入
                    break
                
        return array