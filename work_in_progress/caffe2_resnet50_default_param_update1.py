def gen_param_update_builder_fun(self, model, dataset, is_train):
        def add_parameter_update_ops(model):
            model.AddWeightDecay(1e-4)
        return add_parameter_update_ops
