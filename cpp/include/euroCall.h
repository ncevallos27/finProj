//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef EUROCALL_H
#define EUROCALL_H
#include "payoff.h"

class EuroCall final : public Payoff {
public:
	explicit EuroCall(double strike);
	~EuroCall() override = default;

	double calculate(double price) override;
};

#endif //EUROCALL_H
