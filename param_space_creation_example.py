# from talos.parameters import ParamSpace
p = {
    'first_neuron': [12,20, 24],
    'activation': ['relu', 'elu'],
    'batch_size': [10, 20]
}

def create_param_space(params):

    from talos.parameters.ParamSpace import ParamSpace
    param_keys=params.keys()
    param_grid= ParamSpace(params, param_keys)._param_space_creation()
    def __column(matrix, i):
        return [row[i] for row in matrix]
    new_params={k:[] for k in param_keys}
    for key_index,key in enumerate(param_keys):
        new_params[key]=__column(param_grid,key_index)
    def __split_params(n_splits=2):
        d=new_params
        dicts=[{} for i in range(n_splits)]
        def _chunkify(lst,n):
          return [lst[i::n] for i in range(n)]
        for k,v in d.items():
            for i in range(n_splits):
                dicts[i][k]=_chunkify(v, n_splits)[i]
        return dicts
    new_params=__split_params()
    return new_params
        

print(create_param_space(p))