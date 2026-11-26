pdf2md_prompt="""Você é um sistema especializado em transcrição fiel de provas e documentos a partir de imagens.

Sua tarefa é converter integralmente a página de prova do ENEM fornecida como imagem para Markdown, preservando todo o conteúdo textual e sua estrutura original.

**A prioridade absoluta é a fidelidade à imagem.** Não resuma, interprete, corrija, reescreva, reorganize ou complete o conteúdo por conta própria.

### 1. Transcrição do conteúdo

- Transcreva integralmente todos os textos, enunciados, alternativas, tabelas, títulos, legendas textuais e fórmulas pertencentes à prova.
- Preserve a ordem original de leitura da página, incluindo a disposição das questões e das alternativas.
- Preserve exatamente a redação, a pontuação, a acentuação, as maiúsculas, os números, os símbolos e os valores apresentados.
- Não corrija erros gramaticais ou tipográficos presentes no documento.
- Não omita trechos por serem repetitivos, extensos ou aparentemente pouco relevantes.
- Não acrescente informações, explicações, interpretações, resoluções ou respostas.
- Não tente adivinhar palavras ou símbolos que não possam ser identificados. Quando um trecho estiver efetivamente ilegível, indique apenas `[ilegível]` no local correspondente.

### 2. Formatação das questões

Cada questão deve começar com um cabeçalho Markdown de primeiro nível, utilizando letras maiúsculas e o número original da questão:

`# QUESTÃO 91`

`# QUESTÃO 92`

Continue conforme os números efetivamente identificados na imagem. Não invente ou renumere questões.

Não inclua números de página, cabeçalhos de paginação, rodapés ou outras marcações editoriais que não façam parte do conteúdo da prova.

Inclua indicações de áreas de conhecimento.

### 3. Formatação dos textos

Textos-base, excertos e demais parágrafos de leitura devem ser formatados como citações Markdown, utilizando `>` no início de cada parágrafo.

Exemplo:

> A pesquisadora foi laureada com o World Food Prize. Sua pesquisa usa bactérias que formam nódulos nas raízes.
>
> Essa descoberta contribuiu para o desenvolvimento de novas técnicas agrícolas.

Mantenha os enunciados das perguntas e os comandos fora das citações, exceto quando fizerem parte do próprio texto-base.

Preserve a estrutura dos parágrafos e as divisões de conteúdo existentes na imagem.

### 4. Formatação das alternativas

As alternativas devem ser representadas como uma lista Markdown, com a respectiva letra em negrito.

Utilize exatamente esta estrutura, incluindo o texto integral de cada alternativa:

- **A** Texto completo da alternativa.
- **B** Texto completo da alternativa.
- **C** Texto completo da alternativa.
- **D** Texto completo da alternativa.
- **E** Texto completo da alternativa.

Regras adicionais:

- Cada alternativa deve ocupar um item independente da lista.
- Preserve integralmente o texto de cada alternativa.
- Não omita alternativas, mesmo que sejam extensas.
- Não invente alternativas que não estejam presentes na imagem.
- Preserve a ordem original das letras.
- Se uma alternativa contiver uma fórmula, tabela ou figura, insira o conteúdo correspondente dentro do próprio item da alternativa, na posição original.

### 5. Formatação de fórmulas e tabelas

Utilize LaTeX para representar expressões matemáticas, químicas e físicas:

- Fórmulas inline: `$...$`
- Fórmulas em bloco: `$$...$$`

Preserve todos os valores, índices, expoentes, sinais, unidades e símbolos.

Converta tabelas para tabelas Markdown, preservando sua organização em linhas e colunas, os cabeçalhos e todos os valores.

Não substitua tabelas ou fórmulas por imagens.

### 6. Tratamento e associação das imagens

As figuras presentes na página devem ser representadas exclusivamente por referências Markdown de imagem, utilizando a seguinte sintaxe:

`![descrição objetiva e detalhada](path_da_imagem.png)`

A descrição no texto alternativo deve identificar `detalhada`mente o conteúdo visual da figura, porém sem interpretações ou informações que não sejam diretamente observáveis.

**Regras obrigatórias:**

1. Não transcreva, descreva ou recrie figuras no corpo do Markdown. A descrição visual deve aparecer exclusivamente no texto alternativo da referência de imagem.
2. Não utilize URLs. Utilize somente os caminhos fornecidos na lista de imagens.
3. Preserve exatamente os paths recebidos, sem modificar, completar, normalizar ou substituir seus valores.
4. Associe os paths às figuras estritamente na ordem de leitura fornecida pela lista.
5. Nunca reutilize um path para representar outra figura.
6. Não reordene figuras, alternativas ou referências de imagem.
7. Figuras pertencentes às alternativas devem ser inseridas dentro do item correspondente, exatamente na posição em que aparecem na página.
8. Não crie referências para figuras inexistentes nem associe um path a uma figura por suposição.

A lista fornecida representa os caminhos das imagens extraídas do PDF e já está ordenada conforme a sequência de leitura original. Utilize essa sequência diretamente, sem tentar determinar outra ordenação. Estão também presentes códigos de barras, logos, entre outras imagens dentre os caminhos; lembre-se que caso o número de figuras na página for diferente dos listados, há imagens que não devem ser utilizadas, devendo ser ignoradas segundo sua posição descrita no nome de arquivo.

### 7. Restrições de saída

O resultado deve conter exclusivamente o Markdown correspondente à página da prova.

Não inclua:

- Introduções ou conclusões.
- Explicações sobre o processo de transcrição.
- Comentários ou observações.
- Resumos ou interpretações.
- Respostas das questões.
- Blocos de código envolvendo o Markdown final.
- Qualquer conteúdo que não esteja presente na página ou que não seja necessário à formatação Markdown e às referências de imagem exigidas.

Antes de finalizar, confira se todos os textos, questões, alternativas, fórmulas, tabelas e figuras visíveis foram contemplados, se os paths foram associados sequencialmente e se a ordem original da página foi preservada.

**Imagem fornecida:** página de uma prova do ENEM.

**Lista de paths das imagens extraídas da página do PDF (em ordem de leitura):**

{0}"""

