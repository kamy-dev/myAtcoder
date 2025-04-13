## 復習時に見直すメモ

InsertionSort の問題
[Link](https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A&lang=ja)

## point

- range(n)で問題ない。i=0 の時、j=-1 となるが、問題ない。

## Insertion Sort の特徴

- おおかた整列している入力においては、およそ O(N)で計算できるため、整列している場合には使っても良い。
- しかし、昇順にしたいが、データが降順で並んでいる場合は O(N^2)となるため、計算が遅くなる。
