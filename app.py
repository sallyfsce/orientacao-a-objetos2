from aluno import Aluno
from disciplina import Disciplina

aluno1 = Aluno("João", "123456", "Ciência da Computação")

sers = Disciplina(nome='Soluções Renováveis', professor='Tritiack')
prompt_ia = Disciplina(nome='Prompt IA', professor='José')

aluno1.matricular(sers)
aluno1.matricular(prompt_ia)

aluno1.adicionar_notas(sers, nota=10)
aluno1.adicionar_notas(sers, nota=8)
aluno1.adicionar_notas(prompt_ia, nota=5)
aluno1.adicionar_notas(prompt_ia, nota=3)

# print(aluno1.calcular_media_d(sers))