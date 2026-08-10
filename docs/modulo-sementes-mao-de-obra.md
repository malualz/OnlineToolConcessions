# Módulo de sementes: parametrização por mão de obra

Extração de parâmetros de esforço de coleta a partir de quatro publicações da Embrapa, para
substituir o preço de semente por quilo por uma estrutura baseada em produtividade do trabalho.

## Fontes analisadas

| Documento | Unidade / ano | Natureza | Contém dado de esforço? |
|---|---|---|---|
| Circular Técnica 126 — *Planejamento da Coleta de Sementes Florestais Nativas* (Medeiros & Nogueira) | Embrapa Florestas, Colombo–PR, 2006 | Planejamento operacional | **Sim** — seção 3.3 e Tabela 1 |
| Circular Técnica 131 — *Extração e Beneficiamento de Sementes Florestais Nativas* (Nogueira & Medeiros) | Embrapa Florestas, Colombo–PR, 2007 | Rota de processamento | Não — apenas técnica, por espécie |
| *ABC da Agricultura Familiar — Coleta e manejo de sementes* | Embrapa Amazônia Ocidental, 2011 | Cartilha (digitalizada) | Não — qualitativo |
| *Tecnologia de Sementes de Espécies Florestais Nativas do Estado do Pará* (Leão, Shimizu & Benchimol) | Embrapa Amazônia Oriental, 2015 | Folder técnico | Não — classificação morfológica |

Observação relevante: **os únicos dados quantitativos de esforço vêm da Circular 126, que é da Embrapa
Florestas (Paraná) e trata da Mata Atlântica — não da Amazônia.** Os dois documentos amazônicos são
qualitativos. Isso tem consequência metodológica discutida ao final.

---

## 1. Dados de esforço observados (Circular Técnica 126, seção 3.3)

O documento traz três observações operacionais explícitas. As colunas derivadas são aritmética sobre
os valores relatados, não valores publicados.

| Espécie | Acesso | Equipe | Duração | Massa coletada | Matrizes | kg/pessoa-dia | g/árvore | árvores/dia |
|---|---|---|---|---|---|---|---|---|
| Peroba-rosa (*Aspidosperma polyneuron*) | Escalada (cinto de segurança, esporões, podão) | 3 (responsável + escalador + auxiliar) | — | 300 g/árvore (média) | 3–4 árvores/dia | **0,30–0,40** | 300 | 3–4 |
| Pau-jacaré (*Piptadenia gonoacantha*) | Com escalador | 2 homens | 4 dias | 2.500 g (96 % pureza) | 18 matrizes, ≥ 100 m entre si | **0,31** | ≈ 139 | ≈ 4,5 |
| Vassoura-vermelha (*Dodonaea viscosa*) | Sem escalador | 1 homem | 3 dias | 2.820 g (98 % pureza) | 15 populações × 4–5 árvores | **0,94** | ≈ 42 | ≈ 20–25 |

### O padrão que esses três pontos revelam

A decomposição proposta — `ρ = q_árvore × n_árvores/dia` — se sustenta nos dados, e revela algo mais
específico. As duas espécies que exigem escalada convergem em aproximadamente **0,3 kg/pessoa-dia**,
apesar de pertencerem a famílias distintas (Apocynaceae e Mimosaceae) e de a massa por árvore diferir
por um fator de dois. A espécie coletada sem escalador rende cerca de **três vezes mais** por
pessoa-dia, com massa por árvore quase sete vezes menor.

Ou seja: **o método de acesso à copa explica mais da variação de produtividade do que a identidade da
espécie.** O que a espécie determina é o método; o método é que determina o rendimento. Essa é a
unidade de parametrização correta, e é ela — não a espécie — que transporta entre regiões e países.

---

## 2. Grupos funcionais de coleta, com as âncoras disponíveis

Classificação construída a partir da tipologia de frutos e das rotas de extração da Circular 131,
ancorada nos dados de esforço da Circular 126.

