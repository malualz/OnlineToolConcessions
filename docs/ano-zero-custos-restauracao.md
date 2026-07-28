# Custos de Ano 0 na análise custo-benefício de restauração

Documento analítico sobre a incorporação de linhas de custo de Ano 0 (pré-implantação e implantação
inicial) na plataforma de análise custo-benefício do projeto, que opera com indicadores econômicos
clássicos — valor presente líquido, taxa interna de retorno, razão benefício-custo e prazo de
retorno — sobre um horizonte de 20 anos, para três métodos de restauração: ANR (regeneração natural
assistida), semeadura direta (*seeding*) e plantio de mudas (*seedling*).

**Escopo.** O questionário de custos de restauração é tratado como ponto de partida para a
identificação de categorias e lacunas. Nenhuma recomendação deste documento se dirige à modificação
daquele questionário; o destino das linhas de custo é a plataforma de análise custo-benefício.

**Premissa sobre a plataforma-alvo.** Na ausência de especificação, o destino é tratado como um
modelo anual de fluxo de caixa incremental descontado, com indicadores derivados desse fluxo. As
recomendações são agnósticas de implementação e se expressam como atributos de linha de custo e
regras de mapeamento para o fluxo.

---

## Etapa 1 — Análise do site: NÃO REALIZADA

**O site `https://questionnaire-restoration.vercel.app/` não pôde ser acessado nesta sessão.**

A tentativa de acesso retornou `HTTP 403` na fase de CONNECT do proxy de egresso, registrada no
endpoint de status do proxy como `connect_rejected — gateway answered 403 to CONNECT (policy denial
or upstream failure)` para o host `questionnaire-restoration.vercel.app:443`. Trata-se de uma
negativa da política de rede do ambiente, não de indisponibilidade da aplicação. Conforme a política
do ambiente, negativas 403/407 não devem ser contornadas.

Busca web complementar não retornou conteúdo da aplicação.

### O que, em consequência, NÃO foi verificado

Nenhum elemento do conteúdo real do site foi verificado. Especificamente permanecem desconhecidos:

- as categorias de custo efetivamente presentes em cada aba (ANR, *seeding*, *seedling*);
- as unidades de medida e a periodicidade adotadas para cada categoria;
- o agrupamento das categorias e a existência de condicionalidades entre perguntas;
- a existência e o papel de campos de escala (área, densidade, espaçamento);
- quais custos de Ano 0 já estão total ou parcialmente capturados;
- se há tratamento temporal (desconto, horizonte) já implementado.

### Consequência metodológica para as etapas seguintes

As Etapas 2 a 5 foram elaboradas sem premissas sobre o conteúdo atual da ferramenta. As lacunas da
Etapa 2 estão formuladas de modo condicional: descrevem custos que uma análise custo-benefício de
restauração precisa capturar, com a ressalva de que a verificação de ausência depende de inspeção do
site. Cada item da Etapa 2 traz uma coluna de status de verificação com o valor `não verificado`.

### Protocolo de mapeamento a executar quando houver acesso

Estrutura sugerida para o registro do levantamento, a ser preenchida por aba:

| Campo do levantamento | Conteúdo a registrar |
|---|---|
| Aba | ANR / *seeding* / *seedling* |
| Grupo/seção | Rótulo do agrupamento na interface |
| Categoria de custo | Rótulo exato apresentado ao usuário |
| Objeto do custo | O que a categoria captura (insumo, serviço, ativo, encargo) |
| Unidade | Unidade de entrada e unidade de saída (por ha, por muda, por evento, valor absoluto) |
| Periodicidade | Único / recorrente anual / recorrente por evento / condicional |
| Modulador de escala | Qual campo (área, densidade, espaçamento, nº de mudas) multiplica o custo |
| Condicionalidade | Pergunta que habilita ou suprime o campo |
| Ano de incidência | Se a ferramenta atribui o custo a um ano específico do horizonte |

E, para a comparação entre métodos, uma matriz binária categoria × aba (presente / ausente /
presente com definição distinta), da qual se extrai o conjunto comum e os conjuntos específicos.

---

## Etapa 2 — Lacunas de Ano 0

Legenda de compartilhamento:
**D** = dedicado ao projeto e ao método; **CM** = compartilhável entre métodos dentro do mesmo
projeto; **CP** = compartilhável entre projetos ou entre safras/ciclos; **T** = tipicamente
terceirizável, caso em que o custo migra para o preço unitário de um insumo ou serviço.

