## 復習時に見直すメモ

- [問題リンク](https://atcoder.jp/contests/arc195/tasks/arc195_b)
- [解説リンク](https://www.youtube.com/watch?v=-PzCaRqlZBA&t=360s)

## 前提知識

- [Σ 計算](https://hiraocafe.com/note/sigmaformula.html)

# B - Uniform Sum

## Intention

- [B 問題 詳細解説](https://atcoder.jp/contests/arc195/editorial/12490)

- a(x)を A_i = x となる i の個数
- b(x)を B_i = x となる i の個数

とした時、「f(z)(= A_i≠-1, B_i≠-1 の時 A_i+B_i=z となる i の個数の最大数)は、a(x), b(z-x)の最小値の x=0〜x=z までの合計」と導き出せれば OK。  
x=0~z の時、a(x)、b(z-x)は 1or0 となる。よってその最小値(つまり 0 となる方、もしくはどちらも 1 である時(A_i+B_i=z が成り立つ i の時)は 1)の合計が f(z)となる。
