# Sistema para Resolução do Problema das 8 Rainhas

> O devido sistema foi implementado pelo aluno Wallesson Cavalcante juntamente comigo com o propósito de compor parte da nota da disciplina de Inteligência Artificial pela Universidade Federal do Ceará - Campus Quixadá.

### Finalidade do sistema
O sistema tem como propósito implementar resolver o Problema das 8 Rainhas usando para isso algoritmos das técnicas de Busca em Profundidade e Busca em Largura.

### Descrição
Dada uma execução do algoritmo, o usuário deve de início escolher qual opção de busca executar, onde de início terá um valor padrão para uma mariz em que de início a sua ordem é de 8x8. Essa matriz representa um tabuleiro de xadrez, onde deve-se realizar um processo de busca para alocar uma quantidade de 8 rainhas no mesmo. Para a resolução do problema, foram usadas aplicações dos algoritmos clássicos de Busca Cega. São eles:
* Busca em Profundidade (Depth-First Search - DFS)
* Busca em Largura (Breadth-First Search - BFS)
O objetivo é rodar o programa em busca do melhor estado possível segundo as especificações de cada algoritmo. O estado retornado será sempre um ótimo com relação a execução, ou seja, retornará sempre uma configuração do tabuleiro em que as n rainhas especificadas estarão corretamente alocadas.

### Restrições a serem satisfeitas
De maneira geral, é exigido que as rainhas estejam alocadas no tabuleiro de forma que nenhuma esteja ameaçando uma outra em qualquer outra posição. Isso vai garantir que ao final, seja retornado um estado em que esse seja um ótimo.

### Funcionalidade Extra
O algoritmo está generalizado para receber uma configuração de tabuleiro específica do usuário, para que dessa forma possa gerar uma configuração específica para esse tabuleiro.

### Funcionalidades básicas do sistema
1. Executar a Busca em Profundidade (Depth-First Search - DFS)
2. Executar a Busca em Largura (Breadth-First Search - BFS)
3. Entrar com um valor para a ordem do tabuleiro

### A saber para a execução
De maneira geral, o Algotimo está descrito em duas linguagens distintas, onde a Busca em Profundidade está implementada em C++ e a Busca em Largura está implementada em Python.