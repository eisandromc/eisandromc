---
name: docker-runtime-audit
description: Audita Dockerfiles, compose e imagens com foco em segurança e portabilidade.
---

# Objetivo
Reduzir risco operacional em mudanças Docker.

# Checklist
1. Verificar imagem base, camadas e tamanho.
2. Confirmar portas, variáveis, volumes e healthcheck.
3. Validar execução local, CI e ambiente alvo.
4. Identificar riscos de segredo, usuário root e drift.
