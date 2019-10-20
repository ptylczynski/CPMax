// PCmax.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <stdio.h> 
#include <algorithm>


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

int liczba_procesorow;
int liczba_zadan;
int index_min;
int* zadania;
int* procesory;

int main()
{
	std::cout << "Dane wejsciowe: ";
    std::cin >> liczba_procesorow;
	std::cin >> liczba_zadan;

	zadania = new int[liczba_zadan];
	procesory = new int[liczba_procesorow] {0};

		
		for (int n = 0; n < liczba_zadan; n++)
		{
			std::cin >> zadania[n];
		}	

		std::cout << "\nLiczba procesorow: " << liczba_procesorow << " liczba zadan: " << liczba_zadan << std::endl;

		for (int i = 0; i < liczba_zadan; i++)
		{
			for (int j = i % liczba_procesorow; j < liczba_procesorow; j++)
			{
				if (procesory[j] == 0) procesory[j] += zadania[i];
				else procesory[index_najmniejszego_elementu(procesory, liczba_procesorow)] += zadania[i];
				break;
			}
		}
		std::cout << "Czasy wykonania zadan przez procesory:\n";
		for (int i = 0; i < liczba_procesorow; i++)
		{
			std::cout << i + 1 << ". " << procesory[i] << std::endl;
		}

		std::cout << "Cmax = " << *std::max_element(procesory, procesory + liczba_procesorow) << std::endl;

		std::getchar();
		delete[] zadania;
		return 0;

}
