//
// Created by Nico Cevallos on 11/15/25.
//


#include "pricer.h"

Pricer::Pricer(int paths, double timeStep, double discount, PricerType pricerType) : paths(paths), timeStep(timeStep), r(discount), pricerType(pricerType) {}

double Pricer::getTimeStep() const {
	return timeStep;
}

double Pricer::getDiscount() const {
	return r;
}

PricerType Pricer::identify() {
	return pricerType;
}