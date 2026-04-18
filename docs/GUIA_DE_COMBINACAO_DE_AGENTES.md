# Guia de combinação de agentes

## Núcleo obrigatório
- investigador-de-codigo
- arquiteto-de-software
- implementador
- testes
- revisor-tecnico
- documentador-tecnico

## Núcleo recomendado para produção
- seguranca
- devops
- observabilidade
- performance
- release

## Regra de stack
Adicione agentes de stack somente quando a stack existir no repositório ou na esteira de build.

## Regra de latência
Evite ativar agentes redundantes ao mesmo tempo. Exemplo, não ativar React, Vue e Angular no mesmo projeto sem necessidade real.
