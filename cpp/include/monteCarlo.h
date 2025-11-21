//
// Created by Nico Cevallos on 11/20/25.
//

#ifndef MONTECARLO_H
#define MONTECARLO_H

#include <random>
#include <__random/random_device.h>

#include "pricer.h"

class MonteCarlo : public Pricer {
public:
	MonteCarlo(int paths, double timeStep, double discount);
	~MonteCarlo() = default;

	double getProb() override;
	void priceIndependent(std::vector<std::vector<double>> &vector, double start, int step) override;
	void setup(double vol, double drift) override;

private:
	double vol;
	double drift;
};

void splitWork(std::vector<std::vector<double> > &vector, double drift, double vol, double timeStep, double start, int steps, int startIndex, int endIndex);

#endif //MONTECARLO_H
