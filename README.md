# 📊 Challenge Telecom_X | Análise de Evasão de Clientes (EDA)

## 🚀 Objetivo
Este projeto tem como objetivo entender os fatores que influenciam a saída de clientes da empresa Telecom X, utilizando Python e bibliotecas de análise de dados. A empresa está enfrentando um alto índice de cancelamentos de contratos e busca identificar oportunidades para reduzir a taxa de abandono.

## 🧹 Limpeza e Tratamento de Dados
As principais etapas de preparação dos dados incluíram:

- Importação e normalização de um arquivo JSON
- Separação de campos aninhados em colunas planas
- Remoção de registros com valores ausentes em colunas
- Padronização e tradução de colunas para melhor entendimento dos analistas brasileiros


## 📊 Principais Resultados da Análise

- Proporção de Cancelamentos: Aproximadamente 25,7% dos clientes optaram por cancelar o serviço.
- Proporção de Cancelamentos Maiores: As seguintes categorias apresentaram maior risco de cancelamento:
- Clientes idosos apresentaram uma maior propensão ao cancelamento.
- Contratos mensais tiveram uma maior taxa de cancelamento.
- Certos métodos de pagamento apresentaram um maior risco de cancelamento.
- Distribuição de Gasto Total: Clientes que cancelaram tendem a ter contratos mais curtos e menor gasto total.

## 🧠 Insights Principais

- "Idosos e clientes com contrato mensal ou pagamento eletrônico automático apresentam uma maior propensão ao cancelamento."
- "Clientes com contratos mais curtos e gastos totais mais baixos têm uma maior probabilidade de cancelar."
- "É fundamental desenvolver estratégias de fidelização personalizadas para esses perfis de clientes."

## 🛠 Tecnologias Utilizadas
- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab
- Google Drive
- Markdown

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

## 🤖 Modelo de Classificação
- Treinamos um modelo de classificação Random Forest para prever se um cliente vai cancelar o serviço
- O modelo alcançou uma acurácia de aproximadamente 79%
- O modelo teve um desempenho melhor para a classe 0 (clientes que não cancelaram o serviço) do que para a classe 1 (clientes que cancelaram o serviço)

## 📝 Conclusão
- A análise de evasão de clientes revelou importantes padrões de comportamento entre os clientes
- O modelo de classificação Random Forest mostrou-se eficaz em prever a probabilidade de um cliente abandonar o serviço
- Os resultados podem ser utilizados para desenvolver estratégias de retenção de clientes e melhorar a experiência do usuário.

## 🚀 Próximos Passos
- Implementar o modelo de classificação em produção
- Continuar a coletar e analisar dados para melhorar a acurácia do modelo
- Desenvolver estratégias de retenção de clientes baseadas nos resultados da análise

## 📄 Como Executar o Projeto
- Clone o repositório
- Instale as dependências necessárias
- Execute o código em Python

## 🚀 Acesso ao Projeto
Para executar o projeto, siga as etapas:

- Clone este repositório: git clone [https://github.com/tluistorres/Challenge_Telecom_Alura_ONE.git](https://github.com/tluistorres/Challenge_TelecomX_Alura_ONE)

## 👩‍💻 Desenvolvedor do Projeto
- https://github.com/tluistorres

## 👥 Contato
- [Luís Torres]
- [luistorres090165@gmail.com]
- [www.linkedin.com/in/lu%C3%ADs-torres-4a3264137]