system_prompt_md2json="""Você é um conversor especializado de provas em Markdown para JSON. Sua única tarefa é aplicar exatamente a especificação fornecida na mensagem do usuário. A mensagem do usuário é a autoridade máxima sobre esquema, campos, regras de extração e formato.

Produza somente um objeto JSON válido, em UTF-8, sem texto antes ou depois, sem comentários, sem cercas de código, sem explicações e sem usar ferramentas. Não invente dados; quando a especificação mandar usar null ou [], faça isso. Preserve fielmente textos, ordem, quebras de linha e sintaxe Markdown de imagens. Não inclua alternativas no enunciado nem altere o conteúdo, exceto artefatos óbvios de conversão automática conforme permitido.

Se a entrada estiver vazia ou não contiver uma prova identificável, retorne o JSON mínimo compatível com o esquema, usando null/[] quando aplicável."""

system_prompt_json_commenting="""Você é um especialista em avaliação educacional, itens do ENEM e taxonomia curricular. Sua tarefa é receber um prompt de usuário contendo a matriz de referência e os eixos cognitivos do ENEM e um JSON de uma questão. Analise o JSON da questão e retorne um novo objeto JSON enriquecido.

**Regras obrigatórias:**

1. Preserve todos os campos originais da raiz do JSON exatamente como foram recebidos, sem alterações.
2. Adicione ao final do objeto os seguintes campos:
   - `comentarios`: array de exatamente 5 strings. Cada string deve ser um comentário didático e técnico explicando por que a respectiva alternativa está certa ou errada. A ordem deve seguir rigorosamente as alternativas A, B, C, D, E:
     - índice 0: alternativa A;
     - índice 1: alternativa B;
     - índice 2: alternativa C;
     - índice 3: alternativa D;
     - índice 4: alternativa E.
   - `materias`: array de strings com os nomes das matérias envolvidas na questão.
   - `conteudos`: array de strings com tópicos, matérias, palavras-chave e classificações curriculares abordadas na questão. Considere a grade curricular/taxonomia da matriz de referência do ENEM fornecida no prompt do usuário. Seja extensivo na classificação, melhor incluir mais classes do que menos.
   - `dica`: string com uma dica estratégica e reflexiva para orientar um aluno que está travado na questão. A dica deve apontar o caminho do conceito, mas jamais revelar a resposta correta ou qual é a alternativa gabarito.
3. Use a matriz de referência, os eixos cognitivos e os objetos de conhecimento fornecidos no prompt do usuário como base para classificar matérias e conteúdos.
4. Não altere, remova ou renomeie chaves originais.
5. Retorne apenas JSON válido e formatado.
6. Não inclua saudações, explicações, raciocínios, texto introdutório ou qualquer conteúdo fora do JSON.
7. Não envolva o JSON em blocos de código markdown. Não use cercas de código. Retorne apenas a string JSON crua."""

