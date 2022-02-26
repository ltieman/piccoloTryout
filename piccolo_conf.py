from piccolo.engine.sqlite import SQLiteEngine
from piccolo.conf.apps import AppRegistry
DB = SQLiteEngine(path='piccolo.sqlite')
APP_REGISTRY = AppRegistry(
    apps=["piccolo_admin.piccolo_app"]
)