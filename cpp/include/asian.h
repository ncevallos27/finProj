//
// Created by Nico Cevallos on 11/21/25.
//

#ifndef FINPROJ_ASIAN_H
#define FINPROJ_ASIAN_H
#include "payoff.h"

class Asian : public Payoff {
	public:
	Asian(PayoffType type, int lookBack);
	~Asian() override = default;

	double calculate(std::vector<double> &price, double strike) override;

private:
	int lookBack;

};

#endif //FINPROJ_ASIAN_H