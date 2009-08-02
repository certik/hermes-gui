import os

from enthought.resource.resource_path import resource_path
from enthought.pyface.image_resource import ImageResource

def image_resource(path):
    return ImageResource(path, search_path=[search_path])

def get_data_dir():
    return data_path

def _find_data_path():
    return os.path.join(core_path, "..", "..", "data")

core_path = resource_path()
data_path = _find_data_path()
search_path = os.path.join(core_path, "images")

