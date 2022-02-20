
from talos import DistributeScan

p = {
    'first_neuron': [12, 24],
    'activation': ['relu', 'elu'],
    'batch_size': [10, 20]
}
d=DistributeScan(params=p,config_path='config.json',file_path="talos_test.py")
print(d.distributed_run(run_local=True))


