import os
import sys
from datetime import datetime
import time


def rewrite_encoding(fname: str, before: str, after: str):
    print("{}のencodingを{}⇒{}に変更します".format(fname, before, after))
    timessleep(1)
    now: str = datetime.now().timestamp()
    tmp_fname = "{}_{}".format(now, fname)
    print(tmp_fname)
    # 一旦tmpファイルに書き込む
    with open(tmp_fname, encoding=after, mode="w") as writer:
        with open(fname, encoding=before, mode="r") as reader:
            for line in reader:
                #print(line)
                writer.write(line)
    # 元のファイル名に戻す
    os.remove(fname)
    os.rename(tmp_fname, fname)
    #os.remove(tmp_fname)


if __name__ == "__main__":
    # currentディレクのテキストファイルをすべてutf8に変える
    BEFORE = "utf-8"
    AFTER = "shift-jis"
    fnames = os.listdir()
    print("curent_dirのすべてのtxtファイルのencodingを書き換えます")
    print("{}⇒{}に書き換えます。よろしいですか？".format(BEFORE,AFTER))
    time.sleep(5)
    for fname in fnames:
        if fname.endswith(".txt"):
        	rewrite_encoding(fname, BEFORE, AFTER)
        else:
            continue
    # rewrite_encoding("tmp.txt","shift-jis","utf-8")
    # os.listdir
