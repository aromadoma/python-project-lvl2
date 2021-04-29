import os
from gendiff.scripts.gendiff import generate_diff


def test_stylish_diff():
    test_file1 = os.path.abspath('tests/fixtures/file1.yml')
    test_file2 = os.path.abspath('tests/fixtures/file2.yml')
    with open(os.path.abspath('tests/fixtures/result_stylish')) as result:
        assert generate_diff(test_file1, test_file2) == result.read()


def test_plain_diff():
    test_file1 = os.path.abspath('tests/fixtures/file1.yml')
    test_file2 = os.path.abspath('tests/fixtures/file2.yml')
    with open(os.path.abspath('tests/fixtures/result_plain')) as result:
        assert generate_diff(test_file1, test_file2, view='plain') == result.read()


def test_json_diff():
    test_file1 = os.path.abspath('tests/fixtures/test_file_complex1.json')
    test_file2 = os.path.abspath('tests/fixtures/test_file_complex2.yml')
    with open(os.path.abspath('tests/fixtures/json_view')) as result:
        assert generate_diff(test_file1, test_file2, view='json') == result.read()
