from fastapi import HTTPException, Request, status

from src.application import obj as application
from src.application.exceptions import ApplicationError
from src.presentation.api.v1.arouter import AuthBaseAPIRouter
from src.utils.di_types import IDependency
from src.utils import schemas as util_schemas

from . import schemas


router = AuthBaseAPIRouter()


@router.get('/', response_model=util_schemas.Page[schemas.ObjCreationResponse])
async def page(
    *, 
    page: int = 1,
    page_size: int = 10,
    getter: IDependency[application.GetObjPage],
):
    return await getter(
        getter.DTO(
            page=page,
            page_size=page_size,
        )
    )


@router.get('/{id}', response_model=schemas.ObjCreationResponse)
async def get_by_id(
    *, 
    id: int,
    getter: IDependency[application.GetObjByID],
):
    data = await getter(
        getter.DTO(
            id=id,
        )
    )

    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return data


@router.post('/', response_model=schemas.ObjCreationResponse)
async def create(
    *, 
    request: Request,
    data: schemas.ObjCreationRequest, 
    creator: IDependency[application.CreateObj],
):
    try:
        return await creator(
            creator.DTO(
                **data.model_dump(),
                user_id=request.state.user.id,
            )
        )
    except ApplicationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.details)


@router.put('/{id}', response_model=schemas.ObjCreationResponse)
async def update(
    *, 
    id: int,
    request: Request,
    data: schemas.ObjCreationRequest, 
    updater: IDependency[application.UpdateObj],
):
    try:
        return await updater(
            updater.DTO(
                **data.model_dump(),
                id=id,
                user_id=request.state.user.id,
            )
        )
    except ApplicationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.details)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def delete(
    *, 
    id: int,
    request: Request,
    getter: IDependency[application.GetObjByID],
    deleter: IDependency[application.DeleteObjByID],
):
    data = await getter(
        getter.DTO(
            id=id,
        )
    )

    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    try:
        return await deleter(
            deleter.DTO(
                user_id=request.state.user.id,
                obj=data,
            )
        )
    except ApplicationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.details)
