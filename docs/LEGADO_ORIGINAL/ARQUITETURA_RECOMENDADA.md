# Arquitetura recomendada para GitHub Copilot

## Objetivo
Reduzir falhas, retrabalho e demora por meio de especialização funcional.

## Camadas
### 1. Planejamento
- Investigador de Código
- Arquiteto de Software
- Planejador de Tarefas

### 2. Execução
- Implementador
- Refatorador
- Agente por stack, quando necessário

### 3. Qualidade
- Testes
- Revisor Técnico
- Segurança
- Performance
- Acessibilidade, quando aplicável

### 4. Entrega e Operação
- DevOps
- GitHub Actions
- Release
- Observabilidade
- Documentador

## Regras de desenho
- Não misturar planejamento, implementação e revisão no mesmo agente.
- Não deixar o Implementador aprovar sua própria saída.
- Não embutir lógica de teste dentro do agente de documentação.
- Não criar agentes por linguagem se o projeto não exigir profundidade local.
- Usar agentes de stack apenas quando houver acoplamento técnico real.

## Pacote mínimo
- Investigador
- Arquiteto
- Implementador
- Testes
- Revisor Técnico
- DevOps
- Documentador

## Pacote recomendado
- Investigador
- Arquiteto
- Implementador
- Refatorador
- Testes
- Revisor Técnico
- Segurança
- DevOps
- Observabilidade
- Documentador
- Agentes de stack críticos do projeto

## Critério para adicionar um novo agente
Crie um novo agente apenas quando:
1. houver tarefa recorrente e especializada,
2. o escopo puder ser claramente delimitado,
3. a separação reduzir erro ou latência,
4. houver convenções ou ferramentas específicas demais para um agente genérico.

## Critério para usar skill em vez de agente
Use skill quando a diferença estiver no procedimento, checklist, script, comando ou fluxo recorrente, e não na identidade principal do agente.
