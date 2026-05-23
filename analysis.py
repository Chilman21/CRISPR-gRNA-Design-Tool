def calculate_gc_content(sequence):

    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_count = (
        (g_count + c_count) / len(sequence)
    ) * 100

    return round(gc_count, 2)
