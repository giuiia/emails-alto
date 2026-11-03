# Auditoria técnica · E-mails Verão 26/27 (03/11/2026)

## Peso

| E-mail | HTML | Imagens | Peso das imagens | Total |
|---|---|---|---|---|
| fa-a3-cupom-verao.html | 8.3 KB | 2 | 91 KB | 100 KB |
| v1-lancamento.html | 13.0 KB | 5 | 171 KB | 184 KB |
| v1m-membros-lancamento.html | 9.1 KB | 2 | 92 KB | 101 KB |
| v2-janeiro-resolvido.html | 8.7 KB | 2 | 94 KB | 103 KB |
| v3-hospedes-elogiam.html | 9.5 KB | 2 | 92 KB | 102 KB |
| v4-qual-chale.html | 15.7 KB | 8 | 316 KB | 331 KB |
| v5-marco-na-serra.html | 8.7 KB | 2 | 79 KB | 87 KB |
| v6-ultimos-dias.html | 9.8 KB | 2 | 91 KB | 101 KB |

Todos os HTMLs ficam muito abaixo do limite de corte do Gmail (102 KB). Pasta images/ inteira: ~970 KB.

## Correções feitas (sem mudar visual, textos, imagens ou CTAs)

1. Botão à prova de Outlook: o botão era um <a> com padding, que o Outlook desktop ignora (vira um link pequeno). Agora é uma tabela com bgcolor + mso-padding-alt; nos demais clientes fica idêntico.
2. Cards do V1 e do V4 no Outlook: a tabela-fantasma do Outlook punha todos os cards numa linha só (6 colunas espremidas no V4). Agora quebra a cada 2 cards, igual ao desktop.
3. Largura fixa de 600px no Outlook: o Outlook ignora max-width e esticava o e-mail na tela toda. Entrou um wrapper condicional de 600px só para ele.
4. Escala do Outlook em telas com zoom (120%/150%): adicionado OfficeDocumentSettings PixelsPerInch 96.
5. Head completo: charset, viewport, X-UA-Compatible, x-apple-disable-message-reformatting, format-detection (impede o iPhone de transformar endereço e datas em links azuis) e color-scheme light.
6. Prévia da caixa de entrada: o pré-header agora tem um espaçador, para o texto do corpo não aparecer colado depois dele.
7. Mobile: em telas até 480px, a margem lateral cai de 32 para 22px e o botão ganha menos respiro lateral. Antes, "ESCOLHER MINHAS DATAS" quebrava em duas linhas no iPhone.
8. Imagens: width e height em todas (evita salto de layout e mantém o espaço com imagens bloqueadas), outline:none, e fundo verde com texto do alt visível no banner quando as imagens estão desligadas.
9. border="0" em todas as tabelas (bordas fantasmas em Outlook antigo).
10. Peso: logo de 49 KB para 7 KB (380px, 2x da exibição, PNG de 128 cores); banners recomprimidos para até ~85 KB (antes até 180 KB); fotos dos cards para até ~27 KB. Tudo em JPEG progressivo.

## Compatibilidade (avaliação)

- Gmail (web e app): bom. CSS inline; media query no head é suportada no app do Gmail.
- Outlook desktop (Windows): bom após as correções 1 a 4. Cantos arredondados viram retos (limitação do Outlook, sem quebrar nada).
- Outlook web / Outlook.com: bom.
- Apple Mail / iOS: bom.
- Yahoo, Samsung Mail: bom (estrutura em tabela, sem JS, sem fontes externas).
- Modo escuro: sem cores invertidas em Apple Mail (color-scheme light). O Gmail app e o Outlook podem escurecer o fundo creme; textos continuam legíveis.

## RD Station

- HTML com CSS inline, sem JavaScript, sem formulários e sem fontes externas: importável na Edição Avançada.
- Todos os botões: promocode=VERAO27 + utm_source=rd, utm_medium=email, utm_campaign=verao27 e utm_content próprio. O RD envolve os links no rastreamento dele sem perder os parâmetros.
- Sem caracteres acima de U+00FF no código: travessão, aspas curvas e setas estão como entidades HTML (o RD corrompe esses caracteres quando entram direto).
- Descadastro: o RD Station insere o link de descadastro e o rodapé de compliance automaticamente no envio. Por isso não há link manual.

## Ainda precisam de atenção

- Título dentro da imagem (pedido de layout): quem abre com imagens bloqueadas (comum no Outlook desktop até clicar em "baixar imagens") vê o texto alternativo com o título, sobre fundo verde, em vez da arte. O resto do e-mail segue legível.

- As imagens ainda não estão no GitHub (as URLs de verao1/images respondem 404 até a pasta subir). Depois de subir, abrir as URLs no navegador e mandar um e-mail de teste pelo RD.
- Histórico: no Réveillon, o editor do RD mostrou imagens quebradas com links raw.githubusercontent.com, mesmo com as URLs funcionando. Se acontecer de novo, a saída é subir as imagens na biblioteca do próprio RD e trocar o endereço base.
- V4 é o mais pesado (331 KB, 8 imagens). Está dentro do aceitável; o banner aéreo tem muito detalhe e não comprime mais sem perder qualidade.
- Em telas muito estreitas (320px, iPhone SE antigo), os botões com texto mais longo quebram em 2 linhas. Continuam centralizados e fáceis de tocar.
- Testar no Litmus ou Email on Acid, se a Thrive tiver conta, principalmente Outlook 2016/2019 no Windows.
