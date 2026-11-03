# Gerador dos e-mails Verão 26/27 - Alto de Monte Verde (RD Station)
import os, sys
IMG = 'https://raw.githubusercontent.com/giuiia/emails-alto/main/verao1/images/'
OUT = sys.argv[1]
MOTOR = 'https://hbook.hsystem.com.br/Booking?companyId=63ee3545a74f0691bc7b3f91&promocode=VERAO27'
def utm(cod):
    return (MOTOR + '&utm_source=rd&utm_medium=email&utm_campaign=verao27&utm_content=' + cod).replace('&', '&amp;')

VERDE='#364230'; CREME='#DDD9CD'; CLARO='#F1EEE6'; CARAMELO='#C98939'; TEXTO='#33392C'; BG='#EFEDE6'
SERIF="Georgia,'Times New Roman',serif"; SANS='Arial,Helvetica,sans-serif'
FAIXA_TXT = '10% OFF &middot; M&Iacute;NIMO 2 DI&Aacute;RIAS &middot; ESTADIAS DE JANEIRO A MAR&Ccedil;O DE 2027'
MIUDAS = 'Válido para reservas diretas no site de 01/12/2026 a 31/03/2027, para estadias de 01/01 a 31/03/2027. Mínimo 2 diárias, exceto feriados: Réveillon, Carnaval (05 a 10/02) e Semana Santa (25 a 28/03). Não cumulativo com outras promoções. Sujeito à disponibilidade.'

def row(inner, pad='18px 32px 0', bg=CREME, align='center'):
    return f'''        <tr>
          <td class="px" style="background:{bg};padding:{pad};text-align:{align};">
{inner}
          </td>
        </tr>
'''
def header():
    return f'''        <tr>
          <td style="background:{CLARO};padding:26px 24px 20px;text-align:center;">
            <img src="{IMG}logo-header.png" width="190" height="81" alt="Alto de Monte Verde &middot; Pousada nas Montanhas" style="display:block;margin:0 auto 16px;border:0;outline:none;width:190px;max-width:190px;height:auto;color:{VERDE};font-family:{SERIF};font-size:18px;">
            <span style="display:inline-block;border:1.5px solid {CARAMELO};color:{VERDE};font-family:{SANS};font-size:11px;font-weight:bold;letter-spacing:3px;padding:7px 16px;border-radius:30px;">VER&Atilde;O 26/27</span>
          </td>
        </tr>
'''
def banner(arq, alt):
    return f'''        <tr>
          <td style="padding:0;line-height:0;font-size:0;">
            <img src="{IMG}{arq}" width="600" height="350" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;outline:none;background:{VERDE};color:#FFFFFF;font-family:{SERIF};font-size:22px;line-height:30px;text-align:center;">
          </td>
        </tr>
'''
def faixa():
    return f'''        <tr>
          <td style="background:{VERDE};padding:13px 16px;text-align:center;">
            <p style="margin:0;font-family:{SANS};font-size:11.5px;font-weight:bold;letter-spacing:1.4px;line-height:1.6;color:{CARAMELO};">{FAIXA_TXT}</p>
          </td>
        </tr>
'''
def titulo(t, pad='30px 32px 0'):
    return row(f'            <h1 style="margin:0;font-family:{SERIF};font-size:28px;line-height:1.25;font-weight:normal;color:{VERDE};">{t}</h1>', pad)
def p(t, pad='16px 32px 0', size=16, color=TEXTO, bold=False, italic=False):
    w = ('font-weight:bold;' if bold else '') + ('font-style:italic;' if italic else '')
    return row(f'            <p style="margin:0;font-family:{SERIF};font-size:{size}px;line-height:1.65;{w}color:{color};">{t}</p>', pad)
def botao(txt, url, pad='26px 32px 6px'):
    return row(f'''            <table role="presentation" class="btn" border="0" cellpadding="0" cellspacing="0" align="center" style="margin:0 auto;">
              <tr><td align="center" bgcolor="{CARAMELO}" style="background:{CARAMELO};border-radius:30px;mso-padding-alt:16px 36px;">
                <a href="{url}" target="_blank" style="display:inline-block;color:#FFFFFF;font-family:{SANS};font-size:15px;line-height:18px;font-weight:bold;letter-spacing:1.2px;text-transform:uppercase;text-decoration:none;padding:16px 36px;border-radius:30px;mso-padding-alt:0;">{txt}</a>
              </td></tr>
            </table>''', pad)
