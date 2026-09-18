# emails-alto — Campanha Outubro 2026

Imagens e HTMLs dos 4 e-mails da campanha **Outubro 2026 — Antecipação de Reservas**, pra
subir no MESMO repositório já usado no Réveillon (`github.com/giuiia/emails-alto`).

## Como subir no GitHub (reaproveitando o repo)

⚠️ **Não arraste essa pasta inteira pro repo** — foi exatamente isso que fez os
arquivos do Réveillon ficarem aninhados (`emails-alto/emails-alto/images/...`
em vez de `emails-alto/images/...`). Pra não repetir isso, copie só o
**conteúdo** de `images/` e `emails/` pras pastas que já existem dentro do
seu clone local do repo:

1. Abra sua cópia local do repositório `emails-alto` (a mesma pasta onde você já tem as imagens do Réveillon).
2. Copie os 4 arquivos de `images/` (deste pacote) para dentro da pasta `images/` que já existe no repo.
3. Copie os 4 arquivos de `emails/` (deste pacote) para dentro da pasta `emails/` que já existe no repo.
4. Dentro da pasta do repo, rode:

```
git add .
git commit -m "Imagens e HTML dos e-mails de Outubro 2026"
git push
```

5. Confirme que cada URL abaixo abre a imagem direto no navegador antes de colar o HTML no RD Station:

```
https://raw.githubusercontent.com/giuiia/emails-alto/main/emails-alto/images/banner-01-natal-web.jpg
https://raw.githubusercontent.com/giuiia/emails-alto/main/emails-alto/images/banner-02-verao-web.jpg
https://raw.githubusercontent.com/giuiia/emails-alto/main/emails-alto/images/banner-03-baixa-temporada-web.jpg
https://raw.githubusercontent.com/giuiia/emails-alto/main/emails-alto/images/banner-04-planejamento-web.jpg
```

Os HTMLs já apontam pra essas URLs (o caminho aninhado `emails-alto/images/...` é o
que já está funcionando no repo desde o Réveillon — não o `images/...` "correto" que
o README antigo descrevia). O logo (`logo-header.png`) não precisa ser subido de novo —
os 4 e-mails apontam pro mesmo arquivo que já está no repo.

## Estrutura deste pacote

```
emails-alto/
├── images/
│   ├── banner-01-natal-web.jpg
│   ├── banner-02-verao-web.jpg
│   ├── banner-03-baixa-temporada-web.jpg
│   └── banner-04-planejamento-web.jpg
└── emails/
    ├── email-01-planejamento-antecipado.html
    ├── email-02-baixa-temporada.html
    ├── email-03-verao.html
    └── email-04-natal.html
```

Os `.html` são o código-fonte pra colar direto no editor de HTML do RD Station
("Edição Avançada"), 600px, mobile-first — mesmo padrão dos e-mails de Réveillon.

## Pendências

1. **Link do motor de reservas** — placeholder `#LINK-MOTOR-DE-RESERVAS-A-CONFIRMAR` em todos os botões de CTA.
2. **Imagens quebradas no RD Station** — isso já tinha acontecido nos e-mails de Réveillon: mesmo com a URL certa (abre no navegador), o editor do RD Station às vezes mostra ícone de imagem quebrada. Se isso se repetir aqui, os dois caminhos possíveis são subir as imagens direto na biblioteca do RD Station, ou testar GitHub Pages em vez de raw.githubusercontent.com.
