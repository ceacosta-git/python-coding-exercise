def count_duplicates(items):
    if items is None:
        raise ValueError('You must pass a non-null array')
    counts = {}
    for item in items:
        value = 1 if counts.get(item) is None else counts.get(item) + 1
        counts[item] = value
        # counts.update({item: value})
        # counts.update([(item, value)])
    return counts
