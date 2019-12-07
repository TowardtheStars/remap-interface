
def remap(*args, ___on_conflict=None, ___output_file=None, **kwargs):
    
    def find_methods(clazz, field_name):
        field = getattr(clazz, field_name)
        result = [entry for entry in dir(field) if not entry.startswith("__")]
        return result

    def decorator(clazz):
        
        return clazz

    return decorator

