# Custos de Ano 0 na análise custo-benefício de restauração

Documento analítico sobre a incorporação de custos de Ano 0 (pré-implantação e implantação inicial)
em uma análise custo-benefício com horizonte de 20 anos, aplicada a três métodos de restauração:
ANR (regeneração natural assistida), semeadura direta (*seeding*) e plantio de mudas (*seedling*).

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
| 3 | Capital de giro da produção de mudas | Insumos consumíveis (tubetes, substrato, fertilizantes, defensivos), mão de obra de viveiro, perdas por mortalidade e descarte de padrão, custo do ciclo de produção que antecede o plantio (desembolso em Ano −1) | Parcial | Não | Sim | D, T | Alta para *seedling*; introduz defasagem temporal relevante | não verificado |
| 4 | Coleta de sementes | Identificação e cadastro de matrizes, expedições de coleta, mão de obra especializada, escalada e EPI, transporte, sazonalidade e repetição de safras para compor diversidade | Parcial | Sim | Sim | CM, CP, T | Alta para *seeding*; dominante quando há exigência de riqueza específica | não verificado |
| 5 | Beneficiamento e armazenamento de sementes | Casa de sementes, secagem, extração, peneiramento, tratamento pré-germinativo, câmara fria e desumidificação, embalagens; ativos fixos e operação | Parcial | Sim | Sim | CM, CP, T | Média a alta para *seeding* | não verificado |
| 6 | Análise e controle de qualidade de sementes | Testes de germinação, pureza, viabilidade, teor de umidade; laudos por lote | Parcial | Sim | Sim | D por lote, CP quanto ao laboratório | Média; condiciona a taxa de semeadura | não verificado |
| 7 | Registro e certificação de sementes e mudas | Registro do produtor em sistema nacional de sementes e mudas, inscrição de campos de produção e de matrizes, emissão de notas e termos de conformidade, cadeia de custódia e rastreabilidade | Parcial | Sim | Sim | CP | Média; predominantemente custo fixo, sensível à escala | não verificado |
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
| 18 | Controle inicial de fatores de degradação | Controle de gramíneas exóticas competidoras, combate inicial a formigas cortadeiras, controle de espécies invasoras lenhosas; execução prévia ou concomitante à implantação | Sim | Sim | Sim | D | Alta; risco de sobreposição com itens já capturados em implantação | não verificado |
| 19 | Mobilização e logística inicial | Deslocamento de equipes e maquinário até a área, alojamento, transporte de insumos, montagem de canteiro de obra | Sim | Sim | Sim | CM | Média; escala com distância e com o número de frentes | não verificado |
| 20 | Capacitação de equipes | Treinamento técnico em coleta, viveiro, semeadura, plantio e operação de máquinas; treinamentos de segurança do trabalho e certificações obrigatórias de operadores | Sim | Sim | Sim | CM, CP | Média; recorrente sob rotatividade, mas com componente inicial concentrado | não verificado |
| 21 | Mobilização social e engajamento comunitário | Articulação com comunidades e proprietários vizinhos, reuniões de apresentação, acordos de uso, consulta livre, prévia e informada quando aplicável, comunicação e gestão de conflitos | Sim | Sim | Sim | CM | Média a alta; frequentemente omitido e condicionante do risco de execução | não verificado |
| 22 | Estruturação do monitoramento | Definição do protocolo, inventário de linha de base, estoque inicial de carbono e de solo, instalação e marcação de parcelas permanentes, sistema de gestão de dados, equipamentos de campo | Sim | Sim | Sim | CM, CP | Média; separável entre componente inicial (Ano 0) e recorrente | não verificado |
| 23 | Custos de transação jurídico-financeiros | Elaboração e negociação de contratos de execução, de aquisição de insumos e de comercialização de resultados; *due diligence* socioambiental e jurídica; estruturação financeira, garantias e custo de originação | Sim | Sim | Sim | CM, CP | Alta em projetos com financiamento externo ou venda de créditos | não verificado |
| 24 | Seguros e reserva de contingência | Seguro contra fogo, seca e perda de plantio; provisão para replantio; constituição de reserva de risco (*buffer*) quando exigida por padrão de certificação | Sim | Sim | Sim | CM | Média; a reserva de *buffer* não é desembolso, mas reduz receita | não verificado |
| 25 | Overhead de estruturação | Custo de gestão, coordenação técnica e administração incorrido antes do início operacional | Sim | Sim | Sim | CM, CP | Média; alto risco de dupla contagem com taxa de administração recorrente | não verificado |

