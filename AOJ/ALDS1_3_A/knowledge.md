# Review memo

### Data structure

Stack に関する基本問題  
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A

## Point

### 逆ポーランド記法
- 演算子 `"+", "-", "*"` が来た場合、スタックから2つ取り出して計算し、結果をスタックに入れる。これだけ。
- 四則演算は、二項演算。なので、スタックに3つ以上のオペランドが存在していても、取り出すのは2つ。

### Python におけるスタック
- リストで、Pythonでのスタックを表現できる。`append()`, `pop()` で操作する。

