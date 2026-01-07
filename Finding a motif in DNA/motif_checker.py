def check_motif_in_sequence(sequence: str, motif: str) -> int:
    """
    Function provides the index of the first occurrence of a provided motif within a given sequence.
    If the motif is not found, the function returns -1.
    
    Parameters:
        sequence (str): The sequence in which to search for the motif.
        motif (str): The motif to search for within the sequence.

    Requirements: 
        Only one occurrence of the motif is expected in the sequence.

    Returns:
        int: The index of the first occurrence of the motif in the sequence, or -1 if not found.

    Time Complexity: O(n*m), n = length of sequence, m = length of motif
    Space Complexity: O(1)
    """

    return sequence.upper().find(motif.upper())

def check_motif_positions(sequence: str, motif: str) -> list:
    """
    Function provides a list of all occurrences of a provided motif within a given sequence.
    
    Parameters:
        sequence (str): The sequence in which to search for the motif.
        motif (str): The motif to search for within the sequence.

    Requirements: 
        None.

    Returns:
        list: A list of starting indices of all occurrences of the motif in the sequence.

    Time Complexity: O(n*m), n = length of sequence, m = length of motif

    Space Complexity: O(1)
    """

    pos = []

    seq = sequence.upper()
    mot = motif.upper()


    strt = 0
    
    while True:
        idx = seq.find(mot, strt)
        if idx == -1:
            break
        pos.append(idx + 1)
        strt = idx + 1
    return pos
            

