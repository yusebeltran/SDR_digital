#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jun 14 17:02:50 2020
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import math
import numpy
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.const_type = const_type = 1
        self.variable_static_text_0 = variable_static_text_0 = {0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[const_type] + " - Change const_type for different constellation types!"
        self.samp_rate = samp_rate = 100000
        self.const = const = (digital.constellation_bpsk(), digital.constellation_qpsk(), digital.constellation_8psk())
        self.EbN0 = EbN0 = 10

        ##################################################
        # Blocks
        ##################################################
        _EbN0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._EbN0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_EbN0_sizer,
        	value=self.EbN0,
        	callback=self.set_EbN0,
        	label='Eb / N0 (dB)',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._EbN0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_EbN0_sizer,
        	value=self.EbN0,
        	callback=self.set_EbN0,
        	minimum=-10,
        	maximum=200,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_EbN0_sizer)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='%',
        	minval=0,
        	maxval=1,
        	factor=100,
        	decimal_places=4,
        	ref_level=0,
        	sample_rate=100000,
        	number_rate=15,
        	average=True,
        	avg_alpha=None,
        	label='BER',
        	peak_hold=False,
        	show_gauge=False,
        )
        self.GridAdd(self.wxgui_numbersink2_0.win, 1, 0, 1, 1)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.GetWin(),
        	title='Constellation Plot',
        	sample_rate=samp_rate,
        	frame_rate=5,
        	const_size=2048,
        	M=2,
        	theta=0,
        	loop_bw=6.28/100.0,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=samp_rate/4.,
        	omega_limit=0.005,
        )
        self.GridAdd(self.wxgui_constellationsink2_0.win, 2, 0, 1, 1)
        self._variable_static_text_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0,
        	callback=self.set_variable_static_text_0,
        	label='Constellation Type',
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_static_text_0_static_text)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(const[const_type].base())
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((const[const_type].points()), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=int(10e6),
        	bits_per_symbol=const[const_type].bits_per_symbol(),
        )
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, const[const_type].arity(), int(10e6))), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1.0 / math.sqrt(2.0 * const[const_type].bits_per_symbol() * 10**(EbN0/10)), 42)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blks2_error_rate_0, 0), (self.wxgui_numbersink2_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_constellationsink2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_error_rate_0, 1))

    def get_const_type(self):
        return self.const_type

    def set_const_type(self, const_type):
        self.const_type = const_type
        self.set_variable_static_text_0({0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[self.const_type] + " - Change const_type for different constellation types!")
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.const[self.const_type].points()))
        self.analog_noise_source_x_0.set_amplitude(1.0 / math.sqrt(2.0 * self.const[self.const_type].bits_per_symbol() * 10**(self.EbN0/10)))

    def get_variable_static_text_0(self):
        return self.variable_static_text_0

    def set_variable_static_text_0(self, variable_static_text_0):
        self.variable_static_text_0 = variable_static_text_0
        self._variable_static_text_0_static_text.set_value(self.variable_static_text_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.const[self.const_type].points()))
        self.analog_noise_source_x_0.set_amplitude(1.0 / math.sqrt(2.0 * self.const[self.const_type].bits_per_symbol() * 10**(self.EbN0/10)))

    def get_EbN0(self):
        return self.EbN0

    def set_EbN0(self, EbN0):
        self.EbN0 = EbN0
        self._EbN0_slider.set_value(self.EbN0)
        self._EbN0_text_box.set_value(self.EbN0)
        self.analog_noise_source_x_0.set_amplitude(1.0 / math.sqrt(2.0 * self.const[self.const_type].bits_per_symbol() * 10**(self.EbN0/10)))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
