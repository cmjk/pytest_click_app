import pytest
from click.testing import CliRunner
from pathlib import Path
from upper_case_file import upper_case_file

data_dir = Path(__file__).parent.parent / 'data'


@pytest.mark.parametrize("input_file", ['betty',
                                        'cross',
                                        'peter',
                                        'shell',
                                        'silence',
                                        'something',
                                        'thought',
                                        'toast',
                                        'wood',
                                        'yellow'])
def test_cli(input_file):
    runner = CliRunner()
    out_filename = f'{input_file}.txt'
    with runner.isolated_filesystem():
        with open(data_dir / f'{input_file}.output.txt', 'r') as reference:
            result = runner.invoke(
                upper_case_file, ['--input-file', data_dir / f'{input_file}.input.txt',
                                  '--output-file', out_filename])
            assert result.exit_code == 0
            with open(out_filename, 'r') as output:
                assert output.read() == reference.read()
