from fastapi import File, HTTPException, Request, Response, UploadFile, status

from src.application import binary as application
from src.application.exceptions import ApplicationError
from src.domain.services.file_store.minio import MinioStoreDTO
from src.presentation.api.v1.arouter import AuthBaseAPIRouter
from src.utils.di_types import IDependency
from . import schemas


router = AuthBaseAPIRouter()


@router.get('/{id}')
async def get_by_id(
    *, 
    id: int,
    getter: IDependency[application.GetBinaryByID],
    bytes_getter: IDependency[application.GetBinaryData],
):
    data = await getter(
        getter.DTO(
            id=id,
        )
    )

    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Response(await bytes_getter(data), media_type=data.content_type)


@router.post('/', response_model=schemas.BinaryCreationResponse)
async def create(
    *, 
    request: Request,
    file: UploadFile = File(...),
    creator: IDependency[application.CreateBinary],
):
    return await creator(
        creator.DTO(
            meta=MinioStoreDTO(
                filename=file.filename,
                bf=file.file,
                bf_size=file.size,
                content_type=file.content_type,
            ),
            user_id=request.state.user.id,
        )
    )


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def delete(
    *, 
    id: int,
    request: Request,
    getter: IDependency[application.GetBinaryByID],
    deleter: IDependency[application.DeleteBinaryByID],
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
