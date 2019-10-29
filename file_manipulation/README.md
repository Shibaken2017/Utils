
## 環境構築

標準ライブラリーしか使ってないのでpython3.7installするだけ。　　
※windowsの場合：https://www.python.jp/install/windows/install_py3.html  
※linuxの場合:https://qiita.com/micheleno13/items/39ad85cfe44ca32f53ee  
※python3.7で動作確認済み。

## rewrite_encoding.py
encodingをUTF-8⇒shift-jisに変更するプログラムです。encoding変更対象はプログラムファイルと同じdirにある拡張子が[.txt]のファイルです。
  
#### 使いかた(windows10の場合)
コマンドプロンプトを立ち上げて↓を実行する

```
cd log_dir
※log_dirはlogファイルがおいてあるdirを指定してください  
  
python rewrite_encoding.py
```



 