prompt_template_md2json=r"""Você receberá, dois arquivos Markdown: um contendo a PROVA e outro contendo o GABARITO. Sua tarefa é transformar esses dados em um único JSON válido, sem qualquer texto adicional, explicação, comentário, tag, ferramenta, decorador ou markdown ao redor do JSON. Use o arquivo da PROVA para preencher `id_prova`, `numero_exercicio`, `enunciado` e `alternativas`; use o arquivo do GABARITO exclusivamente para preencher o campo `gabarito`.

## Formato de saída obrigatório

O JSON deve ser um objeto com exatamente esta estrutura:

{
  "id_prova": "<nome e ano da prova, ex.: DIA 1 - ENEM 2022 - Caderno Azul>",
  "numero_exercicio": "<identificador do exercício, ex.: 1,2,3,...,180",
  "enunciado": "<textos de apoio + enunciado da questão, preservando o conteúdo original>",
  "alternativas": [
    "<texto da alternativa A>",
    "<texto da alternativa B>",
    "<texto da alternativa C>",
    "<texto da alternativa D>",
    "<texto da alternativa E>"
  ],
  "gabarito": "<resposta correspondente no arquivo do GABARITO>"
}

## Regras

1. **Entrada com dois Markdowns**: serão fornecidos dois arquivos/blocos Markdown, um da PROVA e um do GABARITO. Se não estiverem rotulados, identifique pelo conteúdo. O arquivo da PROVA contém questões, textos de apoio, imagens e alternativas. O arquivo do GABARITO contém apenas as respostas.
2. **id_prova**: extraia o nome e o ano da prova a partir do conteúdo da PROVA (cabeçalho, título ou contexto). Não utilize o nome do arquivo, mas sim o dia, prova, ano e caderno.
3. **numero_exercicio**: Identifique o exercício com um número. Se a prova não numerar um item, use `null`.
4. **enunciado**: concatene, na ordem original, todo o texto de apoio (textos-base, citações, gráficos descritos em texto, instruções) e o enunciado da questão. Preserve quebras de linha como `\n`. **Não inclua o texto das alternativas nem o texto do gabarito aqui. Altere o texto em caso de erros evidentes na conversão de PDF para Markdown.**
5. **alternativas**: array de strings com o texto de cada alternativa, na ordem em que aparecem na PROVA. Remova marcadores de enumeração redundantes (ex.: `A)`, `(B)`). Se não houver alternativas, use `[]`.
6. **gabarito**: preencha com a resposta correspondente no campo "gabarito". Utilize números 0 indexados (ex.: 0=a, 1=b, 2=c...). Caso a questão for anulada, retorne -1.
7. **Imagens**:
   - Se o Markdown da PROVA contiver imagens em qualquer sintaxe (`![alt](url)`, tags HTML `<img>`, links para arquivos de imagem), **inclua-as no campo correspondente** mantendo o Markdown original da imagem:
     - imagens no enunciado/texto de apoio → dentro de `"enunciado"`;
     - imagens dentro de uma alternativa → dentro da string daquela alternativa em `"alternativas"`.
   - Preserve a URL/caminho exatamente como veio. Se houver apenas texto alternativo (`alt`), preserve-o como `![alt]()`.
   - Não descreva imagens; não gere URLs novas; não omita imagens.
8. **Fidelidade**: não corrija, resuma, traduza nem reescreva o conteúdo. Mantenha o markdown dos enunciados e alternativas, sem remover suas formatações, seja de **negrito**, > blockquote, etc.
9. **Saída**: retorne **somente** o JSON válido (UTF-8, array de objetos, sem vírgula final, sem comentários). Nada antes, nada depois. Não use blocos de código cercados por ```.

## Nome do arquivo de prova

{0}

## GABARITO

{1}

## PROVA

{2}"""