### Observações sobre a distribuição entre métodos

Três assimetrias estruturam a comparação. Primeira: a cadeia de propágulos separa os métodos —
*seedling* depende de viveiro e de capital de giro de produção, *seeding* depende de coleta,
beneficiamento e armazenamento em volume, ANR depende de nenhum dos dois exceto quando há
enriquecimento. Segunda: o diagnóstico de potencial de regeneração natural é um custo de Ano 0 cuja
função é decidir se ANR é viável; ele antecede a escolha do método e não pertence a nenhuma aba
isoladamente. Terceira: isolamento da área e controle de fatores de degradação são custos comuns aos
três métodos, mas seu peso relativo é máximo em ANR, onde constituem a própria intervenção, e menor
em *seedling*, onde competem com custos de insumo e de operação.

Os itens 8 a 15 e 19 a 25 são majoritariamente fixos por projeto: não escalam com a área nem com o
método. Sua omissão subestima sistematicamente o custo de projetos pequenos e distorce a comparação
entre métodos apenas de forma indireta, pela via da escala mínima viável de cada um.

---

## Etapa 3 — Abordagens de inserção dos custos de Ano 0

### Premissa transversal: fluxo de caixa e alocação são problemas distintos

Em uma análise custo-benefício com desconto, o valor presente depende de quando o recurso é
efetivamente desembolsado. Redistribuir contabilmente um desembolso já ocorrido ao longo do horizonte
não altera o custo econômico, mas altera o valor presente calculado, reduzindo-o artificialmente.
Amortização, portanto, não é um instrumento para suavizar desembolso — é um instrumento para alocar
um ativo cujo serviço é consumido por mais de um beneficiário, seja no tempo, seja entre métodos,
seja entre projetos. Confundir os dois usos é a principal fonte de erro no tratamento de custos de
Ano 0. As abordagens abaixo devem ser lidas sob essa distinção: as que operam sobre a fronteira do
projeto (rateio, valor residual, preço-sombra) são legítimas; as que operam apenas sobre a
distribuição temporal de um desembolso integralmente atribuível ao projeto não são, salvo quando
refletem cronograma real de pagamento.

### A. Custo integral no Ano 0

Lançamento do valor total no período inicial.

Adequada quando o ativo ou serviço é dedicado ao projeto, consumido integralmente dentro do horizonte
e sem valor de revenda ao final: diagnóstico, projeto técnico, licenciamento, mobilização inicial,
controle inicial de fatores de degradação, validação inicial de certificação. É também o tratamento
correto para ativos compartilháveis quando a fronteira da análise é o programa inteiro, e não um
projeto dentro dele.

Distorção: quando aplicada a ativo compartilhável com vida útil superior ao horizonte ou a projetos
paralelos, imputa a um único projeto o custo de uma capacidade que ele não consome sozinho,
penalizando o método que depende desse ativo — na prática, penalizando *seedling* pelo viveiro e
*seeding* pela estrutura de sementes. Também é sensível ao ano de referência: parte dos custos de
Ano 0 ocorre em Ano −1 (produção de mudas, coleta na safra anterior, validação prévia), e tratá-los
como Ano 0 subestima levemente o valor presente.

Dados exigidos: valor total e ano de desembolso. É a abordagem menos exigente em dados.

Comparabilidade: preserva comparabilidade apenas se todos os métodos forem avaliados sob a mesma
fronteira de propriedade dos ativos.

Riscos: subestimação por omissão de desembolsos de Ano −1; superestimação por internalizar capacidade
ociosa.

### B. Amortização ao longo do horizonte

Distribuição do valor pelos anos do projeto, linearmente ou segundo a vida útil do ativo.

O critério linear pelo horizonte é arbitrário: vincula a alocação à duração da análise, não ao ativo.
Sob esse critério, alterar o horizonte de 20 para 30 anos muda o custo anual sem que nada de físico
tenha mudado. O critério por vida útil é defensável, porque a fração alocada corresponde ao consumo
do ativo, e é o único que permite tratar coerentemente ativos com vida inferior ao horizonte, que
exigem reposição dentro dos 20 anos (sombrite, mangueiras e sistema de irrigação, telas, bombas,
cercas), e ativos com vida superior, cujo excedente não pertence ao projeto.