def miudas(pad='24px 36px 30px'):
    return row(f'            <p style="margin:0;font-family:{SANS};font-size:11px;line-height:1.6;color:#6B7464;">{MIUDAS}</p>', pad)
def ps(t, pad='22px 32px 0'):
    return p(f'<strong>P.S.</strong> {t}', pad, 14.5)
def rodape():
    return f'''        <tr>
          <td style="background:{VERDE};padding:28px 32px 30px;text-align:center;">
            <p style="margin:0 0 4px;font-family:{SANS};font-size:12px;line-height:1.6;color:#C9CFC0;">Alto de Monte Verde &middot; Pousada nas Montanhas</p>
            <p style="margin:0 0 12px;font-family:{SANS};font-size:12px;line-height:1.6;color:#C9CFC0;">Rua Canela, 110 &middot; Monte Verde (MG)</p>
            <p style="margin:0 0 12px;font-family:{SERIF};font-size:15px;line-height:1.5;color:{CARAMELO};">Seu ponto alto, entre a neblina.</p>
            <p style="margin:0;font-family:{SANS};font-size:11px;line-height:1.6;color:#AEB5A4;">Você recebe este e-mail porque se cadastrou em nossos canais.</p>
          </td>
        </tr>
'''
def cupom_box(pad='26px 32px 0'):
    return row(f'''            <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="background:{CLARO};border:2px solid {CARAMELO};border-radius:10px;">
              <tr><td style="padding:22px 16px 20px;text-align:center;">
                <p style="margin:0 0 6px;font-family:{SANS};font-size:11.5px;font-weight:bold;letter-spacing:3px;color:{CARAMELO};">SEU CUPOM</p>
                <p style="margin:0 0 4px;font-family:{SANS};font-size:36px;line-height:1.1;font-weight:bold;letter-spacing:5px;color:{VERDE};">VERAO27</p>
                <p style="margin:0 0 8px;font-family:{SANS};font-size:13px;font-weight:bold;letter-spacing:2px;color:{CARAMELO};">10% OFF</p>
                <p style="margin:0;font-family:{SERIF};font-size:14.5px;line-height:1.5;font-style:italic;color:#5C6656;">O cupom já vai aplicado no botão.</p>
              </td></tr>
            </table>''', pad)
def caixa(inner, pad='24px 32px 0'):
    return row(f'''            <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="background:{CLARO};border-radius:10px;">
              <tr><td style="padding:20px 24px;text-align:center;">
{inner}
              </td></tr>
            </table>''', pad)
def cards(itens, pad='24px 26px 0'):
    cells = ''
    for n, (arq, t, d) in enumerate(itens):
        if n and n % 2 == 0: cells += '\n<!--[if mso]></tr><tr><![endif]-->'
        cells += f'''<!--[if mso]><td valign="top" width="274" style="padding:0 3px 12px;"><![endif]-->
              <div style="display:inline-block;width:100%;max-width:262px;vertical-align:top;margin:0 3px 12px;">
                <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="background:{CLARO};border-radius:10px;">
                  <tr><td style="padding:0;line-height:0;font-size:0;"><img src="{IMG}{arq}" width="262" height="175" alt="{t}" style="display:block;width:100%;max-width:262px;height:auto;border:0;outline:none;border-radius:10px 10px 0 0;"></td></tr>
                  <tr><td style="padding:14px 16px 18px;text-align:left;">
                    <p style="margin:0 0 6px;font-family:{SERIF};font-size:17px;line-height:1.3;color:{VERDE};">{t}</p>
                    <p style="margin:0;font-family:{SERIF};font-size:14px;line-height:1.55;color:{TEXTO};">{d}</p>
                  </td></tr>
                </table>
              </div>
<!--[if mso]></td><![endif]-->'''
    return f'''        <tr>
          <td style="background:{CREME};padding:{pad};text-align:center;font-size:0;">
<!--[if mso]><table role="presentation" width="548" align="center" border="0" cellpadding="0" cellspacing="0"><tr><![endif]-->
{cells}
<!--[if mso]></tr></table><![endif]-->
          </td>
        </tr>
'''
def prova(nota, depo=None, autor=None):
    h = f'            <p style="margin:0;font-family:{SANS};font-size:13px;font-weight:bold;letter-spacing:1px;line-height:1.6;color:{VERDE};">{nota}</p>'
    if depo:
        h += f'\n            <p style="margin:12px 0 0;font-family:{SERIF};font-size:16px;line-height:1.6;font-style:italic;color:{TEXTO};">{depo}</p>'
        h += f'\n            <p style="margin:6px 0 0;font-family:{SANS};font-size:12px;letter-spacing:.5px;color:#6B7464;">{autor}</p>'
    return row(f'''            <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" style="border-top:1px solid #C3BDAC;border-bottom:1px solid #C3BDAC;">
              <tr><td style="padding:18px 8px;text-align:center;">
{h}
              </td></tr>
            </table>''', '24px 32px 0')