| # | Custo de Ano 0 | Descrição técnica | ANR | Seeding | Seedling | Compartilhamento | Relevância esperada | Verificação no site |
|---|---|---|---|---|---|---|---|---|
| 1 | Infraestrutura física de viveiro | Canteiros, bancadas, estufa/casa de vegetação, sombrite, telado, galpão de substrato, área de rustificação, cercamento do viveiro | Parcial (enriquecimento) | Não | Sim | CP, T | Alta para *seedling*; nula para *seeding* puro | não verificado |
| 2 | Sistemas e equipamentos de viveiro | Captação e adução de água, irrigação (aspersão/nebulização), reservatório, bombeamento, energia/gerador, misturador de substrato, encanteirador, ferramental | Parcial | Não | Sim | CP, T | Alta para *seedling* | não verificado |
| 3 | Capital de giro da produção de mudas | Insumos consumíveis (tubetes, substrato, fertilizantes, defensivos), mão de obra de viveiro, perdas por mortalidade e descarte de padrão, custo do ciclo de produção que antecede o plantio | Parcial | Não | Sim | D, T | Alta para *seedling*; introduz defasagem temporal relevante | não verificado |
| 4 | Coleta de sementes | Identificação e cadastro de matrizes, expedições de coleta, mão de obra especializada, escalada e EPI, transporte, sazonalidade e repetição de safras para compor diversidade | Parcial | Sim | Sim | CM, CP, T | Alta para *seeding*; dominante quando há exigência de riqueza específica | não verificado |
| 5 | Beneficiamento e armazenamento de sementes | Casa de sementes, secagem, extração, peneiramento, tratamento pré-germinativo, câmara fria e desumidificação, embalagens | Parcial | Sim | Sim | CM, CP, T | Média a alta para *seeding* | não verificado |
| 6 | Análise e controle de qualidade de sementes | Testes de germinação, pureza, viabilidade, teor de umidade; laudos por lote | Parcial | Sim | Sim | D por lote, CP quanto ao laboratório | Média; condiciona a taxa de semeadura | não verificado |
| 7 | Registro e certificação de sementes e mudas | Registro do produtor em sistema nacional de sementes e mudas, inscrição de campos de produção e de matrizes, termos de conformidade, cadeia de custódia e rastreabilidade | Parcial | Sim | Sim | CP | Média; predominantemente fixo, sensível à escala | não verificado |
| 8 | Certificação ambiental e de carbono | Documento de concepção do projeto, validação inicial por terceira parte, taxa de registro em *registry*, estudo de adicionalidade e cenário de referência, definição de fronteira e de vazamento, auditoria de linha de base | Sim | Sim | Sim | CM, CP | Alta em projetos com receita de crédito; fixo e regressivo com a escala | não verificado |
| 9 | Certificação de manejo e cadeia de custódia | Certificação florestal e auditoria inicial, quando há componente madeireiro ou de produtos florestais no fluxo de benefícios | Sim | Sim | Sim | CM, CP | Condicional ao modelo de receita | não verificado |
| 10 | Diagnóstico ecológico | Levantamento florístico e fitossociológico, avaliação do potencial de regeneração natural (banco e chuva de sementes, rebrota, matrizes remanescentes, matriz de paisagem), identificação de fatores de degradação | Sim | Sim | Sim | CM | Alta; para ANR é o custo que determina a elegibilidade do método | não verificado |
| 11 | Diagnóstico físico do meio | Análise química e física de solo, compactação, drenagem, erosão, hidrologia, risco de inundação | Sim | Sim | Sim | CM | Média; condiciona preparo de solo e escolha de método | não verificado |
| 12 | Projeto técnico de restauração | Elaboração do plano/projeto, prescrição por unidade de manejo, definição de espécies e densidades, cronograma, responsabilidade técnica | Sim | Sim | Sim | CM | Média a alta | não verificado |
| 13 | Georreferenciamento e demarcação | Levantamento planialtimétrico, delimitação de polígonos, aerolevantamento e ortomosaico inicial, marcos físicos, estratificação de talhões | Sim | Sim | Sim | CM | Média; insumo compartilhado com monitoramento e certificação | não verificado |
| 14 | Licenciamento e conformidade regulatória | Cadastro ambiental, adesão a programa de regularização, protocolo e aprovação do projeto junto ao órgão ambiental, autorizações específicas (supressão, controle de exóticas, uso de fogo controlado), outorga de uso de água e licença de operação do viveiro, anotações de responsabilidade técnica | Sim | Sim | Sim | CM | Média; fortemente fixo por projeto | não verificado |
| 15 | Regularização fundiária e comprovação dominial | Verificação e regularização de titularidade, sobreposições, servidão ambiental, anuências de terceiros, instrumentos de posse e uso da área | Sim | Sim | Sim | CM | Alta quando é condição precedente para contratar ou certificar | não verificado |
| 16 | Acesso e infraestrutura de campo | Abertura e recuperação de estradas internas e carreadores, travessias e drenagem, barracão/apoio de campo, ponto de água | Sim | Sim | Sim | CM | Média; escala com distância e topografia, não com área | não verificado |
| 17 | Isolamento da área | Cercamento, porteiras, mata-burros, retirada de gado, aceiros iniciais e estruturação da prevenção de incêndio | Sim | Sim | Sim | CM | Alta, e desproporcionalmente alta para ANR, onde é o núcleo da intervenção | não verificado |
| 18 | Controle inicial de fatores de degradação | Controle de gramíneas exóticas competidoras, combate inicial a formigas cortadeiras, controle de espécies invasoras lenhosas | Sim | Sim | Sim | D | Alta; risco de sobreposição com itens já capturados em implantação | não verificado |
| 19 | Mobilização e logística inicial | Deslocamento de equipes e maquinário até a área, alojamento, transporte de insumos, montagem de canteiro de obra | Sim | Sim | Sim | CM | Média; escala com distância e com o número de frentes | não verificado |
| 20 | Capacitação de equipes | Treinamento técnico em coleta, viveiro, semeadura, plantio e operação de máquinas; treinamentos de segurança do trabalho e certificações obrigatórias de operadores | Sim | Sim | Sim | CM, CP | Média; recorrente sob rotatividade, com componente inicial concentrado | não verificado |
| 21 | Mobilização social e engajamento comunitário | Articulação com comunidades e proprietários vizinhos, reuniões de apresentação, acordos de uso, consulta livre, prévia e informada quando aplicável, comunicação e gestão de conflitos | Sim | Sim | Sim | CM | Média a alta; frequentemente omitido e condicionante do risco de execução | não verificado |
| 22 | Estruturação do monitoramento | Definição do protocolo, inventário de linha de base, estoque inicial de carbono e de solo, instalação e marcação de parcelas permanentes, sistema de gestão de dados, equipamentos de campo | Sim | Sim | Sim | CM, CP | Média; separável entre componente inicial e recorrente | não verificado |
| 23 | Custos de transação jurídico-financeiros | Elaboração e negociação de contratos de execução, de aquisição de insumos e de comercialização de resultados; *due diligence* socioambiental e jurídica; estruturação financeira, garantias e custo de originação | Sim | Sim | Sim | CM, CP | Alta em projetos com financiamento externo ou venda de créditos | não verificado |
| 24 | Seguros e reserva de contingência | Seguro contra fogo, seca e perda de plantio; provisão para replantio; constituição de reserva de risco (*buffer*) quando exigida por padrão de certificação | Sim | Sim | Sim | CM | Média; a reserva de *buffer* não é desembolso, mas reduz receita | não verificado |
| 25 | Overhead de estruturação | Custo de gestão, coordenação técnica e administração incorrido antes do início operacional | Sim | Sim | Sim | CM, CP | Média; alto risco de dupla contagem com taxa de administração recorrente | não verificado |

