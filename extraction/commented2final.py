print ("Loading modules")

from pathlib import Path

import os
import json
import re

from sentence_transformers import SentenceTransformer
import torch
import veclite

print ("Loaded modules")

program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
commented_json_folder_path=program_path/"provas_json_comentadas"
commented_json_folder_paths=[Path(commented_json_folder_path/x) for x in os.listdir(commented_json_folder_path)]
final_folder_path=program_path/"provas_final"
db_path=final_folder_path/"tstast_db.vec"

index_conteudos=[]

markdown_image_pattern = re.compile(r'!\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)')

mapa_conhecimentos_de_área={
    "Linguagens | Competência de Área 1": [
        "tecnologias da informação",
        "tecnologias da comunicação",
        "comunicação digital",
        "informação",
        "recursos tecnológicos",
        "ferramentas digitais",
        "tecnologia na educação",
        "tecnologia no trabalho",
        "meios de comunicação",
        "contextos sociais"
    ],
    "Linguagens | Competência de Área 2": [
        "língua estrangeira",
        "língua inglesa",
        "língua espanhola",
        "idioma",
        "cultura estrangeira",
        "interculturalidade",
        "compreensão textual",
        "interpretação em língua estrangeira",
        "acesso à informação",
        "grupos sociais",
        "diversidade cultural"
    ],
    "Linguagens | Competência de Área 3": [
        "linguagem corporal",
        "expressão corporal",
        "práticas corporais",
        "identidade corporal",
        "integração social",
        "cultura corporal",
        "esportes",
        "lutas",
        "autonomia",
        "movimento",
        "corpo",
        "identidade"
    ],
    "Linguagens | Competência de Área 4": [
        "arte",
        "estética",
        "manifestações artísticas",
        "produção artística",
        "recepção artística",
        "linguagem artística",
        "patrimônio cultural",
        "significação",
        "identidade",
        "representação do mundo",
        "cultura",
        "concepções artísticas"
    ],
    "Linguagens | Competência de Área 5": [
        "recursos expressivos",
        "interpretação textual",
        "análise textual",
        "contexto de produção",
        "contexto de recepção",
        "gêneros textuais",
        "sequências discursivas",
        "estrutura textual",
        "organização textual",
        "função da linguagem",
        "linguagem literária",
        "texto argumentativo",
        "procedimentos de construção textual",
        "relações entre texto e contexto"
    ],
    "Linguagens | Competência de Área 6": [
        "sistemas simbólicos",
        "signos",
        "símbolos",
        "significação",
        "construção de significados",
        "expressão",
        "comunicação",
        "informação",
        "organização cognitiva",
        "linguagens",
        "representação da realidade",
        "sistemas de comunicação"
    ],
    "Linguagens | Competência de Área 7": [
        "confronto de opiniões",
        "pontos de vista",
        "argumentação",
        "posicionamento crítico",
        "opiniões divergentes",
        "manifestações linguísticas",
        "manifestações artísticas",
        "interpretação crítica",
        "análise de discursos",
        "perspectivas",
        "divergência",
        "debate"
    ],
    "Linguagens | Competência de Área 8": [
        "língua portuguesa",
        "língua materna",
        "norma-padrão",
        "norma culta",
        "variação linguística",
        "usos da língua",
        "identidade linguística",
        "significação",
        "comunicação",
        "contextos comunicativos",
        "adequação linguística",
        "organização do mundo",
        "gramática"
    ],
    "Linguagens | Competência de Área 9": [
        "impacto das tecnologias",
        "tecnologias da informação e comunicação",
        "TICs",
        "tecnologia e sociedade",
        "impacto social",
        "impacto pessoal",
        "produção tecnológica",
        "desenvolvimento do conhecimento",
        "linguagens digitais",
        "processos de produção",
        "conhecimentos científicos",
        "problemas tecnológicos",
        "função social da tecnologia",
        "gêneros digitais"
    ],
    "Matemática | Competência de Área 1": [
        "números naturais",
        "números inteiros",
        "números racionais",
        "números reais",
        "operações numéricas",
        "sistemas numéricos",
        "razão",
        "proporção",
        "frações",
        "porcentagem",
        "técnicas de contagem",
        "representação numérica"
    ],
    "Matemática | Competência de Área 2": [
        "geometria",
        "conhecimentos geométricos",
        "espaço",
        "formas geométricas",
        "figuras geométricas",
        "representação espacial",
        "leitura geométrica",
        "geometria plana",
        "geometria espacial",
        "relações geométricas",
        "interpretação da realidade",
        "plano cartesiano"
    ],
    "Matemática | Competência de Área 3": [
        "grandezas",
        "medidas",
        "unidades de medida",
        "sistema de medidas",
        "comprimento",
        "área",
        "volume",
        "ângulos",
        "escala",
        "conversão de unidades",
        "mensuração",
        "medidas do cotidiano",
        "solução de problemas"
    ],
    "Matemática | Competência de Área 4": [
        "variação de grandezas",
        "relações entre grandezas",
        "proporcionalidade",
        "dependência entre variáveis",
        "funções",
        "função polinomial",
        "função exponencial",
        "função logarítmica",
        "equações",
        "inequações",
        "crescimento",
        "decrescimento",
        "variação",
        "modelagem matemática",
        "problemas do cotidiano"
    ],
    "Matemática | Competência de Área 5": [
        "gráficos",
        "tabelas",
        "interpretação de dados",
        "análise de informações",
        "dados científicos",
        "dados sociais",
        "leitura de gráficos",
        "leitura de tabelas",
        "previsão de tendências",
        "extrapolação",
        "interpolação",
        "análise de tendências",
        "representação gráfica"
    ],
    "Matemática | Competência de Área 6": [
        "estatística",
        "probabilidade",
        "aleatoriedade",
        "fenômenos aleatórios",
        "fenômenos não determinísticos",
        "distribuição estatística",
        "variáveis estatísticas",
        "amostragem",
        "determinação de amostras",
        "cálculo de probabilidades",
        "análise de dados",
        "desvio",
        "variância",
        "interpretação estatística"
    ],
    "Ciências da Natureza | Competência de Área 1": [
        "ciências naturais",
        "tecnologia",
        "ciência e sociedade",
        "construção do conhecimento científico",
        "desenvolvimento social",
        "processos produtivos",
        "fenômenos ondulatórios",
        "oscilações",
        "ondas",
        "circuitos elétricos",
        "dispositivos elétricos",
        "aplicações tecnológicas",
        "desenvolvimento científico"
    ],
    "Ciências da Natureza | Competência de Área 2": [
        "meio ambiente",
        "conservação ambiental",
        "degradação ambiental",
        "impactos ambientais",
        "preservação ambiental",
        "intervenção humana",
        "processos produtivos",
        "processos sociais",
        "sustentabilidade",
        "recursos naturais",
        "tecnologias ambientais",
        "ações científico-tecnológicas",
        "poluição",
        "equilíbrio ecológico"
    ],
    "Ciências da Natureza | Competência de Área 3": [
        "organismos",
        "ambiente",
        "interações ecológicas",
        "saúde humana",
        "saúde pública",
        "relações ecológicas",
        "fatores ambientais",
        "aspectos culturais",
        "tecnologias sociais",
        "qualidade de vida",
        "doenças",
        "organismo e ambiente",
        "funcionamento dos seres vivos"
    ],
    "Ciências da Natureza | Competência de Área 4": [
        "método científico",
        "métodos científicos",
        "procedimentos científicos",
        "investigação científica",
        "experimentação",
        "observação",
        "formulação de hipóteses",
        "análise de resultados",
        "interpretação de dados",
        "pesquisa científica",
        "ciências naturais",
        "aplicação de conhecimentos científicos"
    ],
    "Ciências da Natureza | Competência de Área 5": [
        "física",
        "conhecimentos físicos",
        "fenômenos físicos",
        "situações-problema",
        "interpretação de fenômenos",
        "avaliação de fenômenos",
        "intervenções práticas",
        "planejamento de intervenções",
        "mecânica",
        "movimento",
        "energia",
        "trabalho",
        "potência",
        "eletricidade",
        "magnetismo",
        "ondas",
        "óptica",
        "calor",
        "termodinâmica"
    ],
    "Ciências da Natureza | Competência de Área 6": [
        "química",
        "conhecimentos químicos",
        "fenômenos químicos",
        "transformações químicas",
        "reações químicas",
        "situações-problema",
        "interpretação química",
        "avaliação de processos químicos",
        "intervenções práticas",
        "estrutura atômica",
        "ligações químicas",
        "materiais",
        "propriedades químicas",
        "estequiometria",
        "soluções",
        "eletroquímica",
        "equilíbrio químico",
        "química orgânica",
        "energia química"
    ],
    "Ciências da Natureza | Competência de Área 7": [
        "biologia",
        "conhecimentos biológicos",
        "seres vivos",
        "organismos",
        "características adaptativas",
        "adaptação",
        "evolução",
        "modo de vida",
        "distribuição geográfica",
        "biodiversidade",
        "ecologia",
        "genética",
        "hereditariedade",
        "biotecnologia",
        "células",
        "metabolismo",
        "fisiologia",
        "organismos e ambiente"
    ],
    "Ciências Humanas | Competência de Área 1": [
        "cultura",
        "identidade",
        "elementos culturais",
        "diversidade cultural",
        "cultura material",
        "cultura imaterial",
        "patrimônio cultural",
        "identidade social",
        "identidade coletiva",
        "povos indígenas",
        "povos africanos",
        "escravidão",
        "resistência cultural",
        "movimentos culturais",
        "formação da sociedade brasileira"
    ],
    "Ciências Humanas | Competência de Área 2": [
        "espaço geográfico",
        "território",
        "territorialidade",
        "organização espacial",
        "transformações territoriais",
        "relações sociais",
        "relações econômicas",
        "escala local",
        "escala regional",
        "escala mundial",
        "formação territorial",
        "migração",
        "imigração",
        "reordenamento territorial",
        "urbanização",
        "segregação espacial",
        "hierarquia urbana",
        "geopolítica",
        "globalização"
    ],
    "Ciências Humanas | Competência de Área 3": [
        "instituições sociais",
        "instituições políticas",
        "instituições econômicas",
        "Estado",
        "organização social",
        "organização política",
        "organização econômica",
        "produção histórica",
        "papel histórico",
        "grupos sociais",
        "sujeitos históricos",
        "pensamento político",
        "sistemas políticos",
        "relações de poder",
        "organização da sociedade",
        "formação do Estado"
    ],
    "Ciências Humanas | Competência de Área 4": [
        "cidadania",
        "democracia",
        "fundamentos da cidadania",
        "fundamentos da democracia",
        "conhecimentos históricos",
        "participação política",
        "direitos civis",
        "direitos humanos",
        "direitos políticos",
        "direitos sociais",
        "democracia direta",
        "democracia indireta",
        "democracia representativa",
        "constituições",
        "políticas afirmativas",
        "revoluções",
        "atuação social",
        "consciência política"
    ],
    "Ciências Humanas | Competência de Área 5": [
        "cartografia",
        "representação espacial",
        "espaço geográfico",
        "conhecimentos cartográficos",
        "mapas",
        "leitura de mapas",
        "interpretação cartográfica",
        "orientação espacial",
        "localização geográfica",
        "escalas cartográficas",
        "coordenadas geográficas",
        "representação do território",
        "linguagem cartográfica"
    ],
    "Ciências Humanas | Competência de Área 6": [
        "sociedade",
        "natureza",
        "relação sociedade-natureza",
        "relações socioambientais",
        "meio ambiente",
        "recursos naturais",
        "apropriação da natureza",
        "impactos ambientais",
        "relações ambientais",
        "escalas geográficas",
        "recursos hídricos",
        "conservação ambiental",
        "unidades de conservação",
        "parques ecológicos",
        "zoneamento ecológico-econômico",
        "ação humana",
        "transformações ambientais"
    ]
}