TAB=[]
Q_TXT='A noite fresca da serra lá fora, o aconchego aqui dentro.'
C_TXT='Pães e bolos caseiros, queijos mineiros e pão de queijo feitos na pousada.'
def quarto_cafe(q, c, pad='22px 26px 0'):
    return cards([(q, 'Chalés com lareira', Q_TXT), (c, 'Café da manhã artesanal', C_TXT)], pad)
SPACER = ' &zwnj;&nbsp;' * 60  # evita que o texto do corpo apareça na prévia da caixa de entrada
def email(cod, arq, quando, publico, assA, assB, pre, corpo):
    html = f'''<!DOCTYPE html>
<html lang="pt-BR" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="UTF-8">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{assA}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
  a[x-apple-data-detectors]{{color:inherit!important;text-decoration:none!important;}}
  body{{margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}}
  @media only screen and (max-width:480px){{
    .px{{padding-left:22px!important;padding-right:22px!important;}}
    .btn a{{padding:16px 24px!important;letter-spacing:.8px!important;}}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:{BG};-webkit-text-size-adjust:100%;">
  <div style="display:none;max-height:0;max-width:0;overflow:hidden;opacity:0;mso-hide:all;font-size:1px;line-height:1px;color:{BG};">
    {pre}{SPACER}
  </div>
  <table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="{BG}" style="background:{BG};">
    <tr>
      <td align="center" style="padding:24px 12px;">
<!--[if mso]><table role="presentation" width="600" align="center" border="0" cellpadding="0" cellspacing="0"><tr><td><![endif]-->
        <table role="presentation" width="600" border="0" cellpadding="0" cellspacing="0" style="width:100%;max-width:600px;background:{CREME};">

{corpo}
        </table>
<!--[if mso]></td></tr></table><![endif]-->
      </td>
    </tr>
  </table>
</body>
</html>
'''
    ruins = sorted(set(c for c in html if ord(c) > 0xFF))
    assert not ruins, (arq, ruins)
    assert '&mdash;' not in html and '—' not in html
    open(os.path.join(OUT, arq), 'w', encoding='utf-8').write(html)
    TAB.append((cod, arq, quando, publico, assA, assB, pre)); print(arq, len(html))

H = header; FIM = lambda: miudas() + rodape()

# V1M
email('V1M', 'v1m-membros-lancamento.html', '02/12 (qua), 9h', 'Membros fidelidade',
  'Vocês primeiro: o verão na serra com 10% OFF', 'Para quem já é da casa, o cupom de verão chegou',
  'Estadias de janeiro a março de 2027. Cupom VERAO27.',
  banner('banner-v1m.jpg', 'Alto de Monte Verde &middot; Ver&atilde;o 26/27: Vocês já conhecem o caminho') + faixa()
  + p('Quem já se hospedou aqui sabe: o café da manhã sem pressa, a rede na varanda, a hidromassagem com vista para a mata.')
  + p('Antes de abrir para todo mundo, o cupom de verão é de vocês: 10% OFF em estadias de janeiro a março de 2027.', '10px 32px 0')
  + quarto_cafe('card-quarto-lavanda.jpg', 'card-cafe-mesa.jpg')
  + cupom_box() + botao('Voltar para a serra', utm('v1m'))
  + ps('Se o desconto não aparecer, digitem VERAO27 no campo de cupom.') + FIM())

