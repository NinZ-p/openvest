# Openvest
## Projeto
Este repositório contém:
- [X] Uma série de scripts em /extraction/ que convertem os PDFs de provas em MDs e então em JSONs, que em seguida têm as resoluções comentadas por IA e por fim são unidos em um banco de dados de vetores semânticos.
- [ ] As provas do ENEM pré-processadas com LLMs como markdown, json e banco de vetores semânticos. Resultados podem conter erros.
    - 2026 D1 Completo
    - 2026 D2 Completo
    - 2025 D1 Completo
    - 2025 D2 Completo
    - 2024 D1 Completo
    - 2024 D2 Completo
    - 2023 D1 Completo
    - 2023 D2 Completo
    - 2022 D1 Incompleto
    - 2022 D2 Incompleto
    - 2021 D1 Incompleto
    - 2021 D2 Incompleto
    - 2020 D1 Incompleto
    - 2020 D2 Incompleto
    - 2019 D1 Incompleto
    - 2019 D2 Incompleto
    - 2018 D1 Incompleto
    - 2018 D2 Incompleto
    - 2017 D1 Incompleto
    - 2017 D2 Incompleto
    - 2016 D1 Incompleto
    - 2016 D2 Incompleto
    - 2015 D1 Incompleto
    - 2015 D2 Incompleto
    - 2014 D1 Incompleto
    - 2014 D2 Incompleto
    - 2013 D1 Incompleto
    - 2013 D2 Incompleto
    - 2012 D1 Incompleto
    - 2012 D2 Incompleto
    - 2011 D1 Incompleto
    - 2011 D2 Incompleto
    - 2010 D1 Incompleto
    - 2010 D2 Incompleto
    - 2009 D1 Incompleto
    - 2009 D2 Incompleto

## Contexto
Este projeto está sendo desenvolvido como parte do projeto <i>Otimização de Softwares</i> do ciclo 4 de 2026. Seu objetivo é produzir um programa de estudos para vestibular que possua baixos requisitos computacionais e de memória. Por isso, questões pedagógicas e de UX estão fora do foco de desenvolvimento.

## Uso de IA
Uso do NotebookLM para estruturar os conteúdos das matrizes de referência do ENEM em formato adequado para LLMs. Uso do Deepseek V4.1 flash 1017 para tornar os prompts mais claros para LLMs e formatá-los corretamente.

## Licensa
- Todo código-fonte de produção própria é disponibilizado sob licensa [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.pt-br). Isso <b>não</b> se aplica às dependências externas nem aos binários com inclusões estáticas.
