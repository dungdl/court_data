class Case:
    """
    class to modelize a case in a court
    including: id, legal_rela, age_dist, has_child, husb_age, wife_age, decision
    """

    def __init__(self, id, legal_rela, plaintiff_age, defendant_age, decision):
        self.id = id
        self.legal_rela = legal_rela
        self.plaintiff_age = plaintiff_age
        self.defendant_age = defendant_age
        self.decision = decision
        self.getAgeDistance()
        self.getHasChild()

    def getAgeDistance(self):
        self.age_dist = abs(self.plaintiff_age - self.defendant_age)

    def getHasChild(self):
        if self.legal_rela == 5:
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