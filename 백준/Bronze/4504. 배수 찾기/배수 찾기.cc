#include <iostream>
using namespace std;

int main()
{
	int n, given;
	cin >> n >> given;

	while (given != 0)
	{
		if (given % n)
			cout << given << " is NOT a multiple of " << n << ".\n";
		else
			cout << given << " is a multiple of " << n << ".\n";
		cin >> given;
	}

	return 0;
}