# V1
email('V1', 'v1-lancamento.html', '02/12 (qua), 11h', 'Base Geral (sem membros)',
  'Verão na serra com 10% OFF', 'Enquanto a cidade ferve, a serra refresca',
  'Dias amenos, noites de lareira. Cupom VERAO27 para jan a mar/27.',
  banner('banner-v1.jpg', 'Alto de Monte Verde &middot; Ver&atilde;o 26/27: Enquanto a cidade ferve, a serra refresca') + faixa()
  + p('Dias amenos, noites frescas e a lareira acesa no fim do dia. Neste verão, troquem o calor e o trânsito pelo silêncio da mata de Monte Verde.')
  + p('Com o cupom VERAO27, vocês têm 10% OFF em estadias de janeiro a março de 2027.', '10px 32px 0')
  + cards([('card-hidro.jpg', 'Hidromassagem com vista', 'Hidro dupla de frente para a mata nativa.'),
           ('card-lareira.jpg', 'Lareira em todos os chalés', 'A noite fresca da serra lá fora, o aconchego aqui dentro.'),
           ('card-cafe.jpg', 'Café da manhã artesanal', 'Pães e bolos caseiros, queijos mineiros e pão de queijo feitos na pousada.')])
  + cupom_box('14px 32px 0') + botao('Reservar com 10% OFF', utm('v1'))
  + ps('O cupom já vai aplicado no botão. Se não aparecer, digitem VERAO27 no campo de cupom.') + FIM())

# V2
email('V2', 'v2-janeiro-resolvido.html', '10/12 (qui), 10h', 'Base Engajada + leads BF sem reserva (bf26-lead)',
  'Férias de janeiro: já escolheram a serra?', 'Deixem janeiro resolvido antes das festas',
  '10% OFF em estadias de janeiro a março com o VERAO27.',
  banner('banner-v2.jpg', 'Alto de Monte Verde &middot; Ver&atilde;o 26/27: Janeiro começa aqui') + faixa()
  + p('Dezembro corre: trabalho, festas, presentes. Deixem a primeira escapada do ano resolvida agora e cheguem em janeiro só para descansar.')
  + p('Chalé com lareira, hidromassagem com vista para a mata e o café da manhã mais elogiado pelos nossos hóspedes. Com 10% OFF.', '10px 32px 0')
  + quarto_cafe('card-quarto-margarida.jpg', 'card-cafe.jpg')
  + cupom_box() + botao('Escolher minhas datas', utm('v2'), '26px 32px 34px') + FIM())

# V3
email('V3', 'v3-hospedes-elogiam.html', '07/01 (qui), 10h', 'Base Geral',
  'O que nossos hóspedes mais elogiam', 'Nota 9,7 no Booking e 10% OFF neste verão',
  'Café, atendimento e silêncio. Estadias até março com o VERAO27.',
  banner('banner-v3.jpg', 'Alto de Monte Verde &middot; Ver&atilde;o 26/27: Quem vem, conta') + faixa()
  + p('Escolher onde ficar dá trabalho. Por isso a gente deixa nossos hóspedes falarem: o café da manhã artesanal, o atendimento e o silêncio da mata são o que eles mais elogiam.')
  + prova('9,7 NO BOOKING, COM MAIS DE 500 AVALIA&Ccedil;&Otilde;ES &middot; 4,7 NO GOOGLE &middot; TRAVELLERS&rsquo; CHOICE NO TRIPADVISOR',
          '&ldquo;Equipe simpática e prestativa! Experiência romântica, com pétalas de rosa e café da manhã variado, espetacular.&rdquo;', 'Amanda, Goiânia (TripAdvisor)')
  + quarto_cafe('card-quarto-jasmin.jpg', 'card-cafe-mesa.jpg')
  + cupom_box() + botao('Reservar com 10% OFF', utm('v3'), '26px 32px 34px') + FIM())

