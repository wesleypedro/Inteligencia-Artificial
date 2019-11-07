# Sistema de Controle Acadêmico

> O devido sistema foi implementado pelo aluno Wallesson Cavalcante juntamente comigo com o propósito de compor parte da nota da disciplina de Inteligência Artificial pela Universidade Federal do Ceará - Campus Quixadá.

### Finalidade do sistema
O sistema tem como propósito implementar resolver o problema de Alocações de Enfermeiras em Turnos usando para isso algoritmos das técnicas de Subida de Encosta (Hill Climbing).

### Descrição
Dada uma entrada qualquer, consistindo de uma String de bits, onde 0 representa que o enfermeiro não está alocado para aquele turno e 1 representa que o mesmo está alocado para aquele turno, o objetivo é gerar estados em que essa distribuição fica mais uniforme sem que não haja quebras de restrições. As restrições serão descritas logo a seguir. Os turnos podem ser compreendidos como sendo um período de 8h por dia, em que cada enfermeiro trabalha esse período. Nesse caso, temos 3 turnos por dia o que dá um total de 21 turnos por semana. Dessa forma, teremos uma String de bits representando os turnos para cada enfermeiro e que para cada enfermeiro, teremos um total de 21 bits que serão dispostos por enfermeiros sequencialmente na String. Para a resolução do problema, foram usadas aplicações dos algoritmos clássicos de Subida de Encosta. São eles:
* Subida de Encosta (Hill Climbing)
* Subida de Encosta pelo Melhor Aclive (Steepest-Ascent Hill Climbing)
* Busca pelo Melhor Primeiro (Best-First Search)
O objetivo é rodar o programa em busca do melhor estado possível segundo as especificações de cada algoritmo. O estado retornado será sempre um ótimo com relação a execução, porém pode esse ser um melhor local, onde os estados vizinhos ao estado atual tenham uma função de avaliação pior do que o atual, como pode ser também um estado objetivo global, que é o melhor estado de todo o problema.

### Restrições a serem satisfeitas
Para avaliação dos estados, são analizados os seguintes estados. Cada vez que uma das seguintes restrições é quebrada, um contador é incrementado para determinar ao final a função de avaliação do mesmo.
* _r1_: Deve haver ao menos 1 enfermeiro e no máximo 3 enfermeiros em cada turno.
* _r2_: Cada enfermeiro deve ser alocado em 5 turnos por semana.
* _r3_: Nenhum enfermeiro pode trabalhar mais que 3 turnos seguidos sem folga.
* _r4_: Enfermeiros preferem consistência em seus horários, ou seja, eles preferem trabalhar todos os dias da semana no mesmo turno (dia, noite, ou madrugada).

### Funcionalidades básicas do sistema
1. Executar a busca de Subida de Encosta (Hill Climbing)
2. Executar a busca de Subida de Encosta pelo Melhor Aclive (Steepest-Ascent Hill Climbing)
3. Executar a busca pelo Melhor Primeiro (Best-First Search)
4. Executar a busca de Subida de Encosta para n Estados Aleatórios
5. Entrar com estado manualmente para a execução dos algoritmos
6. Gerar estados aleatórios para a execução do algoritmo
7. Mostar documentação

### Restrições de implementação do sistema
* O sistema deve ser implementado usando a linguagem C.
* O sistema deve possuir  um sistema de arquivos que guarde o que foi alterado pelo usuário para que deva ter continuidade quando for executar novamente.
* O sistema deve armazenar os dados em structs durante o tempo de execução.

##### Instruções para execução
**Requisito:** possuir um interpretador python3

	As instruções aqui apresentadas são mais voltadas para execução em terminais Linux, apesar de uma certa parte poder ser executadas no Windows também.
* Para que o sistema possa rodar, é necessário que todos os seus arquivos estejam na mesma estutura apresentada aqui, bem como completos e seguir as seguintes instruções:
    * Abra uma janela do terminal na pasta em que se encontra as classes do programa.
    * Execute o seguinte comando para a execução do programa:
        `python3 Main.py`.