### Observações sobre a distribuição entre métodos

Três assimetrias estruturam a comparação. Primeira: a cadeia de propágulos separa os métodos —
*seedling* depende de viveiro e de capital de giro de produção, *seeding* depende de coleta,
beneficiamento e armazenamento em volume, ANR depende de nenhum dos dois exceto quando há
enriquecimento. Segunda: o diagnóstico de potencial de regeneração natural é um custo de Ano 0 cuja
função é decidir se ANR é viável; ele antecede a escolha do método e não pertence a nenhum método
isoladamente. Terceira: isolamento da área e controle de fatores de degradação são custos comuns aos
três métodos, mas seu peso relativo é máximo em ANR, onde constituem a própria intervenção.

Os itens 8 a 15 e 19 a 25 são majoritariamente fixos por projeto: não escalam com a área nem com o
método. Sua omissão subestima sistematicamente o custo de projetos pequenos e distorce a comparação
entre métodos pela via da escala mínima viável de cada um.

---

## Etapa 3 — Abordagens de inserção, sob o filtro do fluxo de caixa descontado

### Premissa: o insumo da plataforma é fluxo de caixa, não competência

Indicadores de valor presente e de taxa interna de retorno operam sobre o fluxo de caixa incremental
do projeto: importam o montante e o momento em que o recurso sai ou entra do caixa. Isso separa as
abordagens candidatas em duas classes de natureza distinta.

A primeira classe opera sobre a **fronteira** da análise — define qual parcela do desembolso pertence
ao projeto avaliado. Rateio por uso, rateio por método, valor residual, preço-sombra por
terceirização e tratamento de programa pertencem a essa classe. Todas alteram o valor que entra no
fluxo, e são legítimas em um modelo de fluxo descontado porque respondem à pergunta correta: quanto
deste desembolso é atribuível ao projeto.

A segunda classe opera sobre a **distribuição temporal** de um desembolso já integralmente atribuível
ao projeto. Amortização e depreciação pertencem a essa classe. Não são fluxo de caixa: redistribuir
contabilmente um desembolso já ocorrido reduz o valor presente do custo sem que nada de real tenha
mudado, elevando artificialmente o VPL e a TIR. **A única via legítima pela qual a depreciação afeta
o fluxo de caixa é o escudo fiscal**, quando o modelo incorpora tributação sobre resultado: nesse
caso a depreciação reduz a base tributável, e a economia de imposto é um efeito de caixa real. Fora
desse caso, amortização não deve entrar no fluxo.

Uma terceira observação separa entrada de saída: o custo equivalente anual não é um tratamento de
insumo, e sim uma métrica derivada do valor presente. Pertence ao conjunto de indicadores de
resultado, ao lado de VPL e TIR, não ao conjunto de regras de lançamento.

### Classificação das abordagens quanto à admissibilidade no modelo

| Abordagem | Classe | Admissível como lançamento no fluxo | Observação |
|---|---|---|---|
| A. Custo integral no ano de incidência | Fluxo | Sim | Caso base; exige apenas valor e ano |
| B. Amortização contábil | Competência | Não, salvo escudo fiscal | Só entra como efeito tributário, se houver tributação modelada |
| C. Rateio por uso da capacidade | Fronteira | Sim | Reduz o valor lançado; não altera o momento |
| D. Rateio por método | Fronteira | Sim | Necessário apenas se o resultado for reportado por método |
| E. CAPEX com valor residual | Fluxo | Sim | Desembolso integral no ano de incidência, entrada terminal no ano final |
| F. Fator paramétrico | Estimador de valor | Sim, com alocação explícita a um ano | É método de estimativa, não de distribuição temporal |
| G. Preço-sombra por terceirização | Fronteira | Sim | Substitui a modelagem do ativo pelo preço do serviço |
| H. Custo equivalente anual | Métrica de saída | Não | Derivado do valor presente, não insumo |
| I. Ciclos de reposição | Fluxo | Sim | Lançamentos negativos intercalados no horizonte |
| J. Programa fora da fronteira | Fronteira | Sim | Entra apenas a fração alocada, via preço interno de transferência |
| K. Tratamento condicional | Gatilho | Sim | Inclui ou suprime a linha conforme atributo do projeto |