# V4
email('V4', 'v4-qual-chale.html', '21/01 (qui), 10h', 'Base Engajada',
  'Qual chalé é o de vocês?', 'Da rede na varanda à hidro sob o teto de vidro',
  'Todos com lareira e 10% OFF até março.',
  banner('banner-v4.jpg', 'Alto de Monte Verde &middot; Ver&atilde;o 26/27: Qual chalé é o de vocês?') + faixa()
  + p('Todos os chalés têm lareira, privacidade e café da manhã artesanal incluso. A diferença está no jeito de viver a serra.')
  + cards([('chale-margarida.jpg', 'Margarida', 'Cama king, lareira e rede na varanda.'),
           ('chale-azaleia.jpg', 'Azaleia', 'Hidromassagem dupla e lareira.'),
           ('chale-geranio.jpg', 'Gerânio', 'Hidro sob o teto de vidro e varanda envidraçada.'),
           ('chale-jasmin.jpg', 'Jasmin', 'Ambiente amplo e excelente privacidade.'),
           ('chale-lavanda.jpg', 'Lavanda', 'Mezanino e o maior espaço interno.'),
           ('chale-orquidea.jpg', 'Orquídea', 'A mais exclusiva, com hidromassagem e vista privilegiada para a mata.')])
  + cards([('card-cafe-mesa.jpg', 'Café da manhã artesanal', C_TXT)], '0 26px 0')
  + cupom_box('14px 32px 0') + botao('Ver chalés e datas', utm('v4'), '26px 32px 34px') + FIM())

# V5
email('V5', 'v5-marco-na-serra.html', '11/02 (qui), 10h', 'Base Geral',
  'Depois do Carnaval, a serra fica assim', 'Março em Monte Verde, com 10% OFF',
  'Menos movimento, mais silêncio. VERAO27 até 31/03.',
  banner('banner-v5.jpg', 'Alto de Monte Verde &middot; Ver&atilde;o 26/27: Março é o segredo da serra') + faixa()
  + p('Passadas as férias e o Carnaval, Monte Verde volta ao ritmo dela: trilhas tranquilas, mata sem pressa e o chalé só para vocês.')
  + p('Março ainda tem datas com 10% OFF. Que tal um meio de semana a dois?', '10px 32px 0')
  + quarto_cafe('card-quarto-azaleia.jpg', 'card-cafe-buffet.jpg')
  + cupom_box() + botao('Reservar março', utm('v5'), '26px 32px 34px') + FIM())

# V6
email('V6', 'v6-ultimos-dias.html', '16/03 (ter), 10h', 'Base Geral + Base Engajada',
  'Últimos dias: o VERAO27 termina em 31/03', 'O verão está acabando (e os 10% OFF também)',
  'Estadias até 31/03, exceto Semana Santa.',
  banner('banner-v6.jpg', 'Alto de Monte Verde &middot; Ver&atilde;o 26/27: O verão está acabando') + faixa()
  + p('Ainda dá tempo de uma escapada a dois antes do outono: estadias até 31 de março com 10% OFF.')
  + p('Lareira, hidromassagem e café da manhã artesanal esperando por vocês.', '10px 32px 0')
  + caixa(f'                <p style="margin:0 0 6px;font-family:{SANS};font-size:11.5px;font-weight:bold;letter-spacing:2.5px;color:{CARAMELO};">DATAS COM 10% OFF</p>\n                <p style="margin:0;font-family:{SERIF};font-size:16px;line-height:1.55;color:{TEXTO};">Estadias de 16 a 24/03 e de 29 a 31/03.<br><span style="font-size:14px;color:#5C6656;">A Semana Santa, de 25 a 28/03, fica fora do cupom.</span></p>')
  + quarto_cafe('card-quarto-margarida.jpg', 'card-cafe-buffet.jpg')
  + cupom_box('16px 32px 0') + botao('Garantir minha data', utm('v6'))
  + ps('O cupom vale até 31/03. Depois disso, ele sai do ar.') + FIM())

# A3 (Fluxo A)
email('A3', 'fa-a3-cupom-verao.html', 'Fluxo A, de 01/12 a 31/03', 'Visitou o motor e não reservou',
  '(manter o assunto atual do A3)', '', '(manter o pré-header atual do A3)',
  banner('banner-a3.jpg', 'Alto de Monte Verde &middot; Ver&atilde;o 26/27: Ainda pensando nas datas?') + faixa()
  + p('O cupom de verão segue valendo: 10% OFF em estadias de janeiro a março de 2027, mínimo 2 diárias, exceto feriados.')
  + quarto_cafe('card-lareira.jpg', 'card-cafe.jpg')
  + cupom_box() + botao('Reservar com 10% OFF', utm('fa-a3'), '26px 32px 34px') + FIM())

import json; json.dump(TAB, open(os.path.join(OUT, '..', '_tabela.json'), 'w'), ensure_ascii=False)
