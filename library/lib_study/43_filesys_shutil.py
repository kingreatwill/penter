import os
import shutil
import time

# shutil.copyfile("43_filesys_shutil.py","43_filesys_shutil_copy.py")
# time.sleep(3)
# os.remove("43_filesys_shutil_copy.py")

# f1 = open('name', 'r')
# f2 = open('name_copy', 'w+')
# shutil.copyfileobj(f1, f2, length=16*1024)

# shutil.copymode 权限复制

# shutil.copystat(src, dst, *, follow_symlinks=True)
# 从 src 拷贝权限位、最近访问时间、最近修改时间以及旗标到 dst

# shutil.copy(src, dst, *, follow_symlinks=True)
# 将文件 src 拷贝到文件或目录 dst。 src 和 dst 应为字符串。 如果 dst 指定了一个目录，文件将使用 src 中的基准文件名拷贝到 dst。 返回新创建文件的路径。
# 如果 follow_symlinks 为假值且 src 为符号链接，则 dst 也将被创建为符号链接。 如果 follow_symlinks 为真值且 src 为符号链接，dst 将成为 src 所指向的文件的一个副本。
# 复制文件的内容以及权限，先copyfile后copymode。

# shutil.copy2(src, dst, *, follow_symlinks=True)
# 类似于 copy()，区别在于 copy2() 还会尝试保留文件的元数据。
# 复制文件的内容以及文件的所有状态信息。先copyfile后copystat。

# shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
# 将以 src 为根起点的整个目录树拷贝到名为 dst 的目录并返回目标目录。 dirs_exist_ok 指明是否要在 dst 或任何丢失的父目录已存在的情况下引发异常。

# shutil.rmtree(path, ignore_errors=False, onerror=None)
# 删除一个完整的目录树；path 必须指向一个目录（但不能是一个目录的符号链接）。 如果 ignore_errors 为真值，删除失败导致的错误将被忽略；如果为假值或是省略，此类错误将通过调用由 onerror 所指定的处理程序来处理，或者如果此参数被省略则将引发一个异常。

# shutil.move(src, dst, copy_function=copy2)
# 递归地将一个文件或目录 (src) 移至另一位置 (dst) 并返回目标位置。

print(shutil.disk_usage("."))

# shutil.chown(path, user=None, group=None)
# 修改给定 path 的所有者 user 和/或 group。


# shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)
# 返回当给定的 cmd 被调用时将要运行的可执行文件的路径。 如果没有 cmd 会被调用则返回 None。

# from shutil import copytree, ignore_patterns
#
# copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))


# from shutil import copytree
# import logging
#
# def _logpath(path, names):
#     logging.info('Working in %s', path)
#     return []   # nothing will be ignored
#
# copytree(source, destination, ignore=_logpath)

#
# import os, stat
# import shutil
#
# def remove_readonly(func, path, _):
#     "Clear the readonly bit and reattempt the removal"
#     os.chmod(path, stat.S_IWRITE)
#     func(path)
#
# shutil.rmtree(directory, onerror=remove_readonly)


# shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
# 创建一个归档文件（例如 zip 或 tar）并返回其名称。
# print(shutil.make_archive("archive_name", 'zip',"./"))
# 这样会出现递归  归档！！

# 我们创建了一个 gzip 压缩的 tar 归档文件，其中包含用户的 .ssh 目录下的所有文件:
# from shutil import make_archive
# import os
# archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
# root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
# print(make_archive(archive_name, 'gztar', root_dir))
# '/Users/tarek/myarchive.tar.gz'

# shutil.unpack_archive(filename[, extract_dir[, format]])
# 解包一个归档文件。 filename 是归档文件的完整路径。

print(shutil.get_archive_formats())
# [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]
print(shutil.get_unpack_formats())
# [('bztar', ['.tar.bz2', '.tbz2'], "bzip2'ed tar-file"), ('gztar', ['.tar.gz', '.tgz'], "gzip'ed tar-file"), ('tar', ['.tar'], 'uncompressed tar file'), ('xztar', ['.tar.xz', '.txz'], "xz'ed tar-file"), ('zip', ['.zip'], 'ZIP file')]

print(shutil.get_terminal_size())
