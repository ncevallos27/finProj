//
// Created by Nico Cevallos on 11/15/25.
//

#ifndef OPTION_H
#define OPTION_H
#include <memory>

#include "payoff.h"
#include "stock.h"

class Option {
public:
	Option(std::shared_ptr<Stock> stock, std::shared_ptr<Payoff> payoff);
};

#endif //OPTION_H
