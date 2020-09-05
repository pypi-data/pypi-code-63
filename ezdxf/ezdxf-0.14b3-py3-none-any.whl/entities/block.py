# Copyright (c) 2019-2020 Manfred Moitzi
# License: MIT License
# Created 2019-02-18
from typing import TYPE_CHECKING
from ezdxf.lldxf import validator
from ezdxf.lldxf.attributes import (
    DXFAttr, DXFAttributes, DefSubclass, XType, RETURN_DEFAULT,
)
from ezdxf.lldxf.const import (
    SUBCLASS_MARKER, DXF12, MODEL_SPACE_R12, PAPER_SPACE_R12, MODEL_SPACE_R2000,
    PAPER_SPACE_R2000,
)
from ezdxf.math import NULLVEC
from .dxfentity import base_class, SubclassProcessor, DXFEntity
from .factory import register_entity

if TYPE_CHECKING:
    from ezdxf.eztypes import TagWriter, DXFNamespace

__all__ = ['Block', 'EndBlk']

acdb_entity = DefSubclass('AcDbEntity', {
    # No auto fix for invalid layer names!
    'layer': DXFAttr(8, default='0', validator=validator.is_valid_layer_name),
    'paperspace': DXFAttr(
        67, default=0, optional=True,
        validator=validator.is_integer_bool,
        fixer=RETURN_DEFAULT,
    ),

})

acdb_block_begin = DefSubclass('AcDbBlockBegin', {
    'name': DXFAttr(2, validator=validator.is_valid_block_name),
    # The 2nd name with group code 3 is handles internally, and is not an
    # explict DXF attribute.
    'description': DXFAttr(4, default='', optional=True),

    # Flags:
    # 0 = Indicates none of the following flags apply
    # 1 = This is an anonymous block generated by hatching, associative
    #     dimensioning, other internal operations, or an application
    # 2 = This block has non-constant attribute definitions (this bit is not set
    #     if the block has any attribute definitions that are constant, or has
    #     no attribute definitions at all)
    # 4 = This block is an external reference (xref)
    # 8 = This block is an xref overlay
    # 16 = This block is externally dependent
    # 32 = This is a resolved external reference, or dependent of an external
    #      reference (ignored on input)
    # 64 = This definition is a referenced external reference (ignored on input)
    'flags': DXFAttr(70, default=0),
    'base_point': DXFAttr(10, xtype=XType.any_point, default=NULLVEC),
    'xref_path': DXFAttr(1, default=''),
})

MODEL_SPACE_R2000_LOWER = MODEL_SPACE_R2000.lower()
MODEL_SPACE_R12_LOWER = MODEL_SPACE_R12.lower()
PAPER_SPACE_R2000_LOWER = PAPER_SPACE_R2000.lower()
PAPER_SPACE_R12_LOWER = PAPER_SPACE_R12.lower()


