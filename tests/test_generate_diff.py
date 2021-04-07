import os
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    test_file1 = os.path.abspath('tests/fixtures/test_file1.json')
    test_file2 = os.path.abspath('tests/fixtures/test_file2.json')
    assert generate_diff(test_file1, test_file2) == \
           '{\n' \
           '  - key1: text1\n' \
           '  - key2: text2\n' \
           '  + key2: text2_updated\n' \
           '  + key3: text3\n' \
           '    key4: text4\n' \
           '}'
