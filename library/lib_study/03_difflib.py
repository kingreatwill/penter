import difflib

# class difflib.SequenceMatcher

# 用来查找最长相同段的子方法
s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
print(s.find_longest_match(0, 5, 0, 9))

s = difflib.SequenceMatcher(lambda x: x == " ", " abcd", "abcd abcd")
print(s.find_longest_match(0, 5, 0, 9))

print(s.get_matching_blocks())
print(s.ratio())
# ratio() 返回一个 [0, 1] 范围内的整数作为两个序列相似性的度量。 根据经验，ratio() 值超过 0.6 就意味着两个序列是近似匹配的：


# class difflib.Differ
d = difflib.Differ()
diff = d.compare("e abcd", "abcd abcd")
print('\n'.join(diff))

"""
'- '行为序列 1 所独有

'+ '行为序列 2 所独有

'  '行在两序列中相同

'? '行不存在于任一输入序列
"""

# class difflib.HtmlDiff
d = difflib.HtmlDiff()
diff = d.make_file("e abcd", "abcd abcd")
print(diff)  # 输出html

# difflib.context_diff
import sys

sys.stdout.writelines(difflib.context_diff("e abcd", "abcd abcd", "before", "after"))
print("-----------")
sys.stdout.writelines(difflib.unified_diff("e abcd", "abcd abcd", "before", "after"))
print("-----------")
# 最佳“近似”匹配构成的列表
# 可选参数 n (默认为 3) 指定最多返回多少个近似匹配； n 必须大于 0.
#
# 可选参数 cutoff (默认为 0.6) 是一个 [0, 1] 范围内的浮点数。 与 word 相似度得分未达到该值的候选匹配将被忽略。
print(difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy']))
import keyword

print(difflib.get_close_matches('wheel', keyword.kwlist))

diff = difflib.ndiff("e abcd", "abcd abcd")
print(''.join(diff), end="")

diff = difflib.ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n'.splitlines(keepends=True))
print(''.join(diff), end="")

print("-----------")
diff = difflib.ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n'.splitlines(keepends=True))
diff = list(diff) # materialize the generated delta into a list
print(''.join(difflib.restore(diff, 1)), end="")
print(''.join(difflib.restore(diff, 2)), end="")

