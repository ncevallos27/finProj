//
// Created by Nico Cevallos on 11/16/25.
//

#include "stock.h"

#include <iostream>
#include <ostream>

#include "binomialTree.h"

Stock::Stock(const std::shared_ptr<Pricer> &model, double start, double vol, double drift) : model(model), start(start), vol(vol), drift(drift), priced(false), lastPricedStep(-1) {
	this->model->setup(vol, drift);
}

void Stock::price(int step) {
	if (priced && this->lastPricedStep == step) {
		return;
	}
	priced = true;
	lastPricedStep = step;

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

std::vector<std::vector<double>>& Stock::getRefPrices() {
	return prices;
}

double Stock::getDiscount(double otherMaturity) {
	return std::exp(-1 * this->getPricerDiscount() * otherMaturity);
}

double Stock::getStart() const {
	return this->start;
}