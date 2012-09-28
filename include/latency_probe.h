/* -*- c++ -*- */
/* 
 * Copyright 2012 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_LATENCY_PROBE_H
#define INCLUDED_LATENCY_PROBE_H

#include <latency_api.h>
#include <gr_sync_block.h>

class latency_probe;
typedef boost::shared_ptr<latency_probe> latency_probe_sptr;

LATENCY_API latency_probe_sptr latency_make_probe (int item_size, std::vector<std::string> keys);

/*!
 * \brief <+description+>
 *
 */
class LATENCY_API latency_probe : public gr_sync_block
{
	friend LATENCY_API latency_probe_sptr latency_make_probe (int item_size, std::vector<std::string> keys);

	latency_probe (int item_size, std::vector<std::string> keys);
    std::vector<pmt::pmt_t> d_keys;
    int d_itemsize;

 public:
	~latency_probe ();


	int work (int noutput_items,
		gr_vector_const_void_star &input_items,
		gr_vector_void_star &output_items);
};

#endif /* INCLUDED_LATENCY_PROBE_H */

