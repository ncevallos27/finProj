//
// Created by Nico Cevallos on 11/15/25.
//

#ifndef PRICER_H
#define PRICER_H
#include <string>

class Pricer {
public:
	Pricer(int paths, double timeStep, double discount);
	virtual ~Pricer() = default;
	virtual std::vector<double> price(double start, int step) = 0;
	virtual std::string identify() = 0;
	virtual void setup(double vol) = 0;
	virtual double getProb() = 0;

protected:
	int paths;
	double timeStep;
	double r;
	int currentTime;

};

#endif //PRICER_H
