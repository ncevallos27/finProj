//
// Created by Nico Cevallos on 11/21/25.
//

#include "euro.h"

Euro::Euro(PayoffType type) : Payoff(Path::Independent, type) {}

double Euro::calculate(std::vector<double> &price, double strike) {
	switch (this->payoffType) {
		case PayoffType::Call:
			return std::max(price.back()-strike, 0.0);
		case PayoffType::Put:
			return std::max(strike-price.back(), 0.0);
		default:
			return 0.0;
	}
}

