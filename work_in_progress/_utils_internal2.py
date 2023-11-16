
def throw_abstract_impl_not_imported_error(opname, module, context):
    if module in sys.modules:
        pass
    else:
        raise NotImplementedError(
            f"{opname}: We could not find the abstract impl for this operator. "
            f"The operator specified that you may need to import the '{module}' "
            f"Python module to load the abstract impl. {context}"
        )
