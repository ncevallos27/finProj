//
// Created by Nico Cevallos on 11/17/25.
//

// Testing code for the C++ env

#include <iostream>
#include <monteCarlo.h>
#include <ostream>

#include "option.h"
#include "stock.h"
#include "euro.h"
#include "binomialTree.h"

using namespace std;

int main(int argc, const char * argv[]) {

	shared_ptr<Pricer> p = make_shared<BinomialTree>(1, 1/12.0, 0.05);
	shared_ptr<MonteCarlo> p2 = make_shared<MonteCarlo>(100000, 1/12.0, 0.05);
	shared_ptr<Stock> s = make_shared<Stock>(p2, 60, 0.30, 0.05);
	shared_ptr<Payoff> pf = make_shared<Euro>(PayoffType::Call);
	shared_ptr<Option> o = make_shared<Option>(s, pf, 61, 1.0, OptionPosition::Long);

	cout << o->price() << endl;

	return 0;
}