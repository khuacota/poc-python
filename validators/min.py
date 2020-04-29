def min(num):
    def decorator(function):
        def wrapper(self, score, *args, **kwargs):
            if score < num:
                raise Exception('Value invalid')
            function(self, score, *args, **kwargs)
        return wrapper
    return decorator