| Grupo | Acesso | Rota de extração e beneficiamento | ρ ancorado (kg/pessoa-dia) | Âncora |
|---|---|---|---|---|
| **A** — Seco deiscente, acesso do solo ou de porte baixo | Manual, podão | Secagem (sol ou sombra) → deiscência → agitação em tambor ou batedura → peneira | ≈ 0,9 | *Dodonaea viscosa* |
| **B** — Seco deiscente, dossel, escalada obrigatória | Esporões + cinto, ou rapel; podão ou gancho metálico | Secagem em ambiente ventilado → deiscência → agitação | ≈ 0,3 | *Aspidosperma polyneuron*, *Piptadenia gonoacantha* |
| **C** — Seco indeiscente, fibrolenhoso | Variável | Extração por ferramenta (faca, tesoura, machadinha, martelo, torno, escarificador); em espécies muito lenhosas, o fruto inteiro é semeado sem extração | Sem âncora | — |
| **D** — Carnoso, coleta do solo | Lona plástica, sacudida por linhada | Via úmida: imersão ≈ 1 dia → maceração em peneira → separação por flutuação → secagem | Sem âncora | — |
| **E** — Carnoso, dossel | Escalada | Idem D | Sem âncora | — |
| **F** — Miúda ou alada | Coleta de ramos com frutos, lona, proteção contra vento | Secagem sob tela (evita dispersão e autocoria) → batedura → desalamento | Sem âncora | — |

Espécies citadas pela Circular 131 por rota: deiscentes (*Aspidosperma polyneuron*, *Caesalpinia
echinata*, *Mimosa scabrella*, *Tibouchina pulchra*, *Luehea divaricata*); indeiscentes
(*Peltophorum dubium*, *Pterodon pubescens*, *Caesalpinia ferrea*, *Enterolobium contortisiliquum*);
carnosos (*Ilex paraguariensis*, *Drimys brasiliensis*, *Allophyllus edulis*); aladas exigindo
desalamento (*Cedrela fissilis*, *Cariniana estrellensis*).

**Lacuna persistente:** nenhum dos quatro documentos traz rendimento de beneficiamento — a conversão
de quilo de fruto bruto para quilo de semente limpa. O fator β continua sem fonte. A Circular 131
descreve exaustivamente *como* beneficiar, e em nenhum ponto quanto se perde.

**Ponto adicional da Circular 131 com efeito sobre custo:** para espécies nativas o beneficiamento é
declaradamente manual, por não haver padronização possível diante da diversidade morfológica. Isso
significa que o beneficiamento escala linearmente com o volume, sem ganho de mecanização — não há
economia de escala nessa etapa, ao contrário do que ocorre em sementes agrícolas.

---

## 3. A cadeia de conversão de demanda (Circular 126, Tabela 1)

O documento traz a cadeia completa de área para massa de semente, adaptada de Moestrup (1995),
exemplificada com bracatinga (*Mimosa scabrella*):

| Etapa | Coeficiente no exemplo | Papel na cadeia |
|---|---|---|
| Espaçamento 2 m × 2 m | 2.500 mudas/ha | Densidade de plantio |
| Replantio | 20 % → 500 mudas | Reposição de falhas |
| Necessidade total de mudas | 3.000 | Soma |
| Perdas, refugo e seleção no viveiro | 50 % → 4.500 mudas | Rendimento do viveiro |
| Germinação mínima | 75 % → + 1.500 sementes | Rendimento de germinação |
| Total de sementes a semear | 6.000 | — |
| Sementes por quilo | 46.000 | Atributo da espécie |
| Semente necessária por hectare | 0,13 kg | Equivale a 7,69 ha/kg |
| Área alvo | 5.000 ha | Escala do programa |
| Coleta anual necessária | 650 kg | Demanda a planejar |

Duas observações sobre essa tabela.

Primeira: **é a estrutura que a fórmula atual do módulo comprime em um único fator.** Cada elo é um
rendimento explícito — replantio, refugo de viveiro, germinação — e todos eles hoje estariam
embutidos no multiplicador 1,15. Decompor o fator nesses elos é o que torna o parâmetro auditável e
ajustável por contexto, em vez de uma constante herdada.

