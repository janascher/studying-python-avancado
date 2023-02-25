from src.main import GerenciadorArquivos
from os import path
from pytest import raises


class TestClass:
    def test_quando_arquivo_eh_escrito_conteudo_do_arquivo(self, tmp_path):
        entrada = "conteúdo do arquivo"  # Given-Contexto
        nome_arquivo = "arquivo.txt"

        gerenciador_arquivos = GerenciadorArquivos(tmp_path)
        gerenciador_arquivos.escrever_arquivo(nome_arquivo, entrada)
        resultado = path.exists(
            path.join(gerenciador_arquivos.diretorio, entrada))  # When-ação

        esperado = path.exists(
            path.join(gerenciador_arquivos.diretorio, "conteúdo do arquivo"))

        assert resultado == esperado  # Then-desfecho

    def test_quando_arquivo_abre_deve_ler_conteudo_do_arquivo(self, tmp_path):
        entrada = "conteúdo do arquivo"  # Given-Contexto
        nome_arquivo = "arquivo.txt"

        gerenciador_arquivos = GerenciadorArquivos(tmp_path)
        gerenciador_arquivos.escrever_arquivo(nome_arquivo, entrada)
        resultado = gerenciador_arquivos.ler_arquivo(
            "arquivo.txt")  # When-ação

        esperado = "conteúdo do arquivo"

        assert resultado == esperado  # Then-desfecho

    def test_quando_arquivo_eh_excluido(self, tmp_path):

        entrada = "arquivo.txt"  # Given-Contexto
        conteudo = "conteúdo do arquivo"

        gerenciador_arquivos = GerenciadorArquivos(tmp_path)
        gerenciador_arquivos.escrever_arquivo(entrada, conteudo)
        gerenciador_arquivos.excluir_arquivo(entrada)
        resultado = not path.exists(
            path.join(gerenciador_arquivos.diretorio, entrada))  # When-ação

        esperado = not path.exists(
            path.join(gerenciador_arquivos.diretorio, "arquivo.txt"))

        assert resultado == esperado  # Then-desfecho

    def test_quando_eh_tentado_excluir_arquivo_inxistente(self, tmp_path):
        gerenciador_arquivos = GerenciadorArquivos(tmp_path)
        with raises(FileNotFoundError):
            gerenciador_arquivos.excluir_arquivo('arquivo_inexistente.txt')
