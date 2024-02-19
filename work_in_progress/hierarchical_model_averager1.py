


class HierarchicalModelAverager(averagers.ModelAverager):
    def __init__(self, period_group_size_dict=None, warmup_steps=0, process_group=None):
        if list(period_group_size_dict.values())[-1] != overall_group_size:
            raise ValueError(
                f"The last value in arg ``period_process_group_dict`` {list(period_group_size_dict.values())[-1]} "
                f"must be equal to the size of arg ``process_group`` {overall_group_size}."
            )
