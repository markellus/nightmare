#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
# @file pyTest                                                                 #
# pyTest is a tool for testing commandline applications.                       #
#                                                                              #
# It can be run from the commandline or by using the integrated graphical user #
# interface written with tkinter.                                              #
#                                                                              #
#                                                                              #
# @author Hanno Sternberg <hanno@almostintelligent.de>                         #
#                                                                              #
# This software is licensed under the MIT License                              #
#                                                                              #
# Copyright (c) 2012-2013 Hanno Sternberg                                      #
#                                                                              #
# Permission is hereby granted, free of charge, to any person obtaining a copy #
# of this software and associated documentation files (the "Software"), to     #
# deal in the Software without restriction, including without limitation the   #
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or  #
# sell copies of the Software, and to permit persons to whom the Software is   #
# furnished to do so, subject to the following conditions:                     #
#                                                                              #
# The above copyright notice and this permission notice shall be included in   #
# all copies or substantial portions of the Software.                          #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

import os
import sys

from pyTest import TestState
from pyTestSuite import TestSuite
from pyTestRunner import TestRunner
from pyTestUtils import TermColor


def main():
	TermColor.init()
	if "--no-color" in sys.argv:
		TermColor.active = False
	if "--version" in sys.argv:
		runner = TestRunner(flush = True)
	elif "--no-gui" in sys.argv:
		# Capt. Obvious: We're running in console mode
		runner = TestRunner()
		runner.parseArgv()
		suite = runner.loadSuite()
		if suite is not None:
			for testcase in runner.run():
				pass
			if not runner.options['info'] and not runner.options['length'] and not runner.options['quiet']:
				print "{:2.2f}%".format(suite.getRate())
			sys.exit(suite.lastResult if suite.lastResult not in [TestState.Waiting,TestState.InfoOnly] else 0)
		else:
			sys.exit(1)
	else:
		from pyTestGui import TestRunnerGui
		if len(sys.argv) > 1 and not sys.argv[1].startswith("-") and os.path.exists(sys.argv[1]):
			sys.argv[1] = '--bench='+sys.argv[1]
		gui = TestRunnerGui()	
		gui.buildWindow()
		gui.show()

if __name__ == "__main__":
	main()
	