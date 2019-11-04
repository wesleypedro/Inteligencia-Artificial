/* Nome: Wallesson Cavalcante da Silva 397670
   Nome: Franciso Wesley Pedro Lima 398261
 */
#include <iostream>
#include <vector>

using namespace std;

//Variavel global para contar a quantidade de soluções
int sol = 0;

// Função para mostrar o tabuleiro
void Mostrar(vector<vector<int> > & tab, int N){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			if(tab[i][j] == 1)
				cout << "R\t";
			else
				cout << "-\t";
		}
		cout << "\n\n";
	}
	cout << "\n";

//deixamos bem espaçado para tentar nelhorar a visualização
}

// verifica se é seguro colocar a rainha numa determinada coluna
bool Seguro(vector<vector<int> > & tab, int N, int lin, int col)
{
	int i, j;

	// verifica se existe ameaça na linha ou na coluna
	for(i = 0; i < N; i++){
		//verifica se existe alguma rainha na linha que se deseja inserir	
		if(tab[lin][i] == 1)return false;
		//verifica se existe alguma rainha na coluna que se deseja inserir	
		if(tab[i][col] == 1)return false;
	}

	// verifica se ocorre ataque na diagonal principal
	// acima
	for(i = lin, j = col; i >= 0 && j >= 0; i--, j--){// decrementando i e j é possivel acessar o proximo valor acima na diagonal
		if(tab[i][j] == 1)return false;
	}
	//abaixo
	for(i = lin, j = col; i < N && j < N; i++, j++){ // incrementando i e j é possivel acessar o proximo valor abaixo na diagonal 
		if(tab[i][j] == 1)return false;
	}

	// verifica se ocorre ataque na diagonal secundária
	// acima
	for(i = lin, j = col; i >= 0 && j < N; i--, j++){
		if(tab[i][j] == 1)return false;
	}
	// abaixo
	for(i = lin, j = col; i < N && j >= 0; i++, j--){
		if(tab[i][j] == 1)return false;
	}
	//Caso não exista ameaça na coluna, linha ou diagonais a função retorna TRUE
	//o que autoriza a rainha ser colocafa na posição da coluna.
	return true;
}


//Função que vai tentar colocar as rainhas
void Inserir_Rainha(vector<vector<int> > & tab, int N, int col){
	//É o limite para a quantidade de rainhas a serem colocadas
	if(col == N){
		cout << "Solucao " << sol + 1 << ":\n\n";
		Mostrar(tab, N);
		sol++;
		return;
	}
	for(int i = 0; i < N; i++){
		// verifica se é seguro colocar a rainha naquela coluna
		if(Seguro(tab, N, i, col)){
			// insere a rainha e marca a posição inserida com 1
			tab[i][col] = 1;
			// chamada recursiva
			Inserir_Rainha(tab, N, col + 1);
			// remove a rainha caso não seja posivel inserir
			tab[i][col] = 0;
		}
	}
}

int main(){
	// número de rainhas
	int N = 0;
	int op = 0;
	
	cout << "Informe uma opção\n1. Instancia para oito rainhas\n2. instancia para N Rainhas" << endl;
	cin >> op;
	
	if(op == 1){
		N = 8;
	}
	else if(op == 2){		
		cout << "Infrome a quantidade de Rainhas " <<endl;
		cin>> N;
	}
	else{
		cout << "Opção inválida" << endl;
	}
	// tabuleiro (matriz)
	vector<vector<int> > tab;

	// inserindo todas as linhas
	for(int i = 0; i < N; i++)
	{
		vector<int> linha(N);
		tab.push_back(linha);
	}
	// Chamada para a função que tenta colocar rainhas e imprime todas as soluções
	Inserir_Rainha(tab, N, 0);
	// imprime a quantidade de soluções para as N rainhas
	cout << "Total de Soluções para " << N <<" Rainhas: "<< sol <<"\n";

	return 0;
}
