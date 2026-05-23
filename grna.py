from analysis import calculate_gc_content

# PAM sequence = NGG
PAM = "GG"

def find_grna_targets(sequence):

    results = []

    # Scan sequence
    for i in range(len(sequence) - 23):

        target = sequence[i:i+20]
        pam = sequence[i+20:i+23]

        # Check PAM sequence
        if pam.endswith(PAM):

            gc = calculate_gc_content(target)

            # Efficiency Classification
            if 40 <= gc <= 60:
                efficiency = "High"

            elif gc >= 30:
                efficiency = "Medium"

            else:
                efficiency = "Low"

            results.append({
                "Target": target,
                "PAM": pam,
                "GC_Content": round(gc, 2),
                "Efficiency": efficiency
            })

    return results