### Discussão por abordagem

**A. Custo integral no ano de incidência.** Adequada para ativo ou serviço dedicado, consumido dentro
do horizonte, sem valor de revenda: diagnóstico, projeto técnico, licenciamento, mobilização,
controle inicial de degradação, validação inicial de certificação. É também o tratamento correto para
ativos compartilháveis quando a fronteira da análise é o programa inteiro. Distorce quando aplicada a
ativo compartilhável com vida superior ao horizonte ou usado por projetos paralelos: imputa a um
projeto a capacidade que ele não consome sozinho, penalizando *seedling* pelo viveiro e *seeding*
pela estrutura de sementes. O ponto de atenção é o ano de referência: parte dos custos de Ano 0 ocorre
no período anterior à implantação — produção de mudas, coleta na safra precedente, validação prévia,
estruturação contratual —, e comprimi-los todos no período inicial subestima o valor presente do
custo.

**B. Amortização.** O critério linear pelo horizonte é duplamente problemático: além de não ser fluxo
de caixa, vincula a alocação à duração da análise e não ao ativo, de modo que alterar o horizonte
mudaria o custo anual sem que nada físico mudasse. O critério por vida útil é conceitualmente melhor,
mas sua função correta em um modelo de fluxo é outra: determinar quando há reposição dentro do
horizonte (abordagem I) e quanto sobra ao final (abordagem E). Ou seja, a vida útil é um dado
necessário, mas seu uso não é amortizar — é temporizar reposições e calcular residual.

**C. Rateio por uso.** Conceitualmente a mais correta para ativos de capacidade divisível: separa o
custo da capacidade instalada do custo do serviço consumido, e resolve o viveiro superdimensionado,
deixando a ociosidade com quem detém o ativo. Exige uma definição de capacidade que raramente é
única — a capacidade de um viveiro varia com número de ciclos anuais, tamanho de recipiente e
espécie produzida. Sem padronizar a unidade de capacidade, a fração alocada se torna manipulável e o
VPL, não auditável. Melhora a comparabilidade entre métodos, desde que a mesma lógica se aplique à
infraestrutura de sementes em *seeding*, sob pena de assimetria de tratamento.

**D. Rateio por método.** Necessário quando o projeto é um mosaico de métodos e a plataforma reporta
resultado por método. Os critérios possíveis — área tratada, participação no custo direto,
intensidade de uso do recurso comum, atribuição direta — produzem resultados distintos. Diagnóstico,
licenciamento, georreferenciamento, engajamento e estruturação contratual não têm causalidade clara
com nenhum método; para eles, rateio por área é convenção, não medida. Isolamento e controle de
degradação têm causalidade parcial, mais intensiva em ANR. Cadeia de propágulos é atribuível
diretamente. O risco específico: rateio por área aplicado indistintamente transfere custo fixo para o
método que ocupa mais área, penalizando ANR — justamente o método aplicado em maior escala por exigir
menor intensidade —, o que inverte a conclusão que a análise deveria produzir. Recomenda-se que a
plataforma reporte o custo comum de forma segregada, além de rateado, e que a TIR por método seja
calculada apenas sobre fluxos atribuíveis, com o custo comum tratado em nível de projeto.

**E. CAPEX com valor residual.** Para ativos duráveis com vida superior ao horizonte e com valor de
uso ou revenda ao final. Preserva o perfil real de desembolso e reconhece o não consumido como
entrada terminal. Sob desconto a 20 anos, o residual tem peso reduzido, de modo que a abordagem se
aproxima de A quanto maior a taxa; ainda assim, seu efeito sobre a TIR não é desprezível, porque um
fluxo positivo terminal altera o padrão de sinais. Presume liquidez ou continuidade de uso que pode
não existir: um viveiro construído para um projeto específico em local remoto pode ter residual
próximo de zero independentemente do estado físico. Combinar E com B é dupla contagem.

**F. Fator paramétrico.** Multiplicador sobre custo direto para custos difusos. Como estimador de
valor é aceitável; o problema é a hipótese de proporcionalidade, falsa justamente onde a abordagem é
mais tentadora — certificação, licenciamento e diagnóstico são fixos por projeto e decrescem como
fração do custo direto conforme a área cresce. Um fator constante superestima projetos grandes e
subestima pequenos, que é o erro na direção mais prejudicial, porque é no projeto pequeno que o custo
fixo determina a viabilidade. Aplicado sobre custo direto, penaliza *seedling* por custos que não
dependem do método, e o efeito fica embutido no fator, sem transparência para quem lê o VPL.

**G. Preço-sombra por terceirização.** Adotar o preço da muda entregue em vez de modelar viveiro, o
preço da semente beneficiada em vez de modelar casa de sementes. Reflete a estrutura real da maioria
dos projetos e internaliza depreciação, capital de giro e margem no preço unitário, dispensando
rateio. Oculta a diferença entre produzir e comprar, que pode ser a decisão que a análise quer
informar, e importa a margem do fornecedor — correto na perspectiva financeira do projeto, incorreto
na perspectiva econômica ou social, distinção que importa se a plataforma pretende reportar VPL sob
ambas as óticas. Dupla contagem grave se coexistir com CAPEX de viveiro.

