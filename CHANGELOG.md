# Changelog

Todas as mudanças relevantes deste repositório são registradas aqui.

O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), e as versões seguem o [Versionamento Semântico](https://semver.org/lang/pt-BR/), conforme a seção 5 do [INSTRUCTIONS.md](INSTRUCTIONS.md).

## [1.2.0] - 2026-10-12

Construção do perfil profissional, da identidade visual e do padrão de engenharia Git e GitHub.

### Adicionado

- **Capa do perfil** (`assets/imgs/topo-readme.png`), com link para o site.
- **Imagem de pré-visualização social** (`assets/imgs/social-preview.png`, 1280 × 640 px, menos de 1 MB), para uso como social preview do repositório ao compartilhar o link.
- **Cards visuais em SVG** na identidade da marca, com fundo da capa e borda multicolorida:
  - `stats.svg`: 20+ anos de experiência e 5.000+ alunos formados;
  - `pilares.svg`: Engenharia, IA aplicada e Educação;
  - `metodo.svg`: modelo 20-70-10, metodologias ativas (Aprendizagem Baseada em Problemas, Aprendizagem Baseada em Projetos, Cultura Maker e STEAM) e foco no protagonismo estudantil.
- **Seções do README:**
  - `helloWorld_`: apresentação, trajetória e atalhos de navegação;
  - Projetos que valem a visita;
  - Como penso e construo, com dois diagramas Mermaid: ciclo de engenharia e engenharia com IA em três etapas (entrada, contexto e geração, controle e entrega);
  - Como ensino;
  - Stack e ferramentas, em 9 grupos, com Skill Icons e badges de IA;
  - Conteúdo, comunidade e contato, com DEV Community, TabNews, Medium, Google Developer, NVIDIA Developer, Stack Overflow e Reddit;
  - Vamos conversar?.
- **Badges de contato** para site, LinkedIn, Instagram e YouTube.
- **`.gitignore`** com regras para Claude Code, OpenAI Codex, Python, sistema operacional, editores e arquivos temporários.
- **`INSTRUCTIONS.md`** (versão 1.3.0): padrão operacional de engenharia Git e GitHub, organizado em 15 seções:
  1. Princípios e níveis de exigência, com classes de governança A a D e vocabulário do processo;
  2. Padrão de nomes de repositórios: regra `tipo-dominio-finalidade`, matriz de escolha rápida, metadados mínimos e cuidados ao renomear;
  3. Catálogo de prefixos (detalhado abaixo);
  4. Padrão de commits com Conventional Commits, tipos e emojis de referência, impacto em SemVer, associação a issues, política de squash e validação por hooks;
  5. Versionamento com SemVer e diferença entre commit, tag, release e deploy;
  6. Governança das branches `main`, `desenv` e `test`, com fluxo de promoção em diagrama, contrato dos ambientes e proteções;
  7. Workflow de projeto criado do zero;
  8. Workflow de alterações, correções e inclusões;
  9. Workflow de homologação, tags e release, com modelo de release notes;
  10. Hotfix, rollback e manutenção pós-release;
  11. Qualidade, automações e configuração do GitHub, com modelos de CI e commitlint;
  12. Templates de issue, pull request, changelog e checklist de versão;
  13. Casos completos de execução (A a D);
  14. Checklist de auditoria e implantação;
  15. Fontes, proveniência e limites.
- **Catálogo de prefixos** com 124 prefixos em 12 categorias, no formato Prefixo, Quando usar e Exemplo. Cada prefixo aparece uma única vez e tem uso distinto dos demais; por exemplo, `content-` cobre planejamento editorial (pautas, calendário e roteiros) e `article-` cobre os artigos publicados. Destaques:
  - `design-`: acervo de design, com dados, imagens, identidade visual e regras de uso;
  - `article-`: exemplos e código de artigos ou posts publicados no LinkedIn, Medium, DEV, TabNews e outras plataformas;
  - `classroom-`: material de aula de uma disciplina ou turma, com slides, roteiros, exercícios e códigos usados em sala.
- **Exemplos de commit com Summary e Description**, explicando o papel de cada campo e como usá-los na linha de comando com dois `-m`:
  - tabela de exemplos válidos e tabela de tipos com Summary e Description;
  - comandos `git commit` dos workflows com Description;
  - casos completos de execução com Summary e Description.
- **Referências no formato ABNT NBR 6023:2018**, em ordem alfabética e sem data de acesso, com citações no texto (CONVENTIONAL COMMITS, 2019), (SILVA, [20--]) e (PRESTON-WERNER, [2013]).
- **`CHANGELOG.md`**: este histórico de mudanças.

### Alterado

- **README**: substituído o modelo padrão do GitHub pelo perfil completo.
- **LICENSE**: a licença MIT foi substituída por uma licença em duas partes:
  - marca, personagens, imagens e textos: todos os direitos reservados;
  - trechos de código e configuração: licença MIT.

## [1.1.0] - 2026-10-12

Criação do repositório de perfil `eisandromc/eisandromc` ([824aefb](https://github.com/eisandromc/eisandromc/commit/824aefb)).

### Adicionado

- **README** com o modelo padrão do GitHub para repositórios de perfil ("Hi there 👋"), com as sugestões de preenchimento comentadas.
- **LICENSE** com a licença MIT.

[1.2.0]: https://github.com/eisandromc/eisandromc/compare/824aefb...main
[1.1.0]: https://github.com/eisandromc/eisandromc/commit/824aefb
