# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np

def similarity_search(smf):

    d = len(smf[0])                           # dimension
    nb = len(smf)                      # database size

    # database
    xb = np.asarray(smf, dtype='float32')
    # incoming queries
    xq = np.asarray([[0]*d,[1]*d,[2]*d], dtype='float32')

    import faiss                   # make faiss available
    index = faiss.IndexFlatL2(d)   # build the index
    print(index.is_trained)
    index.add(xb)                  # add vectors to the index
    print(index.ntotal)
    k = 4                          # report back k nearest neighbors.

    print('\nActual Search...')
    D, I = index.search(xq, k)     # actual search
    print(I[:5])                   # neighbors of the 5 first queries
    print(I[-5:])                  # neighbors of the 5 last queries

    print('\nMISC...')
    print(I)

    return I
