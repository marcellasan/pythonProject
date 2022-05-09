import pandas as pd

# importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# quantidade de pordutos vendidos por loja
quantidade = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(quantidade)
print('-' * 50)

# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

# enviar um email com relatório
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'victor_soaresb@hotmail.com'
mail.subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados</p>

<p>Segue o Relatório de Vendas por cada Loja</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>ATT.</p>
<p>Marcella</p>
'''
mail.Send()
print('EMAIL ENVIADO')