Adequada para: infraestrutura de viveiro, câmara fria e casa de sementes, equipamentos de campo e de
monitoramento, cercamento.

Distorção: se aplicada como diluição de desembolso, reduz o valor presente do custo sem contrapartida
real. Só é legítima se acompanhada da representação do desembolso efetivo — isto é, se o objetivo for
alocação entre usuários, e não redistribuição temporal do mesmo usuário.

Dados exigidos: valor do ativo, vida útil por classe de ativo, ciclos de reposição dentro do
horizonte, e uma definição explícita do que a alocação representa.

Riscos: dupla contagem quando há reposição — o ativo é amortizado e a reposição também é lançada como
custo cheio; subestimação quando a vida útil declarada é otimista.

### C. Rateio por uso

Alocação proporcional ao consumo da capacidade do ativo pelo projeto: fração da capacidade anual de
produção de mudas efetivamente demandada, fração da capacidade de armazenamento de sementes ocupada,
fração do tempo de uso de equipamento.

É a abordagem conceitualmente mais correta para ativos de capacidade divisível, porque separa o custo
da capacidade instalada do custo do serviço consumido. Resolve diretamente o problema do viveiro
superdimensionado: o projeto absorve a fração que usa, e a ociosidade permanece com quem detém o
ativo.

Distorção: exige uma definição de capacidade que raramente é única. A capacidade de um viveiro varia
com o número de ciclos anuais, com o tamanho do recipiente e com a espécie produzida; a mesma
estrutura tem capacidades diferentes conforme o padrão de muda. Sem padronizar a unidade de
capacidade, o rateio se torna manipulável.

Comparabilidade: melhora a comparabilidade entre métodos, ao evitar que *seedling* carregue custo de
capacidade não consumida. Mas exige que a mesma lógica seja aplicada à infraestrutura de sementes em
*seeding*, sob pena de assimetria de tratamento.

Dados exigidos: capacidade nominal anual do ativo e unidade em que é medida; volume demandado pelo
projeto; número de ciclos por ano; horizonte de uso.

Riscos: subestimação sistemática se a capacidade nominal for declarada acima da capacidade efetiva;
dupla contagem se o rateio de capacidade coexistir com custo unitário de muda que já embuta
depreciação.

### D. Rateio por método

Distribuição de custos comuns entre ANR, *seeding* e *seedling* conforme a dependência de cada um.

Aplicável quando o projeto é um mosaico de métodos na mesma área, situação comum na prática, e quando
a ferramenta pretende reportar custo por método além de custo total. Os critérios possíveis são
distintos e produzem resultados distintos: rateio por área tratada, por participação no custo direto,
por intensidade de uso do recurso comum, ou atribuição direta quando o custo é rastreável.

Custos como diagnóstico, licenciamento, georreferenciamento, mobilização social e estruturação
contratual não têm causalidade clara com nenhum método; para eles, o rateio por área é uma convenção,
não uma medida. Custos como isolamento e controle de fatores de degradação têm causalidade parcial:
são mais intensivos em ANR. Custos de cadeia de propágulos são atribuíveis diretamente.

Distorção: rateio por área aplicado indistintamente transfere custo fixo para o método que ocupa mais
área, o que tende a penalizar ANR, justamente o método aplicado em maior escala por depender de menor
intensidade. Isso inverte a conclusão que a análise deveria produzir.

Comparabilidade: é a abordagem que mais afeta a comparação entre métodos e, por isso, a que exige
declaração explícita do critério. Recomenda-se reportar o custo comum de forma segregada, além de
rateado, para que a comparação entre métodos possa ser feita sobre custos atribuíveis.

Dados exigidos: fração de área por método; critério de rateio escolhido; identificação de quais custos
são atribuíveis diretamente.

Riscos: dupla contagem quando um custo é atribuído diretamente a um método e também entra na base de
rateio comum.

### E. CAPEX com valor residual

Reconhecimento do valor remanescente do ativo ao final do horizonte, como entrada no último período.

Adequada para ativos duráveis com vida útil superior a 20 anos e com valor de uso ou de revenda ao
final: estrutura de viveiro, benfeitorias, câmara fria, acessos. Equivale economicamente ao rateio
temporal, mas preserva o perfil real de desembolso: o custo integral aparece quando ocorre, e o valor
não consumido retorna ao final, descontado.

