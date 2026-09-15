# emails-alto

Repositório de imagens dos e-mails da campanha **Réveillon 2026/2027 — Pousada Alto de Monte Verde** (2 fluxos de automação no RD Station Marketing).

## Como subir no GitHub

1. Crie o repositório vazio em `https://github.com/giuiia/emails-alto` (pode ser público, é só pra hospedar as imagens).
2. Na pasta que você recebeu (`emails-alto/`), rode:

```
git init
git add .
git branch -M main
git remote add origin https://github.com/giuiia/emails-alto.git
git commit -m "Imagens e HTML dos e-mails de Réveillon"
git push -u origin main
```

**Importante:** o branch precisa se chamar `main` (não `master`) e a pasta `images/` precisa manter esse nome exato — os HTMLs já apontam para:

```
https://raw.githubusercontent.com/giuiia/emails-alto/main/images/<nome-do-arquivo>
```

Se mudar o nome do branch, da pasta ou de algum arquivo dentro de `images/`, as imagens quebram nos e-mails (banner e logo somem). Depois do push, é só abrir uma das URLs acima no navegador pra confirmar que a imagem carrega antes de colar o HTML no RD Station.

## Estrutura

```
emails-alto/
├── images/
│   ├── logo-header.png        (logo pra cabeçalho, fundo verde floresta)
│   ├── banner-f1-e1.jpg       (Fluxo 1, E1)
│   ├── banner-f1-e2.jpg       (Fluxo 1, E2)
│   ├── banner-f1-e3.jpg       (Fluxo 1, E3)
│   ├── banner-f2-e1.jpg       (Fluxo 2, E1)
│   ├── banner-f2-e2.jpg       (Fluxo 2, E2)
│   └── banner-f2-e3.jpg       (Fluxo 2, E3)
└── emails/
    ├── fluxo1-e1-confirmacao-interesse.html
    ├── fluxo1-e2-prova-social.html
    ├── fluxo1-e3-urgencia.html
    ├── fluxo2-e1-anuncio-campanha.html
    ├── fluxo2-e2-reforco-oferta.html
    └── fluxo2-e3-urgencia.html
```

Os `.html` são o código-fonte pra colar direto no editor de HTML do RD Station (modo "código"), 600px, mobile-first.

## O que foi feito pra atender o feedback da equipe

- **Banners bem mais baixos** (600×260, antes seria algo perto do dobro): cabeçalho + banner + o texto do desconto/oferta cabem juntos na tela sem rolar, mesmo no celular.
- **Foto com texto em cima em todos os e-mails** (badge + título direto na imagem), pra tirar aquele ar "engessado" — variando o layout do banner (centralizado vs. alinhado à esquerda) e a foto entre os 6 e-mails.
- Logo abaixo do banner tem sempre uma linha em destaque (cor caramelo) com a oferta/desconto por extenso, garantindo que ela apareça já na abertura do e-mail.

## Pendências (precisam da sua confirmação antes de publicar)

1. **Link da landing page**: os botões "Ver os pacotes de Réveillon" e "Garantir minha vaga" (Fluxo 2) estão com o placeholder `#LINK-DA-LANDING-PAGE-A-CONFIRMAR` — o próprio briefing marca isso como pendência. Assim que tiver a URL publicada da LP, é só substituir esse texto em todos os arquivos.
2. **Link de descadastro**: usei a tag `%unsubscribe_url%` no rodapé — confirme no RD Station se é essa a tag certa do seu plano, ou se o RD já injeta o descadastro automaticamente quando o HTML é colado (nesse caso dá pra remover a linha).
3. **Fotos**: os nomes de arquivo do briefing (`01-quarto-lareira.jpg`, `02-hidro-vista-mata.jpg` etc.) são direções pra designer, não existem esses arquivos prontos — nem na sua pasta local, nem no Google Drive. Usei as 5 fotos já aprovadas e tratadas dos criativos patrocinados de Réveillon (PAT1–PAT5) como substitutas mais próximas de cada direção visual pedida. Se quiser trocar alguma, me diga qual e eu recomponho o banner.
