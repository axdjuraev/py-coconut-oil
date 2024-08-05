from typing import TypeAlias

from src.application.exceptions import ApplicationError
from src.domain.models import OutObjSchema
from src.domain.models import ObjCreationSchema, ObjSchema
from src.application.common import DirectPassCreate
from .repo_binded import RepoBindedApp


class CreateObjDTO(ObjCreationSchema):
    pass


class CreateObj(
    RepoBindedApp, 
    DirectPassCreate[CreateObjDTO, OutObjSchema],
):
    DTO: TypeAlias = CreateObjDTO

    async def prepare_for_store(self, data: 'DTO'):
        return ObjSchema(
            **data.model_dump(),
            created_by_id=data.user_id,
        )

    async def __call__(self, data: 'DTO'):
        if await self.cd.uow.repo.binary.get(data.binary_id) is None:
            raise ApplicationError(details=f"Binary data not found!")

        if (ids := await self.cd.uow.repo.tag.all_non_existence_by_ids(data.tags_id)):
            raise ApplicationError(details=f"Current tags not found: {ids}")

        res = await super().__call__(data)
        await self.cd.uow.repo.obj_tags.add_all_by_obj_id(res.id, data.tags_id)

        return res
