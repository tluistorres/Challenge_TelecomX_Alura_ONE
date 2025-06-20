# 📊 Challenge Telecom_X | Análise de Evasão de Clientes (EDA)

## 🚀 Objetivo
Este projeto tem como objetivo entender os fatores que influenciam a saída de clientes da empresa Telecom X, utilizando Python e bibliotecas de análise de dados. A empresa está enfrentando um alto índice de cancelamentos de contratos e busca identificar oportunidades para reduzir a taxa de abandono.

## 🧹 Limpeza e Tratamento de Dados
As principais etapas de preparação dos dados incluíram:

- Importação e normalização de um arquivo JSON
- Separação de campos aninhados em colunas planas
- Remoção de registros com valores ausentes em colunas
- Padronização e tradução de colunas para melhor entendimento dos analistas brasileiros
- Criação da variável Conta_Diarias, baseada na fatura mensal


## 📈 Análise Exploratória de Dados (EDA)
A análise exploratória revelou importantes padrões de comportamento entre os clientes.

### 📌 Percentual Geral de Cancelamentos
- 25,8% dos clientes cancelaram seus serviços

### 📊 Visualização da Evasão de Clientes
- Gráficos de pizza foram utilizados para visualizar a proporção de cancelamento
- Análise de variáveis como:
- Gênero
- Idoso
- Parceiro
- Dependentes
- Serviço de Telefone
- Serviço de Internet
- Contrato
- Método de Pagamento

## 📈 Correlação entre Variáveis
- A correlação entre tenure e Charges.Total é muito alta (0,825118)
- A correlação entre Charges.Monthly e Charges.Total também é alta (0,652109)


## 🤖 Modelo de Classificação
- Treinamos um modelo de classificação Random Forest para prever se um cliente vai cancelar o serviço
- O modelo alcançou uma acurácia de aproximadamente 79%
- O modelo teve um desempenho melhor para a classe 0 (clientes que não cancelaram o serviço) do que para a classe 1 (clientes que cancelaram o serviço)

## 📝 Conclusão
- A análise de evasão de clientes revelou importantes padrões de comportamento entre os clientes
- O modelo de classificação Random Forest mostrou-se eficaz em prever a probabilidade de um cliente abandonar o serviço
- Os resultados podem ser utilizados para desenvolver estratégias de retenção de clientes e melhorar a experiência do usuário

## 🚀 Próximos Passos
- Implementar o modelo de classificação em produção
- Continuar a coletar e analisar dados para melhorar a acurácia do modelo
- Desenvolver estratégias de retenção de clientes baseadas nos resultados da análise

## 📄 Como Executar o Projeto
- Clone o repositório
- Instale as dependências necessárias
- Execute o código em Python

## 📊 Visualizações
- Gráficos de pizza e outras visualizações estão incluídas no projeto para ajudar a entender os resultados

## 👥 Contato
- [Luís Torres]
- [luistorres090165@gmail.com]
- [www.linkedin.com/in/lu%C3%ADs-torres-4a3264137]
