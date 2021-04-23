import os
from gendiff.gendiff import generate_diff


def test_stylish_diff():
    test_file1 = os.path.abspath('tests/fixtures/test_file_complex1.json')
    test_file2 = os.path.abspath('tests/fixtures/test_file_complex2.yml')
    with open(os.path.abspath('tests/fixtures/stylish_view')) as result:
        assert generate_diff(test_file1, test_file2, view='stylish') == result.read()


def test_plain_diff():
    test_file1 = os.path.abspath('tests/fixtures/test_file_complex1.json')
    test_file2 = os.path.abspath('tests/fixtures/test_file_complex2.yml')
    with open(os.path.abspath('tests/fixtures/plain_view')) as result:
        assert generate_diff(test_file1, test_file2, view='plain') == result.read()


def test_json_diff():
    test_file1 = os.path.abspath('tests/fixtures/test_file_complex1.json')
    test_file2 = os.path.abspath('tests/fixtures/test_file_complex2.yml')
    with open(os.path.abspath('tests/fixtures/json_view')) as result:
        assert generate_diff(test_file1, test_file2, view='json') == result.read()
