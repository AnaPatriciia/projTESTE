class Livro:
    def __init__(self,nome:str,autor:str,editora:str,paginas:int):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def getpaginas(self):
        print(self.paginas)

    def setEditora(self,nomenovo):
        self.editora =nomenovo

livro1 = Livro("Memórias Póstumas de Brás Cubas","Machadinho","Atlas","2268")
livro2 = Livro("Poesia Concreta","Paulo Leminsk", "tesla","199")
livro2.getPaginas()
print(livro2.editora)
livro2.setEditora("nova editora")
print(livro2.editora)



#def alterar_editora(self, nova_editora):
 #       self.editora = nova_editora

  #  def qtde_paginas(self):
   #     print(f'O livro "{self.nome}" possui {self.paginas} páginas.')


#livro1 = Livro("Dom Casmurro", "Machado De Assis", " Saraiva", 100)
    
    
#livro1.qtde_paginas()
    
    
#livro1.alterar_editora("Record")
#print(f'A nova editora do livro "{livro1.nome}" é {livro1.editora}.')