Distorção: o valor residual descontado a 20 anos é fortemente reduzido pela taxa de desconto, de modo
que a abordagem se aproxima do custo integral em Ano 0 para taxas altas. Além disso, presume
liquidez ou continuidade de uso que pode não existir — um viveiro construído para um projeto
específico em local remoto pode ter valor residual próximo de zero, independentemente do estado
físico.

Dados exigidos: vida útil, critério de valoração residual (contábil, de mercado ou de uso
continuado), e premissa explícita sobre continuidade de operação.

Riscos: superestimação do valor residual quando se assume mercado secundário inexistente; dupla
contagem se combinada com amortização.

### F. Tratamento paramétrico

Inserção como multiplicador ou fator de ajuste sobre custos já capturados, em vez de linha de custo
autônoma — por exemplo, um percentual sobre custo direto para representar estruturação, licenciamento
e transação.

Adequada para custos difusos, de difícil especificação individual, ou quando a ferramenta precisa
funcionar com poucos dados de entrada. Também é útil como valor padrão preenchido automaticamente,
sobreponível por dado observado.

Distorção: assume proporcionalidade entre o custo de Ano 0 e o custo direto, hipótese falsa
justamente para a classe de custos onde a abordagem é mais tentadora. Certificação, licenciamento e
diagnóstico são majoritariamente fixos por projeto: como fração do custo direto, decrescem com a
área. Um multiplicador constante superestima esses custos em projetos grandes e os subestima em
projetos pequenos, que é o erro na direção mais prejudicial, porque é no projeto pequeno que o custo
fixo determina a viabilidade.

Comparabilidade: um multiplicador aplicado sobre custo direto penaliza o método de maior custo
direto — *seedling* — por custos que não dependem do método. Isso corrompe a comparação de forma não
transparente, porque o efeito fica embutido no fator.

Dados exigidos: nenhum além do custo direto, o que explica sua atratividade; a base empírica do fator,
porém, exige amostra de projetos comparáveis.

Riscos: dupla contagem quando o fator paramétrico coexiste com linhas explícitas dos mesmos custos;
subestimação em pequena escala.

### G. Preço-sombra por terceirização

Substituição da modelagem do ativo pelo preço de mercado do serviço ou insumo equivalente: adotar o
preço da muda entregue em vez de modelar viveiro, o preço da semente beneficiada em vez de modelar
casa de sementes.

Adequada quando existe mercado local com oferta suficiente e quando a decisão do projeto é
efetivamente comprar em vez de produzir. É a abordagem que melhor reflete a estrutura real de custos
da maioria dos projetos, que não constroem viveiro. Tem a vantagem de internalizar automaticamente
depreciação, capital de giro e margem no preço unitário, eliminando a necessidade de rateio.

Distorção: oculta a diferença entre produzir e comprar, que é precisamente uma das decisões que a
análise pode querer informar. Também importa a margem do fornecedor para dentro do custo do projeto,
o que é correto do ponto de vista do projeto e incorreto do ponto de vista social.

Dados exigidos: preço unitário posto na área, disponibilidade e diversidade de espécies ofertadas,
distância e frete.

Riscos: dupla contagem grave se coexistir com CAPEX de viveiro; subestimação quando o mercado local
não oferece a diversidade de espécies exigida e o projeto é obrigado a produzir.

### H. Custo equivalente anual

Conversão do investimento em um fluxo anual equivalente ao longo da vida útil do ativo, considerando
o custo de capital.

É a forma tecnicamente correta de comparar ativos com vidas úteis diferentes entre si e diferentes do
horizonte, e resolve o problema que a amortização linear resolve mal. É particularmente útil quando a
ferramenta pretende reportar custo anual por hectare como métrica de comparação entre métodos.

Distorção: introduz dependência da taxa de desconto na alocação, o que exige que a taxa seja um
parâmetro declarado e sujeito a análise de sensibilidade.

Dados exigidos: valor do ativo, vida útil, taxa de desconto.

Riscos: inconsistência se aplicado a alguns ativos e não a outros; dupla contagem se somado ao
desembolso integral.

### I. Ciclos de reposição dentro do horizonte

