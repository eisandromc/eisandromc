<a href="https://www.sandromartins.com.br">
  <img src="./assets/imgs/topo-readme.png" alt="Sandro Martins — Menos hype. Mais engenharia com propósito. Código, educação e IA para resolver problemas reais e formar talentos." width="100%" />
</a>

<p>
  <a href="https://www.sandromartins.com.br"><img src="https://img.shields.io/badge/Site-142A6E?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Site" /></a>
  <a href="https://www.linkedin.com/in/eisandromc"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://www.instagram.com/eisandromc/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" /></a>  
  <a href="https://www.youtube.com/@eisandromc"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube" /></a>
</p>

## helloWorld_

Oi, eu sou o Sandro! sou engenheiro de software, desenvolvedor full stack e professor de tecnologia. Há mais de 20 anos trabalho em diferentes contextos de desenvolvimento e formação profissional, aproximando **engenharia, educação e problemas que existem fora das apresentações**.

Uma parte importante da minha trajetória foi construída no desenvolvimento de aplicações web, integrações, APIs e soluções para organizações. A outra acontece em salas de aula, laboratórios e projetos integradores, ajudando estudantes a transformar conhecimento em repertório técnico, autonomia e capacidade de tomar decisões. Essas frentes não competem entre si: uma melhora a outra.

Minha atuação docente inclui experiências em **FIAP, Senac RS e Fundatec**. Além da formação profissional, já participei de iniciativas que aproximam tecnologia e responsabilidade social, como ações de recuperação de equipamentos com participação de estudantes durante as enchentes no Rio Grande do Sul. São situações em que conhecimento técnico precisa se converter em ação responsável e útil.

**Este GitHub é o lugar onde organizo o lado demonstrável desse trabalho.** Aqui você encontra projetos, experimentos, materiais de ensino, ferramentas e decisões de arquitetura que podem ser estudados, executados, adaptados ou discutidos conforme a finalidade de cada repositório.


<div align="center">
  <img src="./assets/imgs/stats.svg" alt="20+ anos de experiência · 5.000+ alunos formados" width="100%" />
  <blockquote style="font-size:18px; padding:10px; margin:30px 0;">Tecnologia não se torna valiosa por ser complexa. Ela ganha valor quando resolve um problema, pode ser compreendida e permanece útil depois da primeira entrega.</blockquote>
  <img src="./assets/imgs/pilares.svg" alt="01 Engenharia · 02 IA aplicada · 03 Educação" width="100%" />
</div>

