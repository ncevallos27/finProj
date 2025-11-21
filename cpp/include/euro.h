//
// Created by Nico Cevallos on 11/21/25.
//

#ifndef FINPROJ_EURO_H
#define FINPROJ_EURO_H
#include "payoff.h"


class Euro : public Payoff {
public:
	Euro(PayoffType type);
	~Euro() override = default;

	double calculate(std::vector<double> &price, double strike) override;

};


#endif //FINPROJ_EURO_H