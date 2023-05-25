class Logic:
    def sort(self, array):
        n = len(array)
        
        for i in range(n): # リストの要素数分のループを実行
            for j in reversed(range(i, n)): # 最後の i 個の要素はすでにソート済みなので、無視する
                
                if array[j] < array[j - 1]: # 隣接する要素を比較して必要なら入れ替える
                    array[j], array[j - 1] = array[j - 1], array[j]

        return array
