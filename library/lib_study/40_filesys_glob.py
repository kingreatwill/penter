import glob
print(
glob.glob('./[0-9][0-9]_*'),
"\n",
glob.glob('*.py'),
"\n",
glob.glob('?.gif'),
"\n",
glob.glob('**/*.txt', recursive=True),
"\n",
glob.glob('./**/', recursive=True),
)