from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.application.exceptions import ApplicationError
from src.domain.models.auth import LoginSchema
from src.utils.di_types import IDependency
from src.utils.web.injected_router import InjectedAPIRouter
from src.application import auth as application
from . import schemas


router = InjectedAPIRouter()


@router.post('/register/', response_model=None, status_code=status.HTTP_201_CREATED)
async def signup(
    data: schemas.RegisterRequestSchema,
    action: IDependency[application.CreateAuth],
):
    try:
        await action(
            action.DTO(
                **data.model_dump(),
            )
        )
    except ApplicationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.details)


@router.post('/login/', response_model=LoginSchema)
async def signin(
    *,
    form: OAuth2PasswordRequestForm = Depends(),
    action: IDependency[application.Login],
):
    try:
        res = await action(
            action.DTO(
                email=form.username,
                password=form.password,
            )
        )

        if res is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        return res
    except ApplicationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.details)


@router.post('/refresh/', response_model=LoginSchema)
async def refresh(
    refresh_token: str,
    action: IDependency[application.Refresh],
):
    try:
        return await action(
            action.DTO(
                token=refresh_token,
            )
        )
    except ApplicationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.details)
