import shlex
import subprocess 
from external import get_latest_argo_logs
from yaml_gen_ruamel import generate_yaml

#argo submit my_file.yaml -p build-push-image=false -p execute-train=true -p docker-user=govindkag -p github-user=govindKAG -p train-name=emote-trainb11 -p version=4.0

ARGUMENT_FILE = 'sample-args.txt'

def build(template_yaml,yaml_file,docker_user, github_user,train_name, version):
    generate_yaml(template_yaml, yaml_file,ARGUMENT_FILE)
    subprocess.run(f"argo submit {yaml_file} -p build-push-image=true -p execute-train=false -p docker-user={docker_user} -p github-user={github_user} -p train-name={train_name} -p version={version}", shell=True)
    get_latest_argo_logs(train_name)
    
def train(template_yaml, yaml_file,docker_user, github_user,train_name, version):
    generate_yaml(template_yaml, yaml_file,ARGUMENT_FILE)
    subprocess.run(f"argo submit {yaml_file} -p build-push-image=false -p execute-train=true -p docker-user={docker_user} -p github-user={github_user} -p train-name={train_name} -p version={version}", shell=True)
    get_latest_argo_logs(train_name, pod_logs=True)

#build('new-training.yaml', 'my_file.yaml', docker_user = 'govindkag', github_user = 'govindKAG', train_name = 'emote-trainb17', version='4.3')
train('new-training.yaml', 'my_file.yaml', docker_user = 'govindkag', github_user = 'govindKAG', train_name = 'emote-trainb23', version='4.3')

