# DubblyLinkedList クラス
## Identity
> 「そのクラスは何か」  
> クラスの責務を一文で言えるか

双方向連結リストとして、Nodeの集合を順序付きで管理する

## State
> 「何を知っているか」

- `head`
    - 連結リストの先頭を指すポインター

- `tail`
    - 連結リストの末尾を指すポインター

## Behavior
> 「何ができるか」

- `insert x`
    - 連結リストの先頭にキー x を持つ要素を継ぎ足す。

- `delete x`
    - キー x を持つ最初の要素を連結リストから削除する。そのような要素が存在しない場合は何もしない。

- `delete_first`
    - リストの先頭の要素を削除する。

- `delete_last` 
    - リストの末尾の要素を削除する。

## Invariant(不変条件)/Constraints
> 「常に守るべきルール」

- `head` と `tail` は `Node | None` のみ
- リストが空のとき `head` と `tail` は両方 `None`
- リストが1要素のとき `head is tail`
- head.prev は常に None、tail.next は常に None

## Relationships
> 「他クラスとの関係」

- `Node` クラスを各メソッドで利用する。継承はしない。

# Node クラス
## Identity
> 「そのクラスは何か」  
> クラスの責務を一文で言えるか

双方向連結リスト内の1つのデータ要素と、その前後の接続情報を保持する

## State
> 「何を知っているか」

- `data`
    - データそのもの。

- `prev`
    - 前のノードを指すポインター
    - 初期値: `None`
    - 型: `Node | None`

- `next`
    - 次のノードを指すポインター
    - 初期値: `None`
    - 型: `Node | None`

## Behavior
> 「何ができるか」

特になし  
dunderメソッドは以下実装

- `__repr__`


## Invariant(不変条件)/Constraints
> 「常に守るべきルール」

- `prev`と`next`は、`Node`か`None`のみ

## Relationships
> 「他クラスとの関係」

- `DubblyLinkedList` に所有される (部品として使われれる)

