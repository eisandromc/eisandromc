# Arquitetura recomendada

## Núcleo mínimo
1. investigador-de-codigo
2. arquiteto-de-software
3. implementador
4. testes
5. revisor-tecnico
6. devops
7. documentador-tecnico

## Núcleo expandido
8. refatorador
9. seguranca
10. observabilidade
11. performance
12. banco-de-dados
13. apis-e-integracoes
14. github-actions
15. release

## Stack agents opcionais
Ative somente os agentes coerentes com a stack real do repositório. Exemplo, em um projeto Laravel use `php`, `laravel`, `javascript` ou `typescript`, `mysql` ou `postgresql`, `docker` e `github-actions`, mas não carregue stacks irrelevantes.

## Regra de latência e falha
- não usar todos os agentes ao mesmo tempo
- ativar agentes por necessidade real
- preferir skills para checklists e rotinas reutilizáveis
- manter agentes com escopo pequeno e previsível
