class Case:
    """
    represent a case in a court
    including: 
     id,
     legal_rela, 
     age_dist, 
     has_child, 
     husb_age, 
     wife_age, 
     decision
    """

    def __init__(self, id, legal_rela, plaintiff_age, defendant_age, decision):
        self.id = id
        self.legal_rela = legal_rela
        self.getPlaintiffAge(plaintiff_age)
        self.getDefendantAge(defendant_age)
        self.decision = decision
        self.getAgeDistance(plaintiff_age, defendant_age)
        self.getHasChild(legal_rela)

    def getDefendantAge(self, defendant_age):
        if defendant_age <= 30:
            self.defendant_age = 1
        else:
            self.defendant_age = 2

    def getPlaintiffAge(self, plaintiff_age):
        if plaintiff_age <= 30:
            self.plaintiff_age = 1
        else:
            self.plaintiff_age = 2

    def getAgeDistance(self, plaintiff_age, defendant_age):
        age_dist = abs(plaintiff_age - defendant_age)

        if age_dist <= 5:
            self.age_dist = 1
        elif age_dist <= 10:
            self.age_dist = 2
        else:
            self.age_dist = 3

    def getHasChild(self, legal_rela):
        if legal_rela == 5:
            self.has_child = 0
        else:
            self.has_child = 1

    def toString(self):
        output = []
        output.append(str(self.legal_rela))
        output.append(str(self.has_child))
        output.append(str(self.plaintiff_age))
        output.append(str(self.defendant_age))
        output.append(str(self.age_dist))
        output.append(str(self.decision))


        output = ','.join(output)
        output += '\n'
        return output