import os


class GerenciadorArquivos:
    def __init__(self, diretorio: str) -> None:
        self.diretorio: str = diretorio

    def escrever_arquivo(self, nome_arquivo: str, conteudo: str) -> None:
        """
            Cria o arquivo e escreve o conteúdo nele.
        """
        with open(os.path.join(self.diretorio, nome_arquivo), 'w') as f:
            f.write(conteudo)
        # retornar: arquivo criado

    def ler_arquivo(self, nome_arquivo: str) -> str:
        """
            Abre o arquivo e lê o seu conteúdo.
        """
        with open(os.path.join(self.diretorio, nome_arquivo), 'r') as f:
            print("lido")
            return f.read()
        # retornar: o que está escrito

    def excluir_arquivo(self, nome_arquivo: str) -> None:
        """
            Exclui o arquivo.
        """
        os.remove(os.path.join(self.diretorio, nome_arquivo))
        #retornar: excluído
