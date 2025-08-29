class DNA: 

    def __init__(self, dna):
        dna = dna.upper()
        if not self._validate(dna):
            raise ValueError("Invalid data")
        self.dna = dna

    def _validate(self, dna): 
        allowed = {'A', 'T', 'C', 'G', 'N'}  
        return all(base in allowed for base in dna)

    def getDna(self): 
        return self.dna
    
    def genome_length(self): 
        return len(self.dna)
    
