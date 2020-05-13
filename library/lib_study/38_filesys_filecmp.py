# 文件及目录的比较
# https://docs.python.org/zh-cn/3/library/filecmp.html
import filecmp

print(
    filecmp.cmp("38_filesys_filecmp.py", "38_filesys_filecmp.py"),
    filecmp.cmpfiles("../", "../", ["lib_study"]),
)

from filecmp import dircmp


def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("diff_file %s found in %s and %s" % (name, dcmp.left,
                                                   dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)


dcmp = dircmp('../lib_study', '../functions')
print_diff_files(dcmp)
