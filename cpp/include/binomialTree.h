#ifndef BINOMIALTREE_H
#define BINOMIALTREE_H

#include <vector>
#include <string>

#include "pricer.h"

class BinomialTree : public Pricer {
public:
  // Constructor
	BinomialTree(int paths, double timeStep, double discount);
  BinomialTree(int paths, double timeStep, double discount, double u, double d);

  ~BinomialTree() override = default;
  // Calculates risk-neutral probability of an up move
  double getProb() override;
  void calcUp(double vol);

  // Returns the prices at a given step (from smallest to largest)
  void priceIndependent(std::vector<std::vector<double>> &prices, double start, int step) override;
  void setup(double vol) override;

private:
  double u;
  double d;

};

#endif // BINOMIALTREE_H