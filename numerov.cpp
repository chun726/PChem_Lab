#include <iostream>
#include <math.h>

using namespace std;
int main() {
	int m, i, nn;
	double x[1000], g[1000], p[1000], E, s, ss;

	// Setting basic constants
	cout << "Enter initial x_r: ";
	cin >> x[0];
	
	cout << "Enter the increment s_r: ";
	cin >> s;

	cout << "Enter the number of intervals m: ";
	cin >> m;

	label1:
	cout << "Enter the reduced energy Er (enter 1e10 to quit): ";
	cin >> E;

	if (E > 1e9) {
		cout << "Quitting\n";
		return 0;
	}

	//Initial value and second point
	nn = 0;
	p[0] = 0;
	p[1] = 0.0001;
	x[1] = x[0] + s;

	//G_n calculation(2V - 2E) for harmonic oscillator
	g[0] = x[0] * x[0] - 2 * E;
	g[1] = x[1] * x[1] - 2 * E;

	//For convenience
	ss = s * s / 12;

	//Calculating using recurrence relation
	for (i = 1; i <= m - 1; i++) {
		x[i + 1] = x[i] + s;
		g[i + 1] = x[i + 1] * x[i + 1] - 2 * E;
		p[i + 1] = (-p[i - 1] + 2 * p[i] + 10 * g[i] * p[i] * ss + g[i - 1] * p[i - 1] * ss) / (1 - g[i + 1] * ss);
		if (p[i + 1] * p[i] < 0) {
			nn++;
		}
	}

	cout << " Er = " << E << " || Nodes = " << nn << " || Psir(xm) = " << p[m] << endl;
	goto label1;
}