Reconhecimento explícito de reinvestimentos para ativos cuja vida útil é inferior a 20 anos.

Não é alternativa às demais abordagens, mas complemento necessário a qualquer uma delas. Sua omissão
é uma fonte silenciosa de subestimação: cercas, aceiros, telas, sistemas de irrigação e equipamentos
de campo não sobrevivem ao horizonte. Em ANR, onde o isolamento é a intervenção central, a omissão da
reposição de cercamento subestima o custo do método mais barato, o que altera a conclusão da
comparação na direção de reforçá-la indevidamente.

Dados exigidos: vida útil por classe de ativo e política de reposição.

### J. Custo de programa fora da fronteira do projeto

Manutenção do ativo compartilhado fora da fronteira da análise, com entrada apenas da fração alocada
via preço interno de transferência.

Adequada quando a ferramenta avalia projetos individuais dentro de um programa que já detém
infraestrutura. Torna explícito que a decisão sobre o ativo não pertence ao projeto avaliado.

Distorção: se o preço interno for arbitrado abaixo do custo, transfere subsídio implícito e faz o
projeto parecer viável às custas do programa.

Dados exigidos: existência do ativo, preço interno de transferência e sua base.

### K. Tratamento condicional e por cenário

Reconhecimento de que parte dos custos de Ano 0 é contingente: certificação de carbono só se
materializa se houver decisão de comercializar créditos; regularização fundiária só incide se houver
pendência; capacitação varia com a existência de equipe prévia.

Adequada para os custos das linhas 8, 9, 15 e 24 da Etapa 2. Trata-se de condicionar a inclusão a uma
resposta do usuário, e não de estimar valor esperado ponderado por probabilidade, que introduziria
custo em todos os projetos sem que ele ocorra em nenhum deles individualmente.

Riscos: se implementado como valor esperado, produz um custo que não corresponde a nenhum projeto
real.

---

## Etapa 4 — Recomendação por categoria

