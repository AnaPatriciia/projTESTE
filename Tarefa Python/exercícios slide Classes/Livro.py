class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def getNome(self):
        return self.nome
    
    def getAutor(self):
        return self.autor

    def setEditora(self,nova_editora): #Metodo para alterar editiora
        self.editora = nova_editora    

    def getPaginas(self):# metodo para listar qtde paginas
        return self.paginas
    
livro = Livro("DOM Casmurro","Machado deAssis","Record","100")
livro.getNome()
print("Livro: ",livro.nome)

livro.getAutor()
print("Autor: ",livro.autor)

livro.getPaginas()  #Listar qtde
print("total de páginas: ",livro.paginas)

print("A primeira editora: ",livro.editora)

livro.setEditora("Saraiva")  #Alterar editora

print("Editora atualizada: ",livro.editora)

