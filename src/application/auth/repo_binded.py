from src.application.common import RepoBindedApp as _RepoBindedApp


class RepoBindedApp(_RepoBindedApp):
    @property
    def repo(self):
        return self.cd.uow.repo.users

