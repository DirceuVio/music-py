from music_py.scales import NOTES, scale


def _minor(key_chord):
    note, _ = key_chord.split('m')
    if '+' in key_chord:
        tonic, third, fifth = triade(note, 'minor')
        notes = [tonic, third, semitom(fifth, interval=1)]
        degrees = ['I', 'III-', 'V+']
    else:
        notes = triade(note, 'minor')
        degrees = ['I', 'III-', 'V']
    return notes, degrees


def semitom(note, interval):
    position = NOTES.index(note) + interval
    return NOTES[position % 12]


def triade(note, tonality):
    degrees = (0, 2, 4)
    scale_notes, _ = scale(note, tonality).values()
    return [scale_notes[degree] for degree in degrees]


def chord(key_chord):
    """
    Examples:
        >>> chord('C')
        {'notes': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}
    """

    if 'm' in key_chord:
        notes, degrees = _minor(key_chord)
    elif '°' in key_chord:
        note, _ = key_chord.split('°')
        tonic, third, fifth = triade(note, 'minor')
        notes = [tonic, third, semitom(fifth, interval=-1)]
        degrees = ['I', 'III-', 'V-']
    elif '+' in key_chord:
        note, _ = key_chord.split('+')
        tonic, third, fifth = triade(note, 'major')
        notes = [tonic, third, semitom(fifth, interval=1)]
        degrees = ['I', 'III-', 'V+']
    else:
        notes = triade(key_chord, 'major')
        degrees = ['I', 'III', 'V']

    return {'notes': notes, 'degrees': degrees}
