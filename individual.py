class Individual:

    __alelos = ['AA', 'Ai', 'BB', 'AB', 'Bi', 'ii']
    __count = 0

    def __init__(self, genotype: str, name=None):
        self.genotype = self.validate_genotype(genotype)
        self.name = self.generator_name(name, genotype)
        
        def genotypeGet(self):
            return self.genotype
        genotype = property(genotypeGet)

        def nameGet(self):
            return self.name
        name = property(nameGet)

    def __str__(self):
        return (("%s, %s") % (self.name, self.genotype))

    def validate_genotype(self,genotype: str):
        if genotype in Individual.__alelos:
            return genotype
        elif genotype not in Individual.__alelos:
            raise ValueError("Invalid genotype")

    def generator_name(self, name, genotype):
        if isinstance(name, str):
            Individual.__count += 1
            pass
        elif name is None:
                Individual.__count += 1
                name = "Indiv"+str(Individual.__count)
        elif isinstance(genotype, Individual):
            name=genotype.name
        return name
 
    def blood_type(self):
        if (self.genotype == "AA") or (self.genotype == "Ai"):
            return "A"
        elif (self.genotype == "BB") or (self.genotype == "Bi"):
            return "B"
        elif (self.genotype == "AB"):
            return "AB"
        else:
            return "O"

    blood_type = property(blood_type)

    def agglutinogens(self):
        if (self.genotype == "AA") or (self.genotype =="Ai"):
            return "A"
        elif (self.genotype == "BB") or (self.genotype == "Bi"):
            return "B"
        elif (self.genotype == "AB"):
            return "AB"
        else:
            return "Não possui"

    agglutinogens = property(agglutinogens)        

    def agglutinins(self):
        if (self.genotype == "ii"):
            return "AB"
        elif (self.genotype == "AA") or (self.genotype =="Ai"):
            return "B"
        elif (self.genotype == "BB") or (self.genotype == "Bi"):
            return "A"
        else:
            return "Não possui"

    agglutinins = property(agglutinins)

    def repeated_elements(lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l
    
    def offsprings_genotypes(self, indiv2):
        genotypes = list()
        for alelo_a in self.genotype:
            for alelo_b in  indiv2.genotype:
                genotypes.append(alelo_a + alelo_b)
        genotypes = list(set(genotypes))
        return genotypes
    

    def offsprings_blood_types(self, indiv2):
        blood_types = list()
        for genotype in self.offsprings_genotypes(indiv2):
            if (genotype == "AA") or (genotype == "Ai"):
                blood_types.append("A")                
            elif (genotype == "BB") or (genotype == "Bi"):
                blood_types.append("B")
            elif genotype == "AB":
                blood_types.append("AB")
            else:
                blood_types.append("O")
        blood_types = list(set(blood_types))
        
        return blood_types
    
    def can_donate(self, indiv2):
        if (self.blood_type == indiv2.blood_type):
            return True
        elif (self.blood_type == "O"):
            return True
        elif (self.blood_type == "A") and (indiv2.blood_type == "AB"):
            return True
        elif (self.blood_type == "B") and (indiv2.blood_type == "AB"):
            return True
        else:
            return False

    def can_receive(self, indiv2):
        if (self.blood_type == indiv2.blood_type):
            return True
        elif (self.blood_type == "AB"):
            return True
        elif (indiv2.blood_type == "AB"):
            if self.blood_type == "AB":
                return True
            else:
                return False
        elif (indiv2.blood_type == "O"):
            return True
        else:
            return False













