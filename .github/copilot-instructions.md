# Instruções globais do repositório, Stack Alvo Especializada

Este repositório opera com foco preferencial em PHP, TypeScript, Flutter, Dart, C#, Docker, AWS e GitHub Actions.

## Regras operacionais
- Priorize mudanças pequenas, rastreáveis e reversíveis.
- Não implemente sem resumir objetivo, restrições e critério de aceitação.
- Leia apenas o contexto necessário antes de editar.
- Sempre proponha ou atualize testes quando houver mudança funcional.
- Em pipelines, containers e infraestrutura, valide impacto operacional antes de editar.
- Em contratos entre backend, frontend e mobile, valide compatibilidade antes de alterar tipos, DTOs, schemas ou payloads.

## Ordem preferencial de agentes
1. investigador-de-codigo
2. arquiteto-de-software
3. implementador
4. agente de stack aplicável
5. testes
6. revisor-tecnico
7. github-actions, devops ou aws, quando houver impacto operacional
8. documentador-tecnico, quando houver mudança de uso ou setup

## Regras por stack
### PHP
- Preserve compatibilidade e clareza de contratos.
- Prefira mudanças que respeitem estrutura existente do projeto.
- Ao tocar backend web, valide rotas, serviços, validação, exceptions e testes.

### TypeScript
- Não degrade tipagem para acelerar entrega.
- Prefira tipos explícitos em superfícies críticas.
- Valide build, lint e testes antes de concluir.

### Flutter e Dart
- Preserve arquitetura de estado já adotada no projeto.
- Evite quebrar navegação, tema, internacionalização e lifecycle.
- Sempre considerar impacto em Android e iOS quando a mudança for cross-platform.

### C#
- Preserve contratos, DI, logging e convenções do ecossistema .NET.
- Valide configuração, build e testes antes de concluir.

### Docker
- Minimize tamanho, superfície de ataque e inconsistência entre ambiente local e CI.
- Evite alterar imagens base sem necessidade técnica clara.

### AWS
- Trate alterações de cloud como sensíveis.
- Descreva impacto em custo, segurança, permissões, observabilidade e rollback.

### GitHub Actions
- Preserve segurança de secrets, permissões mínimas, cache, matrix e reprodutibilidade.
- Em workflows críticos, priorize mudanças incrementais.
