---
name: dotnet-delivery-gate
description: Aplica validação curta para mudanças C# e .NET antes de merge.
---

# Objetivo
Padronizar validação de entrega em projetos .NET.

# Checklist
1. Verificar DI, configuração e logging.
2. Confirmar compatibilidade de contratos e serialização.
3. Revisar efeitos em migrations, background jobs e APIs, quando houver.
4. Solicitar build e testes aplicáveis.