| # | Custo de Ano 0 | Abordagem recomendada | Justificativa técnica | Dados necessários |
|---|---|---|---|---|
| 1 | Infraestrutura física de viveiro | G como padrão; C combinada com E quando produção própria | A maioria dos projetos compra mudas, e o preço internaliza a estrutura; quando há viveiro próprio, o projeto consome fração da capacidade e o ativo sobrevive ao horizonte | Regime de suprimento (próprio/terceirizado/compartilhado); valor do investimento; capacidade nominal anual e unidade; volume demandado; vida útil; premissa de valor residual |
| 2 | Sistemas e equipamentos de viveiro | C combinada com I | Vida útil inferior à da estrutura civil, com reposição dentro do horizonte | Valor por classe de equipamento; vida útil; ciclos de reposição; fração de uso |
| 3 | Capital de giro da produção de mudas | A, com desembolso alocado ao ano anterior ao plantio | É consumo, não ativo; a defasagem entre produção e plantio é real e afeta o valor presente | Ciclo de produção em meses; mortalidade e taxa de descarte em viveiro; custo unitário de produção; ano de desembolso |
| 4 | Coleta de sementes | A quando dedicada; C quando há estrutura de coleta compartilhada; G quando há compra de sementes | Custo majoritariamente operacional e atribuível ao lote; a estrutura de apoio é que é compartilhável | Origem das sementes (coleta própria/compra/rede de coletores); volume por espécie; número de expedições; distância |
| 5 | Beneficiamento e armazenamento | C combinada com E para os ativos; A para a operação | Câmara fria e casa de sementes são capacidade divisível e durável; a operação é consumo do lote | Valor dos ativos; capacidade de armazenamento e ocupação pelo projeto; vida útil; custo operacional por lote |
| 6 | Análise de qualidade de sementes | A, por lote | Custo recorrente por lote, atribuível diretamente, sem componente de ativo relevante | Número de lotes e de espécies; custo por análise |
| 7 | Registro e certificação de sementes e mudas | A, com rateio D por área quando o projeto é misto | Custo fixo por produtor e por período, sem relação com o volume do projeto individual | Obrigatoriedade aplicável; periodicidade de renovação; base de rateio |
| 8 | Certificação ambiental e de carbono | K para inclusão; A para o componente inicial; separar o componente recorrente de verificação | Custo fixo por projeto, condicional à decisão de comercializar créditos, com componente inicial distinto do recorrente | Decisão de comercialização; padrão adotado; escopo e área; periodicidade de verificação; custo de validação inicial e de registro |
| 9 | Certificação de manejo e cadeia de custódia | K para inclusão; A para auditoria inicial | Condicional ao modelo de receita; não incide na maioria dos projetos de restauração pura | Existência de componente madeireiro; padrão; escopo |
| 10 | Diagnóstico ecológico | A, com rateio D declarado | Custo antecedente à escolha do método; atribuí-lo a um método individual induz erro de comparação | Área diagnosticada; número de unidades amostrais; fração de área por método |
| 11 | Diagnóstico físico do meio | A, com rateio D declarado | Mesma natureza do item 10 | Número de amostras de solo; área; profundidades |
| 12 | Projeto técnico de restauração | A, com rateio D declarado | Custo fixo por projeto, com componente que escala fracamente com a área | Área; número de unidades de manejo; regime de contratação do responsável técnico |
| 13 | Georreferenciamento e demarcação | A no Ano 0, com reconhecimento de reaquisição periódica de imagens sob I | O levantamento inicial é único; imagens e sobrevoos de acompanhamento são recorrentes e pertencem ao monitoramento | Área; método de levantamento; frequência de reaquisição |
| 14 | Licenciamento e conformidade | A, condicional K por autorização específica | Fixo por projeto, com itens condicionais à situação regulatória da área | Situação regulatória; autorizações aplicáveis; taxas e emolumentos; existência de outorga de água |
| 15 | Regularização fundiária | K para inclusão; A quando incide | Não incide em áreas regulares; quando incide, é condição precedente e custo concentrado | Situação dominial; existência de pendências; instrumento de uso da área |
| 16 | Acesso e infraestrutura de campo | A para abertura; I para manutenção e reposição | O investimento inicial é único; a conservação é recorrente e frequentemente omitida | Extensão de acessos; condição inicial; distância à via principal; regime de conservação |
| 17 | Isolamento da área | A para implantação; I obrigatoriamente para reposição | Vida útil de cercas e aceiros é inferior ao horizonte; omitir a reposição subestima ANR de forma assimétrica | Perímetro; tipo de cerca; vida útil; necessidade de aceiro e sua extensão; pressão externa (gado, fogo) |
| 18 | Controle inicial de fatores de degradação | A, com verificação explícita de fronteira contra itens de implantação | Custo real de Ano 0, mas com alta sobreposição com preparo de área já capturado | Nível de infestação; número de operações; método de controle; declaração de o que já está incluído em implantação |
| 19 | Mobilização e logística inicial | A | Desembolso único, escalando com distância e número de frentes, não com área | Distância à base; número de frentes; necessidade de alojamento |
| 20 | Capacitação de equipes | A para o componente inicial; I para reciclagem | Componente inicial concentrado, com necessidade de reciclagem sob rotatividade | Tamanho da equipe; treinamentos obrigatórios; rotatividade esperada |
| 21 | Mobilização social e engajamento | A, com rateio D por área e componente recorrente segregado | Custo fixo por projeto e por contexto social, sem relação com o método | Número de partes interessadas; existência de território tradicional; exigência de consulta; número de eventos |
| 22 | Estruturação do monitoramento | A para linha de base e instalação de parcelas; C ou G para equipamentos; separar o recorrente | Linha de base é única e irreproduzível; equipamentos são compartilháveis; medições posteriores são recorrentes e não pertencem ao Ano 0 | Número de parcelas; protocolo adotado; equipamentos e sua vida útil; frequência de medição |
| 23 | Custos de transação | A, condicional K à existência de financiamento externo ou venda de créditos | Concentrado no Ano 0 e ausente em projetos autofinanciados; não é proporcional ao custo direto | Existência de financiamento externo; número e complexidade de contratos; exigência de *due diligence* |
| 24 | Seguros e contingência | I para o prêmio recorrente; tratamento como redução de receita para reserva de *buffer* | Prêmio é fluxo anual, não custo de Ano 0; a reserva de crédito não é desembolso e não deve entrar como custo | Contratação de seguro; percentual de reserva exigido pelo padrão; base de incidência |
| 25 | Overhead de estruturação | F como último recurso, com declaração explícita de que substitui itens 12, 14 e 23 | É a única categoria em que o tratamento paramétrico se justifica, e apenas quando os itens específicos não são coletados | Percentual adotado; base de incidência; lista dos itens que o fator substitui |

