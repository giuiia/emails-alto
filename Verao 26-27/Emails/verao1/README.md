# E-mails Verão 26/27 · Alto de Monte Verde

7 disparos (V1M a V6) + o A3 do Fluxo A com o VERAO27, prontos para colar na Edição Avançada do RD Station.

## O que tem aqui

- `emails/`: 8 HTMLs
- `images/`: 8 banners (1200x700, com logo, selo e título aplicados na imagem), fotos de quarto e café da manhã de cada e-mail e as 6 fotos dos chalés do V4

## Como subir no GitHub (repositório giuiia/emails-alto)

1. No repositório, na RAIZ (ao lado de `black-friday-2026` e `campanha-outubro-2026`), suba a pasta `verao1` inteira.
   Pelo site: "Add file" > "Upload files", estando na raiz, e arraste a pasta `verao1`.
   Não arraste para dentro de outra pasta, senão fica aninhado e as imagens quebram.
2. O caminho final precisa ser `verao1/images/...` e `verao1/emails/...`.
3. Antes de colar no RD, abra estes links no navegador. Tem que abrir a imagem direto:
   - https://raw.githubusercontent.com/giuiia/emails-alto/main/verao1/images/logo-header.png
   - https://raw.githubusercontent.com/giuiia/emails-alto/main/verao1/images/banner-v1.jpg
   - https://raw.githubusercontent.com/giuiia/emails-alto/main/verao1/images/chale-orquidea.jpg

## Assuntos e pré-headers (configurar no RD, teste A/B)

| E-mail | Arquivo | Quando | Público | Assunto A | Assunto B | Pré-header |
|---|---|---|---|---|---|---|
| V1M | v1m-membros-lancamento.html | 02/12 (qua), 9h | Membros fidelidade | Vocês primeiro: o verão na serra com 10% OFF | Para quem já é da casa, o cupom de verão chegou | Estadias de janeiro a março de 2027. Cupom VERAO27. |
| V1 | v1-lancamento.html | 02/12 (qua), 11h | Base Geral (sem membros) | Verão na serra com 10% OFF | Enquanto a cidade ferve, a serra refresca | Dias amenos, noites de lareira. Cupom VERAO27 para jan a mar/27. |
| V2 | v2-janeiro-resolvido.html | 10/12 (qui), 10h | Base Engajada + leads BF sem reserva (bf26-lead) | Férias de janeiro: já escolheram a serra? | Deixem janeiro resolvido antes das festas | 10% OFF em estadias de janeiro a março com o VERAO27. |
| V3 | v3-hospedes-elogiam.html | 07/01 (qui), 10h | Base Geral | O que nossos hóspedes mais elogiam | Nota 9,7 no Booking e 10% OFF neste verão | Café, atendimento e silêncio. Estadias até março com o VERAO27. |
| V4 | v4-qual-chale.html | 21/01 (qui), 10h | Base Engajada | Qual chalé é o de vocês? | Da rede na varanda à hidro sob o teto de vidro | Todos com lareira e 10% OFF até março. |
| V5 | v5-marco-na-serra.html | 11/02 (qui), 10h | Base Geral | Depois do Carnaval, a serra fica assim | Março em Monte Verde, com 10% OFF | Menos movimento, mais silêncio. VERAO27 até 31/03. |
| V6 | v6-ultimos-dias.html | 16/03 (ter), 10h | Base Geral + Base Engajada | Últimos dias: o VERAO27 termina em 31/03 | O verão está acabando (e os 10% OFF também) | Estadias até 31/03, exceto Semana Santa. |
| A3 | fa-a3-cupom-verao.html | Fluxo A, de 01/12 a 31/03 | Visitou o motor e não reservou | (manter o assunto atual do A3) |  | (manter o pré-header atual do A3) |

O pré-header já está embutido (oculto) no HTML de cada e-mail. Todos os botões levam ao motor com `promocode=VERAO27` e UTM `utm_source=rd · utm_medium=email · utm_campaign=verao27 · utm_content=` (v1m, v1, v2, v3, v4, v5, v6, fa-a3).

## Fluxo A

O `fa-a3-cupom-verao.html` é um A3 completo no padrão desta campanha (cupom + botão com VERAO27). Se preferir manter o A3 atual do RD, basta copiar dele o box do cupom e o botão. Período: 01/12/2026 a 31/03/2027; em 01/04 o A3 volta ao incentivo anterior. Lembrar de tirar a exclusão da tag bf26-lead.

## O que mudei em relação ao briefing

- **Abertura com a foto:** o e-mail abre direto no banner. Logo, selo VERÃO 26/27 e título ficam na própria imagem, com o texto alinhado à direita e um degradê verde leve. O título também está no texto alternativo (alt) do banner, para quem abre com imagens bloqueadas.
- **Quarto e café em todos os e-mails:** cada envio tem um bloco com foto de chalé com lareira e do café da manhã (no V1 já eram 3 blocos; no V4 entrou o café junto dos chalés).

- **Orquídea (V4):** a hidro do Orquídea não fica sob o teto de vidro. O card ficou "A mais exclusiva, com hidromassagem e vista privilegiada para a mata".
- **Banner do V4:** o briefing pedia "Orquídea, banheira com teto de vidro", que não existe. Usei a foto aérea dos chalés na mata, para não repetir nenhuma foto dos cards.
- **Travessões retirados:** no depoimento da Amanda (V3) e no endereço do rodapé.
- **Sem "Descadastrar" manual no rodapé:** o RD Station já coloca esse link sozinho.
- **Setas dos botões:** o briefing usa "→" para indicar o link; os botões ficaram só com o texto.

## Pontos para confirmar (do briefing)

- **Notas e depoimento do V3:** 9,7 no Booking, 4,7 no Google e Travellers' Choice no TripAdvisor. Conferir antes de 07/01.
- **Parcelamento:** se o VERAO27 tiver parcelamento, incluir nas letras miúdas.
- **Período do Réveillon fora do cupom:** as letras miúdas dizem só "Réveillon".
- **Leads da Black Friday no V2** e **tag reserva-confirmada** para exclusão.
- **Prazo:** V1M, V1 e V2 precisam estar aprovados até 26/11.
