import inspect
from copy import copy
from typing import Iterable
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from src.domain.services.auth.base import AuthSystemService
from src.domain.types import CommonDependency
from src.utils.di_types import IDependency
from src.utils.web.injected_router import InjectedAPIRouter


OAuthSchema = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/")


def local_request(request: Request):
    return request


class AuthBaseAPIRouter(InjectedAPIRouter):
    NON_SECURE_METHODS = ['GET']

    def api_route(self, path, *args, methods=None, **kwargs):
        for m in self.NON_SECURE_METHODS:
            if [m] == methods:
                return super().api_route(path, *args, methods=methods, **kwargs)

        def decorator(func):
            inner_decorator = super(self.__class__, self).api_route(path, *args, methods=methods, **kwargs)
            func = self.patch_with_wrapper_params(func)
            return inner_decorator(func)

        return decorator 
    
    def patch_with_wrapper_params(
        self, 
        func, 
        except_wrapper_params: Iterable[str] = tuple(),
    ):
        async def wrapper(
            *args, 
            cd: IDependency[CommonDependency],
            local_request = Depends(local_request),
            auth_system: IDependency[AuthSystemService],
            token: str = Depends(OAuthSchema),
            **kwargs,
        ):
            try:
                email = auth_system.get_token_data(token)
            except Exception:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

            user = await cd.uow.repo.users.get_by_email(email)

            if user is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

            local_request.state.user = user

            return await func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        except_wrapper_params = set(except_wrapper_params) | {'func', 'args', 'kwargs'}
        func_signature = inspect.signature(func)
        patched_wrapper_signature = inspect.signature(wrapper)

        all_params = (
            *filter(
                lambda p: p.name not in except_wrapper_params,
                patched_wrapper_signature.parameters.values(),
            ),
            *func_signature.parameters.values(), 
        )
        all_annotations = func.__annotations__.copy()
        all_annotations.update({
            k: v
            for k, v in wrapper.__annotations__.items()
            if k not in except_wrapper_params
        })

        res = copy(wrapper)
        res.__signature__ = patched_wrapper_signature.replace(parameters=all_params)
        res.__annotations__ = all_annotations

        return res