### Regras de consistência a aplicar sobre a matriz

Três regras evitam os erros mais prováveis. Primeira, exclusividade entre G e as abordagens de ativo:
se o regime de suprimento é terceirizado, os blocos de CAPEX de viveiro e de estrutura de sementes
devem ser suprimidos, não zerados pelo usuário. Segunda, exclusividade entre F e as linhas
específicas que o fator representa. Terceira, separação obrigatória entre componente inicial e
componente recorrente nas categorias 8, 13, 16, 17, 20, 21 e 22, porque em todas elas existe um custo
de Ano 0 e um custo anual de mesma natureza, e a ausência dessa separação produz simultaneamente
dupla contagem no Ano 0 e subestimação nos anos seguintes.

---

## Etapa 5 — Implicações para o questionário

### Estrutura proposta

A organização por método não comporta bem a maior parte dos custos de Ano 0, porque a maioria deles é
fixa por projeto e independe do método. Propõe-se uma estrutura em três níveis:

1. **Seção transversal de projeto (nova, anterior às abas):** escala, contexto e regime institucional.
   Área total, fração de área por método, distância à base logística, situação dominial e regulatória,
   existência de financiamento externo, decisão de comercializar créditos, existência de equipe
   própria, contexto social. Esses campos condicionam a exibição de blocos posteriores.
2. **Seção transversal de Ano 0 (nova):** os custos comuns aos três métodos — diagnóstico,
   planejamento, licenciamento, georreferenciamento, acesso, isolamento, mobilização, capacitação,
   engajamento, monitoramento inicial, certificação, transação.
3. **Blocos de Ano 0 dentro de cada aba:** apenas os custos específicos do método — cadeia de
   propágulos em *seeding* e *seedling*, controle inicial de fatores de degradação com intensidade
   específica por método, enriquecimento em ANR.

Essa separação é também o que viabiliza reportar, além do custo total, o custo atribuível por método,
que é a base correta para a comparação entre métodos.

### Campos a criar

| Bloco | Campo | Natureza | Função na análise |
|---|---|---|---|
| Projeto | Área total e fração por método | Escala | Base de rateio e denominador das métricas por hectare |
| Projeto | Horizonte e taxa de desconto | Parâmetro | Condição para custo equivalente anual e valor residual |
| Projeto | Distância à base logística | Escala | Modula mobilização, acesso e frete |
| Projeto | Situação dominial | Condicional | Habilita bloco de regularização fundiária |
| Projeto | Situação regulatória e autorizações aplicáveis | Condicional | Habilita itens de licenciamento |
| Projeto | Comercialização de créditos (sim/não) e padrão | Condicional | Habilita bloco de certificação e de reserva |
| Projeto | Financiamento externo (sim/não) | Condicional | Habilita bloco de custos de transação |
| Projeto | Contexto social e exigência de consulta | Condicional | Habilita bloco de engajamento |
| Ano 0 transversal | Diagnóstico: número de unidades amostrais e amostras de solo | Escala | Custo do diagnóstico |
| Ano 0 transversal | Perímetro a isolar e tipo de cerca | Escala | Custo de cercamento; base para reposição |
| Ano 0 transversal | Extensão de aceiros e de acessos a abrir | Escala | Custo de infraestrutura de campo |
| Ano 0 transversal | Número de parcelas permanentes e protocolo | Escala | Custo de linha de base e de monitoramento |
| Ano 0 transversal | Vida útil por classe de ativo | Parâmetro | Habilita reposição e valor residual |
| Ano 0 transversal | Custos já incluídos em outro item (lista de verificação) | Controle | Prevenção de dupla contagem |
| Aba *seedling* | Regime de suprimento de mudas: próprio / terceirizado / compartilhado | Condicional | Seleciona entre preço-sombra e modelagem de ativo |
| Aba *seedling* | Se próprio: capacidade nominal anual, unidade de capacidade, ciclos por ano, valor investido, vida útil | Escala e parâmetro | Rateio por uso e valor residual |
| Aba *seedling* | Se compartilhado: número de projetos usuários ou critério de rateio acordado | Parâmetro | Fração alocada |
| Aba *seedling* | Se terceirizado: preço da muda posto na área e diversidade ofertada | Preço | Preço-sombra; supressão do bloco de CAPEX |
| Aba *seedling* | Ciclo de produção e ano de desembolso | Temporal | Alocação do capital de giro ao ano correto |
| Aba *seedling* | Mortalidade em viveiro e taxa de descarte | Técnico | Volume a produzir por muda plantada |
| Aba *seeding* | Origem das sementes: coleta própria / compra / rede de coletores | Condicional | Seleciona entre modelagem de coleta e preço-sombra |
| Aba *seeding* | Se coleta própria: número de expedições, espécies, distância, estrutura de beneficiamento e armazenamento | Escala | Custo de coleta e rateio de ativos |
| Aba *seeding* | Capacidade e ocupação da câmara fria | Escala | Rateio por uso |
| Aba *seeding* | Número de lotes e análises de qualidade | Escala | Custo de controle de qualidade |
| Aba ANR | Potencial de regeneração natural avaliado (sim/não) e custo do estudo | Condicional | Custo que determina a elegibilidade do método |
| Aba ANR | Necessidade de enriquecimento e densidade | Condicional | Habilita subconjunto do bloco de mudas dentro de ANR |
| Aba ANR | Pressão externa: gado, fogo, invasoras | Escala | Modula isolamento e controle de degradação |

