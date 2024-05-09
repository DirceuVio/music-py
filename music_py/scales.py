NOTES = 'C C# D D# E F F# G G# A A# B'.split()
SCALES = {'major': (0, 2, 4, 5, 7, 9, 11)}


def scales(tonic: str, tonality: str) -> dict[str: list[str]]:
    """
    Generates a scale from a tonic and tonality

    Parameters:
        tonic: Tonic note of the scale
        tonality: Scales' tonality
    
    Returns:
        A dict with with scale and its degrees

    Examples:
        >>> scales('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scales('A', 'major')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """

    intervals = SCALES[tonality]
    tonic_index = NOTES.index(tonic)

    return {
        'notes': [
            NOTES[(interval + tonic_index) % 12] for interval in intervals
        ],
        'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
