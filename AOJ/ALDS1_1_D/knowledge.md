## 復習時に見直すメモ

[Link](https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D)

- Rj−Ri where j>i

## 減少するパターンも考える必要がある

5
5
4
3
2
1

この場合、-1 となる。

また
4
3
1000
5
1

だと、997 が最大。

## ポイント

- maxv の値を、Rt の制約から「10\*\*9 -1」以下にすること
- Rj を進めつつ、その時点(t=j)での最大値を求めつつ、最小値を保持すると、for 文を 2 回回さなくて済む。
