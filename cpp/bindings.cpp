//
// Created by Nico Cevallos on 11/18/25.
//


#include "payoff.h"
#include "pricer.h"
#include "bindings.h"

#include "euroCall.h"
#include "euroPut.h"


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
}