prompt_template_question_enrichment="""A seguir se encontra a matriz de referência e eixos cognitivos do ENEM.

---

**EIXOS COGNITIVOS (COMUNS A TODAS AS ÁREAS DE CONHECIMENTO)** [Eixo Cognitivo 1] **Dominar linguagens (DL):** Dominar a norma culta da língua portuguesa, espanhola e inglesa.[1] [Eixo Cognitivo 2] **Compreender fenômenos (CF):** Construir e aplicar conceitos das várias áreas do conhecimento para a compreensão de fenômenos naturais, de processos histórico-geográficos, de equipamentos tecnológicos, de manifestações artísticas ou do cotidiano.[1] [Eixo Cognitivo 3] **Enfrentar situações-problema (SP):** Selecionar, organizar, relacionar, interpretar dados e informações representados de diferentes formas, para tomar decisões e enfrentar situações-problema.[1] [Eixo Cognitivo 4] **Construir argumentação (CA):** Relacionar informações e conhecimentos disponíveis em diferentes situações para construir argumentação consistente.[1] [Eixo Cognitivo 5] **Elaborar propostas (EP):** Recorrer aos conhecimentos desenvolvidos na escola para elaboração de propostas de intervenção solidária na realidade, respeitando os valores humanos e considerando a diversidade sociocultural.[1][2]

**MATRIZ DE REFERÊNCIA - LINGUAGENS, CÓDIGOS E SUAS TECNOLOGIAS** [Linguagens | Competência de Área 1] **Tecnologias da Informação e Comunicação:** Aplicar as tecnologias da comunicação e da informação na escola, no trabalho e em outros contextos relevantes para sua vida (abrange as habilidades H1, H2, H3, H4).[2] [Linguagens | Competência de Área 2] **Língua Estrangeira Moderna:** Conhecer e usar língua(s) estrangeira(s) moderna(s) como instrumento de acesso a informações e a outras culturas e grupos sociais (abrange as habilidades H5, H6, H7, H8).[2] [Linguagens | Competência de Área 3] **Linguagem Corporal:** Compreender e usar a linguagem corporal como relevante para a própria vida, integradora social e formadora da identidade (abrange as habilidades H9, H10, H11).[3] [Linguagens | Competência de Área 4] **Arte e Estética:** Compreender a arte como saber cultural e estético gerador de significação e integrador da organização do mundo e da própria identidade (abrange as habilidades H12, H13, H14).[3] [Linguagens | Competência de Área 5] **Recursos Expressivos e Contexto:** Analisar, interpretar e aplicar recursos expressivos das linguagens, relacionando textos com seus contextos, mediante a natureza, função, organização, estrutura das manifestações, de acordo com as condições de produção e recepção (abrange as habilidades H15, H16, H17).[3][4] [Linguagens | Competência de Área 6] **Sistemas Simbólicos:** Compreender e usar os sistemas simbólicos das diferentes linguagens como meios de organização cognitiva da realidade pela constituição de significados, expressão, comunicação e informação (abrange as habilidades H18, H19, H20).[4] [Linguagens | Competência de Área 7] **Confronto de Opiniões:** Confrontar opiniões e pontos de vista sobre as diferentes linguagens e suas manifestações específicas (abrange as habilidades H21, H22, H23, H24).[4][5] [Linguagens | Competência de Área 8] **Língua Portuguesa e Identidade:** Compreender e usar a língua portuguesa como língua materna, geradora de significação e integradora da organização do mundo e da própria identidade (abrange as habilidades H25, H26 e a H27 - Reconhecer os usos da norma-padrão da língua portuguesa nas diferentes situações de comunicação).[5] [Linguagens | Competência de Área 9] **Impacto Social das TICs:** Entender os princípios, a natureza, a função e o impacto das tecnologias da comunicação e da informação na sua vida pessoal e social, no desenvolvimento do conhecimento, associando-os aos conhecimentos científicos, às linguagens que lhes dão suporte, às demais tecnologias, aos processos de produção e aos problemas que se propõem solucionar (abrange as habilidades H28, H29, H30).[5][6]

**MATRIZ DE REFERÊNCIA - MATEMÁTICA E SUAS TECNOLOGIAS** [Matemática | Competência de Área 1] **Conhecimentos Numéricos:** Construir significados para os números naturais, inteiros, racionais e reais (abrange as habilidades H1, H2, H3, H4, H5).[6] [Matemática | Competência de Área 2] **Conhecimentos Geométricos:** Utilizar o conhecimento geométrico para realizar a leitura e a representação da realidade e agir sobre ela (abrange as habilidades H6, H7, H8, H9).[6] [Matemática | Competência de Área 3] **Grandezas e Medidas:** Construir noções de grandezas e medidas para a compreensão da realidade e a solução de problemas do cotidiano (abrange as habilidades H10, H11, H12, H13, H14).[6] [Matemática | Competência de Área 4] **Variação de Grandezas:** Construir noções de variação de grandezas para a compreensão da realidade e a solução de problemas do cotidiano (abrange as habilidades H15, H16, H17, H18, H19, H20, H21, H22, H23).[7] [Matemática | Competência de Área 5] **Gráficos e Tabelas:** Interpretar informações de natureza científica e social obtidas da leitura de gráficos e tabelas, realizando previsão de tendência, extrapolação, interpolação e interpretação (abrange as habilidades H24, H25, H26).[7] [Matemática | Competência de Área 6] **Estatística e Probabilidade:** Compreender o caráter aleatório e não determinístico dos fenômenos naturais e sociais, e utilizar instrumentos adequados para medidas, determinação de amostras e cálculos de probabilidade para interpretar informações de variáveis apresentadas em uma distribuição estatística (abrange as habilidades H27, H28, H29, H30).[7][8]

**MATRIZ DE REFERÊNCIA - CIÊNCIAS DA NATUREZA E SUAS TECNOLOGIAS** [Ciências da Natureza | Competência de Área 1] **Ciências e Sociedade:** Compreender as ciências naturais e as tecnologias a elas associadas como construções humanas, percebendo seus papéis nos processos de produção e no desenvolvimento social (abrange H1 a H7; ex: H1 - Reconhecer características ou propriedades de fenômenos ondulatórios ou oscilatórios; H5 - Dimensionar circuitos ou dispositivos elétricos de uso cotidiano).[8] [Ciências da Natureza | Competência de Área 2] **Conservação e Degradação Ambiental:** Associar intervenções que resultam em degradação ou conservação ambiental a processos produtivos e sociais e a instrumentos ou ações científico-tecnológicos (abrange as habilidades H8, H9, H10, H11, H12).[8][9] [Ciências da Natureza | Competência de Área 3] **Saúde e Organismos:** Compreender interações entre organismos e ambiente, em particular aquelas relacionadas à saúde humana, relacionando conhecimentos científicos, aspectos culturais e/ou das tecnologias sociais (abrange as habilidades H13, H14, H15, H16).[9] [Ciências da Natureza | Competência de Área 4] **Métodos Científicos:** Entender métodos e procedimentos próprios das ciências naturais e aplicá-los em diferentes contextos (abrange as habilidades H17, H18, H19).[9][10] [Ciências da Natureza | Competência de Área 5] **Aplicações da Física:** Apropriar-se de conhecimentos da física para, em situações-problema, interpretar, avaliar ou planejar intervenções prático-existenciais (abrange as habilidades H20, H21, H22, H23).[10] [Ciências da Natureza | Competência de Área 6] **Aplicações da Química:** Apropriar-se de conhecimentos da química para, em situações-problema, interpretar, avaliar ou planejar intervenções prático-existenciais (abrange as habilidades H24, H25, H26, H27).[10] [Ciências da Natureza | Competência de Área 7] **Aplicações da Biologia:** Apropriar-se de conhecimentos da biologia para, em situações-problema, interpretar, avaliar ou planejar intervenções prático-existenciais (abrange H28 a H30; ex: H28 - Associar características adaptativas dos organismos com seu modo de vida ou distribuição geográfica).[10]

**MATRIZ DE REFERÊNCIA - CIÊNCIAS HUMANAS E SUAS TECNOLOGIAS** [Ciências Humanas | Competência de Área 1] **Cultura e Identidade:** Compreender os elementos culturais que constituem as identidades (abrange as habilidades H1, H2, H3, H4, H5).[10] [Ciências Humanas | Competência de Área 2] **Espaço e Territorialidade:** Compreender a organização do espaço e as transformações territoriais como produto das relações sociais e econômicas em escala local, regional ou mundial (abrange as habilidades H6, H7, H8, H9, H10).[10][11] [Ciências Humanas | Competência de Área 3] **Instituições Sociais e Políticas:** Compreender a produção e o papel histórico das instituições sociais, políticas e econômicas, associando-as aos diferentes grupos sociais e aos sujeitos históricos (abrange as habilidades H11, H12, H13, H14, H15).[11] [Ciências Humanas | Competência de Área 4] **Cidadania e Democracia:** Utilizar os conhecimentos históricos para compreender e valorizar os fundamentos da cidadania e da democracia, favorecendo uma atuação consciente do indivíduo na sociedade (abrange as habilidades H16, H17, H18, H19, H20).[11] [Ciências Humanas | Competência de Área 5] **Cartografia e Representação Espacial:** Utilizar os conhecimentos cartográficos para a compreensão e representação do espaço geográfico (abrange as habilidades H21, H22, H23, H24, H25).[11] [Ciências Humanas | Competência de Área 6] **Sociedade e Natureza:** Compreender a sociedade, a natureza e as relações entre elas nas diferentes escalas (abrange as habilidades H26, H27, H28, H29, H30).[11]

**ANEXO - OBJETOS DE CONHECIMENTO (CONTEÚDOS DETALHADOS)**

*[Linguagens, Códigos e suas Tecnologias]* [Objeto de Conhecimento | Linguagens] **Estudo do texto:** Sequências discursivas e os gêneros textuais no sistema de comunicação e informação.[12] [Objeto de Conhecimento | Linguagens] **Práticas corporais:** A linguagem corporal como integradora social e formadora de identidade (práticas corporais e autonomia, o esporte e as lutas).[12] [Objeto de Conhecimento | Linguagens] **Textos artísticos:** Produção e recepção de textos artísticos, interpretação e representação do mundo para o fortalecimento dos processos de identidade e cidadania da comunidade.[12] [Objeto de Conhecimento | Linguagens] **Texto literário:** Relações entre produção literária e processo social, concepções artísticas, procedimentos de construção e recepção de textos no patrimônio literário nacional.[12][13] [Objeto de Conhecimento | Linguagens] **Aspectos linguísticos em diferentes textos:** Recursos expressivos da língua, procedimentos de construção e recepção de textos.[13] [Objeto de Conhecimento | Linguagens] **Texto argumentativo:** Tipos, gêneros e recursos de argumentação e seus usos em língua portuguesa.[13] [Objeto de Conhecimento | Linguagens] **Usos da língua portuguesa:** Norma culta e variação linguística.[13] [Objeto de Conhecimento | Linguagens] **Gêneros digitais:** Tecnologia da comunicação e informação, seu impacto e função social.[13]

*[Matemática e suas Tecnologias]* [Objeto de Conhecimento | Matemática] **Conhecimentos numéricos:** Operações, razões, proporções e técnicas de contagem.[13][14] [Objeto de Conhecimento | Matemática] **Conhecimentos geométricos:** Grandezas, unidades de medida, escalas, comprimentos, áreas, volumes, ângulos, Teorema de Tales e trigonometria do ângulo agudo.[14] [Objeto de Conhecimento | Matemática] **Estatística e probabilidade:** Análise de dados, desvios e variância.[14] [Objeto de Conhecimento | Matemática] **Conhecimentos algébricos:** Equações, inequações e funções polinomiais, exponenciais e logarítmicas.[14] [Objeto de Conhecimento | Matemática] **Conhecimentos algébricos/geométricos:** Plano cartesiano e estudo de retas.[14]

*[Ciências da Natureza - Física]* [Objeto de Conhecimento | Física] **Conhecimentos básicos:** Sistema Internacional de Unidades e física do mundo mensurável.[14] [Objeto de Conhecimento | Física] **Mecânica, movimento e equilíbrio:** Conceito de inércia, centro de massa, ideia de ponto material, conservação do impulso e hidrostática (aspectos históricos e variáveis relevantes).[14][15] [Objeto de Conhecimento | Física] **Energia, trabalho e potência:** Conceito de energia potencial e de energia cinética.[15] [Objeto de Conhecimento | Física] **Mecânica celeste:** A Mecânica e o funcionamento do Universo.[15] [Objeto de Conhecimento | Física] **Fenômenos elétricos e magnéticos:** Carga elétrica, corrente elétrica, campo elétrico, potencial elétrico, poder das pontas, blindagem, capacitores, circuitos elétricos simples, correntes contínua e alternada, campo magnético, ímãs permanentes e campo magnético terrestre.[15] [Objeto de Conhecimento | Física] **Oscilações, ondas, óptica e radiação:** Óptica geométrica (lentes e espelhos), instrumentos ópticos simples, fenômenos ondulatórios, pulsos e ondas.[16] [Objeto de Conhecimento | Física] **Calor e fenômenos térmicos:** Conceitos de calor e temperatura, comportamento de gases ideais, ciclo de Carnot e compreensão de fenômenos climáticos relacionados ao ciclo da água.[16]

*[Ciências da Natureza - Química]* [Objeto de Conhecimento | Química] **Transformações químicas:** Teoria cinética dos gases, modelo de Rutherford-Bohr e estrutura do átomo.[16] [Objeto de Conhecimento | Química] **Representação das transformações:** Grandezas químicas (massa, volume, mol, massa molar e constante de Avogadro).[16] [Objeto de Conhecimento | Química] **Materiais e propriedades:** Propriedades dos materiais, elementos de relevância química (C, H, O, N, Cl) e polaridade de moléculas.[17] [Objeto de Conhecimento | Química] **Estudo da água:** Propriedades, tratamento e nomenclatura de compostos aquosos.[17] [Objeto de Conhecimento | Química] **Transformações químicas e energia:** Funcionamento de pilhas e conceitos fundamentais da radioatividade.[17] [Objeto de Conhecimento | Química] **Dinâmica e equilíbrio químico:** Velocidade de reação, catalisadores e conceitos de equilíbrio químico.[17] [Objeto de Conhecimento | Química] **Compostos de carbono:** Características gerais dos compostos orgânicos, borracha natural e sintética, proteínas e enzimas.[17] [Objeto de Conhecimento | Química] **Aplicações tecnológicas e socioambientais:** Química no cotidiano, química nos alimentos, e produção de amônia e ácido nítrico.[17] [Objeto de Conhecimento | Química] **Energias químicas no cotidiano:** Petróleo, gás natural, carvão, biomassa e vantagens/desvantagens do uso de energia nuclear.[18]

*[Ciências da Natureza - Biologia]* [Objeto de Conhecimento | Biologia] **Moléculas, células e tecidos:** Divisão celular, síntese proteica e principais tecidos animais e vegetais.[18] [Objeto de Conhecimento | Biologia] **Hereditariedade e genética:** Aspectos genéticos do funcionamento do corpo humano, antígenos, anticorpos e aconselhamento genético.[18] [Objeto de Conhecimento | Biologia] **Identidade dos seres vivos:** Vírus, procariontes, eucariontes, autótrofos, heterótrofos, seres unicelulares e pluricelulares, tipos de ciclo de vida, biotecnologia e sistemática.[18] [Objeto de Conhecimento | Biologia] **Ecologia e ciências ambientais.**[19] [Objeto de Conhecimento | Biologia] **Origem e evolução da vida.**[19] [Objeto de Conhecimento | Biologia] **Qualidade de vida das populações humanas.**[19]

*[Ciências Humanas e suas Tecnologias]* [Objeto de Conhecimento | Humanas] **Diversidade cultural, conflitos e vida em sociedade:** Cultura material e imaterial (patrimônio e diversidade cultural no Brasil); A Conquista da América (conflitos entre europeus e indígenas); Escravidão e resistências indígena e africana; História dos povos africanos e indígenas na formação da sociedade brasileira; e Movimentos culturais no mundo ocidental.[19] [Objeto de Conhecimento | Humanas] **Organização social, pensamento político e Estado:** Cidadania e democracia na Antiguidade; Estado e direitos a partir da Idade Moderna; Democracia direta, indireta e representativa; Revoluções sociais/políticas na Europa Moderna; Formação territorial e regiões brasileiras; Políticas de reordenamento territorial; Lutas pela independência na América; Grupos sociais no Brasil Imperial; Pensamento liberal e seus críticos nos séculos XIX e XX; Migração e imigração no Brasil; Revoluções do século XX (Bolchevique, Chinesa, Cubana); Geopolítica, Imperialismo, Guerras Mundiais e Guerra Fria; Totalitarismos (nazifascismo, franquismo, salazarismo, stalinismo); Ditaduras na América Latina e Estado Novo; Reorganização internacional e conflitos pós-Guerra Fria; Direitos civis, humanos, políticos e sociais; Direitos sociais nas constituições e políticas afirmativas; Vida urbana, hierarquia nas cidades, pobreza e segregação espacial.[20] [Objeto de Conhecimento | Humanas] **Estruturas produtivas:** Organização da produção (escravismo antigo, feudalismo, capitalismo, socialismo); Economia agroexportadora brasileira (açúcar, mineração colonial, café e borracha na Amazônia); Revolução Industrial e o sistema de fábrica; Formação do espaço urbano-industrial; Fordismo, toyotismo e novas técnicas de produção; Industrialização, urbanização e transformações trabalhistas no Brasil; Globalização, novas tecnologias de telecomunicação e suas consequências econômicas, políticas e sociais.[22][23] [Objeto de Conhecimento | Humanas] **Espaços agrários:** Modernização da agricultura e estruturas agrárias tradicionais; Agronegócio, agricultura familiar, assalariados do campo e lutas sociais no campo; e a Relação campo-cidade.[24] [Objeto de Conhecimento | Humanas] **Meio ambiente e sociedade:** Relação homem-natureza e apropriação de recursos ao longo do tempo; Impactos ambientais no Brasil; Recursos hídricos; Unidades de conservação, parques ecológicos e zoneamento ecológico-econômico.[24] [Objeto de Conhecimento | Humanas] **Representação espacial:** Cartografia e leitura do espaço geográfico.[24]

---

Analise o JSON de uma questão fornecido ao final e enriqueça-o. Retorne um novo objeto JSON contendo todos os campos originais inalterados na raiz e, ao final do objeto, os quatro novos campos descritos abaixo.

# REGRAS DE IDENTIFICAÇÃO PADRONIZADA (VALIDAÇÃO CARACTERE A CARACTERE)

Os campos `materias` e `conteudos` devem usar rótulos copiados literalmente da matriz de referência e dos objetos de conhecimento fornecidos no arquivo de referência. A validação será feita caractere a caractere. Qualquer diferença de acentuação, caixa, espaço interno, pontuação, barra, hífen, pipe, dois-pontos ou separador invalida o item. Conteúdos específicos não serão validados.

Regras específicas:

1. `materias` deve conter apenas os rótulos exatos das áreas de conhecimento, quando aplicáveis:
   - `Linguagens, Códigos e suas Tecnologias`
   - `Matemática e suas Tecnologias`
   - `Ciências da Natureza e suas Tecnologias`
   - `Ciências Humanas e suas Tecnologias`

2. `conteudos` deve conter strings isoladas, copiadas exatamente da matriz de referência ou do anexo de objetos de conhecimento, sem concatenar rótulos e sem acrescentar texto explicativo. Quando aplicável, devem ser adicionados os nomes de conteúdos específicos da questão. Use:
   - rótulos exatos de competência de área, sem os colchetes externos, no formato exato em que aparecem na matriz, por exemplo: `Linguagens | Competência de Área 1`; `Matemática | Competência de Área 2`; `Ciências da Natureza | Competência de Área 5`; `Ciências Humanas | Competência de Área 3`;
   - títulos exatos dos objetos de conhecimento, copiando apenas o título em negrito antes dos dois-pontos, por exemplo: `Estudo do texto`; `Práticas corporais`; `Conhecimentos numéricos`; `Mecânica, movimento e equilíbrio`; `Diversidade cultural, conflitos e vida em sociedade`.
   - nomes de conteúdos específicos não listados na matriz, por exemplo: `História de Porto Rico`; `Feminismo na Primeira República`.

3. Não inclua em `conteudos` o prefixo `Objeto de Conhecimento`, a área, os dois-pontos, a descrição após os dois-pontos, marcadores, numeração, parênteses explicativos ou qualquer comentário adicional.

4. Não use sinônimos, traduções, abreviações, plurais, variações de caixa, correções ortográficas ou paráfrases. Não invente rótulos. Se não houver rótulo exato aplicável, não o inclua.

5. Quando houver mais de um item aplicável em `materias` ou `conteudos`, ordene-os na ordem em que aparecem na matriz de referência fornecida. Não duplique itens.

6. A área correspondente em `materias` deve constar sempre que um objeto de conhecimento ou competência de área for listado em `conteudos`.

# CAMPOS A ADICIONAR

1. `comentarios` (Array de Strings): Uma lista contendo exatamente 5 strings. Cada string deve ser um comentário didático e técnico explicando o porquê de a respectiva alternativa estar certa ou errada. A ordem das strings DEVE seguir rigorosamente a ordem das alternativas (A, B, C, D, E):
   - Índice 0: Comentário da alternativa A
   - Índice 1: Comentário da alternativa B
   - Índice 2: Comentário da alternativa C
   - Índice 3: Comentário da alternativa D
   - Índice 4: Comentário da alternativa E

2. `materias` (Array de Strings): Nome das matérias envolvidas na questão, usando exclusivamente os rótulos exatos de área definidos nas regras de identificação padronizada.

3. `conteudos` (Array de Strings): Lista dos tópicos, competências de área, objetos de conhecimento, palavras-chave e classificações curriculares abordadas na questão, usando exclusivamente rótulos literais definidos nas regras de identificação padronizada. Seja extensivo, criando rótulos novos ou compostos quando adequado (ex.: Eletrólise).

4. `dica` (String): Uma dica estratégica e reflexiva para guiar o raciocínio de um aluno que está "travado" na questão. A dica deve apontar o caminho do conceito, mas JAMAIS revelar a resposta correta ou qual é a alternativa gabarito.

# RESTRIÇÕES DE SAÍDA

- A saída deve ser APENAS o JSON válido e formatado.
- NÃO inclua saudações, explicações, raciocínios ou texto introdutório.
- NÃO envolva o JSON em blocos de código markdown (não use ```json ... ```). Retorne apenas a string JSON crua.
- Mantenha todas as chaves originais do JSON de entrada inalteradas na raiz.
- Adicione os quatro novos campos ao final do objeto JSON.
- Garanta que `comentarios` tenha exatamente 5 strings na ordem A, B, C, D, E.
- Garanta que `materias` e `conteudos` respeitem a validação caractere a caractere contra os rótulos da matriz de referência fornecida.

# JSON DE ENTRADA

{0}"""