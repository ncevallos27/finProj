//
// Created by Nico Cevallos on 11/20/25.
//

#include "monteCarlo.h"

#include <thread>
#include <vector>


MonteCarlo::MonteCarlo(int paths, double timeStep, double discount) : Pricer(paths, timeStep, discount, PricerType::MonteCarlo), drift(0), vol(0) {}

double MonteCarlo::getProb() {
	return 1/static_cast<double>(paths);
}

void MonteCarlo::priceIndependent(std::vector<std::vector<double>> &prices, double start, int step) {
	/*
	 *	This function will take care of resizing the vector and making sure that everything is threaded
	 */

	prices.clear();
	prices.resize(paths);
	int nThreads = static_cast<int>(std::thread::hardware_concurrency());

	if (paths < nThreads) {
		nThreads = paths;
	}

	std::vector<std::thread> threads;
	threads.reserve(nThreads);

	int block = std::ceil(paths/static_cast<double>(nThreads));
	int current = 0;

	for (int i = 0; i < nThreads; i++) {
		if (i == nThreads - 1) {
			threads.emplace_back(splitWork, std::ref(prices), drift, vol, timeStep, start, step, current, paths);
			continue;
		}
		threads.emplace_back(splitWork, std::ref(prices), drift, vol, timeStep, start, step, current, current+block);
		current += block;
	}

	for (auto& th : threads) {
		th.join();
	}

}

void MonteCarlo::setup(double vol, double drift) {
	this->drift = drift;
	this->vol = vol;
}

void splitWork(std::vector<std::vector<double> > &vector, double drift, double vol, double timeStep, double start, int steps, int startIndex, int endIndex) {
	/*
	 *	splits montecarlo work from [start, end)
	 */

	std::mt19937 rng{std::random_device{}()};
	std::normal_distribution d{0.0, 1.0};

	// making sure that there is no out of bounds errors
	if (endIndex > vector.size()) {
		endIndex = static_cast<int>(vector.size());
	}

	const double first = (drift-((std::pow(vol, 2))/2.0))*timeStep;
	for (int i = startIndex; i < endIndex; i++) {
		vector[i].clear();
		vector[i].emplace_back(start);
		for (int j = 1; j <= steps; j++) {
			double second = vol*d(rng)*std::sqrt(timeStep);
			vector[i].push_back(vector[i][j-1] * std::exp(first+second));
		}
	}
}
