
def argumenttype_type(
    t: Type, *, mutable: bool, binds: ArgName, symint: bool
) -> NamedCType:
        return NamedCType(binds, MutRefCType(tensor_type))
