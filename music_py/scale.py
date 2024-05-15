NOTES = 'C C# D D# E F F# G G# A A# B'.split()
SCALES = {'major': (0, 2, 4, 5, 7, 9, 11)}


def scale(tonic: str, tonality: str) -> dict[str : list[str]]:
    """
    Generates a scale from a tonic and tonality

    Parameters:
        tonic: Tonic note of the scale
        tonality: Scales' tonality

    Returns:
        A dict with with scale and its degrees

    Raises:
        ValueError: Case tonic is not in NOTES
        KeyError: Case scale does not exists or was not implemented

    Examples:
        >>> scale('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('a', 'major')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    try:
        intervals: str = SCALES[tonality.lower()]
        tonic_index: str = NOTES.index(tonic.upper())
    except ValueError:
        raise ValueError(
            f'This tonic does not exist. You need to try one of these {NOTES}'
        )
    except KeyError:
        raise KeyError(
            f'This scale wasn not implemented yet. You need to try one of these {SCALES.keys()}'
        )

    return {
        'notes': [
            NOTES[(interval + tonic_index) % 12] for interval in intervals
        ],
        'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
