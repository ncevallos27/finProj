#ifndef BINOMIALTREE_H
#define BINOMIALTREE_H

#include <vector>
#include <string>

#include "pricer.h"

class BinomialTree : public Pricer {
public:
  // Constructor
	BinomialTree::BinomialTree(int paths, double timeStep, double discount);
  BinomialTree::BinomialTree(int paths, double timeStep, double discount, double u, double d);

  ~BinomialTree() override = default;
  // Calculates risk-neutral probability of an up move
  double getProb() override;
  void BinomialTree::calcUp(double vol);

  // Returns the prices at a given step (from smallest to largest)
  std::vector<double> price(double start, int step) override;
  void setup(double vol) override;

  std::string identify() override;

private:
  double u;
  double d;

};

#endif // BINOMIALTREE_H