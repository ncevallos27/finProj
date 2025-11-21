//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef EUROCALL_H
#define EUROCALL_H
#include "payoff.h"

class EuroCall final : public Payoff {
public:
	EuroCall();
	~EuroCall() override = default;

	double calculate(std::vector<double> &price, double strike) override;
};

#endif //EUROCALL_H