### Captura da dimensão de compartilhamento

Recomenda-se um padrão único de pergunta, aplicado a toda categoria que envolva ativo: regime de
acesso (próprio dedicado / próprio compartilhado / de terceiros / serviço contratado), seguido, nos
casos de ativo próprio, de capacidade nominal, unidade de capacidade, consumo do projeto e vida útil.
A resposta de regime é o que seleciona a abordagem de inserção — não cabe ao usuário escolher entre
amortizar, ratear ou lançar integralmente; essa decisão deve ser derivada da estrutura declarada.

A unidade de capacidade precisa ser explicitada em cada caso, porque não é única: mudas por ano em
determinado padrão de recipiente, quilogramas de semente armazenados, horas-máquina. Sem isso, o
rateio por uso não é auditável.

### Condicionalidades

As condicionalidades que mais reduzem ruído e erro são: suprimir integralmente o bloco de CAPEX de
viveiro quando o suprimento é terceirizado; suprimir o bloco de certificação quando não há
comercialização de créditos; suprimir regularização fundiária quando não há pendência dominial;
suprimir custos de transação financeira quando não há financiamento externo; exibir o bloco de
enriquecimento em ANR apenas quando declarado; e, em projetos de método único, ocultar os campos de
rateio entre métodos, exibindo-os apenas quando a fração de área declarada indicar mosaico.

Uma condicionalidade adicional, de natureza distinta, merece existir: uma verificação de fronteira
que pergunte, para as categorias com sobreposição conhecida — controle inicial de fatores de
degradação, preparo de solo, monitoramento, overhead — se o custo já foi informado em outro campo.
É o mecanismo mais simples para conter dupla contagem, que é o risco dominante quando se adiciona uma
camada de custos de Ano 0 a um questionário que já captura custos de implantação.

### Saídas a acrescentar

Para que as escolhas de alocação sejam auditáveis, a ferramenta precisa reportar, além do resultado
agregado: o custo total desembolsado por ano, sem alocação; o custo alocado por método, com o critério
de rateio explicitado; e o custo comum não rateado, apresentado separadamente. A comparação entre
métodos deve ser feita preferencialmente sobre custos atribuíveis, com o custo comum reportado como
parcela do projeto, e não distribuído por convenção.

---

## Incertezas declaradas

- Todo o conteúdo atual do questionário permanece não verificado, pela negativa de política de rede
  descrita na Etapa 1. Qualquer afirmação sobre ausência de uma categoria na ferramenta é
  condicional a essa verificação.
- Não foi possível determinar se a ferramenta já implementa horizonte temporal, desconto ou
  distinção entre custo único e recorrente; as recomendações das Etapas 4 e 5 pressupõem que essa
  estrutura temporal exista ou seja criada.
- Exigências regulatórias e de certificação variam por jurisdição e por padrão adotado; os itens 7,
  8, 9 e 14 da Etapa 2 estão descritos genericamente e requerem especificação conforme o contexto
  legal aplicável ao projeto.
