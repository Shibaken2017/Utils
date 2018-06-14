import string
import random

n=10

def random_str_generator(n=10):

    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    return random_str


def random_list_generator(n=100):
    '''
    generate str obejcts like this （→）["hoaj","oiuoas","oiha"]
    :return:
    '''
    tmp=r'['
    for i in range(n):
        tmp+=r'"{}",'.format(random_str_generator())

    tmp+=r'"{}"'.format(random_str_generator())+r']'
    return tmp
# ユーティリティ関数にすると便利かも?

if __name__=="__main__":

    with open("test.txt","w")as writer:
        writer.write(random_list_generator(300))