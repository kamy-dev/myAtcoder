## 復習時に見直すメモ

最大公約数 の問題  
[ALDS1_1_B](https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_B)

## point

- x, y = y, x % yとすることで、例えx <= yであっても成り立つ。  
    例: x = 3, y = 12の時
    ```bash
    [1回目]
    x, y = 12, 3 % 12
    x,y = 12, 3
    
    [2回目] ※ ここで入れ替わる。
    x, y = 3, 12 % 3
    ```

## 参考資料

- [ユークリッド互除法 証明](https://univ-juken.com/euclids-gozyoho#google_vignette)
-
