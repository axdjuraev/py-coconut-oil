from typing import TypeAlias

from src.application.exceptions import ApplicationError
from src.domain.models import OutObjSchema
from src.domain.models import ObjCreationSchema
from src.application.common import DirectPassCreate
from .repo_binded import RepoBindedApp


class UpdateObjDTO(ObjCreationSchema):
    id: int


class UpdateObj(
    RepoBindedApp, 
    DirectPassCreate[UpdateObjDTO, OutObjSchema],
):
    DTO: TypeAlias = UpdateObjDTO 

    async def __call__(self, data: 'DTO'):
        if await self.cd.uow.repo.binary.get(data.binary_id) is None:
            raise ApplicationError(details=f"Binary data not found!")

        if (ids := await self.cd.uow.repo.tag.all_non_existence_by_ids(data.tags_id)):
            raise ApplicationError(details=f"Current tags not found: {ids}")

        await self.cd.uow.repo.obj_tags.delete_all_by_obj_id(data.id)
        await self.cd.uow.repo.obj_tags.add_all_by_obj_id(data.id, data.tags_id)
        res = await self.cd.uow.repo.obj.update(
            self.cd.uow.repo.obj.OSchema(
                **data.model_dump(),
                created_by_id=data.user_id,
            )
        )

        return res
