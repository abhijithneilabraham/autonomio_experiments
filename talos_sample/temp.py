from talos import DistributeScan

p = {'first_neuron': [12, 24],
     'activation': ['relu', 'elu'], 
     'batch_size': [10, 20]}

d = DistributeScan(
    params=p,
    config='config.json',
    file_path='talos_test.py',
    experiment_name='diabetes_exp',
)

print(d.distributed_run(run_central_node=False,
                        show_results=True))
