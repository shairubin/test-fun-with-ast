
@dataclasses.dataclass(frozen=True)
class ODictGetItemSource(ChainedSource):
    def name(self):
        if isinstance(self.index, type):
            rep = f'__load_module("{self.index.__module__}").{self.index.__qualname__}'
            return f"___odict_getitem({self.base.name()}, {rep})"



