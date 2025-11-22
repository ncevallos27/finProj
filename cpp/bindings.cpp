//
// Created by Nico Cevallos on 11/18/25.
//


#include "payoff.h"
#include "pricer.h"
#include "bindings.h"

#include <binomialTree.h>
#include <monteCarlo.h>
#include <option.h>

#include <pybind11/native_enum.h>
#include <pybind11/stl.h>

#include "asian.h"
#include "euro.h"


PYBIND11_MODULE(finProj, m) {
	m.doc() = "finProj bindings";

	/*
	 *	BINDINGS FOR payoff CLASS
	 */
	py::class_<Payoff, py::smart_holder> payoff(m, "Payoff");
	payoff.def("getPayoffVector", &Payoff::getPayoffVector);
	payoff.def("getType", &Payoff::getType);
	payoff.def("fakeCalculate", &Payoff::fakeCalcuate);

	/*
	 *	BINDINGS FOR derived payoff CLASSES
	 */
	py::class_<Euro, Payoff, py::smart_holder> euro(m, "Euro", py::is_final());
	euro.def(py::init<PayoffType>());
	euro.def("calculate", &Euro::calculate);

	py::class_<Asian, Payoff, py::smart_holder> asian(m, "Asian", py::is_final());
	asian.def(py::init<PayoffType, int>());
	asian.def("calculate", &Asian::calculate);

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

	py::native_enum<PayoffType>(m, "PayoffType", "enum.Enum")
		.value("Call", PayoffType::Call)
		.value("Put", PayoffType::Put)
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
	stock.def("getRefPrices", &Stock::getRefPrices, py::return_value_policy::reference_internal);

	/*
	 *	BINDINGS FOR option CLASS
	 */
	py::class_<Option, py::smart_holder> option(m, "Option");
	option.def(py::init<std::shared_ptr<Stock>&, std::shared_ptr<Payoff>&, double, double, OptionPosition>());
	option.def("price", py::overload_cast<>(&Option::price));
	option.def("price", py::overload_cast<double>(&Option::price));
	option.def("getPosition", &Option::getPosition);
	option.def("getStrike", &Option::getStrike);
	option.def("fakeCalculate", &Option::fakeCalculate);

	/*
	 *	BINDINGS FOR montecarlo CLASS
	 */
	py::class_<MonteCarlo, Pricer, py::smart_holder> monteCarlo(m, "MonteCarlo");
	monteCarlo.def(py::init<int, double, double>());
	monteCarlo.def("getProb", &MonteCarlo::getProb);
	monteCarlo.def("price", &MonteCarlo::priceIndependent);
	monteCarlo.def("setup", &MonteCarlo::setup);

}