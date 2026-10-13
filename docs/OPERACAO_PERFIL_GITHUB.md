# Governança operacional do repositório de perfil GitHub

**Repositório:** `eisandromc/eisandromc`  
**Escopo:** infraestrutura de revisão, rastreabilidade e validação do README de perfil.  
**Estado:** proposta em Pull Request; configurações administrativas são independentes do merge.

## Fluxo recomendado

1. Abra uma **Issue** para problema ou melhoria relevante.
2. Crie uma branch curta de trabalho a partir da `main`, como `fix/link-site` ou `docs/perfil-projetos`.
3. Edite os arquivos necessários; registre a alteração em um commit semântico.
4. Abra um **Pull Request** para `main` com o template de revisão.
5. Aguarde a validação **Validar perfil / Conferir README e assets**.
6. Verifique o visual no GitHub, inclusive em tela estreita, e avalie os riscos.
7. Faça o merge apenas após aprovação do responsável; confirme o resultado publicado.

A documentação geral de branches, commits e releases está em [`INSTRUCTIONS.md`](../INSTRUCTIONS.md). Para este repositório de perfil, uma branch temporária e uma PR são suficientes na maioria dos casos. `desenv` e `test` devem ser utilizadas somente quando houver uma etapa real de integração ou homologação a justificar sua criação.

## O que a automação verifica

O workflow `.github/workflows/validate-profile.yml` é acionado em Pull Requests e pushes para `main` que alteram README, imagens, scripts, testes ou arquivos `.github`, e também pode ser executado manualmente.

- Executa testes unitários do validador.
- Verifica se imagens e caminhos relativos referenciados pelo README existem.
- Exige texto alternativo em imagens HTML e Markdown.
- Valida sintaxe XML de arquivos SVG e cabeçalhos básicos de PNG.
- Não modifica arquivos, não efetua deploy e utiliza token de leitura.

**Limites:** não confirma URLs externas, execução de serviços de terceiros, renderização oficial do Markdown, conformidade de acessibilidade integral, licenças ou funcionamento de aplicações. Texto, diagramas Mermaid e imagens ainda exigem revisão humana.

## Configurações a realizar pelo administrador no GitHub

Estas ações não são implementadas apenas com arquivos versionados.

### Proteger a `main`

Em `Settings > Branches` ou `Settings > Rules > Rulesets`, crie uma regra direcionada à branch `main`:

- Exigir PR antes de alterações diretas, quando compatível com o fluxo.
- Desativar force push e exclusão da branch.
- Exigir status check **Conferir README e assets** somente **depois** da primeira execução bem-sucedida do workflow.
- Não exigir aprovação de outro usuário enquanto o mantenedor trabalhar sozinho.
- Verificar se regras e eventuais exceções atingem o proprietário conforme pretendido.

**Atenção:** proteções podem bloquear automações que escrevem diretamente na `main`. Confirme os efeitos antes de aplicá-las.

### GitHub Actions

Em `Settings > Actions > General`, mantenha as permissões mínimas necessárias. O workflow proposto não depende de segredos nem de acesso de escrita. Se o GitHub bloquear o workflow por política do repositório, um administrador deverá autorizá-lo.

### Issues e Projects

Crie as etiquetas `bug`, `docs`, `design`, `content`, `enhancement`, `accessibility` e `security`, conforme necessidade. Os templates são fornecidos, mas o cadastro das etiquetas pode exigir configuração adicional.

Um Project opcional pode usar: **Backlog → Pronto → Em andamento → Em revisão → Publicado**. Não é necessário manter um Project se o volume de Issues for pequeno.

### Wiki, Pages e segurança

- **Wiki:** desabilite se não existir documentação colaborativa independente.
- **Pages:** só desabilite após confirmar que não há página ou integração necessária.
- **Segurança:** confira alertas e verificações disponíveis ao plano em `Settings > Security and analysis`.
- **Branches antigas:** avalie `readme` e `vazio`; nenhuma exclusão faz parte desta proposta.

## Critérios de aceite desta implantação

1. Nova branch aberta sem alteração na `main`.
2. Pull Request contém **somente arquivos novos** de `.github/`, `scripts/`, `tests/` e `docs/`.
3. `README.md`, `assets/`, `INSTRUCTIONS.md`, `CHANGELOG.md` e `LICENSE` permanecem inalterados.
4. Verificações locais executadas; workflow no GitHub validado quando for possível observá-lo.
5. Merge reservado exclusivamente à aprovação explícita do responsável.
