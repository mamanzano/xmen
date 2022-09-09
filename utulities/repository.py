
from magneto import stat


class Repository():

    LATTERS_VALIDS = 'ATCG'

    def __init__(self,dna) -> None:
        self.dna = dna

    def is_mutant(self):
        stat = stat.Stat('1',self.dna,False)
        stat._is_mutant = self.is_mutant_x()

        return stat

    def is_mutant_x(self):

        if self.validate_size_dna() and self.validate_letetrs_dna():
            vertical_dna = self.create_vertical()
            horizontal_dna = self.dna
            diagonal_dna = self.create_diagonal()

            num_base_valid = 0
            num_base_valid = num_base_valid + self.get_num_base_valid(vertical_dna)
            num_base_valid = num_base_valid + self.get_num_base_valid(horizontal_dna)
            num_base_valid = num_base_valid + self.get_num_base_valid(diagonal_dna)

            if num_base_valid >= 2:
                return True
            else:
                return False
        else:
            print('El dna no es valido')


    def get_num_base_valid(self,base_list):
        num_base_valid = 0
        for base in base_list:
            bv = self.funt_x(base)
            if bv :
                num_base_valid = num_base_valid + 1

        return num_base_valid


    def funt_x(self,base):
        leng = len(base)
        cadena = 4

        for i in range(0, leng):
            if i > 0:
                cadena = cadena + 1
            if cadena <= leng:
                val = base[i:cadena]
                mutant = self.valide_base(val)
                if mutant:
                    return True
                else:
                    continue
            else:
                return False


    def valide_base(self, val):
        ref = ''
        count = 0
        for l in val:
            if count == 0:
                ref = l
                count = count + 1
            elif ref == l:
                ref = l
            else:
                return False
        
        return True

    def create_vertical(self):
        size = len(self.dna)
        vertical_dna = []
        for i in range(0,size):
            e = ''
            for element in self.dna:
                e = e + element[i]
            vertical_dna.append(e)

        return vertical_dna

    def create_diagonal(self):
        diagonal_dna = []
        
        e = ''
        count = 0
        for elemen in self.dna:
            e = e + elemen[count]
            count = count + 1
        diagonal_dna.append(e)

        return  diagonal_dna

    def validate_size_dna(self):

        size = 0
        for base in self.dna:
            if size == 0:
                size = len(base)
            elif size != len(base):
                return False
        return True

    def validate_letetrs_dna(self):

        for base in self.dna:
            for l in base:
                index = self.LATTERS_VALIDS.find(l)
                if index == -1:
                    return False
        
        return True
