/* -*- c++ -*- */

#define LATENCY_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "latency_swig_doc.i"

%{
#include "latency_tagger.h"
%}

GR_SWIG_BLOCK_MAGIC(latency,tagger);
%include "latency_tagger.h"

#if SWIGGUILE
%scheme %{
(load-extension-global "libguile-gnuradio-latency_swig" "scm_init_gnuradio_latency_swig_module")
%}

%goops %{
(use-modules (gnuradio gnuradio_core_runtime))
%}
#endif
