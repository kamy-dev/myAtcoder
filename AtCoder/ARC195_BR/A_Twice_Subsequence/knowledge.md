## 復習時に見直すメモ

- [問題リンク](https://atcoder.jp/contests/arc195/tasks/arc195_a)  
- [解説リンク](https://atcoder.jp/contests/arc195/editorial/12489)

# A - Twice Subsequence
参考リンク集  
- [部分文字列について](https://qiita.com/drken/items/a207e5ae3ea2cf17f4bd)

## Intention
部分列Bが数列A内に2回以上存在する = 前から走査 + 後ろから走査の2回をやった後、それぞれのインデックスが異なれば、数列Aの中に部分列Bが2回以上出現したと言える。
なので、「前から走査、後ろから走査すればいいじゃん！」と気づければ解けた。