@register_entity
class Block(DXFEntity):
    """ DXF BLOCK entity """
    DXFTYPE = 'BLOCK'
    DXFATTRIBS = DXFAttributes(base_class, acdb_entity, acdb_block_begin)
    
    # Block entity flags:
    # This is an anonymous block generated by hatching, associative
    # dimensioning, other internal operations, or an application:
    ANONYMOUS = 1

    # This block has non-constant attribute definitions (this bit is not set
    # if the block has any attribute definitions that are constant, or has no
    # attribute definitions at all):
    NON_CONSTANT_ATTRIBUTES = 2

    # This block is an external reference:
    XREF = 4

    # This block is an xref overlay:
    XREF_OVERLAY = 8

    # This block is externally dependent:
    EXTERNAL = 16

    # This is a resolved external reference, or dependent of an external reference:
    RESOLVED = 32

    # This definition is a referenced external reference:
    REFERENCED = 64

    def load_dxf_attribs(self,
                         processor: SubclassProcessor = None) -> 'DXFNamespace':
        dxf = super().load_dxf_attribs(processor)
        if processor is None:
            return dxf

        processor.load_dxfattribs_into_namespace(dxf, acdb_entity)
        processor.load_dxfattribs_into_namespace(dxf, acdb_block_begin)
        if processor.r12:
            if dxf.name.lower() == MODEL_SPACE_R12_LOWER:
                dxf.name = MODEL_SPACE_R2000
            elif dxf.name.lower() == PAPER_SPACE_R12_LOWER:
                dxf.name = PAPER_SPACE_R2000
        return dxf

    def export_entity(self, tagwriter: 'TagWriter') -> None:
        """ Export entity specific data as DXF tags. """
        super().export_entity(tagwriter)

        if tagwriter.dxfversion > DXF12:
            tagwriter.write_tag2(SUBCLASS_MARKER, acdb_entity.name)
        if self.dxf.hasattr('paperspace'):
            tagwriter.write_tag2(67, 1)
        self.dxf.export_dxf_attribs(tagwriter, 'layer')
        if tagwriter.dxfversion > DXF12:
            tagwriter.write_tag2(SUBCLASS_MARKER, acdb_block_begin.name)

        name = self.dxf.name
        if tagwriter.dxfversion == DXF12:
            # export modelspace and paperspace with leading '$' instead of '*'
            if name.lower() == MODEL_SPACE_R2000_LOWER:
                name = MODEL_SPACE_R12
            elif name.lower() == PAPER_SPACE_R2000_LOWER:
                name = PAPER_SPACE_R12

        tagwriter.write_tag2(2, name)
        self.dxf.export_dxf_attribs(tagwriter, ['flags', 'base_point'])
        tagwriter.write_tag2(3, name)
        self.dxf.export_dxf_attribs(tagwriter, ['xref_path', 'description'])

    @property
    def is_layout_block(self) -> bool:
        """ Returns ``True`` if this is a :class:`~ezdxf.layouts.Modelspace` or
        :class:`~ezdxf.layouts.Paperspace` block definition.
        """
        name = self.dxf.name.lower()
        return name.startswith('*model_space') or name.startswith(
            '*paper_space')

    @property
    def is_anonymous(self) -> bool:
        """ Returns ``True`` if this is an anonymous block generated by
        hatching, associative dimensioning, other internal operations, or an
        application.

        """
        return self.get_flag_state(Block.ANONYMOUS)

    @property
    def is_xref(self) -> bool:
        """ Returns ``True`` if bock is an external referenced file."""
        return self.get_flag_state(Block.XREF)

    @property
    def is_xref_overlay(self) -> bool:
        """ Returns ``True`` if bock is an external referenced overlay file. """
        return self.get_flag_state(Block.XREF_OVERLAY)


acdb_block_end = DefSubclass('AcDbBlockEnd', {})


@register_entity
class EndBlk(DXFEntity):
    """ DXF ENDBLK entity """
    DXFTYPE = 'ENDBLK'
    DXFATTRIBS = DXFAttributes(base_class, acdb_entity, acdb_block_end)

    def load_dxf_attribs(self,
                         processor: SubclassProcessor = None) -> 'DXFNamespace':
        dxf = super().load_dxf_attribs(processor)
        if processor is None:
            return dxf

        processor.load_dxfattribs_into_namespace(dxf, acdb_entity)
        processor.load_dxfattribs_into_namespace(dxf, acdb_block_end)
        return dxf

    def export_entity(self, tagwriter: 'TagWriter') -> None:
        """ Export entity specific data as DXF tags. """
        super().export_entity(tagwriter)

        if tagwriter.dxfversion > DXF12:
            tagwriter.write_tag2(SUBCLASS_MARKER, acdb_entity.name)
        if self.dxf.hasattr('paperspace'):
            tagwriter.write_tag2(67, 1)
        self.dxf.export_dxf_attribs(tagwriter, 'layer')
        if tagwriter.dxfversion > DXF12:
            tagwriter.write_tag2(SUBCLASS_MARKER, acdb_block_end.name)
