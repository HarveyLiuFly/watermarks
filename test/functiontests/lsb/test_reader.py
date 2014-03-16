import os

from nose.tools import assert_equal
from PIL import Image

from watermarker.core.readers.lsb import Lsb
import generate_test_cases
from . import WM1_1, WM1_255


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
DST_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'tmp')


def setup_module():
    if not os.path.exists(DST_DIR):
        os.mkdir(DST_DIR)
    generate_test_cases.main()


def run_and_assert(filename, wm_data):
    base, ext = os.path.splitext(filename)
    filepath = os.path.join(DATA_DIR, filename)
    reader = Lsb([filepath], DST_DIR, ext.lstrip('.'))
    reader.run()
    src_img = Image.open(filepath)
    len_bands = len(src_img.getbands())
    for band_index in xrange(len_bands):
        res_filename = '%s_%d%s' % (base, band_index, ext)
        res_filepath = os.path.join(DST_DIR, res_filename)
        res_img = Image.open(res_filepath)
        res_img.load()
        assert_equal(list(res_img.getdata()), wm_data)


def test_g_gif():
    run_and_assert('shape1-g.gif', WM1_255)


def test_g_l0_png():
    run_and_assert('shape1-g-l0.png', WM1_255)


def test_g_l9_png():
    run_and_assert('shape1-g-l9.png', WM1_255)


#def test_rgb_16_1555_bmp():
#    run_and_assert('shape1-rgb-16-1555.bmp', WM1_255)


def test_rgb_l0_png():
    run_and_assert('shape1-rgb-l0.png', WM1_255)


def test_rgb_l9_png():
    run_and_assert('shape1-rgb-l9.png', WM1_255)


def test_gen_l_bmp():
    run_and_assert('gen-g.bmp', WM1_255)


def test_gen_l_gif():
    run_and_assert('gen-g.gif', WM1_255)


def test_gen_l_png():
    run_and_assert('gen-g.png', WM1_255)


def test_gen_rgb_bmp():
    run_and_assert('gen-rgb.bmp', WM1_255)


def test_gen_rgb_png():
    run_and_assert('gen-rgb.png', WM1_255)