Segunda: **há uma inconsistência aritmética no elo de perdas.** O documento declara 50 % de perdas e
refugo e apresenta 4.500 mudas selecionadas a partir de 3.000, o que corresponde a multiplicar por
1,5, e não a dividir por 0,5 — que resultaria em 6.000. As duas leituras de "50 % de perdas" são
defensáveis em português, mas produzem valores diferentes. Se a cadeia for implementada, a convenção
precisa ser fixada explicitamente.

---

## 4. Restrições operacionais que se tornam parâmetros do modelo

Extraídas da Circular 126 e da cartilha ABC. Nenhuma delas aparece na fórmula atual.

| Restrição | Conteúdo na fonte | Efeito no modelo |
|---|---|---|
| Teto ecológico de coleta | O BASEMFLOR coleta apenas **25 % da produção estimada por matriz**, para preservar regeneração e fauna | Limite superior sobre `q_árvore`; não é escolha econômica, é restrição |
| Número de matrizes por raridade | Espécie de ampla ocorrência: 3–5 matrizes por população, em 12–25 populações. Espécie rara: 12 matrizes individuais em populações distintas. Metodologia geral: 25–30 matrizes por população, ~100 m entre si, em 3–5 populações | Determina deslocamento e, portanto, `n`; a raridade é um multiplicador de esforço |
| Periodicidade de frutificação | Algumas espécies frutificam todo ano; outras a cada 2–3 anos; outras levam mais de 3 anos. Floração abundante costuma ser seguida de 2–3 anos fracos | Probabilidade de safra; anos sem coleta; exige coleta plurianual |
| Estoque regulador | Colher em safras de superprodução e armazenar por 2–3 anos; nessas épocas "os custos de produção são menores e as sementes de melhor qualidade" | Só viável para ortodoxas; recalcitrantes não estocam |
| Horizonte orçamentário | O orçamento de coleta "deve ser flexível e abranger um período de **dois a quatro anos**", com cronograma de desembolso mensal e **reserva técnica em torno de 5 %** | Confirma desembolso em `t−1` e `t−2`; a reserva de 5 % é um fator paramétrico com fonte |
| Prospecção prévia | Entrevistas com mateiros, consulta a herbários, visitas às populações, avaliação na floração. "Se não tiver ocorrido florada intensa, haverá grande possibilidade de que a coleta não será rentável" | Custo fixo por temporada que pode terminar sem coleta |
| Tamanho mínimo de equipe | O BASEMFLOR estipula **três operários** como equipe ideal; exige sempre um segundo membro treinado em escalada, para resgate e substituição | O custo mínimo de equipe não é uma pessoa, mesmo quando um escalador bastaria; a segurança impõe o piso |
| Capacitação | Seleção, recrutamento e treinamento para coleta e escalada "podem durar vários dias ou até semanas" | Custo de capacitação em ano 0, com antecedência obrigatória |
| Manutenção de equipamento | Equipamentos de escalada "precisam ser vistoriados, anualmente, por firmas credenciadas" | Custo recorrente obrigatório, não discricionário |
| Acesso e declividade | Terreno plano e acessível permite caminhão com escada tipo bombeiro, alcançando copas de 10–15 m; baixa acessibilidade e alta declividade exigem material leve e simples | É o canal pelo qual a paisagem entra em `n` |
| Categoria legal da fonte | ACS-NS e ACS-AS dispensam marcação individual de matrizes; ACS-NM e ACS-AM exigem marcação e registro individual | Custo diferencial de marcação e registro conforme a categoria escolhida |
| Autorização | Recomendada consulta prévia ao órgão ambiental estadual; coleta em Unidade de Conservação exige licença do órgão federal | Custo e prazo de licenciamento em ano 0 |
| Armazenamento | Ambiente abaixo de 20 °C e umidade relativa abaixo de 65 %; acima disso, insetos e fungos encontram condições favoráveis | Especifica a câmara fria e seu custo de operação |
| Recalcitrância | Muitas espécies arbóreas tropicais são recalcitrantes: perdem viabilidade rapidamente ao secar e não toleram armazenamento | Impede estoque regulador; força sincronia entre coleta e semeadura; cria pico de mão de obra |

### Terceirização não zera o custo

