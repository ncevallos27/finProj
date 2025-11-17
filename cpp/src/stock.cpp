//
// Created by Nico Cevallos on 11/16/25.
//

#include "stock.h"
#include "binomialTree.h"

Stock::Stock(std::shared_ptr<Pricer> model, double start, double vol) : model(std::move(model)), start(start), vol(vol) {
	this->model->setup(vol);
}

std::vector<double> Stock::price(int step) const {
	return this->model->price(this->start, step);
}
