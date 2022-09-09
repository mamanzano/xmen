from utulities import repository


#DNA = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
DNA = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACT"]

if __name__ == '__main__':

    repo = repository.Repository(DNA)

    stat = repo.is_mutant()

    print(stat._is_mutant)