import signal

"""
$ kill -l
 1) SIGHUP   2) SIGINT   3) SIGQUIT  4) SIGILL   5) SIGTRAP
 6) SIGABRT  7) SIGBUS   8) SIGFPE   9) SIGKILL 10) SIGUSR1
11) SIGSEGV 12) SIGUSR2 13) SIGPIPE 14) SIGALRM 15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD 18) SIGCONT 19) SIGSTOP 20) SIGTSTP
21) SIGTTIN 22) SIGTTOU 23) SIGURG  24) SIGXCPU 25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF 28) SIGWINCH    29) SIGIO   30) SIGPWR
31) SIGSYS  34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX  


# windows https://docs.microsoft.com/en-us/previous-versions/xdkz3x12(v=vs.140) 
SIGABRT	Abnormal termination 异常终止
SIGFPE	Floating-point error 浮点错误
SIGILL	Illegal instruction 非法指令
SIGINT	CTRL+C signal
SIGSEGV	Illegal storage access 非法存储访问
SIGTERM	Termination request 终止请求
// Signal types
#define SIGINT     2       // interrupt(Ctrl+C中断)
#define SIGILL     4       // illegal instruction - invalid function image(非法指令)
#define SIGFPE     8       // floating point exception(浮点异常)
#define SIGSEGV    11      // segment violation(段错误)
#define SIGTERM    5       // Software termination signal from kill(Kill发出的软件终止)
#define SIGBREAK   21      //Ctrl-Break sequence(Ctrl+Break中断)
#define SIGABRT    22      // abnormal termination triggered by abort call(Abort)
"""

print(signal.SIG_DFL)
print(signal.SIG_IGN)
# print(signal.SIGKILL)

# import signal, os
#
# def handler(signum, frame):
#     print('Signal handler called with signal', signum)
#     raise OSError("Couldn't open device!")
#
# # Set the signal handler and a 5-second alarm
# signal.signal(signal.SIGALRM, handler)
# signal.alarm(5)
#
# # This open() may hang indefinitely
# fd = os.open('/dev/ttyS0', os.O_RDWR)
#
# signal.alarm(0)          # Disable the alarm

import signal, time

# 3秒后终止程序
signal.alarm(3) # Unix

while True:
    time.sleep(1)
    print("working")
