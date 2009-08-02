import os

from enthought.resource.resource_path import resource_path
from enthought.pyface.image_resource import ImageResource

def image_resource(path):
    return ImageResource(path, search_path=[search_path])

def get_data_dir():
    return data_path

def _find_data_path():
    p = os.path.join(core_path, "..", "..", "data")
    if os.path.exists(p):
        return p
    p = os.path.join(core_path, "..", "..", "..", "..",
        "share", "hermesgui", "data")
    if os.path.exists(p):
        return p
    p = os.path.join(core_path, "..", "..", "..", "..", "..",
        "share", "hermesgui", "data")
    if os.path.exists(p):
        return p
    raise Exception("Can't find the data directory")

core_path = resource_path()
data_path = _find_data_path()
search_path = os.path.join(core_path, "images")

