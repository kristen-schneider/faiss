# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np
import faiss  # make faiss available

def similarity_search(smf, queries, k):
    num_variants = len(smf[0])            # dimension

    # database to numpy
    numpy_smf = np.asarray(smf, dtype='float32')
    numpy_queries = np.asarray(queries, dtype='float32')

    index = faiss.IndexFlatL2(num_variants)   # build the index
    print('Index is trained: ', index.is_trained)
    index.add(numpy_smf)                    # add vectors to the index
    print('Number of samples: ', index.ntotal)

    print('\nSearching...')
    D, I = index.search(numpy_queries, k)     # actual search
    print('\n...search complete.')

    return I
