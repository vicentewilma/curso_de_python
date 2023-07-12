identidade=input("Qual é o numero do BI?")
resultado=identidade.strip()
base_de_dados={"006234852LA041":
               {"nome":"Wilma Vicente",
                "cursos":["Python","Desenvolvimento Web"],
                "computador":"Code Academy Girls"
                }
               }
aluna=base_de_dados.get(resultado)
if aluna:
    print("aluna foi encontrada com sucesso")
    "hora de entrada"
else:
    print("o BI não corresponde a nenhuma aluna")
    
