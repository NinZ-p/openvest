# open-vest
## Projeto
Este repositório contém:
- [ ] Uma série de scripts em /extraction que convertem os PDFs em MDs em JSONs, que então têm as resoluções comentadas por IA e por fim são unidos em um banco de dados de vetores semânticos.
- [ ] Um programa em Rust que oferece uma GUI para permitir estudo de determinados conteúdos dentre o material extraído.

## Contexto
Este projeto está sendo desenvolvido como parte do projeto <i>Otimização de Softwares</i> do ciclo 4 de 2026. Seu objetivo é produzir um programa de estudos para vestibular que possua baixos requisitos computacionais e de memória. Por isso, questões pedagógicas e de UX estão fora do foco de desenvolvimento.

## Uso de IA
Uso do NotebookLM para estruturar os conteúdos das matrizes de referência do ENEM em formato adequado para LLMs. Uso do Deepseek V4.1 flash 1017 para tornar os prompts mais claros para LLMs e formatá-los corretamente.

## Licensa
- Todo código-fonte de produção própria é disponibilizado sob licensa [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.pt-br). Isso <b>não</b> se aplica às dependências externas nem aos binários com inclusões estáticas.