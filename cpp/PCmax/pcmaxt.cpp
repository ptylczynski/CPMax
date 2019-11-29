#include <iostream>
#include <stdio.h> 
#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <fstream>
#define ZAKRES 100

int liczba_procesorow;
int liczba_zadan;
int index_min;
int* zadania;
int* procesory;

void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		std::cout << arr[i] << " ";
	std::cout << std::endl;
}

int index_najmniejszego_elementu(int arr[], int size)
{
	int index = 0;

	for (int i = 1; i < size; i++)
	{
		if (arr[i] < arr[index])
			index = i;
	}

	return index;
}

void generuj_instancje(int liczba_p, int liczba_z, int zakres)
{
	zadania = new int[liczba_z];
	procesory = new int[liczba_p] {};
	std::ofstream zapis("dane.txt");
	for (int i = 0; i < liczba_z; i++)
	{
		zadania[i] = rand() % zakres + 1;
		zapis << zadania[i] << " ";
	}		
	zapis.close();
}

int main()
{
	std::cin >> liczba_procesorow;
	std::cin >> liczba_zadan;
	generuj_instancje(liczba_procesorow, liczba_zadan, ZAKRES);
	std::cout << "\nDane wejsciowe: ";
	printArray(zadania, liczba_zadan);

	//zadania = new int[liczba_zadan];
	//procesory = new int[liczba_procesorow] {0};

	// Wpisywanie czasow zadan z wejscia do tablicy
	for (int n = 0; n < liczba_zadan; n++)
	{
		std::cin >> zadania[n];
	}
	std::cout << "\nLiczba procesorow: " << liczba_procesorow << " liczba zadan: " << liczba_zadan << std::endl;

	//auto start = std::chrono::high_resolution_clock::now();

	std::cout << "Algorytm zachlanny: \n";

	for (int i = 0; i < liczba_zadan; i++)
	{
		for (int j = i % liczba_procesorow; j < liczba_procesorow; j++)
		{
			if (procesory[j] == 0) procesory[j] += zadania[i];
			else procesory[index_najmniejszego_elementu(procesory, liczba_procesorow)] += zadania[i];
			break;
		}
	}

	/*
			std::cout << "Czasy wykonania zadan przez poszczegolne procesory:\n";
	for (int i = 0; i < liczba_procesorow; i++)
	{
		std::cout << i + 1 << ". " << procesory[i] << ", ";
	}
	*/

	// auto stop = std::chrono::high_resolution_clock::now();
	std::cout << "Cmax = " << *std::max_element(procesory, procesory + liczba_procesorow) << std::endl;

	//std::chrono::duration<double> elapsed = stop - start;
	//std::cout << elapsed.count() << " s\n" << std::endl;

	std::cout << "Algorytm lpt:\n";

	//auto start2 = std::chrono::high_resolution_clock::now();

	std::sort(zadania, zadania + liczba_zadan, std::greater<int>());
	for (int i = 0; i < liczba_procesorow; i++)
	{
		procesory[i] = 0;
	}
	for (int i = 0; i < liczba_zadan; i++)
	{
		for (int j = i % liczba_procesorow; j < liczba_procesorow; j++)
		{
			if (procesory[j] == 0) procesory[j] += zadania[i];
			else procesory[index_najmniejszego_elementu(procesory, liczba_procesorow)] += zadania[i];
			break;
		}
	}

	/*
	std::cout << "Czasy wykonania zadan przez procesory:\n";
	for (int i = 0; i < liczba_procesorow; i++)
	{
		std::cout << i + 1 << ". " << procesory[i] << ", ";
	}
	*/
	//auto stop2 = std::chrono::high_resolution_clock::now();

	std::cout << "Cmax = " << *std::max_element(procesory, procesory + liczba_procesorow) << std::endl;

	//std::chrono::duration<double> elapsed2 = stop2 - start2;
	//std::cout << elapsed.count() << " s\n" << std::endl;

	//std::getchar();
	delete[] zadania;
	delete[] procesory;
	return 0;

}