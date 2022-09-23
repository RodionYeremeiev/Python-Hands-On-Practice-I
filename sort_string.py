def sort_string(phrase: str):
    return ' '.join(sorted(phrase.split(), key=str.casefold))