A Circular 126 descreve a contratação de cooperantes para espécies de grande volume ou de coleta
intensiva em mão de obra, com contrato prevendo padrões de qualidade, preço, bonificação por
qualidade superior, e despesas de obtenção, conservação e transporte por conta da contratada. Mas
prevê também **supervisão pelo contratante em pelo menos três épocas**: seleção e marcação de
matrizes, floração, e colheita.

Isso qualifica o tratamento por preço-sombra: mesmo sob compra de sementes, resta um custo de
supervisão técnica no contratante. Modelar terceirização como custo zero de estrutura subestima.

---

## 5. Consequência para a estrutura da fórmula

A fórmula original,

```
custo_semente_por_ha = taxa_semeadura (kg/ha) × preço_semente (US$/kg) × 1,15
```

pode agora ser reescrita com origem documentada para a maior parte dos termos:

```
PD_ha  = S × Σ_g [ p_g × (β_g / ρ_g) ]                       pessoa-dia por hectare
custo_ha = Σ_g ( PD_g,ha × w_g ) + (C_prosp + C_desloc) / A_temporada
custo_total = custo_ha × A
```

com `g` indexando grupo funcional de coleta, `p_g` a participação em massa do grupo na mistura,
`ρ_g` o rendimento do grupo e `β_g` o fator bruto-para-limpo.

Estado das evidências por termo:

| Termo | Situação |
|---|---|
| `S` (taxa de semeadura) | Cadeia de derivação disponível na Tabela 1 da Circ. 126, com a ressalva aritmética do item 3 |
| `ρ_g` grupos A e B | Ancorado em três observações da Circ. 126 |
| `ρ_g` grupos C a F | **Sem fonte** — exige dado operacional |
| `β_g` (bruto → limpo) | **Sem fonte em nenhum dos quatro documentos** |
| `w_g` (custo da pessoa-dia) | Local, por definição; não vem de manual |
| `p_g` (composição da mistura) | Depende do projeto |
| `C_prosp`, `C_desloc` | Descritos qualitativamente na Circ. 126, sem valores |
| Fator 1,15 | Decomponível nos elos da Tabela 1 (replantio, refugo, germinação) mais a reserva técnica de 5 % |

---

## 6. Sobre a transportabilidade entre países

A hipótese de trabalho era que o esforço de coleta é transportável entre países quando balizado por
espécie tropical. Os dados sustentam uma versão mais forte e mais útil: **o esforço é balizado pelo
método de acesso e pela rota de beneficiamento, não pela espécie.** Duas espécies de famílias
distintas convergem no mesmo rendimento por pessoa-dia por exigirem a mesma técnica de escalada, e
divergem em três vezes de uma terceira espécie apenas porque esta dispensa escalada.

Isso é preferível à formulação original por uma razão prática: espécies amazônicas não ocorrem na
Bacia do Congo nem no Sudeste Asiático, de modo que uma tabela por espécie não viajaria. Uma tabela
por grupo funcional viaja, porque tipo de fruto, estrato e método de acesso existem em qualquer
floresta tropical.

Três ressalvas delimitam o alcance.

Primeira, e a mais imediata: **os dados de esforço disponíveis não são amazônicos.** Vêm da Embrapa
Florestas, no Paraná, sobre espécies de Mata Atlântica. Os dois documentos amazônicos consultados são
qualitativos. A transferência que se pretende fazer entre países já precisa ser feita, antes disso,
entre biomas brasileiros — sob exatamente a mesma hipótese. Se a hipótese de grupo funcional se
sustenta, ambas as transferências são legítimas; se não se sustenta, nenhuma é.

Segunda: o fator `n` — árvores trabalhadas por dia — carrega a paisagem, não a espécie. O caso da
vassoura-vermelha, com 15 populações visitadas em três dias por uma pessoa, só é possível em
paisagem onde as populações são densas e acessíveis. Densidade de coespecíficos na Amazônia é
tipicamente menor e o acesso mais oneroso. Os valores de `ρ` devem entrar como âncora sujeita a um
multiplicador de paisagem calibrado localmente, não como constante.

