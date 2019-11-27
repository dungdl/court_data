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

    def rela_convert(self, legal_rela):
        switcher = {
            1: "MTGD",
            2: "NN",
            3: "NT",
            4: "TNXH",
            5: "BT",
            6: "MT",
            7: "MTKT",
            8: "BLGD"
        }
        return switcher.get(legal_rela, "MTGD")

    def child_convert(self, has_child):
        switcher = {
            0: "khong",
            1: "co"

        }
        return switcher.get(has_child, "khong")

    def age_convert(self, age):
        switcher = {
            1: "<=30",
            2: ">30"
        }
        return switcher.get(age, "<=30")

    def dist_convert(self, age_dist):
        switcher = {
            1: "<=5",
            2: "5_10",
            3: ">10"
        }
        return switcher.get(age_dist, "<=5")

    def decision_convert(self, decision):
        switcher = {
            1: "Hoagiai",
            2: "Xetxu"
        }
        return switcher.get(decision, "Hoagiai")

    def toString(self):
        output = []
        output.append(self.rela_convert(self.legal_rela))
        output.append(self.child_convert(self.has_child))
        output.append(self.age_convert(self.plaintiff_age))
        output.append(self.age_convert(self.defendant_age))
        output.append(self.dist_convert(self.age_dist))
        output.append(self.decision_convert(self.decision))

        output = ','.join(output)
        output += '\n'
        return output
