from ruamel.yaml import YAML
from splitter import get_args

def generate_yaml(input_file_name, output_file_name, argument_file_name):
    yaml = YAML()
    yaml.preserve_quotes = True
    
    arglist = get_args(argument_file_name)
    command = arglist.pop(0)
    command_str = [ '"' + i +'"' for i in command]
    command_str = '[' + ','.join(command_str) + ']'
    print(arglist)
    transformed = ['"--' +str(i[0]) + '=' + str(i[1]) + '"'  for i in arglist]
    print(','.join(transformed))
    tranformed_str = '['+','.join(transformed) + ']'
    with open(f'{input_file_name}', 'r') as f:
        ogfile = yaml.load(f)
    
    ogfile['spec']['templates'][2]['resource']['manifest'] = ogfile['spec']['templates'][2]['resource']['manifest'].format(command=command_str, args=tranformed_str)
    
    
    with open(f"{output_file_name}", "w") as f:
        #yaml.dump(ogfile, f, default_flow_style=False)
        yaml.dump(ogfile, f) 

if __name__ == "__main__":
    generate_yaml('new-training.yaml', 'my_file.yaml', 'sample-args.txt')
