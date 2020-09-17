#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: MPSK Demod Demo
# Generated: Sun Jun 14 21:12:23 2020
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

from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class mpsk_demond(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="MPSK Demod Demo")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samps_per_sym = samps_per_sym = 4
        self.samp_rate = samp_rate = 32000
        self.noise = noise = 0.1
        self.freq_on = freq_on = 0

        ##################################################
        # Blocks
        ##################################################
        _noise_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	label='Noise',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noise_sizer)
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "Constellation")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "FFT")
        self.Add(self.nb)
        _freq_on_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_on_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_on_sizer,
        	value=self.freq_on,
        	callback=self.set_freq_on,
        	label='freq_on',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_on_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_on_sizer,
        	value=self.freq_on,
        	callback=self.set_freq_on,
        	minimum=-0.5,
        	maximum=0.5,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_on_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=32000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        	win=window.blackmanharris,
        )
        self.nb.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.nb.GetPage(0).GetWin(),
        	title='Constellation Plot',
        	sample_rate=samp_rate,
        	frame_rate=5,
        	const_size=1024,
        	M=4,
        	theta=0,
        	loop_bw=0.030,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=samp_rate/4.,
        	omega_limit=0.005,
        )
        self.nb.GetPage(0).Add(self.wxgui_constellationsink2_0.win)
        self.digital_constellation_8psk_sptr = digital.dbpsk_mod(
        	samples_per_symbol=4,
        	excess_bw=0.35,
        	mod_code="gray",
        	verbose=False,
        	log=True)

        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq_on,
        	epsilon=1.0,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2**8, 10000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_8psk_sptr, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_constellationsink2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_constellation_8psk_sptr, 0), (self.channels_channel_model_0, 0))

    def get_samps_per_sym(self):
        return self.samps_per_sym

    def set_samps_per_sym(self, samps_per_sym):
        self.samps_per_sym = samps_per_sym

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self._noise_slider.set_value(self.noise)
        self._noise_text_box.set_value(self.noise)
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_freq_on(self):
        return self.freq_on

    def set_freq_on(self, freq_on):
        self.freq_on = freq_on
        self._freq_on_slider.set_value(self.freq_on)
        self._freq_on_text_box.set_value(self.freq_on)
        self.channels_channel_model_0.set_frequency_offset(self.freq_on)


def main(top_block_cls=mpsk_demond, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
