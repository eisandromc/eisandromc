# Melhorias aplicadas

## Correções estruturais
- reorganização para `.github/agents`
- reorganização para `.github/skills`
- criação de `SKILL.md` com frontmatter em todas as skills

## Correções de configuração
- remoção de aliases não padronizados como `codebase` e `terminal`
- adoção de aliases oficiais: `read`, `edit`, `search`, `execute`
- inclusão de `target: github-copilot`
- inclusão de `disable-model-invocation` e `user-invocable`
- inclusão de `metadata` útil para catalogação

## Ajustes de arquitetura
- agentes read-only com toolset restrito
- agentes de escrita com `edit`
- agentes de execução com `execute`
- stack agents mantidos como opcionais e com auto-invocação desativada
- regras operacionais adicionadas ao corpo dos agentes

## Observações
- `handoffs` não foram codificados porque o GitHub informa que essa propriedade é ignorada no Copilot cloud agent em GitHub.com.
- o pacote foi otimizado para compatibilidade de repositório e uso prático em GitHub Copilot.
