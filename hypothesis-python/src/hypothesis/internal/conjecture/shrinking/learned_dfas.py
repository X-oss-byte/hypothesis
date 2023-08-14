# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Copyright the Hypothesis Authors.
# Individual contributors are listed in AUTHORS.rst and the git log.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.

from hypothesis.internal.conjecture.dfa import ConcreteDFA

SHRINKING_DFAS = {
    'datetimes()-d66625c3b7': ConcreteDFA(
        [
            [(0, 1), (1, 255, 2)],
            [(0, 3), (1, 255, 4)],
            [(0, 255, 4)],
            [(0, 5), (1, 255, 6)],
            [(0, 255, 6)],
            [(5, 255, 7)],
            [(0, 255, 7)],
            [],
        ],
        {7},
    )
}

SHRINKING_DFAS['emails()-fde8f71142'] = ConcreteDFA([[(0, 1), (1, 255, 2)], [(0, 255, 2)], []], {2})  # noqa: E501
SHRINKING_DFAS['floats()-58ab5aefc9'] = ConcreteDFA([[(1, 1), (2, 255, 2)], [(1, 3)], [(0, 1, 3)], []], {3})  # noqa: E501
SHRINKING_DFAS['floats()-6b86629f89'] = ConcreteDFA([[(3, 1), (4, 255, 2)], [(1, 3)], [(0, 1, 3)], []], {3})  # noqa: E501
SHRINKING_DFAS['floats()-aa8aef1e72'] = ConcreteDFA([[(2, 1), (3, 255, 2)], [(1, 3)], [(0, 1, 3)], []], {3})  # noqa: E501
SHRINKING_DFAS['floats()-bf71ffe70f'] = ConcreteDFA([[(4, 1), (5, 255, 2)], [(1, 3)], [(0, 1, 3)], []], {3})  # noqa: E501
SHRINKING_DFAS['text()-05c917b389'] = ConcreteDFA([[(0, 1), (1, 8, 2)], [(9, 255, 3)], [(0, 255, 4)], [], [(0, 255, 5)], [(0, 255, 3)]], {3})  # noqa: E501
SHRINKING_DFAS['text()-807e5f9650'] = ConcreteDFA([[(0, 8, 1), (9, 255, 2)], [(1, 8, 3)], [(1, 8, 3)], [(0, 4)], [(0, 255, 5)], []], {2, 5})  # noqa: E501

# fmt: on
