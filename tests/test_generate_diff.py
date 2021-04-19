import os
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    test_file1 = os.path.abspath('tests/fixtures/test_file1.json')
    test_file2 = os.path.abspath('tests/fixtures/test_file2.yml')
    assert generate_diff(test_file1, test_file2) == \
        '{\n' \
        '  - key1: text1\n' \
        '  - key2: text2\n' \
        '  + key2: text2_updated\n' \
        '  + key3: text3\n' \
        '    key4: text4\n' \
        '}\n'


def test_generate_diff_2():
    test_file1 = os.path.abspath('tests/fixtures/test_file_complex1.json')
    test_file2 = os.path.abspath('tests/fixtures/test_file_complex2.yml')
    assert generate_diff(test_file1, test_file2) == \
        '{\n' \
        '    common: {\n' \
        '      + follow: False\n' \
        '        setting1: Value 1\n' \
        '      - setting2: 200\n' \
        '      - setting3: True\n' \
        '      + setting3: None\n' \
        '      + setting4: blah blah\n' \
        '      + setting5: {\n' \
        '            key5: value5\n' \
        '        }\n' \
        '        setting6: {\n' \
        '            doge: {\n' \
        '              - wow: \n' \
        '              + wow: so much\n' \
        '            }\n' \
        '            key: value\n' \
        '          + ops: vops\n' \
        '        }\n' \
        '    }\n' \
        '    group1: {\n' \
        '      - baz: bas\n' \
        '      + baz: bars\n' \
        '        foo: bar\n' \
        '      - nest: {\n' \
        '            key: value\n' \
        '        }\n' \
        '      + nest: str\n' \
        '    }\n' \
        '  - group2: {\n' \
        '        abc: 12345\n' \
        '        deep: {\n' \
        '            id: 45\n' \
        '        }\n' \
        '    }\n' \
        '  + group3: {\n' \
        '        deep: {\n' \
        '            id: {\n' \
        '                number: 45\n' \
        '            }\n' \
        '        }\n' \
        '        fee: 100500\n' \
        '    }\n' \
        '}\n'