**I. Ciclos de reposição.** Complemento necessário a qualquer abordagem, não alternativa. Cercas,
aceiros, telas, sistemas de irrigação e equipamentos de campo não sobrevivem a 20 anos. Em ANR, onde
o isolamento é a intervenção central, omitir a reposição de cercamento subestima o custo do método
mais barato, reforçando indevidamente a conclusão da comparação. Há um efeito específico sobre a TIR
discutido adiante: reposições introduzem fluxos negativos intercalados.

**J. Programa fora da fronteira.** Manter o ativo compartilhado fora da fronteira, com entrada apenas
da fração alocada via preço interno de transferência. Adequada quando a plataforma avalia projetos
dentro de um programa que já detém infraestrutura, e torna explícito que a decisão sobre o ativo não
pertence ao projeto avaliado. Se o preço interno for arbitrado abaixo do custo, transfere subsídio
implícito e produz VPL positivo às custas do programa.

**K. Tratamento condicional.** Parte dos custos de Ano 0 é contingente: certificação só se materializa
sob decisão de comercializar créditos; regularização fundiária só sob pendência dominial; capacitação
varia com a existência de equipe prévia. O tratamento correto é condicionar a inclusão da linha a um
atributo declarado do projeto, e não estimar valor esperado ponderado por probabilidade — este último
produziria um custo que não corresponde a nenhum projeto real e contaminaria o VPL de todos os
cenários. Probabilidade é instrumento de análise de risco sobre o resultado, não de composição do
fluxo determinístico.

### Efeitos específicos sobre cada indicador

**Valor presente líquido.** O período inicial não é descontado, de modo que cada unidade monetária de
Ano 0 entra no VPL com o peso máximo possível. Isso torna as linhas de Ano 0 as de maior alavancagem
sobre o resultado por unidade de valor, e as primeiras candidatas à análise de sensibilidade. A
consequência prática é que erros de escopo no Ano 0 — omissão ou dupla contagem — deslocam o VPL mais
do que erros de igual magnitude em qualquer ano posterior.

**Taxa interna de retorno.** O custo de Ano 0 define a magnitude do desembolso inicial e, portanto, é
o principal determinante da TIR. Dois cuidados são específicos: reposições (I) e verificações
periódicas de certificação introduzem fluxos negativos intercalados entre fluxos positivos; quando o
sinal do fluxo líquido muda mais de uma vez ao longo dos 20 anos, a TIR pode ser múltipla ou
inexistente, e perde interpretação como critério de decisão. Nesses casos a plataforma precisa
detectar a mudança de sinal e reportar taxa interna de retorno modificada, ou restringir a decisão ao
VPL. O segundo cuidado: em configurações sem receita monetizada — restauração por obrigação legal,
sem venda de créditos nem produto —, o fluxo é integralmente negativo e a TIR não existe. A
comparação entre métodos deve então se dar por valor presente dos custos, custo equivalente anual e
indicadores de custo-efetividade, e não por TIR.

**Razão benefício-custo.** Classificar uma linha de Ano 0 como custo no denominador ou como redução
de benefício no numerador altera a razão sem alterar o VPL. A reserva de risco exigida por padrões de
certificação é o caso mais claro: não é desembolso, é retenção de crédito, e seu lugar natural é
como redução de receita. Sem uma regra fixa de classificação, a razão benefício-custo deixa de ser
comparável entre projetos e entre métodos, mesmo com VPL correto.

**Prazo de retorno.** Custos de Ano 0 deslocam a data de recuperação, e o efeito é desproporcional
para *seedling*, cujo desembolso inicial é maior. O prazo descontado deve ser preferido ao simples,
sob pena de premiar métodos com desembolso concentrado no início.

**Capital de giro.** A convenção clássica é que o capital de giro imobilizado é recuperado ao final
do horizonte, como entrada terminal. Aplicada à produção de mudas, a convenção só faz sentido se
houver estrutura continuada de produção; em projeto único, o capital de giro é consumido e não
retorna. A escolha precisa ser declarada, porque afeta VPL e TIR na mesma direção do valor residual.

**Consistência de preços e taxa.** Custos de Ano 0 tendem a ser levantados em preços correntes, e
receitas de longo prazo — crédito de carbono, madeira — costumam ser projetadas em séries nominais.
Misturar as duas bases dentro do mesmo fluxo produz erro sistemático que nenhuma escolha de alocação
corrige. A plataforma precisa declarar se opera em termos reais ou nominais e aplicar a taxa de
desconto correspondente.

**Custos afundados.** Diagnóstico, projeto técnico e estruturação frequentemente já foram incorridos
quando a análise é feita. Para uma decisão marginal — prosseguir ou não —, não são incrementais e não
deveriam entrar. Para uma avaliação ex-ante do projeto completo, entram. A plataforma precisa
distinguir os dois usos, porque a mesma linha de custo muda de status conforme a pergunta.

---

## Etapa 4 — Recomendação por categoria

