#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Test1
# Generated: Fri Sep 28 13:16:43 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser
import latency

import numpy, os;
from pylab import *;


#os.environ['GR_SCHEDULER'] = "STS";
os.environ['GR_SCHEDULER'] = "TPB";
#nsamp = int(500e3);
nsamp = int(500e3);

class test1(gr.top_block):

    def __init__(self, samp_rate, bufsize):
        gr.top_block.__init__(self, "Test1")


        ##################################################
        # Variables
        ##################################################
#        self.samp_rate = samp_rate = 32000
        self.lspace = lspace = 512

        ##################################################
        # Blocks
        ##################################################
        self.latency_tagger_0 = latency.tagger(gr.sizeof_gr_complex, lspace, "latency0")
        self.latency_probe_0 = latency.probe(gr.sizeof_gr_complex, ["latency0"])
        self.gr_vector_source_x_0 = gr.vector_source_c((0,1,2,3,4,5,6,7), True, 1)
        self.gr_throttle_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.gr_multiply_const_vxx_1 = gr.multiply_const_vcc((0, ))
        self.gr_multiply_const_vxx_0 = gr.multiply_const_vcc((0, ))
        self.gr_head_0 = gr.head(gr.sizeof_gr_complex*1, nsamp)


        for b in [self.gr_vector_source_x_0, self.gr_head_0, self.latency_tagger_0, self.gr_multiply_const_vxx_0, self.gr_multiply_const_vxx_1]:
            print bufsize;
            b.set_max_output_buffer(int(bufsize));

        ##################################################
        # Connections
        ##################################################

        self.connect((self.gr_head_0, 0), (self.latency_tagger_0, 0))

        self.connect((self.gr_vector_source_x_0, 0), (self.gr_head_0, 0))

        self.connect((self.gr_multiply_const_vxx_0, 0), (self.gr_multiply_const_vxx_1, 0))

        self.connect((self.latency_tagger_0, 0), (self.gr_multiply_const_vxx_0, 0))

        self.connect((self.gr_multiply_const_vxx_1, 0), (self.gr_throttle_0, 0))

        self.connect((self.gr_throttle_0, 0), (self.latency_probe_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_lspace(self):
        return self.lspace

    def set_lspace(self, lspace):
        self.lspace = lspace

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()

    means = [];

    srv = {};
    #srs = [10e3, 50e3, 100e3, 200e3, 500e3, 1e6, 2e6, 3e6];
    srs = [0.78125e6, 1.5625e6, 3.125e6, 6.25e6, 12.5e6, 25e6];
    #sr = srs[0];
    sr = srs[1];
    fidx = 0;
    fidx = fidx + 1;
    f = figure(fidx);
    ax = subplot(1,1,1);
    bufsizes = list(numpy.power(2, range(4,17)))
    for bufsize in bufsizes:
        pts = [];

        tb = test1(sr, bufsize)
        print "running fg @ sr = %f MS/s"%(sr/1e6);
        tb.run()
        ks = tb.latency_probe_0.get_keys();
        tb.gr_head_0.reset();
        for k in ks:
            offsets = tb.latency_probe_0.get_offsets(k);
            delays = numpy.array(tb.latency_probe_0.get_delays(k))*1e3;
            print "Mean delay: %f ms"%(numpy.mean(delays));
            means.append(numpy.mean(delays));
            srv[sr] = [offsets, delays]
        hold(True);
        pts.append(  ax.plot(srv[sr][0], srv[sr][1], label="%d items"%(bufsize))  )
           
        ax.set_yscale('log'); 
        title('GR Latency Measurement');
        xlabel("sample count");
        ylabel("propagation time (ms)");
        ax.legend(loc='upper right');

    figure();
    ax = subplot(1,1,1);
    ax.set_xscale('log'); 
    title("Buffer size / Latency trade off @ %f MS/s"%(sr/1e6));
    xlabel("Buffer size (bytes)");
    ylabel("Mean Latency (ms)");
    plot(bufsizes, means);
    

    show();
