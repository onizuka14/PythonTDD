from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Joao ouviu falar de uma nova aplicação online interessante para listas de tarefas
		# Ele decide verificar a homepage
		self.browser.get('http://localhost:8000')

		# Ele percebe que o titulo da pagina e o cabecalho mencionam listas de tarefas 
		self.assertIn('Lista de Tarefas', self.browser.title)
		self.fail('Finish the test!')
	
		# Ele então é convidado a inserir um item da tarefa imediatamente
		
		# Ele digita "Comprar uma gtx1070" em uma caixa de textos
		
		# Quando ele tecla enter a pagina é atualizada e agora a pagina lista 
		# 1 : Comprar uma gtx1070
		
		# Ainda continua havendo uma caixa de texto convidando ele a inserir outro item. 
		# Ele insere "Comprar jogos para utilizar a gtx1070"
		
		# A pagina é atualizada novamente e agora mostra dois itens da lista
		
		# Joao se pergunta se o site lembrara de sua lista. Entao ele nota que o site gerou um URL 
		# unico para ele -- há um texto explicando isso
		
		# Ele acessa esse URL - sua lista continua lambda
		
		# Satisfeito ele sai do pc

if __name__ == '__main__':
	unittest.main(warnings='ignore')