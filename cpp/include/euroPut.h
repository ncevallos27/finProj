//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef EUROCALL_H
#define EUROCALL_H
#include "payoff.h"

class EuroPut final : public Payoff {
public:
	explicit EuroPut(double strike);
	~EuroPut() override = default;

	double calculate(double price) override;
};

#endif //EUROCALL_H