A coluna de lançamento indica como a linha entra no fluxo de caixa da plataforma. `t0` designa o
período inicial; `t−1` designa desembolso anterior à implantação; `tn` designa o ano final do
horizonte; `recorrente` indica lançamento em anos subsequentes segundo periodicidade própria.

| # | Custo | Abordagem | Lançamento no fluxo | Justificativa | Dados necessários |
|---|---|---|---|---|---|
| 1 | Infraestrutura de viveiro | G padrão; C+E se produção própria | G: embutido no preço unitário. C+E: saída em `t0` pela fração alocada, entrada residual em `tn` | A maioria dos projetos compra mudas e o preço internaliza a estrutura; com viveiro próprio o projeto consome fração da capacidade e o ativo sobrevive ao horizonte | Regime de suprimento; valor investido; capacidade nominal anual e unidade; volume demandado; vida útil; critério de residual |
| 2 | Equipamentos de viveiro | C+I | Saída em `t0` pela fração alocada; saídas de reposição nos anos de fim de vida útil | Vida útil inferior à da estrutura civil, com reposição dentro do horizonte | Valor por classe; vida útil; ciclos de reposição; fração de uso |
| 3 | Capital de giro da produção de mudas | A, com convenção declarada de recuperação | Saída em `t−1`; entrada em `tn` apenas se houver estrutura continuada | É consumo, não ativo; a defasagem entre produção e plantio afeta o valor presente | Ciclo de produção em meses; mortalidade e descarte; custo unitário; decisão sobre recuperação do giro |
| 4 | Coleta de sementes | A se dedicada; C se estrutura compartilhada; G se compra | Saída em `t−1` ou `t0` conforme a safra; recorrente se houver replantio | Custo operacional atribuível ao lote; a estrutura de apoio é que é compartilhável | Origem das sementes; volume por espécie; nº de expedições; distância |
| 5 | Beneficiamento e armazenamento | C+E para ativos; A para operação | Ativos: saída em `t0` pela fração alocada, residual em `tn`. Operação: saída no ano do lote | Câmara fria e casa de sementes são capacidade divisível e durável; a operação é consumo do lote | Valor dos ativos; capacidade e ocupação; vida útil; custo operacional por lote |
| 6 | Análise de qualidade de sementes | A, por lote | Saída no ano do lote | Recorrente por lote, atribuível, sem componente de ativo relevante | Nº de lotes e espécies; custo por análise |
| 7 | Registro de sementes e mudas | A, com rateio D se projeto misto | Saída em `t0` e nos anos de renovação | Fixo por produtor e por período, sem relação com o volume do projeto | Obrigatoriedade aplicável; periodicidade de renovação; base de rateio |
| 8 | Certificação ambiental e de carbono | K para inclusão; A para o componente inicial | Saída em `t0` para validação e registro; saídas recorrentes nos anos de verificação | Fixo por projeto, condicional à comercialização, com componente inicial distinto do recorrente — a separação evita que a verificação periódica seja tratada como custo de Ano 0 | Decisão de comercialização; padrão; escopo e área; periodicidade de verificação; custo de validação e de registro |
| 9 | Certificação de manejo | K para inclusão; A para auditoria inicial | Saída em `t0`; recorrente conforme ciclo de auditoria | Condicional ao modelo de receita; não incide em restauração sem componente comercial | Existência de componente madeireiro; padrão; escopo |
| 10 | Diagnóstico ecológico | A, com rateio D declarado, e status de afundado declarado | Saída em `t−1` ou `t0` | Antecede a escolha do método; atribuí-lo a um método induz erro de comparação; é o candidato mais frequente a custo afundado | Área diagnosticada; unidades amostrais; fração de área por método; se já incorrido |
| 11 | Diagnóstico físico do meio | A, com rateio D declarado | Saída em `t−1` ou `t0` | Mesma natureza do item 10 | Nº de amostras de solo; área; profundidades |
| 12 | Projeto técnico de restauração | A, com rateio D declarado | Saída em `t−1` ou `t0` | Fixo por projeto, escala fracamente com a área | Área; unidades de manejo; regime de contratação do responsável técnico |
| 13 | Georreferenciamento e demarcação | A no `t0`; reaquisição sob I | Saída em `t0`; saídas nos anos de reaquisição de imagens | O levantamento inicial é único; sobrevoos de acompanhamento pertencem ao monitoramento e não ao Ano 0 | Área; método de levantamento; frequência de reaquisição |
| 14 | Licenciamento e conformidade | A, com K por autorização específica | Saída em `t0`; recorrente nos anos de renovação de licença ou outorga | Fixo por projeto, com itens condicionais à situação regulatória da área | Situação regulatória; autorizações aplicáveis; taxas; outorga de água; validade das licenças |
| 15 | Regularização fundiária | K para inclusão; A quando incide | Saída em `t−1` ou `t0` | Não incide em áreas regulares; quando incide, é condição precedente e custo concentrado | Situação dominial; pendências; instrumento de uso da área |
| 16 | Acesso e infraestrutura de campo | A para abertura; I para conservação | Saída em `t0`; saídas recorrentes de conservação | Investimento inicial único; conservação recorrente e frequentemente omitida | Extensão de acessos; condição inicial; distância; regime de conservação |
| 17 | Isolamento da área | A para implantação; I obrigatório para reposição | Saída em `t0`; saídas nos anos de fim de vida útil da cerca; manutenção de aceiro recorrente | Vida útil de cercas e aceiros é inferior ao horizonte; omitir a reposição subestima ANR de forma assimétrica e distorce a comparação entre métodos | Perímetro; tipo de cerca; vida útil; extensão de aceiro; pressão externa |
| 18 | Controle inicial de degradação | A, com verificação de fronteira contra implantação | Saída em `t0`, eventualmente repartida entre `t0` e `t1` | Custo real de Ano 0, com alta sobreposição com preparo de área já capturado em implantação | Nível de infestação; nº de operações; método; declaração do que já está em implantação |
| 19 | Mobilização e logística inicial | A | Saída em `t0` | Desembolso único, escala com distância e número de frentes, não com área | Distância à base; frentes; alojamento |
| 20 | Capacitação de equipes | A para o inicial; I para reciclagem | Saída em `t0`; saídas recorrentes de reciclagem | Componente inicial concentrado, com necessidade de reciclagem sob rotatividade | Tamanho da equipe; treinamentos obrigatórios; rotatividade esperada |
| 21 | Mobilização social e engajamento | A, com rateio D e componente recorrente segregado | Saída em `t−1`/`t0`; saídas recorrentes de relacionamento | Fixo por projeto e por contexto social, sem relação com o método | Partes interessadas; território tradicional; exigência de consulta; nº de eventos |
| 22 | Estruturação do monitoramento | A para linha de base e parcelas; C ou G para equipamentos; recorrente segregado | Saída em `t0` para linha de base e instalação; equipamentos pela fração alocada com reposição; medições recorrentes | A linha de base é única e irreproduzível; equipamentos são compartilháveis; medições posteriores não são custo de Ano 0 | Nº de parcelas; protocolo; equipamentos e vida útil; frequência de medição |
| 23 | Custos de transação | A, com K para financiamento externo | Saída em `t−1` ou `t0`; custo de originação eventualmente vinculado ao desembolso do financiamento | Concentrado no início, ausente em projetos autofinanciados, e não proporcional ao custo direto | Existência de financiamento externo; nº e complexidade de contratos; *due diligence*; estrutura de garantias |
| 24 | Seguros e contingência | I para o prêmio; reserva de *buffer* como redução de receita | Prêmio: saída recorrente. Reserva: dedução do fluxo de receita, não linha de custo | O prêmio é fluxo anual e não pertence ao Ano 0; a reserva não é desembolso e lançá-la como custo distorce a razão benefício-custo | Contratação de seguro; percentual de reserva do padrão; base de incidência |
| 25 | Overhead de estruturação | F como último recurso, declarando o que substitui | Saída em `t0`, valor derivado de fator sobre custo direto | Única categoria em que o tratamento paramétrico se justifica, e apenas quando os itens específicos não são coletados | Percentual adotado; base de incidência; lista dos itens substituídos |

