# E-mails Black Friday 2026 · Alto de Monte Verde

10 e-mails prontos para o RD Station, com a identidade da campanha (mesma da landing page black-2026).

## O que tem aqui

- `emails/` : os 10 HTMLs para colar na Edição Avançada do RD Station
- `images/` : 10 banners, 4 fotos dos cards e o logo do cabeçalho

## Como subir no GitHub (repositório giuiia/emails-alto)

1. No repositório, crie a pasta `black-friday-2026` na raiz (ao lado de `campanha-outubro-2026`).
2. Suba para dentro dela as pastas `images` e `emails`. O caminho final precisa ser `black-friday-2026/images/...`.
   Pelo site: "Add file" > "Upload files" e arraste a pasta `black-friday-2026` inteira estando na RAIZ do repositório.
   Não arraste para dentro de outra pasta, senão fica aninhado e as imagens quebram.
3. Antes de colar no RD, abra um destes links no navegador. Tem que abrir a imagem direto:
   - https://raw.githubusercontent.com/giuiia/emails-alto/main/black-friday-2026/images/logo-header.png
   - https://raw.githubusercontent.com/giuiia/emails-alto/main/black-friday-2026/images/banner-f01-e1.jpg

## Assuntos e pré-headers (configurar no RD, teste A/B)

| E-mail | Arquivo | Quando | Público | Assunto A | Assunto B | Pré-header |
|---|---|---|---|---|---|---|
| F01-E1 | f01-e1-seu-cupom.html | na hora do cadastro | leads da LP | Seu cupom chegou: 40% OFF no seu refúgio na serra | Pronto! Seu BLACK26 está aqui | Estadias de janeiro a março de 2027. Reserve até 30/11. |
| F01-E2 | f01-e2-experiencia.html | 3 dias após o cadastro | leads da LP | Lareira acesa, hidro quente e 40% OFF | O que espera por vocês na serra | Seu BLACK26 continua valendo até 30/11. |
| 02A-1 | 02a-1-abertura.html | 01/11, 11h | Base Geral | Black Friday Alto de Monte Verde: 40% OFF | 40% OFF no seu refúgio na serra | Para estadias de janeiro a março de 2027. Cupom na hora. |
| 02A-2 | 02a-2-semana-black-friday.html | 27/11 | Base Geral | É Black Friday: 40% OFF no seu chalé na serra | Faltam 4 dias para garantir 40% OFF | Termina na segunda, 30/11. Cupom na hora. |
| 02A-3 | 02a-3-ultimo-dia.html | 30/11, 10h | Base Geral | Último dia: 40% OFF termina hoje às 23h59 | Hoje é o último dia da Black Friday da serra | Depois de hoje, só na próxima Black Friday. |
| 02B-1 | 02b-1-membros-abertura.html | 01/11, 9h | Membros | Para quem já é da casa: Black Friday com 40% OFF | Vocês são os primeiros a saber: 40% OFF na Alto de Monte Verde | Uma mensagem especial para quem já subiu a serra com a gente. |
| 02B-2 | 02b-2-membros-semana-black-friday.html | 27/11 | Membros | Seu refúgio está esperando: 40% OFF até segunda | A serra sente falta de vocês | Faltam 4 dias para a Black Friday terminar. |
| 02B-3 | 02b-3-membros-ultimo-dia.html | 30/11, 10h | Membros | Último dia para voltar à serra com 40% OFF | Termina hoje: a Black Friday da Alto de Monte Verde | Até 23h59 de hoje. |
| 03-1 | 03-1-a-serra-sem-pressa.html | 10/11 | Base Geral + Engajada | Monte Verde em janeiro: a serra sem pressa | Trocar a praia lotada por neblina e lareira? | E o maior desconto do ano para viver isso. |
| 03-2 | 03-2-cada-chale-um-refugio.html | 20/11 | Base Geral + Engajada | Um chalé, uma lareira e vocês dois | O refúgio que vocês estavam procurando | Seis chalés, um mesmo clima: aconchego. |

O pré-header do assunto A já está embutido (oculto) no HTML de cada e-mail.

## O que mudei em relação ao documento de redação

- **"Domingo, 30/11" virou "segunda, 30/11"**: 30/11/2026 cai numa segunda-feira. Afeta o 02A-2 (texto e pré-header) e o 02B-2 (assunto A e texto).
- **Travessões retirados** e trocados por vírgula, dois-pontos ou ponto (02A-2, 02B-1, card da hidro e depoimento no F01-E2, endereço do rodapé).
- **Sem "Descadastrar" manual no rodapé**: o RD Station já coloca esse link sozinho.

## Pontos para confirmar

- **"O maior desconto do ano"** aparece em 02A-1, 02A-2, 02B-1, 03-1 e 03-2. O briefing da landing page pedia para não usar essa frase, por ser uma promessa difícil de comprovar. Mantive como veio na redação.
- **"Até 3x sem juros"** está nas letras miúdas de todos os e-mails e no F01-E1. Na LP essa condição ainda estava pendente de confirmação com a pousada.
- **Fotos**: usei fotos reais do acervo da pousada, as mais próximas de cada descrição. No 02B-3 ("varanda com vista para a serra") entrou a foto da vista de Monte Verde, que não é da varanda da pousada.
- **Depoimento da Amanda (F01-E2)**: texto veio do briefing de Réveillon, não foi conferido no TripAdvisor.
