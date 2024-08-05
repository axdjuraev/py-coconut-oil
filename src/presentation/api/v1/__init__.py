__all__ = [
    'auth_router',
    'tags_router',
    'binary_router',
    'obj_router',
]


from .auth.routers import router as auth_router
from .tags.routers import router as tags_router
from .binary.routers import router as binary_router
from .obj.routers import router as obj_router