Terceira: as restrições da seção 4 são em parte institucionais — categorias legais de fonte de
semente, exigência de licença, regras de registro. Essas não transportam entre países e precisam ser
substituídas pelo equivalente local.

---

## 7. Lacunas a preencher com dado operacional

Em ordem de impacto sobre o resultado:

1. **Fator bruto-para-limpo por grupo funcional.** Ausente nas quatro fontes. É o parâmetro que mais
   afeta grupos carnosos, onde a massa descartada é grande.
2. **Rendimento de coleta dos grupos C a F.** Só há âncora para acesso do solo e para escalada em
   frutos secos deiscentes.
3. **Rendimento de beneficiamento em pessoa-dia.** Sendo manual e sem economia de escala, pode rivalizar
   com a coleta em espécies carnosas — e não há um único valor publicado nas fontes consultadas.
4. **Multiplicador de paisagem sobre `n`.** Requer dado local: densidade de matrizes frutificando e
   tempo de deslocamento entre elas.
5. **Custo fixo de prospecção por temporada e probabilidade de safra frustrada.** A Circular 126
   estabelece que a decisão de coletar depende de avaliação prévia que pode concluir pela não-coleta.

As fontes prováveis para esses itens são relatórios operacionais de redes de coletores e dados
próprios de execução, não manuais técnicos. Manuais de coleta são normativos: descrevem o
procedimento correto, não o rendimento observado. Das quatro publicações analisadas, apenas uma
contém números de esforço, e em três parágrafos.

---

## 8. Janela de coleta: o que as fontes efetivamente dizem

### O único caso quantificado

A Circular 131 detalha o cedro-rosa (*Cedrela fissilis*):

- maturidade fisiológica entre **29 e 31 semanas após a antese**, com umidade de 50 % a 60 %;
- momento ideal de colheita entre **30 e 32 semanas após a antese** — uma janela de **duas semanas**;
- a mudança de coloração que sinaliza a maturidade ocorre **duas a três semanas antes da deiscência
  natural**.

É o único ponto do corpus em que a janela é expressa em unidade de tempo. Ela converge para duas a
três semanas entre o sinal visual de maturação e a perda por dispersão.

### Os demais casos, qualitativos, convergem para o mesmo intervalo

| Espécie | Restrição declarada | Janela implícita |
|---|---|---|
| Peroba-rosa (*Aspidosperma polyneuron*) | Dispersa as sementes "quase imediatamente" após mudar de verde para marrom-escuro; coletar antes da dispersão | Dias |
| Pata-de-vaca (*Bauhinia forficata*) | Autocórica; coletar após virar marrom mas antes da deiscência | Dias a uma semana |
| Quaresmeira (*Tibouchina pulchra*) | Colher marrons, antes da abertura, por serem sementes minúsculas | Dias |
| Angico-branco (*Anadenanthera colubrina*) | Coletar após o início da abertura espontânea, quando começa a disseminação | Estreita, do lado oposto |
| Araucária (*Araucaria angustifolia*) | Pinhões sofrem ataque de roedores e insetos "tão logo as sementes atingem o solo" | Coleta no solo praticamente inviável |
| Bracatinga (*Mimosa scabrella*) | Colhidos de árvores abatidas ou quando iniciam a queda espontânea | Ligada à queda |
| Erva-mate (*Ilex paraguariensis*) | Frutos colhidos há mais de três dias iniciam fermentação | Três dias — janela de beneficiamento, não de coleta |

A Circular 126 acrescenta a restrição de planejamento: a melhor época para prever a safra é pouco
antes da maturidade fisiológica, e essa época "é, em geral, próxima ao momento recomendado para
coleta, deixando pouco tempo para o planejamento das operações". Ou seja, a janela de decisão é
quase tão estreita quanto a de execução.

### Composição de mistura

**Nenhuma das quatro publicações trata de composição de mistura para semeadura direta.** As três da
Embrapa Florestas tratam de banco de sementes e produção de mudas; as duas amazônicas tratam de
coleta e manejo para viveiro. O folder do Pará lista espécies potenciais para plantio em APP e
Reserva Legal, mas lista de espécies não é participação em massa.

