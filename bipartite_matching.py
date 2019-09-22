class bipartite_matching(object):
    def __init__(self, preferences_men, preferences_women):
        self.preferences_men = preferences_men
        self.preferences_women = preferences_women
        self.couples = list()
        self.single_men = list()
        for man in self.preferences_men.keys():
            self.single_men.append(man)

    def find_matching(self):
        while self.single_men:
            for man in self.single_men:
                self._find_matching(man)

    def _find_matching(self, man):
        for woman in self.preferences_men[man]:
            couples = list()
            for couple in self.couples:
                if woman in couple:
                    couples.append(couple)
            if not couples:
                self.couples.append([man, woman])
                self.single_men.remove(man)
                break
            else:
                man_current = self.preferences_women[woman].index(couples[0][0])
                man_potential = self.preferences_women[woman].index(man)
                if man_current > man_potential:
                    self.single_men.remove(man)
                    self.single_men.append(couples[0][0])
                    couples[0][0] = man
                    break


if __name__ == "__main__":
    preferences_men = {
        "m1": ["w1", "w4", "w3", "w2"],
        "m2": ["w2", "w4", "w3", "w1"],
        "m3": ["w4", "w3", "w2", "w1"],
        "m4": ["w3", "w4", "w2", "w1"]
    }

    preferences_women = {
        "w1": ["m1", "m3", "m2", "m4"],
        "w2": ["m1", "m2", "m3", "m4"],
        "w3": ["m4", "m1", "m3", "m2"],
        "w4": ["m2", "m1", "m4", "m3"]
    }

    bipartite_matching_inst = bipartite_matching(preferences_men, preferences_women)
    bipartite_matching_inst.find_matching()
    print(bipartite_matching_inst.couples)
