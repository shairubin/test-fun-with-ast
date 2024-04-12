



class TritonBenchmarkRequest(BenchmarkRequest):

    def __str__(self) -> str:
        return f"{self.kernel_name=}, {self.module_path=}, {self.module_cache_key=}"

