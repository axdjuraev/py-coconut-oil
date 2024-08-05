from axabc.db import BaseRepoCollector
from src.database import repository as repo


class RepoCollection(BaseRepoCollector):
    users: repo.UsersRepository
    tag: repo.TagRepository
    binary: repo.BinaryRepository
    obj: repo.ObjRepository
    obj_tags: repo.ObjTagsRepository
