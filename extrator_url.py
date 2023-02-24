class extrator_url:
    def __init__(self,url): #        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()


    def sanitiza_url(self,url): #        """Retorna a url removendo espaços em branco."""
        return url.strip()

    def valida_url(self): #        """Valida se a url está vazia"""
        if self.url == '':
            raise ValueError('A URL NAO É VALIDA ')

    def get_url_base(self): #        """Retorna a base da url."""
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self): #        """Retorna os parâmetros da url."""
        indice_interrogacao = self.url.find('?')
        url_parametro = self.url[indice_interrogacao +1:]
        return url_parametro

    def get_valor_parametro(self, nome_parametro): #        """Retorna os parâmetros da url."""
        indice_parametro = self.get_url_parametros().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) +1
        indice_e_comercial = self.get_url_parametros().find('&',indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return  valor

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = extrator_url(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)


