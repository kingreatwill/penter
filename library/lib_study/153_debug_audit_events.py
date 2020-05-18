# https://docs.python.org/zh-cn/3/library/audit_events.html
# https://www.python.org/dev/peps/pep-0578/
import sys
# def audit_hook(event,args):
#   print(event)
# sys.addaudithook(audit_hook)
# print('test')

#sys.audit("shutil.copyfile")
print("-----------------")
def audit_hook2(event,args):
  if event in ['test']:
    print('event:'+event)
    print(args)
sys.addaudithook(audit_hook2)
sys.audit('test','Hello World!')


