import subprocess 
import shlex

#subprocess.run(["kubectl","logs","emote-trainb2-8xskr","-f"])
subprocess.run(shlex.split('argo list'))
subprocess.run(shlex.split('kubectl logs emote-trainb2-8xskr -f'))
