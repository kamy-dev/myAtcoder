# Review memo

## Dictionary - 辞書 / ハッシュ法
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_C

## Point
### 解説
https://onlinejudge.u-aizu.ac.jp/resources/commentaries/ALDS1_4_C/ja/post?general=Algorithm

### 用語の使い分け
- ハッシュ関数 : キーを数値（位置）に変換する「関数」そのもの。h(k) = k mod 7 のような計算式です。
- ハッシュ法 : ハッシュ関数を使ってデータを管理する「手法・考え方」のこと。アルゴリズムの名前です。
- ハッシュテーブル : ハッシュ法を使って実際にデータを格納する「データ構造」（配列）のこと。
- 辞書（dict）: Pythonが提供するハッシュテーブルの「実装」です。中身はハッシュテーブルですが、ユーザーはそれを意識せず使えます。

### 全体像

```mermaid
graph TD
      subgraph 辞書 dict
          direction TB
          subgraph ハッシュ法["ハッシュ法（データの格納・検索手法）"]
              direction TB

              Input["入力データ（キー）"]

              subgraph HF["ハッシュ関数"]
                  F["key を整数に変換<br/>例: hash('apple') → 4827<br/>4827 % 4 = 3"]
              end

              subgraph HT["ハッシュテーブル（配列）"]
                  B0["[0] 'banana' → 200"]
                  B1["[1] (empty)"]
                  B2["[2] 'cherry' → 300"]
                  B3["[3] 'apple' → 100"]
              end
          end
      end

      Input --> F
      F -->|"インデックス 3"| B3

      style HF fill:#e8f4fd,stroke:#333
      style HT fill:#fff3e0,stroke:#333
      style ハッシュ法 fill:#f9f9f9,stroke:#666
      style 辞書 fill:#f0f0f0,stroke:#000
```
