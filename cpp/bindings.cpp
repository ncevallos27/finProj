//
// Created by Nico Cevallos on 11/18/25.
//


#include "payoff.h"
#include "pricer.h"
#include "bindings.h"

#include <binomialTree.h>
#include <option.h>

#include "euroCall.h"
#include "euroPut.h"
#include <pybind11/native_enum.h>


PYBIND11_MODULE(finProj, m) {
	m.doc() = "finProj bindings";

	/*
	 *	BINDINGS FOR payoff CLASS
	 */
	py::class_<Payoff, py::smart_holder> payoff(m, "Payoff");
	payoff.def("getPayoffVector", &Payoff::getPayoffVector);

	/*
	 *	BINDINGS FOR derived payoff CLASSES
	 */
	py::class_<EuroCall, Payoff, py::smart_holder> eurocall(m, "EuroCall");
	eurocall.def(py::init<>());
	eurocall.def("calculate", &EuroCall::calculate);

	py::class_<EuroPut, Payoff, py::smart_holder> europut(m, "EuroPut");
	europut.def(py::init<>());
	europut.def("calculate", &EuroPut::calculate);

	/*
	 *	BINDINGS FOR enum CLASS
	 */
	py::native_enum<PricerType>(m, "PricerType", "enum.Enum")
		.value("BinomialTree", PricerType::BinomialTree)
		.value("MonteCarlo", PricerType::MonteCarlo)
		.finalize();

	py::native_enum<OptionPosition>(m, "OptionPosition", "enum.Enum")
		.value("Long", OptionPosition::Long)
		.value("Short", OptionPosition::Short)
		.finalize();

	/*
	 *	BINDINGS FOR binomialtree CLASS
	 */
	py::class_<BinomialTree, Pricer, py::smart_holder> binomialTree(m, "BinomialTree");
	binomialTree.def(py::init<int, double, double>());
	binomialTree.def(py::init<int, double, double, double, double>());
	binomialTree.def("getProb", &BinomialTree::getProb);
	binomialTree.def("calcUp", &BinomialTree::calcUp);
	binomialTree.def("price", &BinomialTree::price);
	binomialTree.def("setup", &BinomialTree::setup);

}