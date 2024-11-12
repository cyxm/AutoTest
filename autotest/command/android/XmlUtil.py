# encoding=UTF-8
import xml.etree.ElementTree as Et
from xml.etree.ElementTree import ElementTree

from typing_extensions import Buffer


class XmlUtil:
    XML_HEAD = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"

    @classmethod
    def genContentAddHead(cls, content: Buffer):
        return cls.XML_HEAD.encode() + content

    @classmethod
    def toTree(cls, content: bytes):
        return Et.ElementTree(Et.fromstring(content))

    @classmethod
    def fromTree(cls, tree: ElementTree) -> bytes:
        return Et.tostring(tree.getroot())

    @classmethod
    def fromTreeWithHead(cls, tree: ElementTree) -> bytes:
        return cls.genContentAddHead(cls.fromTree(tree))
