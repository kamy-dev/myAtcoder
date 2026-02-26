# Review memo

双方向連結リスト の問題  
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_C

## Point

- 振り返るときに便利なdllの図↓
```bash
初期状態: head → [1] ⇔ [3] ⇔ [2] ⇔ [5] ← tail
```

### deleteメソッド
> 1. prev で一つずつ辿る  
> 2. prev.next が削除対象か毎回チェック  
> 3. 見つけたら prev.next を一つ先に付け替えて対象を切り離す  
> 4. return で即終了

```bash
prev = head(A) からスタート

ループ1回目: prev = A, prev.next = B
  prev.next.data == "B" → 一致！
  
  prev.next is self.tail? → BはtailではないのでNo
  
  prev.next = prev.next.next を実行:
    A.next = B.next = C
    
    A  ------→  C
    ↑            ↑
   prev        tail
  
  Bが切り離された。終了。
```


