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
        output = str("%s,%s,%s,%s,%s", self.legal_rela, self.has_child, self.plaintiff_age, self.defendant_age, self.decision)
        return output