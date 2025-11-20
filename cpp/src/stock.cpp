//
// Created by Nico Cevallos on 11/16/25.
//

#include "stock.h"
#include "binomialTree.h"

Stock::Stock(const std::shared_ptr<Pricer> &model, double start, double vol) : model(model), start(start), vol(vol) {
	this->model->setup(vol);
}

void Stock::price(std::vector<std::vector<double>> &prices, int step) {
	this->model->priceIndependent(prices, this->start, step);
}

double Stock::getPricerTimeStep() const {
	return this->model->getTimeStep();
}

PricerType Stock::getPricerIdentity() {
	return this->model->identify();
}

double Stock::getPricerDiscount() const {
	return this->model->getDiscount();
}

double Stock::getPricerProb() const {
	return this->model->getProb();
}