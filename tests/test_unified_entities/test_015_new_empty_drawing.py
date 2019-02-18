# Copyright (c) 2019 Manfred Moitzi
# License: MIT License
# created: 2019-02-18
import pytest

from ezdxf.drawing2 import Drawing
from ezdxf.sections.objects2 import _OBJECT_TABLE_NAMES


@pytest.fixture
def doc():
    return Drawing.new()


def test_create_new_empty_drawing(doc):
    assert doc.dxfversion == 'AC1032'
    rootdict = doc.rootdict
    assert rootdict.DXFTYPE == 'DICTIONARY'
    for name in _OBJECT_TABLE_NAMES:
        assert name in rootdict


def test_section(doc):
    assert doc.header['$ACADVER'] == 'AC1032'

    e = doc.objects.get_entity_space()
    assert e[0] is doc.rootdict

    assert len(doc.blocks) == 2
    assert '*Model_Space' in doc.blocks
    assert '*Paper_Space' in doc.blocks


def test_tables(doc):
    assert len(doc.layers) == 0
    assert len(doc.views) == 0
    assert len(doc.viewports) == 0


def test_get_modelspace(doc):
    msp = doc.modelspace()
    assert len(msp) == 0
    msp.add_line((0, 0), (1, 1))
    assert len(msp) == 1
