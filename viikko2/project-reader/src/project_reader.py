from urllib import request
from project import Project
import tomllib

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = tomllib.loads(content)
        dtp = data["tool"]["poetry"]

        return Project(dtp["name"], dtp["description"], dtp["license"], dtp["authors"], dtp["dependencies"], dtp["group"]["dev"]["dependencies"])
