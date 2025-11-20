//
// Created by Nico Cevallos on 11/17/25.
//

#include "euroPut.h"

EuroPut::EuroPut() : Payoff(Path::Independent) {}

void EuroPut::calculate(std::vector<double>& price, double strike) {
	price[-1] = std::max(strike-price[-1], 0.0);
}

