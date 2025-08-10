import os
import pytest
from algokraken.sprint_2.final_a.solution import main
from algokraken.tools.parsers import read_file_content

TASK_NAME = 'final_a'
SPRINT_NAME = 'sprint_2'
PROJECT_NAME = 'algokraken'

def get_fixture_path(file_name: str) -> str:
    return os.path.join(os.getcwd(), PROJECT_NAME, SPRINT_NAME, TASK_NAME,  file_name)


@pytest.mark.parametrize(
    'file_input, file_output, file_expected',
    [
        ['input.txt', 'output.txt', 'expected.txt'],
        ['input_2.txt', 'output_2.txt', 'expected_2.txt'],
        ['input_3.txt', 'output_3.txt', 'expected_3.txt'],
    ]
)
def test(file_input, file_output, file_expected):
    path_input = get_fixture_path(file_input)
    path_output = get_fixture_path(file_output)
    path_expected = get_fixture_path(file_expected)
    
    main(path_input, path_output)
    assert read_file_content(path_output) == read_file_content(path_expected)
