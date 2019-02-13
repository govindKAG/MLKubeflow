import shlex
def get_args():
    l = []
    with open('sample-args.txt','r') as f:
        command = f.readline().strip()
        l.append(shlex.split(command))
        for i in f:
            l.append(i.strip().split(':'))
    return l

#res = get_args()

#print(res)
#command = res.pop(0)
#print(command)
#print(res)
#command_str = [ '"' + i +'"' for i in command]
#command_str = '[' + ','.join(command_str) + ']'
#print(command_str)
