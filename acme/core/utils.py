import os

from enthought.resource.resource_path import resource_path
from enthought.pyface.image_resource import ImageResource

core_path = resource_path()
search_path = os.path.join(core_path, "..", "..", "images")

def image_resource(path):
    return ImageResource(path, search_path=[search_path])
