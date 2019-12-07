
def remap(*args, **kwargs):
    
    def find_methods(clazz, field_name):
        field = getattr(clazz, field_name)
        result = [entry for entry in dir(field) if not entry.startswith("__")]
        return result

    def decorator(clazz):
        
        return clazz

    return decorator

