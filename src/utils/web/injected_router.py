from fastapi import APIRouter
from dishka.integrations.fastapi import inject


class InjectedAPIRouter(APIRouter):
    def route(self, path, *args, **kwargs):
        def decorator(func):
            func = inject(func)
            return self.add_route(path, func, *args, **kwargs)
        
        return decorator

    def api_route(self, path, *args, **kwargs):
        def decorator(func):
            func = inject(func)
            return self.add_api_route(path, func, *args, **kwargs)
        
        return decorator
