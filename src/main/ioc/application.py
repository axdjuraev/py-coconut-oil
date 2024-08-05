from dishka import Scope, provide

from src.application import binary as binary_app
from src.application import auth as auth_app
from src.application import obj as obj_app
from src.application import tags as tags_app
from .base import BaseIoCProvider


class ApplicationIoCProvider(BaseIoCProvider):
    create_obj = provide(obj_app.CreateObj, scope=Scope.REQUEST)
    update_obj = provide(obj_app.UpdateObj, scope=Scope.REQUEST)
    get_obj_page = provide(obj_app.GetObjPage, scope=Scope.REQUEST)
    get_obj_by_id = provide(obj_app.GetObjByID, scope=Scope.REQUEST)
    delete_obj_by_id = provide(obj_app.DeleteObjByID, scope=Scope.REQUEST)

    create_tags = provide(tags_app.CreateTag, scope=Scope.REQUEST)
    get_tags_page = provide(tags_app.GetTagPage, scope=Scope.REQUEST)
    get_tags_by_id = provide(tags_app.GetTagByID, scope=Scope.REQUEST)
    delete_tags_by_id = provide(tags_app.DeleteTagByID, scope=Scope.REQUEST)

    create_binary = provide(binary_app.CreateBinary, scope=Scope.REQUEST)
    get_binary_by_id = provide(binary_app.GetBinaryByID, scope=Scope.REQUEST)
    get_binary_data = provide(binary_app.GetBinaryData, scope=Scope.REQUEST)
    delete_binary_by_id = provide(binary_app.DeleteBinaryByID, scope=Scope.REQUEST)

    create_auth = provide(auth_app.CreateAuth, scope=Scope.REQUEST)
    login_auth = provide(auth_app.Login, scope=Scope.REQUEST)
    refresh_auth = provide(auth_app.Refresh, scope=Scope.REQUEST)
