//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef EUROPUT_H
#define EUROPUT_H
#include "payoff.h"

class EuroPut final : public Payoff {
public:
	EuroPut() = default;
	~EuroPut() override = default;

	double calculate(double price, double strike) override;
};

#endif //EUROPUT_H
