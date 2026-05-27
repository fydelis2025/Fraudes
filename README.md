Detecção de Fraudes 🛡️
Sobre o Projeto
Este repositório foi desenvolvido como parte de um projeto acadêmico, com foco em detecção de fraudes em transações e comportamentos. O objetivo é aplicar conceitos de análise de dados, estatística e aprendizado de máquina para identificar padrões suspeitos, reduzir riscos e entender como funcionam as estratégias de prevenção de fraudes em setores como o financeiro, varejo e serviços digitais.
Todo o conteúdo foi elaborado para fins educacionais, visando o aprendizado prático das etapas de um projeto de ciência de dados: desde a coleta e tratamento de dados até a avaliação de modelos preditivos.
Objetivos do Projeto
Entender o cenário de fraudes, seus tipos e impactos econômicos e sociais.
Realizar limpeza, tratamento e preparação de dados brutos, resolvendo problemas como valores ausentes, dados inconsistentes e desbalanceamento de classes.
Explorar os dados para encontrar padrões, relações e características que diferenciam atividades legítimas de fraudulentas.
Implementar algoritmos de aprendizado de máquina adequados para problemas de classificação.
Avaliar os modelos com métricas específicas para esse tipo de problema, já que a acurácia por si só não é suficiente.
Documentar todo o processo e apresentar resultados com explicações claras.
📂 Estrutura do Repositório
plaintext
Fraudes/
├── dados/               # Conjuntos de dados: brutos, tratados e amostras
├── notebooks/           # Arquivos Jupyter Notebook com análises e códigos
├── scripts/             # Scripts Python para processamento e automação
├── resultados/          # Gráficos, relatórios e métricas de desempenho
├── documentos/          # Materiais de referência, artigos e anotações
└── README.md            # Documento atual com informações do projeto
🛠️ Tecnologias e Ferramentas Utilizadas
Linguagem: Python 3.x
Manipulação de dados: Pandas, NumPy
Visualização: Matplotlib, Seaborn
Aprendizado de Máquina: Scikit-learn, Imblearn (para desbalanceamento)
Ambiente de desenvolvimento: Jupyter Notebook, VS Code
🚀 Como Executar o Projeto
Clone o repositório
bash
git clone https://github.com/fydelis2025/Fraudes.git
cd Fraudes
Crie um ambiente virtual (recomendado)
bash
# Criação
python -m venv venv

# Ativação - Windows
venv\Scripts\activate

# Ativação - Linux / macOS
source venv/bin/activate
Instale as dependências
bash
pip install pandas numpy matplotlib seaborn scikit-learn imblearn jupyter
Abra os arquivos de análise
bash
jupyter notebook
Acesse a pasta notebooks e siga a ordem dos arquivos para reproduzir todo o estudo.
📊 Metodologia Aplicada
Coleta e Preparação: Tratamento de valores nulos, codificação de variáveis e normalização.
Análise Exploratória: Identificação de distribuições, correlações e características relevantes.
Desbalanceamento de Dados: Uso de técnicas como SMOTE ou subamostragem, já que fraudes são eventos raros.
Modelagem: Teste de algoritmos como Regressão Logística, Floresta Aleatória e Árvores de Decisão.
Avaliação: Uso de métricas como Precisão, Revocação, F1-Score e Matriz de Confusão.
✅ Resultados Esperados
Identificação dos principais fatores que aumentam o risco de fraude.
Modelo preditivo capaz de detectar fraudes com equilíbrio entre acertos e erros.
Relatório com explicações sobre o desempenho e limitações dos modelos testados.
📝 Observações Importantes
Os dados utilizados são públicos ou simulados, sempre anonimizados para garantir privacidade e conformidade.
Este é um trabalho acadêmico e pode receber atualizações, melhorias e novas abordagens ao longo do tempo.
👤 Autor
fydelis2025Projeto desenvolvido para fins educacionais, como parte das atividades do curso de Ciência de Dados / Inteligência Artificial.
📄 Licença
Este projeto está sob a licença MIT — consulte o arquivo LICENSE para mais detalhes sobre uso e distribuição.
