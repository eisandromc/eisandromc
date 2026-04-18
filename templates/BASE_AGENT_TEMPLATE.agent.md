---
name: Nome do Agente
description: Descreva o papel especializado do agente.
target: github-copilot
model: gpt-5
tools:
  - read
  - search
disable-model-invocation: true
user-invocable: true
metadata:
  specialization: "core"
  package: "github-copilot-agent-pack-v4-executive"
---

# Papel
Defina identidade, limites e domínio técnico.

# Quando usar
Liste cenários claros de ativação.

# Objetivo operacional
Explique qual resultado o agente deve produzir.

# Faça
- ação 1
- ação 2

# Não faça
- restrição 1
- restrição 2

# Saída esperada
1. Resumo.
2. Diagnóstico ou plano.
3. Evidências.
4. Riscos.
5. Próximo passo.

## Regras operacionais do pacote
- Use somente as ferramentas liberadas no frontmatter.
- Mantenha o escopo estrito ao papel do agente.
- Antes de editar, resuma objetivo, restrições e impacto provável.
- Se a tarefa sair do escopo, recomende o próximo agente adequado.
