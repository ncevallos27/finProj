//
// Created by Nico Cevallos on 11/21/25.
//

#include "asian.h"

#include <iostream>

Asian::Asian(PayoffType type, int lookBack) : Payoff(Path::Dependent, type), lookBack(lookBack) {}

double Asian::calculate(std::vector<double> &price, double strike) {
	std::size_t newLookBack;
	if (price.size() < lookBack) {
		std::cerr << "lookBack to big, truncating to size of path: " << price.size() << std::endl;
		newLookBack = price.size();
	} else {
		newLookBack = lookBack;
	}

	if (newLookBack == 0) {
		std::cerr << "lookBack is 0 or path is empty, returning 0 payoff" << std::endl;
		return 0.0;
	}

	double total = 0;
	int count = 0;
	for (auto i = price.rbegin(); i != price.rend() && count >= newLookBack; ++i) {
		total += *i;
		count++;
	}

	total /= newLookBack;

	switch (payoffType) {
		case PayoffType::Call:
			return std::max(total-strike, 0.0);
		case PayoffType::Put:
			return std::max(strike-total, 0.0);
		default:
			return 0.0;
	}
}