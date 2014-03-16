import os

from nose.tools import assert_equal
from PIL import Image

from watermarker.core.writers.lsb import Lsb
#import generate_test_cases
from . import WM1_WM


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
DST_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'tmp')


def run_and_assert(filename, wm_filename, wm_data):
    base, ext = os.path.splitext(filename)
    filepath = os.path.join(DATA_DIR, filename)
    wm_filepath = os.path.join(DATA_DIR, wm_filename)
    writer = Lsb([filepath], DST_DIR, ext.lstrip('.'), wm_filepath)
    writer.run()
    src_img = Image.open(filepath)
    res_filename = '%s_watermarked%s' % (base, ext)
    res_filepath = os.path.join(DST_DIR, res_filename)
    res_img = Image.open(res_filepath)
    res_img.load()
    for band in res_img.split():
        assert_equal(list(band.getdata()), wm_data)


def test_g_gif():
    run_and_assert('shape1-g.gif', 'wm-png-24-16b.png', WM1_WM)


def test_g_l0_png():
    run_and_assert('shape1-g-l0.png', 'wm-png-24-16b.png', WM1_WM)


def test_g_l9_png():
    run_and_assert('shape1-g-l9.png', 'wm-png-24-16b.png', WM1_WM)


#def test_rgb_16_1555_bmp():
#    run_and_assert('shape1-rgb-16-1555.bmp', 'wm-png-24-16b.png', WM1_WM)


def test_rgb_l0_png():
    run_and_assert('shape1-rgb-l0.png', 'wm-png-24-16b.png', WM1_WM)


def test_rgb_l9_png():
    run_and_assert('shape1-rgb-l9.png', 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_bmp():
    run_and_assert('gen-g.bmp', 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_gif():
    run_and_assert('gen-g.gif', 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_png():
    run_and_assert('gen-g.png', 'wm-png-24-16b.png', WM1_WM)


def test_gen_rgb_bmp():
    run_and_assert('gen-rgb.bmp', 'wm-png-24-16b.png', WM1_WM)


def test_gen_rgb_png():
    run_and_assert('gen-rgb.png', 'wm-png-24-16b.png', WM1_WM)
