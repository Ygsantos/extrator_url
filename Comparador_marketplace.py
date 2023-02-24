#Comparar precos do marketplace facebook e olx
#escolher cidade
#escolher produto
# facebook: https://pt-br.facebook.com/marketplace/manaus/search/?query=carros
#olx: https://www.olx.com.br/estado-am/regiao-de-manaus?q=carros

class Comparador:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def valida_url(self):
        if self.url == '':
            raise ValueError('A URL NAO É VALIDA ')

    def sanitiza_url(self,url):
        return url.strip()

    def get_url_base(self): #        """Retorna a base da url."""
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self): #        """Retorna os parâmetros da url."""
        indice_interrogacao = self.url.find('=')
        url_parametro = self.url[indice_interrogacao +1:]
        return url_parametro

    def pesquisa_facebook_olx(self,parametro, palavra):
        tratamento_pesquisa = palavra.replace(' ','%20')
        return self.url.replace(parametro,tratamento_pesquisa)


    '''def get_valor_parametro(self, nome_parametro): #        """Retorna os parâmetros da url."""
        indice_parametro = self.get_url_parametros().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) +1
        indice_e_comercial = self.get_url_parametros().find('&',indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return  valor'''

#url_bruta
url_facebook = Comparador('https://pt-br.facebook.com/marketplace/manaus/search/?query=carros')
url_olx = Comparador('https://www.olx.com.br/estado-am/regiao-de-manaus?q=carros')

#item pesquiasdo
palavra_pesquisada = input('Digite o item a ser pesquisado: ')

#facebook
url_facebook_base = url_facebook.get_url_base()
url_facebook_parametro = url_facebook.get_url_parametros()
url_nova_facebook = url_facebook.pesquisa_facebook_olx(url_facebook_parametro,palavra_pesquisada)

#olx
url_olx_base = url_olx.get_url_base()
url_olx_parametro = url_olx.get_url_parametros()
url_olx_nova = url_olx.pesquisa_facebook_olx(url_olx_parametro,palavra_pesquisada)
print(url_nova_facebook)
print(url_olx_nova)







