



def nome(arquivo):
    config = ConfigController(arquivo)
    prolog = PrologController()
    notas_treino = NotasTreinoController(config.obterDiretorio)
    lAlunos = notas_treino.obterListaAlunos()
    
    for(aluno in lAlunos):
        arquivo = aluno[3]
        resultado = prolog.executar(arquivo)
        aluno[4] = resultado
        
    notas_treino.atualizar(lAlunos)