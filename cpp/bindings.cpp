//
// Created by Nico Cevallos on 11/18/25.
//


#include "payoff.h"
#include "pricer.h"
#include "bindings.h"

#include <binomialTree.h>
#include <monteCarlo.h>
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
	payoff.def("getType", &Payoff::getType);

	/*
	 *	BINDINGS FOR derived payoff CLASSES
	 */
	py::class_<EuroCall, Payoff, py::smart_holder> eurocall(m, "EuroCall", py::is_final());
	eurocall.def(py::init<>());
	eurocall.def("calculate", &EuroCall::calculate);

	py::class_<EuroPut, Payoff, py::smart_holder> europut(m, "EuroPut", py::is_final());
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

	py::native_enum<Path>(m, "Path", "enum.Enum")
		.value("Dependent", Path::Dependent)
		.value("Independent", Path::Independent)
		.finalize();

	/*
	 *	BINDINGS FOR pricer CLASS
	 */
	py::class_<Pricer, py::smart_holder> pricer(m, "Pricer");

	/*
	 *	BINDINGS FOR binomialtree CLASS
	 */
	py::class_<BinomialTree, Pricer, py::smart_holder> binomialTree(m, "BinomialTree");
	binomialTree.def(py::init<int, double, double>());
	binomialTree.def(py::init<int, double, double, double, double>());
	binomialTree.def("getProb", &BinomialTree::getProb);
	binomialTree.def("calcUp", &BinomialTree::calcUp);
	binomialTree.def("price", &BinomialTree::priceIndependent);
	binomialTree.def("setup", &BinomialTree::setup);

	/*
	 *	BINDINGS FOR stock CLASS
	 */
	py::class_<Stock, py::smart_holder> stock(m, "Stock");
	stock.def(py::init<std::shared_ptr<Pricer>&, double, double, double>());
	stock.def("price", &Stock::price);
	stock.def("getPricerTimeStep", &Stock::getPricerTimeStep);
	stock.def("getPricerIdentity", &Stock::getPricerIdentity);
	stock.def("getPricerDiscount", &Stock::getPricerDiscount);
	stock.def("getPricerProb", &Stock::getPricerProb);

	/*
	 *	BINDINGS FOR option CLASS
	 */
	py::class_<Option, py::smart_holder> option(m, "Option");
	option.def(py::init<std::shared_ptr<Stock>&, std::shared_ptr<Payoff>&, double, double, OptionPosition>());
	option.def("price", py::overload_cast<>(&Option::price));
	option.def("price", py::overload_cast<double>(&Option::price));
	option.def("getPosition", &Option::getPosition);

	/*
	 *	BINDINGS FOR montecarlo CLASS
	 */
	py::class_<MonteCarlo, Pricer, py::smart_holder> monteCarlo(m, "MonteCarlo");
	monteCarlo.def(py::init<int, double, double>());
	monteCarlo.def("getProb", &MonteCarlo::getProb);
	monteCarlo.def("price", &MonteCarlo::priceIndependent);
	monteCarlo.def("setup", &MonteCarlo::setup);

}