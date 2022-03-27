/*Stai lavorando su un sistema di gestione della coda e devi creare la classe per contenere i dati della coda, 
che sono ID cliente (interi).
Crea una classe Queue, che ha un attributo size e un array, per contenere i dati della coda.
La classe ha un metodo remove() per rimuovere l'elemento principale della coda, un metodo print() per emettere la coda.

Devi creare un metodo add() per la classe Queue, che prenderà un elemento e lo aggiungerà alla fine della coda.
Il codice deve funzionare completamente, in modo che la dichiarazione della coda e il codice di manipolazione in 
main() funzionino.*/

#include <iostream>
using namespace std; 


class Queue { 
	int size; 
	int* queue; 
	
	public:
	Queue() {
		size = 0;
		queue = new int[100];
	}
	void remove() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		else { 
			for (int i = 0; i < size - 1; i++) { 
				queue[i] = queue[i + 1]; 
			} 
			size--; 
		} 
	} 
	void print() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		for (int i = 0; i < size; i++) { 
			cout<<queue[i]<<" <- ";
		} 
		cout <<endl;
	}

	void add(int x) {
        queue[size]=x;
        size++;
    }
	
}; 

int main() { 
	Queue q; 
	q.add(42); q.add(2); q.add(8); q.add(1); 
	q.print();
	q.remove(); 
	q.add(128); 
	q.print(); 
	q.remove(); 
	q.remove(); 
	q.print(); 

	return 0; 
}