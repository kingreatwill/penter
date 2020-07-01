# gensim使用腾讯开源的预训练好的word2vec模型 : https://ai.tencent.com/ailab/nlp/en/data/Tencent_AILab_ChineseEmbedding.tar.gz
# https://www.ctolib.com/mip/cliuxinxin-TX-WORD2VEC-SMALL.html
# 利用gensim使用腾讯开源的预训练好的词向量 https://www.jianshu.com/p/bba1bf9518dc
from gensim.models import KeyedVectors
# 每个world是200维的向量
file = r'E:\bigdata\ai\Tencent_AILab_ChineseEmbedding\70000-small.txt'
model = KeyedVectors.load_word2vec_format(file, binary=False)
model.init_sims(replace=True)  # 神奇，很省内存，可以运算most_similar

print(model.most_similar(positive=['女', '国王'], negative=['男'], topn=1))

print(model.doesnt_match("上海 成都 广州 北京".split(" ")))

print(model.similarity('女人', '男人'))

print(model.most_similar('特朗普', topn=10))

# 未知词短语向量补齐：
import numpy as np

def compute_ngrams(word, min_n, max_n):
    #BOW, EOW = ('<', '>')  # Used by FastText to attach to all words as prefix and suffix
    extended_word =  word
    ngrams = []
    for ngram_length in range(min_n, min(len(extended_word), max_n) + 1):
        for i in range(0, len(extended_word) - ngram_length + 1):
            ngrams.append(extended_word[i:i + ngram_length])
    return list(set(ngrams))


def wordVec(word, model, min_n = 1, max_n = 3):
    '''
    ngrams_single/ngrams_more,主要是为了当出现oov的情况下,最好先不考虑单字词向量
    '''
    # 确认词向量维度
    word_size = model.wv.syn0[0].shape[0]
    # 计算word的ngrams词组
    ngrams = compute_ngrams(word,min_n = min_n, max_n = max_n)
    # 如果在词典之中，直接返回词向量
    if word in model.wv.vocab.keys():
        return model[word]
    else:
        # 不在词典的情况下
        word_vec = np.zeros(word_size, dtype=np.float32)
        ngrams_found = 0
        ngrams_single = [ng for ng in ngrams if len(ng) == 1]
        ngrams_more = [ng for ng in ngrams if len(ng) > 1]
        # 先只接受2个单词长度以上的词向量
        for ngram in ngrams_more:
            if ngram in model.wv.vocab.keys():
                word_vec += model[ngram]
                ngrams_found += 1
                #print(ngram)
        # 如果，没有匹配到，那么最后是考虑单个词向量
        if ngrams_found == 0:
            for ngram in ngrams_single:
                word_vec += model[ngram]
                ngrams_found += 1
        if word_vec.any():
            return word_vec / max(1, ngrams_found)
        else:
            raise KeyError('all ngrams for word %s absent from model' % word)


# vec = wordVec('you', model, min_n = 1, max_n = 3)
# model.most_similar(positive=[vec], topn=20)