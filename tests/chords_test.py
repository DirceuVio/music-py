from pytest import mark

from music_py.chords import chord


@mark.parametrize(
    'note,test_result',
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('C°', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('F#', ['F#', 'A#', 'C#']),
    ],
)
def test_chord_should_return_corresponding_notes(note, test_result):
    notes, _ = chord(note).values()
    assert notes == test_result


@mark.parametrize(
    'note,test_result',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('C°', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III-', 'V+']),
    ],
)
def test_chord_should_return_corresponding_degrees(note, test_result):

    _, degrees = chord(note).values()
    assert degrees == test_result
