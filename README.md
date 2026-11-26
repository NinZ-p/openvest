# Openvest
## Projeto
Este repositório contém:
- [X] Uma série de scripts em /extraction/ que convertem os PDFs de provas em MDs e então em JSONs, que em seguida têm as resoluções comentadas por IA e por fim são unidos em um banco de dados de vetores semânticos.
- [ ] As provas do ENEM pré-processadas como markdown, json e banco de vetores semânticos. 
    - 2026 D1 FIG MD
    - 2026 D2 FIG MD
    - 2025 D1 FIG
    - 2025 D2 FIG MD
    - 2024 D1 FIG
    - 2024 D2 FIG
    - 2023 D1 FIG
    - 2023 D2 FIG
    - 2022 D1 FIG
    - 2022 D2 FIG
## Contexto
Este projeto está sendo desenvolvido como parte do projeto <i>Otimização de Softwares</i> do ciclo 4 de 2026. Seu objetivo é produzir um programa de estudos para vestibular que possua baixos requisitos computacionais e de memória. Por isso, questões pedagógicas e de UX estão fora do foco de desenvolvimento.

## Uso de IA
Uso do NotebookLM para estruturar os conteúdos das matrizes de referência do ENEM em formato adequado para LLMs. Uso do Deepseek V4.1 flash 1017 para tornar os prompts mais claros para LLMs e formatá-los corretamente.

## Licensa
- Todo código-fonte de produção própria é disponibilizado sob licensa [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.pt-br). Isso <b>não</b> se aplica às dependências externas nem aos binários com inclusões estáticas.