**Por onde começar:** [projetos](#projetos-que-valem-a-visita) · [engenharia](#como-penso-e-construo) · [educação](#como-ensino) · [tecnologias](#stack-e-ferramentas) · [comunidade](#conteudo-comunidade-e-contato)


<br>

## 👨‍💻 Projetos que valem a visita

Prefiro apresentar projetos com uma finalidade clara a usar uma parede de logos como argumento de competência. Os exemplos a seguir mostram diferentes partes do meu trabalho, de automação e interfaces a atividades didáticas e soluções voltadas à educação.

| Projeto | Por que vale conhecer |
|---|---|
| **[SummumOpus](https://github.com/eisandromc/SummumOpus)** · PowerShell | Explora auditoria, configuração, otimização e observabilidade do Windows. Um ponto de partida para discutir automação, critérios operacionais e responsabilidade ao intervir em sistemas. |
| **[Oficina E-commerce](https://github.com/eisandromc/oficina-ecommerce)** · JavaScript | Exercício de carrinho de compras para estudar manipulação do DOM, estado da interface e estruturas de dados em um problema familiar. |
| **[CSS Moderno](https://github.com/eisandromc/css-moderno-container-queries-has-subgrid)** · HTML/CSS | Demonstra Container Queries, `:has()` e Subgrid. O objetivo é compreender quando os recursos melhoram a organização e a adaptação das interfaces. |
| **[Modularização, Componentes e Microsserviços](https://github.com/eisandromc/modularizacao-componentes-microsservios)** · JavaScript | Material para discutir separação de responsabilidades, composição e limites arquiteturais com exemplos navegáveis. |
| **[Cards de Produtos](https://github.com/eisandromc/fiap_front-end-design_cards-produtos)** · Front-end | Atividade de interface para observar hierarquia, espaçamento, contraste e componentes reutilizáveis em um cenário de catálogo. |
| **[Sistema de Banca Avaliativa](https://github.com/eisandromc/sistema-banca-avaliativa)** · Educação e produto | Projeto relacionado à organização do processo de apresentação e avaliação de trabalhos acadêmicos. Consulte o repositório para verificar seu estágio e escopo. |

A organização do conteúdo, a documentação e as licenças variam conforme a finalidade e a maturidade de cada projeto. Nem todo repositório é um produto pronto para produção; alguns foram concebidos para experimentar, ensinar ou documentar uma abordagem.

**[Explorar todos os repositórios](https://github.com/eisandromc?tab=repositories)**

<br>

## 🧠 Como penso e construo

Minha referência inicial não é uma linguagem, um framework ou a ferramenta mais recente. É **o problema a resolver, quem será afetado pela solução e quais restrições precisam ser respeitadas**. A arquitetura deve surgir dessas decisões, com complexidade proporcional ao contexto.

Costumo organizar a análise técnica em cinco perguntas: qual resultado é esperado; quais dados e integrações são necessários; o que precisa ser confiável e seguro; como o trabalho será validado; e como alguém conseguirá manter a solução depois. A documentação é parte dessa conversa, não um artefato preparado apenas no encerramento.

```mermaid
flowchart LR
    P[Problema e contexto] --> R[Requisitos e prioridades]
    R --> A[Modelo e arquitetura]
    A --> I[Implementação]
    I --> V[Testes e validação]
    V --> E[Entrega e observação]
    E -. Aprendizados e melhoria .-> R
    classDef principio fill:#DCEEFF,stroke:#0B7EF3,color:#07142F
    classDef entrega fill:#DDF8EE,stroke:#38CFA2,color:#07142F
    class P,R,A principio
    class I,V,E entrega
```

### Engenharia com IA, sem promessas impossíveis

Em soluções que usam modelos de linguagem, procuro separar **instruções, conhecimento recuperado, ferramentas externas, validação e decisão humana**. Um modelo pode ajudar a interpretar ou produzir informações, mas isso não substitui controle de acesso, testes, rastreabilidade ou revisão quando o risco exige.

RAG e integrações por ferramentas podem ser úteis, mas não são requisitos de toda aplicação. O desenho abaixo representa **uma arquitetura possível**, não uma garantia de precisão ou uma configuração implantada em todos os projetos.


```mermaid
flowchart TB
    subgraph E ["① Entrada"]
        direction LR
        U(["👤 Pessoa e demanda"]) --> O["🧭 Orquestração da tarefa"]
    end
    subgraph G ["② Contexto e geração"]
        direction LR
        R["📚 Consulta autorizada<br/>RAG ou API<br/>(só se precisar de dados externos)"] -.-> M["🧠 Modelo de linguagem"]
    end
    subgraph C ["③ Controle e entrega"]
        direction LR
        Q["✅ Checagens e<br/>critérios de qualidade"] -->|baixo risco| S(["📤 Resposta ou resultado"])
        Q -->|risco ou incerteza| H["🧑‍⚖️ Revisão humana"] --> S
    end
    E --> G --> C
    classDef foco fill:#DCEEFF,stroke:#0B7EF3,stroke-width:2px,color:#07142F
    classDef dados fill:#DDF8EE,stroke:#38CFA2,stroke-width:2px,color:#07142F
    classDef alerta fill:#FFF2C9,stroke:#FFC84A,stroke-width:2px,color:#07142F
    class U,O,S foco
    class R,M,Q dados
    class H alerta
    style E fill:#F7FBFF,stroke:#0B7EF3,stroke-width:1px,color:#07142F
    style G fill:#F5FDF9,stroke:#38CFA2,stroke-width:1px,color:#07142F
    style C fill:#FFFCF2,stroke:#FFC84A,stroke-width:1px,color:#07142F
```

Um princípio orienta essas decisões: **menos improvisação naquilo que importa; mais espaço para experimentar onde o erro é controlável**. Quem mantém um sistema precisa entender suas escolhas, não apenas admirar o resultado na demonstração.

<br>
 
## 🎓 Como ensino

A experiência como professor molda minha forma de desenvolver e comunicar tecnologia. Tenho atuado na formação técnica e no ensino superior, aproximando programação, projetos integradores, arquitetura e empregabilidade. O ponto de partida é sempre tornar o aprendizado **compreensível, praticável e transferível para novos desafios**.

<p align="center">
  <img src="./assets/imgs/metodo.svg" alt="Modelo de planejamento didático 20-70-10: uma referência de 20% de introdução, 70% de prática e 10% de consolidação, com metodologias ativas e foco no estudante." width="100%" />
</p>

O **20-70-10 é uma referência de planejamento que utilizo**, não uma proporção universal ou rígida: uma parte do encontro organiza o conhecimento, a maior parte privilegia investigação e prática e outra parte consolida decisões, dúvidas e aprendizados. A distribuição precisa mudar de acordo com os objetivos, o tempo disponível, o repertório da turma e as necessidades de acessibilidade.

O estudante aprende melhor quando consegue explicar **o que construiu, por que decidiu daquele modo, como verificou o resultado e o que faria diferente**. Por isso, valorizo exercícios reproduzíveis, atividades de projeto, colaboração, documentação, pensamento crítico e espaço real para revisão e erro.

Não se trata de substituir teoria por atividade incessante. Trata-se de dar à teoria o lugar que ela merece: **fundamentar escolhas práticas**. E lembrar que copiar código sem compreender a decisão não é exatamente a habilidade mais disputada do mercado.

<br>

## 🛠️ Stack e ferramentas

Minha base de atuação reúne tecnologias web, integração de sistemas, dados e ferramentas de desenvolvimento. Nesta vitrine, priorizo o conjunto mais relacionado aos projetos e aos conteúdos apresentados, em vez de tratar toda ferramenta explorada como especialidade consolidada.

| Grupo | Tecnologias |
|---|---|
| **Linguagens** | <img src="https://skillicons.dev/icons?i=ts,js,python,php,dart,bash" alt="TypeScript, JavaScript, Python, PHP, Dart, Bash" height="40" /> |
| **Front-end** | <img src="https://skillicons.dev/icons?i=react,nextjs,vue,svelte,astro,vite,tailwind,html,css" alt="React, Next.js, Vue, Svelte, Astro, Vite, Tailwind, HTML, CSS" height="40" /> |
| **Mobile** | <img src="https://skillicons.dev/icons?i=react,flutter" alt="React Native, Flutter" height="40" /> |
| **Back-end** | <img src="https://skillicons.dev/icons?i=nodejs,nestjs,express,laravel,graphql" alt="Node.js, NestJS, Express, Laravel, GraphQL" height="40" /> |
| **Banco de dados** | <img src="https://skillicons.dev/icons?i=postgres,mysql,mongodb,redis,prisma" alt="PostgreSQL, MySQL, MongoDB, Redis, Prisma" height="40" /> |
| **Mensageria** | <img src="https://skillicons.dev/icons?i=rabbitmq,kafka" alt="RabbitMQ, Kafka" height="40" /> |
| **IA e dados** | <img src="https://skillicons.dev/icons?i=python,sklearn" alt="Python, scikit-learn" height="40" /><br /><img src="https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Claude" /> <img src="https://img.shields.io/badge/OpenAI_API-142A6E?style=flat-square" alt="OpenAI API" /> <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangChain" /> <img src="https://img.shields.io/badge/MCP-142A6E?style=flat-square&logo=modelcontextprotocol&logoColor=white" alt="MCP" /> <img src="https://img.shields.io/badge/RAG_+_Vetores-0191FE?style=flat-square" alt="RAG e busca vetorial" /> <img src="https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white" alt="n8n" /> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas" /> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter" /> |
| **DevOps e infra** | <img src="https://skillicons.dev/icons?i=docker,kubernetes,terraform,linux,nginx,githubactions,vercel,netlify" alt="Docker, Kubernetes, Terraform, Linux, Nginx, GitHub Actions, Vercel, Netlify" height="40" /> |
| **Ferramentas e design** | <img src="https://skillicons.dev/icons?i=git,github,vscode,powershell,figma" alt="Git, GitHub, VS Code, PowerShell, Figma" height="40" /> |

Quando uma tecnologia aparece em uma demonstração, procuro deixar clara sua finalidade: o problema que ela resolve, as limitações relevantes e as alternativas possíveis. Uma lista de ferramentas pode ser extensa; capacidade de decisão é o que faz diferença.

<br />

## 🌐 Conteúdo, comunidade e contato

Compartilho experiências e materiais sobre programação, engenharia de software, arquitetura, educação tecnológica, IA aplicada e desenvolvimento profissional. O conteúdo pode assumir a forma de demonstração, atividade de aula, estudo de caso, experimento ou reflexão técnica. A proposta é a mesma: sair da abstração e gerar algo que outra pessoa consiga aproveitar

Para estudantes, valorizo caminhos que desenvolvem autonomia e repertório. Para profissionais, discussões sobre decisões, manutenção, ferramentas e evolução de carreira. Para instituições e equipes, projetos, oficinas e experiências de aprendizagem conectadas a situações reais.

<!-- Para adicionar um membership: copie uma linha da tabela abaixo e troque o nome, o badge e o link.
Badge sem ícone: https://img.shields.io/badge/NOME-COR?style=for-the-badge
Badge com ícone: acrescente &logo=NOME-DO-ICONE&logoColor=white (nomes em https://simpleicons.org) -->

| Community | Perfil |
|---|---|
| <a href="https://dev.to/eisandromc"><img src="https://img.shields.io/badge/DEV_Community-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white" alt="DEV Community" /></a> | [dev.to/eisandromc](https://dev.to/eisandromc) |
| <a href="https://www.tabnews.com.br/eisandromc"><img src="https://img.shields.io/badge/TabNews-142A6E?style=for-the-badge" alt="TabNews" /></a> | [tabnews.com.br/eisandromc](https://www.tabnews.com.br/eisandromc) |
| <a href="https://medium.com/@eisandromc"><img src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" /></a> | [medium.com/@eisandromc](https://medium.com/@eisandromc) |
| <a href="https://g.dev/eisandromc"><img src="https://img.shields.io/badge/Google_Developer-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Developer" /></a> | [g.dev/eisandromc](https://g.dev/eisandromc) |
| <a href="https://developer.nvidia.com/"><img src="https://img.shields.io/badge/NVIDIA_Developer-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="NVIDIA Developer" /></a> | [developer.nvidia.com](https://developer.nvidia.com/) |
| <a href="https://stackoverflow.com/users/26036021/eisandromc"><img src="https://img.shields.io/badge/Stack_Overflow-F58025?style=for-the-badge&logo=stackoverflow&logoColor=white" alt="Stack Overflow" /></a> | [stackoverflow.com/users/26036021/eisandromc](https://stackoverflow.com/users/26036021/eisandromc) |
| <a href="https://www.reddit.com/user/eisandromc/"><img src="https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit" /></a> | [reddit.com/user/eisandromc](https://www.reddit.com/user/eisandromc/) |

<br />

## 🤝 Vamos conversar?


Se você quer desenvolver um projeto, discutir uma decisão de arquitetura, planejar uma formação técnica ou compartilhar uma experiência de aprendizagem, podemos conversar. Gosto especialmente de iniciativas que reúnam **problemas reais, boa engenharia e pessoas dispostas a aprender juntas**.


 <blockquote style="font-size:18px; padding:10px; margin:30px 0;"Aprender, construir e compartilhar. Com critério, curiosidade e propósito.

📬 Fale comigo pelo [LinkedIn](https://www.linkedin.com/in/eisandromc) ou pelo [site](https://www.sandromartins.com.br). Se algum repositório te ajudou, deixe uma ⭐
</blockquote>