Essa lacuna é estrutural, não acidental: composição de muvuca é definida por protocolo de
restauração e por disponibilidade local de sementes, não por manual de tecnologia de sementes.

## 9. Como fechar os dois parâmetros sem inventar dado

### Janela: usar o bloco sazonal, não a janela da espécie nem o ano

A janela individual (2–3 semanas) e o ano civil são ambos errados para dimensionar equipe. A primeira
superdimensiona, porque supõe que todas as espécies precisam ser coletadas simultaneamente; o
segundo subdimensiona, porque dilui o pico.

A unidade correta é o **bloco sazonal de frutificação**, dentro do qual as janelas individuais se
escalonam e a mesma equipe migra entre espécies. Em floresta tropical sazonal, os blocos se separam
por síndrome de dispersão: espécies anemocóricas de fruto seco concentram-se no fim da estação seca,
espécies zoocóricas de fruto carnoso na estação chuvosa. Isso reduz o parâmetro de N janelas
específicas para dois blocos.

O dimensionamento fica:

```
N_bloco = ( PD_total do bloco / dias úteis do bloco ) × c
```

onde `c ≥ 1` é o **fator de concentração**: vale 1 quando as espécies do bloco se escalonam
perfeitamente, e tende à razão entre a duração do bloco e a janela individual quando todas frutificam
em sincronia. Um único parâmetro interpretável, e o candidato natural a análise de sensibilidade —
porque é ele, e não a área nem o rendimento, que domina o número de coletores.

### Composição: separar a mistura em duas frações com estruturas de custo distintas

A mistura de semeadura direta tem duas frações de natureza econômica diferente:

| Fração | Conteúdo típico | Participação em massa | Estrutura de custo |
|---|---|---|---|
| Recobrimento e adubação verde | Espécies de crescimento rápido e sementes agrícolas de adubação verde | Alta | **Preço de mercado por quilo** — existe oferta comercial |
| Diversidade nativa | Espécies florestais de sucessão tardia, alta riqueza | Baixa | **Mão de obra de coleta** — é a fração que exige a estrutura deste documento |

A consequência é que a fórmula do módulo não é nem só preço nem só mão de obra: é híbrida.

```
custo_semente_ha = S × [ f_agrícola × preço_kg + f_nativa × Σ_g ( p_g × w_g / ρ_g ) ]
```

E o dimensionamento de coletores incide **apenas sobre `f_nativa`** — a fração menor em massa e maior
em custo unitário. Aplicar a estrutura de mão de obra à massa total da mistura superestimaria o
número de coletores por um fator igual ao inverso da fração nativa.

A participação em massa de cada fração é parâmetro de protocolo de restauração, a ser obtido da
prescrição técnica do projeto ou de rede de sementes local — não das fontes analisadas.

---

## 10. Estação de frutificação em países tropicais (revisão de literatura)

### A distinção que precede qualquer número

A literatura fenológica reporta **duração da fenofase de frutificação** — o período em que há frutos
na árvore. Isso não é a janela de coleta. A fenofase inclui o desenvolvimento do fruto imaturo; a
janela de coleta é o intervalo entre maturidade fisiológica e dispersão, que as fontes Embrapa
situam em duas a três semanas. Usar a duração da fenofase como janela subdimensionaria a equipe por
uma ordem de grandeza.

As duas grandezas cumprem papéis distintos no dimensionamento: a fenofase e a época de floração
definem a **largura do bloco sazonal**; a janela de coleta define a **oportunidade por espécie**
dentro do bloco.

### Duração da fenofase por época de floração

Em floresta tropical decídua, a duração da fenofase de frutificação varia conforme a estação de
floração: 3 a 4 meses em espécies de floração na seca, 6 a 9 meses em espécies de floração na
estação chuvosa, e até 11 meses em espécies de floração de verão. A frutificação prossegue por 2 a 3
meses após o pico de floração, e os eventos fenológicos da maioria das espécies têm periodicidade de
8 a 12 meses.

### Sazonalidade por síndrome de dispersão

A literatura confirma a separação em blocos por síndrome, com um refinamento:

