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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gr_io_signature.h>
#include <latency_probe.h>


latency_probe_sptr
latency_make_probe (int item_size, std::vector<std::string> keys)
{
	return latency_probe_sptr (new latency_probe (item_size, keys));
}


latency_probe::latency_probe (int item_size, std::vector<std::string> keys)
	: gr_sync_block ("probe",
		gr_make_io_signature (1,1, item_size),
		gr_make_io_signature (0,1, item_size)),
      d_itemsize(item_size)
{
    for(size_t i=0; i<keys.size(); i++){
        d_keys.push_back( pmt::pmt_intern(keys[i]) );
        }
}


latency_probe::~latency_probe ()
{
}


int
latency_probe::work (int noutput_items,
			gr_vector_const_void_star &input_items,
			gr_vector_void_star &output_items)
{
  
    std::vector<gr_tag_t> tags;
    get_tags_in_range(tags, 0, nitems_read(0), nitems_read(0) + noutput_items);
    for(int i=0; i<tags.size(); i++){
        std::cout << "got tag\n";
        }

	// copy outputs if connected and return
    if(output_items.size() > 0){
        memcpy(output_items[0], input_items[0], noutput_items*d_itemsize);
        }
	return noutput_items;
}

