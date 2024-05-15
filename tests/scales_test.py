from pytest import mark, raises

from music_py.scale import NOTES, SCALES, scale


def test_works_lowercase():

    tonic = 'c'
    tonality = 'major'

    result = scale(tonic, tonality)

    assert result


def test_return_non_existent_tonic_error():
    tonic = 'X'
    tonality = 'major'
    error_message = (
        f'This tonic does not exist. You need to try one of these {NOTES}'
    )
    with raises(ValueError) as error:
        scale(tonic, tonality)
    assert error.value.args[0] == error_message


def test_return_non_existent_scale_error():
    tonic = 'c'
    tonality = 'minor'
    error_message = f'This scale wasn not implemented yet. You need to try one of these {SCALES.keys()}'
    with raises(KeyError) as error:
        scale(tonic, tonality)
    assert error.value.args[0] == error_message


@mark.parametrize(
    'tonic,test_result',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_should_return_correct_notes(tonic, test_result):
    result = scale(tonic, 'major')
    assert result['notes'] == test_result


def test_should_return_7_degrees():
    tonic = 'c'
    tonality = 'major'

    test_result = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    result = scale(tonic, tonality)

    assert result['degrees'] == test_result