| Síndrome | Época de dispersão | Mecanismo |
|---|---|---|
| Anemocórica | Pico na estação seca; dispersão no fim da seca e na transição seca-chuva | A perda de folhas aumenta a circulação de vento |
| Autocórica | Estação seca e transição chuva-seca | — |
| Zoocórica | Frutifica o ano todo, com pico na estação chuvosa | Disponibilidade de dispersores e umidade |

O espectro de dispersão depende da sazonalidade climática: quanto mais marcada a estação seca, mais
concentrado o bloco anemocórico. Anemocóricas e autocóricas compartilham o bloco seco; zoocóricas
ocupam o bloco chuvoso com cauda ao longo do ano.

### Padrões por região

| Região | Estrutura do ano | Observação para dimensionamento |
|---|---|---|
| Floresta tropical sazonalmente seca | Período reprodutivo concentrado na estação seca, com sub-picos no início (out–nov) e no fim (fev–mar) | Bloco longo, mas bimodal internamente |
| Amazônia (Maranhense) | Floração e frutificação o ano todo, com **dois picos de frutificação**: mar–jul e out–dez | Dois blocos por ano, não um |
| Amazônia Central | Período seco de 5 a 6 meses (jun–nov); forte sincronia entre indivíduos, ligada à precipitação | Sincronia intraespecífica alta favorece o rendimento por espécie e enrijece a janela |
| Bacia do Congo | Estação chuvosa out–mai, seca jun–set | **Sem dado de frutificação localizado**; existe base de fenologia histórica publicada, não consultada |
| Sudeste Asiático (dipterocarpáceas) | Floração geral e frutificação em massa em intervalos irregulares de **2 a 10 anos**, frequentemente associados ao ENSO, com meses de fartura seguidos de 2 a 10 anos de escassez | O modelo anual não se aplica |

### O caso que quebra o modelo anual

Em florestas de dipterocarpáceas do Sudeste Asiático, a reprodução é supra-anual e sincronizada em
escala de centenas a milhares de quilômetros. Não há estação anual de coleta a planejar: há eventos
esporádicos e imprevisíveis. Combinado ao fato de sementes de dipterocarpáceas serem notoriamente
recalcitrantes — o que impede estoque regulador —, isso significa que a demanda de coletores em ano
de floração geral é extrema e nula nos demais.

Se o modelo pretende cobrir o Sudeste Asiático, o parâmetro de janela precisa ser substituído por
uma estrutura de evento com probabilidade anual, e o dimensionamento de equipe deixa de ser
planejável e passa a ser mobilizável sob aviso.

### Convenções propostas para a Amazônia, com 100 % de espécies nativas

| Parâmetro | Valor proposto | Base |
|---|---|---|
| Blocos por ano | 2 | Picos de frutificação mar–jul e out–dez |
| Duração de cada bloco | 3 a 5 meses | Amplitude dos picos reportados |
| Janela de coleta por espécie | 2 a 3 semanas | Cedro-rosa quantificado e convergência qualitativa (seção 8) |
| Fator de concentração `c` | Faixa de 2 a 4, em sensibilidade | Convenção — razão entre bloco e janela, corrigida por escalonamento parcial entre espécies |
| Dias úteis por mês de bloco | Convenção do projeto | Depende de chuva e acesso |

O fator `c` tem limites interpretáveis: vale 1 se as espécies se escalonam perfeitamente ao longo do
bloco, e tende à razão entre duração do bloco e janela individual — algo próximo de 6 para bloco de
4 meses — se todas frutificam em sincronia. A sincronia documentada na Amazônia Central é
**intraespecífica**, entre indivíduos da mesma espécie, o que aumenta o rendimento por espécie sem
implicar sincronia entre espécies. Isso justifica um `c` intermediário, e não extremo.

### Efeito de dois blocos sobre a estrutura de custo

Com dois blocos separados por intervalos, o beneficiamento do primeiro bloco pode ocorrer no
intervalo até o segundo, o que achata a demanda de mão de obra sem reduzi-la. Também implica que a
equipe é sazonal em dois períodos por ano, e não contínua — o que muda o regime de contratação e o
custo de mobilização, que passa a incidir duas vezes.