### Regras de consistência

Cinco regras evitam os erros mais prováveis na plataforma.

Primeira, exclusividade entre G e as abordagens de ativo: sob suprimento terceirizado, os blocos de
CAPEX de viveiro e de estrutura de sementes devem ser suprimidos do fluxo, não zerados manualmente.

Segunda, exclusividade entre F e as linhas específicas que o fator representa.

Terceira, separação obrigatória entre componente inicial e recorrente nas categorias 8, 13, 16, 17,
20, 21 e 22. Em todas há um custo de Ano 0 e um custo anual de mesma natureza; a ausência dessa
separação produz simultaneamente dupla contagem em `t0` e subestimação nos anos seguintes, com efeito
oposto sobre VPL e TIR que pode se cancelar parcialmente e mascarar o erro.

Quarta, exclusividade entre B e as abordagens E e I: um ativo não pode ser amortizado, reposto e ter
residual reconhecido ao mesmo tempo.

Quinta, verificação de sinais do fluxo líquido antes de reportar TIR, com bloqueio ou qualificação do
indicador quando houver mais de uma inversão.

---

## Etapa 5 — Incorporação das linhas de custo na plataforma de análise custo-benefício

### Esquema de atributos da linha de custo

A recomendação central é que cada custo de Ano 0 entre na plataforma como uma linha com atributos
explícitos, e não como um valor agregado. São os atributos, e não o valor, que permitem à plataforma
derivar o lançamento correto no fluxo, aplicar as regras de consistência e sustentar sensibilidade.

| Atributo | Conteúdo | Função no modelo |
|---|---|---|
| Identificador e categoria | Código estável e categoria da Etapa 2 | Rastreabilidade e agregação |
| Natureza econômica | CAPEX, OPEX, capital de giro, encargo regulatório, custo de transação, item não-caixa | Determina o tratamento: residual, recuperação, dedutibilidade |
| Período de incidência | Ano relativo ao início da implantação, admitindo valores negativos | Posiciona o lançamento no fluxo; sem isso, todo Ano 0 colapsa em `t0` |
| Periodicidade | Único, recorrente anual, recorrente por ciclo, por evento | Gera os lançamentos subsequentes |
| Base de escala | Fixo por projeto, por hectare, por perímetro, por muda, por lote, por distância | Define o que multiplica o valor e como o custo se comporta com o tamanho do projeto |
| Método aplicável | ANR, *seeding*, *seedling*, comum | Habilita o rateio por método e o reporte de custo atribuível |
| Regime de compartilhamento | Dedicado, compartilhado entre métodos, compartilhado entre projetos, terceirizado | Seleciona a abordagem de fronteira |
| Fração alocada e critério | Valor e base do rateio | Torna auditável a parcela lançada |
| Vida útil | Anos | Gera reposições e residual; não gera amortização |
| Política de reposição | Reposição integral, parcial, ou não reposição | Define os lançamentos negativos intercalados |
| Valor residual e critério | Valor e base (contábil, mercado, uso continuado, zero) | Entrada terminal |
| Condição de existência | Atributo do projeto que aciona a linha | Implementa o tratamento condicional |
| Tratamento fiscal | Depreciável, dedutível, não dedutível | Único canal legítimo da depreciação para o fluxo |
| Marcador de fronteira | Referência às linhas com sobreposição conhecida | Prevenção de dupla contagem |
| Status de incremento | Incremental ou afundado | Permite alternar entre avaliação ex-ante e decisão marginal |
| Origem e confiabilidade do valor | Cotação, referência de mercado, estimativa paramétrica, valor histórico | Base para faixas de sensibilidade |

