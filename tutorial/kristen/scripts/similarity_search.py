# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np
import faiss  # make faiss available

def similarity_search(smf, queries):

    num_variants = len(smf[0])            # dimension
    num_samples = len(smf)                # database size

    # database
    all_samples = np.asarray(smf, dtype='float32')

    index = faiss.IndexFlatL2(num_variants)   # build the index
    print(index.is_trained)
    index.add(all_samples)                  # add vectors to the index
    print(index.ntotal)
    k = 3                          # report back k nearest neighbors.

    print('\nActual Search...')
    D, I = index.search(queries, k)     # actual search
    print(I[:5])                   # neighbors of the 5 first queries
    print(I[-5:])                  # neighbors of the 5 last queries

    print('\nMISC...')
    #print(I)

    return I
