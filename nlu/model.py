import yaml
import numpy as np

data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs,outputs = [],[]

for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}\{}'.format(command['entity'], command['action']))

#Processar texto: plavras, categorias, ...

max_seq = max([len(bytes(x.encode('utf-8'))) for x in inputs])

print('Maior seq:', max_seq)


#Criando dataset