image_count=0

monolith=[]

print("Starting pre processing")

for current_json_file_path in commented_json_folder_paths:
    current_images_folder=program_path/"provas_markdown"/(current_json_file_path.stem+"_artifacts")

    with open(current_json_file_path, "r", encoding="utf-8") as file_obj:
        file_contents="".join(file_obj.readlines())
    parsed_json_content=json.loads(file_contents)
    
    for question in parsed_json_content:
        str_numero_exercicio=question["numero_exercicio"]
        if type(str_numero_exercicio)==str:
            if str_numero_exercicio.isdecimal():
                numero_exercicio=int(str_numero_exercicio)
            else:
                str_red_numero_exercicio=""
                for c in str_numero_exercicio:
                    if c.isdecimal(): str_red_numero_exercicio+=c
                
                if str_red_numero_exercicio.isdecimal():
                    numero_exercicio=int(str_red_numero_exercicio)
                else:
                    raise RuntimeError
        else:
            numero_exercicio=str_numero_exercicio
        
        question["numero_exercicio"]=numero_exercicio

        materias=sorted(question["materias"])
        conteudos=question["conteudos"]
        
#        for conteudo in conteudos:
#            if conteudo in mapa_conhecimentos_de_área.keys():
#                conteudos_adicionais=mapa_conhecimentos_de_área[conteudo]
#                for conteudo_adicional in conteudos_adicionais:
#                    conteudos.append(conteudo_adicional)
        for conteudo in conteudos:
            if not conteudo in index_conteudos:
                index_conteudos.append(conteudo)

        question["conteudos"]=conteudos
        
        enunciado=question["enunciado"]
        original_image_paths = markdown_image_pattern.findall(enunciado)
        for original_image_path in original_image_paths:
            prs_original_image_path=original_image_path
            new_image_name=f"tstast_img{image_count}{Path(prs_original_image_path).suffix}"
            enunciado=enunciado.replace(original_image_path,new_image_name)
            (current_images_folder/prs_original_image_path).copy(final_folder_path/new_image_name)
            image_count+=1
        question["enunciado"]=enunciado
        
        alternativas=question["alternativas"]
        for i in range(len(alternativas)):
            original_image_paths = markdown_image_pattern.findall(alternativas[i])
            for original_image_path in original_image_paths:
                prs_original_image_path=original_image_path
                new_image_name=f"tstast_img{image_count}{Path(prs_original_image_path).suffix}"
                alternativas[i]=alternativas[i].replace(original_image_path,new_image_name)
                (current_images_folder/prs_original_image_path).copy(final_folder_path/new_image_name)
                image_count+=1
        question["alternativas"]=alternativas

        question["materias"]=[x.lower() for x in question["materias"]]
        question["conteudos"]=[x.lower() for x in question["conteudos"]]

        monolith.append(question)

print("Finished pre processing")

with open(final_folder_path/"tstast_monolith.json","w",encoding="utf8") as file_obj:
    file_obj.writelines(json.dumps(monolith))

print ("Loading model")
MODEL_ID = "google/embeddinggemma-2"

model = SentenceTransformer(
    MODEL_ID,
    config_kwargs={"vision_config": None, "audio_config": None},
    model_kwargs={"dtype": torch.float32}
)
print ("Finished loading model")

print ("Creating/loading DB")
db = veclite.VecLite(str(db_path))
print ("Finished creating/loading DB")

print ("Embedding questions")

for idx,question in enumerate(monolith):
    print (f"{idx+1}/{len(monolith)}")
    str_question=f"Conteúdos: {json.dumps(question["conteudos"])}"
    embedding = model.encode(str_question, prompt_name="Document",truncate_dim=768,normalize_embeddings=True)
    db.insert(str(idx), embedding)

print ("Finished embedding questions")