### Agrupamento das linhas na plataforma

A separação recomendada não é por método, porque a maior parte dos custos de Ano 0 é fixa por projeto.
Três blocos de lançamento, agregados no mesmo fluxo mas rastreáveis separadamente:

1. **Custos comuns de projeto** — diagnóstico, planejamento, licenciamento, regularização,
   georreferenciamento, acesso, isolamento, mobilização, capacitação, engajamento, monitoramento
   inicial, certificação, transação. Entram no fluxo do projeto e, se houver reporte por método,
   apenas então são rateados, com o critério explicitado.
2. **Custos de cadeia de propágulos** — viveiro, capital de giro de mudas, coleta, beneficiamento,
   armazenamento, análise de qualidade. Atribuíveis diretamente a *seeding* e *seedling*, e a ANR
   apenas sob enriquecimento.
3. **Custos de intensidade específica por método** — controle inicial de fatores de degradação e
   parcela do isolamento cuja intensidade varia com o método.

Essa separação é o que permite reportar, além do VPL total, o VPL de custos atribuíveis por método —
base correta para comparação — mantendo o custo comum visível como parcela do projeto, e não diluído
por convenção.

### Parâmetros de nível de projeto exigidos pelas linhas de Ano 0

As linhas acima só se resolvem se a plataforma dispuser de parâmetros que hoje podem não estar
presentes: fração de área por método, distância à base logística, perímetro a isolar, regime de
suprimento de mudas e de sementes, capacidade e ocupação dos ativos compartilhados, decisão de
comercializar créditos e padrão adotado, existência de financiamento externo, situação dominial e
regulatória, vida útil por classe de ativo, base real ou nominal, e taxa de desconto. A ausência de
qualquer um deles força o preenchimento por convenção, o que é aceitável desde que a convenção seja
declarada junto ao resultado.

### Saídas a acrescentar

Para que as escolhas de fronteira e de alocação sejam auditáveis a partir do resultado:

- fluxo de caixa anual desagregado, com os custos de Ano 0 identificáveis por linha e por período,
  incluindo períodos anteriores à implantação;
- VPL decomposto entre custos de Ano 0, custos recorrentes e benefícios, de modo que se veja quanto
  do resultado é determinado pelo período inicial;
- VPL de custos atribuíveis por método, separado do custo comum;
- indicação explícita quando a TIR for múltipla, inexistente ou não aplicável, com o indicador
  substituto correspondente;
- registro das convenções adotadas — critério de rateio, tratamento do capital de giro, base do valor
  residual, status de custos afundados, base real ou nominal.

### Sensibilidade e cenários

Como o período inicial não sofre desconto, as linhas de Ano 0 concentram a maior alavancagem sobre
VPL e TIR por unidade de valor, e são as candidatas naturais à análise de sensibilidade. Três
famílias de parâmetros merecem tratamento prioritário: a fração alocada de ativos compartilhados,
porque é a mais discricionária; o valor e a existência dos custos condicionais, sobretudo certificação
e regularização fundiária, porque alternam entre presença e ausência e não entre valores próximos; e
a vida útil dos ativos de isolamento, porque governa o número de reposições dentro do horizonte e
afeta assimetricamente o método de menor custo direto.

Para os custos condicionais, a forma adequada é o cenário discreto — com e sem certificação, com e
sem pendência fundiária —, não a variação contínua em torno de um valor médio, que descreveria um
projeto inexistente.

---

## Incertezas declaradas

- Todo o conteúdo atual do questionário permanece não verificado, pela negativa de política de rede
  descrita na Etapa 1. Qualquer afirmação sobre ausência de uma categoria naquela ferramenta é
  condicional a essa verificação.
- A estrutura interna da plataforma de análise custo-benefício não foi inspecionada. Assume-se um
  modelo anual de fluxo de caixa incremental descontado com VPL e TIR; se a plataforma opera com
  periodicidade diferente da anual, com múltiplas óticas (financeira e econômica) ou com tributação
  modelada, as recomendações sobre período de incidência, tratamento fiscal e escudo de depreciação
  precisam ser reespecificadas.
- Exigências regulatórias e de certificação variam por jurisdição e por padrão adotado; os itens 7,
  8, 9 e 14 da Etapa 2 estão descritos genericamente e requerem especificação conforme o contexto
  legal aplicável ao projeto.
