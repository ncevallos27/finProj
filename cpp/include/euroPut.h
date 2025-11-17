//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef EUROCALL_H
#define EUROCALL_H
#include "payoff.h"

class EuroPut final : public Payoff {
public:
	EuroPut();
	~EuroPut() override = default;

	double calculate(double price, double strike) override;
};

#endif //EUROCALL_H
