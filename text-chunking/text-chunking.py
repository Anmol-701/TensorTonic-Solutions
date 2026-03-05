def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if not tokens:
        return []
    lst = []
    step = chunk_size - overlap

    # Special case: tokens smaller than chunk_size
    if len(tokens) <= chunk_size:
        return [tokens]

    for i in range(0, len(tokens), step):
        chunk = tokens[i:i + chunk_size]

        if len(chunk) == chunk_size:
            lst.append(chunk)
        else:
            break

    return lst