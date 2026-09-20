# campanha-outubro-2026 — pasta de campanha no repo emails-alto

A partir de agora, o repositório `github.com/giuiia/emails-alto` passa a ter **uma pasta
por campanha** (decisão de 20/09), pra não ficar difícil achar e-mails/imagens conforme
mais campanhas forem entrando. Esta pasta (`campanha-outubro-2026/`) é a primeira nesse
novo padrão.

## Padrão adotado (vale pras próximas campanhas também)

- Nome da pasta: **kebab-case**, ex. `campanha-outubro-2026/`, `reveillon-2026-2027/`.
- Dentro de cada pasta de campanha: `images/` e `emails/`, igual já era.
- **Logo duplicado em cada pasta de campanha** (não fica um logo só compartilhado entre
  todas). Motivo: cada campanha fica 100% independente — se um dia você apagar ou mover
  a pasta de uma campanha antiga, não corre o risco de quebrar o logo de outra que ainda
  está no ar. O custo é só 22KB a mais por campanha, não faz diferença.

```
emails-alto/                          (raiz do repositório)
└── campanha-outubro-2026/
    ├── images/
    │   ├── logo-header.png
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

Os 4 HTMLs já apontam para:
`https://raw.githubusercontent.com/giuiia/emails-alto/main/campanha-outubro-2026/images/...`

## Como subir (arrumando a bagunça atual primeiro)

Hoje o repositório está com duas pastas soltas na raiz que não seguem esse padrão:

- `emails-alto/` — conteúdo do Réveillon, um nível aninhado a mais do que devia
  (`emails-alto/emails-alto/images/...`).
- `Emails/emails-alto/` — o que você tentou subir da campanha de Outubro, mas arrastando
  a pasta "Emails" junto por engano, então os links ainda não funcionam.

Pra deixar tudo limpo com a pasta de Outubro no padrão novo:

1. Abra sua cópia local do repositório `emails-alto`.
2. **Apague a pasta `Emails/` inteira** (a que tem `Emails/emails-alto/...` dentro) — é a
   tentativa de upload que não deu certo, pode remover sem medo.
3. Crie uma pasta nova na raiz do repo chamada `campanha-outubro-2026`.
4. Copie pra dentro dela o conteúdo desta pasta (`images/` e `emails/`, com os arquivos
   já listados acima).
5. Rode:

```
git add .
git commit -m "Organiza e-mails por pasta de campanha: adiciona campanha-outubro-2026"
git push
```

6. Confirme que cada URL abre a imagem direto no navegador antes de colar o HTML no RD Station:

```
https://raw.githubusercontent.com/giuiia/emails-alto/main/campanha-outubro-2026/images/logo-header.png
https://raw.githubusercontent.com/giuiia/emails-alto/main/campanha-outubro-2026/images/banner-01-natal-web.jpg
https://raw.githubusercontent.com/giuiia/emails-alto/main/campanha-outubro-2026/images/banner-02-verao-web.jpg
https://raw.githubusercontent.com/giuiia/emails-alto/main/campanha-outubro-2026/images/banner-03-baixa-temporada-web.jpg
https://raw.githubusercontent.com/giuiia/emails-alto/main/campanha-outubro-2026/images/banner-04-planejamento-web.jpg
```

## Sobre a pasta antiga do Réveillon (`emails-alto/emails-alto/...`)

Por enquanto ela continua exatamente como está, no ar e funcionando — não mexi nela.
Ela é a única coisa ainda fora do padrão novo. Quando quiser, posso preparar a
migração dela pra `reveillon-2026-2027/` (mesma lógica desta pasta), mas como isso
envolve 6 e-mails que já estão em uso, prefiro fazer isso numa etapa separada e com
seu aval, em vez de mexer nisso junto com a entrega de Outubro.

## Pendências

1. **Confirmar migração do Réveillon** pro padrão novo (`reveillon-2026-2027/`) — ver
   nota acima. Só faço se você confirmar que quer isso agora.
2. **Imagens quebradas no editor do RD Station** — já aconteceu no Réveillon (mesmo com
   a URL certa, abrindo no navegador, o editor às vezes mostra ícone de imagem
   quebrada). Se acontecer aqui também, os caminhos alternativos são subir as imagens
   direto na biblioteca do RD Station, ou testar GitHub Pages em vez de
   raw.githubusercontent.com.
